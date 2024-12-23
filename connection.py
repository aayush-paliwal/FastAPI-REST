import os
from dotenv import load_dotenv
from model.sql_model import BASE
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database


# Load the .env file
load_dotenv()

# db_user: str = os.getenv("DB_USER")
# db_port: int = os.getenv("DB_PORT")
# db_host: str = os.getenv("DB_HOST")
# db_password: str = os.getenv("DB_PASSWORD")

# uri = f'postgresql://{db_user}:{db_password}@localhost:{db_port}/to-do-app'
uri = os.getenv("DATABASE_URL")
engine = create_engine(uri)

# Create the database if it doesn't exist
if not database_exists(engine.url):
    create_database(engine.url)
print(f"Database exists: {database_exists(engine.url)}")

# Create tables based on models
BASE.metadata.create_all(bind=engine)

# Create a session
session = sessionmaker(bind=engine, autoflush=True)
db_session = session()

try:
    # Test connection to the database
    connection = engine.connect()
    print("Connected to the database")
    connection.close()
except Exception as e:
    print(f"Error connecting to the database: {str(e)}")
