import requests
from bs4 import BeautifulSoup


URL = "https://nafezly.com/projects"

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


def scrape_nafezly():
    response = requests.get(
        URL,
        headers=HEADERS,
        timeout=20
    )

    response.raise_for_status()

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    jobs = []

    # هنبدأ بالسحب العام للروابط
    for link in soup.find_all("a", href=True):

        href = link.get("href", "")
        title = link.get_text(
            " ",
            strip=True
        )

        if not title:
            continue

        # روابط المشاريع فقط
        if "/project/" not in href:
            continue

        if href.startswith("/"):
            href = "https://nafezly.com" + href

        jobs.append({
            "title": title,
            "url": href,
            "description": "",
            "platform": "Nafezly"
        })

    # إزالة التكرار
    unique = {}

    for job in jobs:
        unique[job["url"]] = job

    return list(unique.values())