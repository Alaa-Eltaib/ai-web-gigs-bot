RELEVANT_KEYWORDS = [
    # AI
    "artificial intelligence",
    "ذكاء اصطناعي",
    "الذكاء الاصطناعي",
    "machine learning",
    "deep learning",
    "llm",
    "rag",
    "chatbot",
    "شات بوت",
    "agentic ai",
    "ai agent",
    "computer vision",
    "opencv",
    "yolo",
    "nlp",

    # Python / Data
    "python",
    "بايثون",
    "بيتون",
    "pandas",
    "data analysis",
    "تحليل بيانات",
    "data entry",
    "إدخال بيانات",
    "data cleaning",
    "تنظيف بيانات",
    "csv",
    "etl",
    "api",
    "fastapi",
    "automation",
    "أتمتة",
    "web scraping",
    "scraping",
    "excel",
    "google sheets",
    "sql",
    "power bi",

    # Frontend / Web
    "frontend",
    "front-end",
    "react",
    "next.js",
    "nextjs",
    "angular",
    "javascript",
    "typescript",
    "html",
    "css",
    "tailwind",
    "bootstrap",

    # Websites
    "landing page",
    "صفحة هبوط",
    "موقع بسيط",
    "موقع تعريفي",
    "موقع شركة",
    "موقع شخصي",
    "portfolio website",
    "business website",
    "company website",
    "web development",
    "تطوير موقع",
    "برمجة موقع",
    "تصميم موقع",
    "تصميم وبرمجة موقع",
    "dashboard",
    "لوحة تحكم",
]


def get_matched_keywords(title, description=""):
    text = f"{title} {description}".lower()

    matches = []

    for keyword in RELEVANT_KEYWORDS:
        if keyword.lower() in text:
            matches.append(keyword)

    return matches


def is_relevant_job(title, description=""):
    return len(
        get_matched_keywords(
            title,
            description
        )
    ) > 0