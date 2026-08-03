
import os

from dotenv import load_dotenv
from sqlalchemy import create_engine


# Load Environment Variables


load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")


# Create SQLAlchemy Engine


DATABASE_URL = (
    f"mysql+mysqlconnector://"
    f"{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}/{DB_NAME}"
)

engine = create_engine(
    DATABASE_URL,
    echo=False
)


def get_engine():
    """
    Returns SQLAlchemy engine.
    """
    return engine


if __name__ == "__main__":

    try:
        connection = engine.connect()

        print("=" * 50)
        print("Connected to MySQL Successfully")
        print("=" * 50)

        connection.close()

    except Exception as e:
        print(e)