import time

from database import (
    init_db,
    job_exists,
    save_job
)

from filters import is_relevant_job
from telegram_sender import send_job

from scrapers.mostaql import scrape_mostaql
from scrapers.nafezly import scrape_nafezly
from scrapers.khamsat import scrape_khamsat
from scrapers.rebhy import scrape_rebhy
from scrapers.ureed import scrape_ureed
from scrapers.kafiil import scrape_kafiil


CHECK_INTERVAL = 300


SCRAPERS = [
    scrape_mostaql,
    scrape_nafezly,
    scrape_khamsat,
    scrape_rebhy,
    scrape_ureed,
    scrape_kafiil
]


def process_jobs(jobs):
    for job in jobs:

        if job_exists(job):
            continue

        title = job["title"]
        description = job.get("description", "")

        relevant = is_relevant_job(
            title,
            description
        )

        # لو مش مناسبة: خزنيها فقط عشان ما نفحصهاش تاني
        if not relevant:
            save_job(job, relevant=False)
            continue

        print(
            f"🆕 {job['platform']}: "
            f"{job['title']}"
        )

        # الوظيفة المناسبة تتبعت الأول
        sent = send_job(job)

        if sent:
            print("✅ Sent")
            save_job(job, relevant=True)
        else:
            print("❌ Telegram failed")


def run():
    for scraper in SCRAPERS:
        try:
            jobs = scraper()

            print(
                f"Found {len(jobs)} jobs "
                f"from {scraper.__name__}"
            )

            process_jobs(jobs)

        except Exception as e:
            print(
                f"❌ Error in "
                f"{scraper.__name__}: {e}"
            )

   

def main():
    init_db()

    print("🚀 GigsBot started")
    print("⏱ Checking every 5 minutes")

    while True:
        run()

        print(
            "\n⏳ Waiting 5 minutes...\n"
        )

        time.sleep(CHECK_INTERVAL)



if __name__ == "__main__":
    main()
    