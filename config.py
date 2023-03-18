import os

from dotenv import load_dotenv

load_dotenv()
# DB_HOST = os.environ.get('DB_HOST')
# DB_PORT = os.environ.get('DB_PORT')
# DB_NAME = os.environ.get('DB_NAME')
# DB_USER = os.environ.get('DB_USER')
# DB_PASSWORD = os.environ.get('DB_PASSWORD')

DB_HOST = 'db'
DB_PORT = '5432'
DB_NAME = 'units_db'
DB_USER = 'postgres'
DB_PASSWORD = 'postgres'
