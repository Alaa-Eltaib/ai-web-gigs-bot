import re
import requests
from bs4 import BeautifulSoup

URL = "https://rebhy.com/projects"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/130.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "ar,en-US;q=0.9,en;q=0.8",
}


def clean_title(title):
    title = " ".join(title.split())

    # لو العنوان اتكرر مرتين وراء بعض
    half = len(title) // 2

    if (
        len(title) % 2 == 0
        and title[:half] == title[half:]
    ):
        title = title[:half]

    return title.strip()


def scrape_rebhy():
    response = requests.get(
        URL,
        headers=HEADERS,
        timeout=20
    )

    print("Rebhy status:", response.status_code)

    response.raise_for_status()

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    jobs = []

    seen_urls = set()

    for link in soup.find_all("a", href=True):
        href = link.get("href", "")

        if not re.search(r"/projects/\d+/", href):
            continue

        if href.startswith("/"):
            href = "https://rebhy.com" + href

        if href in seen_urls:
            continue

        seen_urls.add(href)

        title = clean_title(
            link.get_text(" ", strip=True)
        )

        if not title:
            continue

        # نحاول نجيب الكارد/الكونتينر الأب
        card = link

        for _ in range(5):
            if card.parent:
                card = card.parent

            text = card.get_text(
                " ",
                strip=True
            )

            if (
                "الميزانية" in text
                or "عروض" in text
                or "طلب نشط" in text
            ):
                break

        full_text = card.get_text(
            " ",
            strip=True
        )

        # نقلل التكرار
        full_text = " ".join(
            full_text.split()
        )

        jobs.append({
            "title": title,
            "url": href,
            "description": full_text[:1200],
            "platform": "Rebhy"
        })

    print(
        "Rebhy jobs found:",
        len(jobs)
    )

    return jobs


if __name__ == "__main__":
    jobs = scrape_rebhy()

    for job in jobs[:10]:
        print("\n----------------")
        print("Title:", job["title"])
        print("URL:", job["url"])
        print(
            "Description:",
            job["description"][:300]
        )