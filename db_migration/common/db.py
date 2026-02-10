import os
import mysql.connector
from mysql.connector import pooling
from dotenv import load_dotenv

load_dotenv()

def create_pool(prefix: str):
    return pooling.MySQLConnectionPool(
        pool_name=f"{prefix}_pool",
        pool_size=5,
        host=os.getenv(f"{prefix}_DB_HOST"),
        port=int(os.getenv(f"{prefix}_DB_PORT")),
        user=os.getenv(f"{prefix}_DB_USER"),
        password=os.getenv(f"{prefix}_DB_PASSWORD"),
        database=os.getenv(f"{prefix}_DB_NAME"),
        autocommit=False
    )

SRC_POOL = create_pool("SRC")
TGT_POOL = create_pool("TGT")
