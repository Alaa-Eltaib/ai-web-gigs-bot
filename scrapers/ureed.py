import requests
from bs4 import BeautifulSoup


URLS = [
    "https://public.ureed.com/jobs/frontend-development/",
    "https://public.ureed.com/jobs/data-science/",
    "https://public.ureed.com/jobs/data-analysis-reports/",
    "https://public.ureed.com/jobs/web-programming/",
    "https://public.ureed.com/jobs/backend-development/",
]

UREED_PROJECTS_URL = (
    "https://app.ureed.com/login"
    "?returnUrl=%2Ffreelancer%2Ffind-projects"
)

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/130.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9,ar;q=0.8",
}


def scrape_ureed():
    jobs = []
    seen = set()

    for page_url in URLS:
        try:
            response = requests.get(
                page_url,
                headers=HEADERS,
                timeout=20
            )

            print("Ureed:", page_url, response.status_code)

            if response.status_code != 200:
                continue

            soup = BeautifulSoup(
                response.text,
                "html.parser"
            )

            headings = soup.find_all(["h3", "h4"])

            for heading in headings:
                title = heading.get_text(
                    " ",
                    strip=True
                )

                if not title:
                    continue

                # تجاهل الأمثلة الوهمية
                if title.lower().startswith("example:"):
                    continue

                description_parts = []

                current = heading.find_next()
                steps = 0

                while current and steps < 25:
                    steps += 1

                    # لو دخلنا مشروع جديد، نقف
                    if (
                        current.name in ["h3", "h4"]
                        and current != heading
                    ):
                        break

                    if current.name in ["p", "div", "span"]:
                        text = current.get_text(
                            " ",
                            strip=True
                        )

                        if (
                            text
                            and text not in description_parts
                        ):
                            description_parts.append(text)

                    current = current.find_next()

                description = " ".join(
                    description_parts
                )

                description = " ".join(
                    description.split()
                )

                # لأن كل الوظائف هتستخدم نفس رابط الدخول،
                # نمنع التكرار بالعنوان بدل الرابط
                job_key = title.lower().strip()

                if job_key in seen:
                    continue

                seen.add(job_key)

                jobs.append({
                    "title": title,
                    "url": UREED_PROJECTS_URL,
                    "description": description[:1200],
                    "platform": "Ureed"
                })

        except Exception as e:
            print(
                "Ureed page error:",
                page_url,
                e
            )

    print(
        "Ureed jobs found:",
        len(jobs)
    )

    return jobs


if __name__ == "__main__":
    jobs = scrape_ureed()

    for job in jobs[:20]:
        print("\n----------------")
        print("Title:", job["title"])
        print("URL:", job["url"])
        print(
            "Description:",
            job["description"][:300]
        )