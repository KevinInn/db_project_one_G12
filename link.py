import psycopg2
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path=os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))

DB_USER = os.getenv('USER')
DB_HOST = os.getenv('HOST')
DB_PORT = os.getenv('PORT')
DB_PASSWORD = os.getenv('PASSWORD')
DB_NAME = os.getenv('DB')

connection = psycopg2.connect(
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT,
    dbname=DB_NAME  # PostgreSQL 的資料庫名稱
)
cursor = connection.cursor()

