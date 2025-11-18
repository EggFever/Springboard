import sqlite3

def explore_database(db_file):
    """Explore all tables and sample their contents."""
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()

    # 🔹 Step 1: Show all tables in the database
    print("📋 All tables in the database:\n")
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [t[0] for t in cur.fetchall()]
    for t in tables:
        print("-", t)
    print("\n" + "="*60)

    # 🔹 Step 2: For each table, show its columns and first few rows
    for t in tables:
        print(f"\n🔍 Table: {t}")
        print("-" * 60)

        # Get column info
        cur.execute(f"PRAGMA table_info({t});")
        columns = cur.fetchall()
        print("Columns:")
        for col in columns:
            print(f"  {col[1]} ({col[2]})")
        
        # Show first few rows
        print("\nSample rows:")
        cur.execute(f"SELECT * FROM {t} LIMIT 5;")
        rows = cur.fetchall()
        for row in rows:
            print(row)

        print("\n" + "="*60)

    conn.close()

# Run it
if __name__ == "__main__":
    explore_database("sqlite_db_pythonsqlite.db")
