import os
import requests
from dotenv import load_dotenv

from filters import get_matched_keywords


load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")


def send_job(job):
    matches = get_matched_keywords(
        job["title"],
        job.get("description", "")
    )

    skills = ", ".join(matches[:6])

    description = job.get(
        "description",
        ""
    )[:450]

    message = f"""
🔥 وظيفة جديدة مناسبة ليكي

📌 {job['title']}

🌐 {job['platform']}

🎯 Match:
{skills}

📝
{description}

🔗 {job['url']}
"""

    url = (
        f"https://api.telegram.org/"
        f"bot{BOT_TOKEN}/sendMessage"
    )

    response = requests.post(
        url,
        data={
            "chat_id": CHAT_ID,
            "text": message,
            "disable_web_page_preview": True
        },
        timeout=20
    )

    return response.ok