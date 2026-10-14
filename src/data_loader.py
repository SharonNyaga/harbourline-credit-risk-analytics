import pandas as pd
from src.database import get_connection

def load_table(table_name):
    conn = get_connection()

    df = pd.read_sql_query(
        f"SELECT * FROM {table_name}",
        conn
    )

    conn.close()

    return df