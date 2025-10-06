import psycopg2

try:
    connection = psycopg2.connect(
        host="practice-aurora-db.cluster-cgnskimikjmx.us-east-1.rds.amazonaws.com",
        user="postgres",
        password="Practice123!",
        dbname="practice_db"
    )

    cursor = connection.cursor()
    cursor.execute("SELECT 'Connected successfully!'")
    print(cursor.fetchone())

except Exception as e:
    print("Error:", e)

finally:
    if connection:
        cursor.close()
        connection.close()
