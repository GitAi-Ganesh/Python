import psycopg2

def get_db():
    return psycopg2.connect(
        dbname="stickman_combat",
        user="postgres",
        password="4160",
        host="localhost",
        port="5432"
    )
