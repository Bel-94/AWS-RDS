import psycopg2
import os

from dotenv import load_dotenv
load_dotenv()  # loads your .env variables


# Load credentials from environment variables
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
    print("Successfully connected to RDS Aurora PostgreSQL database!")

    # Test a simple query
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("Database version:", record)

except Exception as e:
    print("Error connecting to database:", e)

finally:
    if connection:
        cursor.close()
        connection.close()
