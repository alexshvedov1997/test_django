import os
import time

import psycopg2
from dotenv import load_dotenv
from psycopg2 import OperationalError

load_dotenv()


def wait_for_db(host, port, user, password, database, timeout=30):
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            connection = psycopg2.connect(
                host=host,
                port=port,
                user=user,
                password=password,
                database=database,
            )
            cursor = connection.cursor()
            cursor.execute("SELECT 1")
            result = cursor.fetchone()
            cursor.close()
            if result and result[0] == 1:
                connection.close()
                break
        except OperationalError as e:
            time.sleep(1)


if __name__ == "__main__":
    wait_for_db(
        host=os.environ.get('DB_HOST', '127.0.0.1'),
        port=os.environ.get('DB_PORT', 5432),
        user=os.environ.get('DB_USER'),
        password=os.environ.get('DB_PASSWORD'),
        database=os.environ.get('DB_NAME'),
        timeout=30
    )
