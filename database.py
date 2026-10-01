import os
import sqlite3


DB_NAME = os.getenv(
    "DB_PATH",
    "jobs.db"
)


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            url TEXT,
            platform TEXT,
            relevant INTEGER DEFAULT 0,
            UNIQUE(platform, title)
        )
    """)

    conn.commit()
    conn.close()


def job_exists(job):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT 1
        FROM jobs
        WHERE platform = ?
        AND title = ?
        """,
        (
            job["platform"],
            job["title"]
        )
    )

    exists = cursor.fetchone() is not None

    conn.close()

    return exists


def save_job(job, relevant=False):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT OR IGNORE INTO jobs (
            title,
            url,
            platform,
            relevant
        )
        VALUES (?, ?, ?, ?)
        """,
        (
            job["title"],
            job["url"],
            job["platform"],
            1 if relevant else 0
        )
    )

    conn.commit()
    conn.close()