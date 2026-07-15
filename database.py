import sqlite3

# Database Connection
conn = sqlite3.connect("signals.db", check_same_thread=False)
cursor = conn.cursor()

# Table Create
cursor.execute("""
CREATE TABLE IF NOT EXISTS signals (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pair TEXT,
    signal TEXT,
    confidence INTEGER,
    entry_time TEXT,
    result TEXT
)
""")

conn.commit()


def save_signal(pair, signal, confidence, entry_time):
    cursor.execute("""
        INSERT INTO signals
        (pair, signal, confidence, entry_time, result)
        VALUES (?, ?, ?, ?, ?)
    """, (
        pair,
        signal,
        confidence,
        entry_time,
        "PENDING"
    ))

    conn.commit()


def update_result(entry_time, result):
    cursor.execute("""
        UPDATE signals
        SET result = ?
        WHERE entry_time = ?
    """, (
        result,
        entry_time
    ))

    conn.commit()


def last_signal():
    cursor.execute("""
        SELECT pair, signal
        FROM signals
        ORDER BY id DESC
        LIMIT 1
    """)

    return cursor.fetchone()


def get_today_stats():

    cursor.execute("""
        SELECT
            COUNT(*) as total,
            SUM(CASE WHEN result='WIN' THEN 1 ELSE 0 END) as wins,
            SUM(CASE WHEN result='LOSS' THEN 1 ELSE 0 END) as losses
        FROM signals
    """)

    row = cursor.fetchone()

    total = row[0] or 0
    wins = row[1] or 0
    losses = row[2] or 0

    return {
        "total": total,
        "wins": wins,
        "losses": losses
    }