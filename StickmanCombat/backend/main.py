from fastapi import FastAPI
import psycopg2

app = FastAPI()

def get_db():
    return psycopg2.connect(
        dbname="stickman_combat",
        user="postgres",
        password="4160",
        host="localhost",
        port="5432"
    )

@app.get("/weapons")
def weapons():
    try:
        db = get_db()
        cur = db.cursor()
        cur.execute("SELECT name, damage, speed, range, sound FROM weapons")
        data = cur.fetchall()
        db.close()
        return data
    except Exception as e:
        return {"ERROR": str(e)}

@app.get("/moves")
def moves():
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT name, stamina, multiplier, sound FROM moves")
    return cur.fetchall()
