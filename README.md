# AI Web Gigs Bot

A Telegram bot that monitors multiple Arabic freelance platforms and sends filtered job alerts based on selected technical fields such as AI, data, frontend development, landing pages, and simple web development projects.

Want to try it? Check out the bot on Telegram: **@getgigsbot**

## Features

- Monitors multiple freelance platforms automatically.
- Sends new matching opportunities directly to Telegram.
- Filters jobs based on selected technical keywords.
- Avoids sending duplicate jobs.
- Stores previously seen jobs using SQLite.
- Checks for new jobs periodically.
- Supports both Arabic and English job keywords.
- Can run locally or continuously on a cloud service.

## Supported Platforms

The bot currently monitors:

- Mostaql
- Nafezly
- Khamsat — Requests section
- Rebhy
- Ureed
- Kafiil

## Target Job Categories

The bot focuses on opportunities related to:

- Artificial Intelligence
- Machine Learning
- Generative AI
- LLMs
- RAG
- AI Agents
- Computer Vision
- Python
- Data Analysis
- Data Cleaning
- ETL
- Web Scraping
- Automation
- SQL
- Power BI
- Frontend Development
- React
- Next.js
- Angular
- Landing Pages
- Simple Websites
- Company Websites
- Dashboards

Jobs outside the selected technical areas can be excluded using the filtering configuration.

## Project Structure

```text
ai-web-gigs-bot/
│
├── main.py
├── database.py
├── filters.py
├── telegram_sender.py
├── requirements.txt
├── Dockerfile
│
├── scrapers/
│   ├── __init__.py
│   ├── mostaql.py
│   ├── nafezly.py
│   ├── khamsat.py
│   ├── rebhy.py
│   ├── ureed.py
│   └── kafiil.py
│
└── .env
```

## How It Works

The bot follows this pipeline:

```text
Freelance Platforms
        ↓
     Scrapers
        ↓
   Job Filtering
        ↓
 Duplicate Check
        ↓
     SQLite
        ↓
 Telegram Alerts
```

Each scraper collects available jobs from its platform and converts them into a common structure:

```python
{
    "title": "Job title",
    "url": "Job URL",
    "description": "Job description",
    "platform": "Platform name"
}
```

The job is then checked against the configured filters.

If the job is relevant and has not been seen before, it is sent to Telegram.

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/ai-web-gigs-bot.git
cd ai-web-gigs-bot
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root:

```env
BOT_TOKEN=your_telegram_bot_token
CHAT_ID=your_telegram_chat_id
```

Optional variables used for cloud deployment:

```env
CHROMIUM_PATH=/usr/bin/chromium
DB_PATH=/data/jobs.db
```

Do not commit the `.env` file to GitHub.

## Telegram Bot Setup

Create a Telegram bot using `@BotFather`.

Get the bot token and add it to the `.env` file.

Send a message to your bot, then open:

```text
https://api.telegram.org/botYOUR_BOT_TOKEN/getUpdates
```

Find your Telegram `chat.id` and add it as `CHAT_ID`.

## Running the Bot

Run:

```bash
python main.py
```

The bot checks all supported platforms periodically and sends matching opportunities to Telegram.

Example console output:

```text
🚀 GigsBot started
⏱ Checking every 5 minutes

Found 25 jobs from scrape_mostaql
Found 21 jobs from scrape_nafezly
Found 25 jobs from scrape_khamsat
Found 15 jobs from scrape_rebhy
Found 8 jobs from scrape_ureed
Found 10 jobs from scrape_kafiil

⏳ Waiting 5 minutes...
```

## Example Telegram Alert

```text
🔥 New Freelance Job

📌 Data Analytics Project

🌐 Ureed

🎯 Match:
power bi, dashboard, data analysis

📝
Looking for someone to build a data analytics dashboard...

🔗 Open Project
```

## Job Filtering

Relevant keywords are configured inside:

```text
filters.py
```

Example:

```python
RELEVANT_KEYWORDS = [
    "artificial intelligence",
    "machine learning",
    "python",
    "data analysis",
    "data cleaning",
    "fastapi",
    "react",
    "next.js",
    "landing page",
    "صفحة هبوط",
    "ذكاء اصطناعي",
    "تحليل بيانات"
]
```

Unwanted job categories can also be excluded.

Example:

```python
EXCLUDED_KEYWORDS = [
    "flutter",
    ".net",
    "translation",
    "ترجمة",
    "motion graphic",
    "مونتاج"
]
```

## Duplicate Prevention

SQLite is used to store previously discovered jobs.

The bot checks the platform and job title before sending a new alert.

This prevents the same opportunity from being sent repeatedly during each scan.

## Cloud Deployment

The project can be deployed using Docker on platforms such as Railway.

The included `Dockerfile` installs Chromium so Kafiil can be monitored using Playwright.

Recommended environment variables:

```env
BOT_TOKEN=...
CHAT_ID=...
CHROMIUM_PATH=/usr/bin/chromium
DB_PATH=/data/jobs.db
```

For persistent SQLite storage, mount a persistent volume to:

```text
/data
```

## Technologies

- Python
- Requests
- BeautifulSoup
- Playwright
- SQLite
- Telegram Bot API
- Docker

## Future Improvements

Possible future improvements include:

- AI-based job relevance scoring.
- Job ranking based on skills and experience.
- Budget extraction and filtering.
- Automatic skill matching.
- Estimated proposal price suggestions.
- AI-generated proposal drafts.
- More freelance platforms.
- Web dashboard for managing filters.
- Telegram commands for changing preferences.
- Daily job summaries.

## Disclaimer

This project is intended for personal productivity and job discovery.

Each platform may have its own terms of service, rate limits, and policies regarding automated access. Scrapers should be used responsibly and with reasonable request intervals.

## Author

Alaa Mohamed 

AI / Machine Learning / Web Development