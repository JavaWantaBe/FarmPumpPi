import os
import time
import pymysql
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    # Get database URL from environment
    db_url = os.getenv('DATABASE_URL')
    logger.info(f"Starting Pump Controller with DB URL: {db_url}")

    # Example: Periodically log a message
    while True:
        logger.info("Pump Controller is running...")
        # Add your pump control logic here
        # Example: Connect to MariaDB
        try:
            connection = pymysql.connect(
                host='mariadb',
                user='user',
                password='userpassword',
                database='myapp',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1")
                result = cursor.fetchone()
                logger.info(f"Database query result: {result}")
            connection.close()
        except Exception as e:
            logger.error(f"Error connecting to database: {e}")
        
        time.sleep(60)  # Run every 60 seconds

if __name__ == "__main__":
    main()