import requests
from bs4 import BeautifulSoup


URL = "https://khamsat.com/community/requests"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/130.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "ar,en-US;q=0.9,en;q=0.8",
}


def scrape_khamsat():

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

    for link in soup.find_all("a", href=True):

        href = link.get("href", "")
        title = link.get_text(
            " ",
            strip=True
        )

        if not title:
            continue

        # لازم يكون رابط طلب
        if "/community/requests/" not in href:
            continue

        # استبعاد إنشاء موضوع جديد
        if href.endswith("/new"):
            continue

        if title == "موضوع جديد":
            continue

        if href.startswith("/"):
            href = "https://khamsat.com" + href

        jobs.append({
            "title": title,
            "url": href,
            "description": "",
            "platform": "Khamsat"
        })

    # Remove duplicates
    unique = {}

    for job in jobs:
        unique[job["url"]] = job

    return list(unique.values())


if __name__ == "__main__":

    jobs = scrape_khamsat()

    print(
        "Khamsat jobs found:",
        len(jobs)
    )

    for job in jobs[:10]:

        print("\n----------------")
        print(job["title"])
        print(job["url"])