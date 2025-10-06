import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()  # loads your .env variables

db_host = os.getenv("DB_HOST")
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")

try:
    connection = psycopg2.connect(
        host=db_host,
        database=db_name,
        user=db_user,
        password=db_pass,
        port=5432
    )
    cursor = connection.cursor()

    # Step 1: Create a demo table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        email VARCHAR(150),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)
    connection.commit()
    print(" Table 'users' created successfully!")

    # Step 2: Insert sample data
    users_data = [
        ("Belinda Ntinyari", "belinda@example.com"),
        ("John Mwenda", "john.mwenda@example.com"),
        ("Grace Wambui", "grace.wambui@example.com")
    ]

    cursor.executemany("""
        INSERT INTO users (name, email) VALUES (%s, %s);
    """, users_data)
    connection.commit()
    print(" Sample data inserted successfully!")

    # Step 3: Fetch data to confirm
    cursor.execute("SELECT * FROM users;")
    rows = cursor.fetchall()
    print("\n Current records in 'users' table:")
    for row in rows:
        print(row)

except Exception as e:
    print("Error:", e)

finally:
    if connection:
        cursor.close()
        connection.close()
