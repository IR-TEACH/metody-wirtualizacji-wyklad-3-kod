"""Backend Stacji: przyjmuje pomiary od czujników i zapisuje je w PostgreSQL (REST API)."""
import os

import psycopg
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

DB = os.environ["DATABASE_URL"]  # adres bazy przychodzi z zewnątrz (Compose)

app = FastAPI(title="Stacja pomiarowa")
# CORS: strona z :8080 może czytać odpowiedzi z :8000
app.add_middleware(CORSMiddleware, allow_origins=["http://localhost:8080"])

with psycopg.connect(DB) as conn:  # przy starcie: tabela, jeśli jej jeszcze nie ma
    conn.execute("CREATE TABLE IF NOT EXISTS pomiary (id serial, sala text, temp real)")


class Pomiar(BaseModel):
    sala: str
    temp: float


@app.post("/measurements", status_code=201)
def dodaj(pomiar: Pomiar):
    with psycopg.connect(DB) as conn:
        conn.execute("INSERT INTO pomiary (sala, temp) VALUES (%s, %s)", (pomiar.sala, pomiar.temp))
    return pomiar


@app.get("/measurements")
def lista():
    with psycopg.connect(DB) as conn:
        rows = conn.execute("SELECT sala, temp FROM pomiary ORDER BY id DESC LIMIT 20").fetchall()
    return [{"sala": s, "temp": t} for s, t in reversed(rows)]  # 20 najnowszych


@app.get("/health")
def health():  # zdrowy = proces odpowiada i baza działa (dla healthchecka)
    with psycopg.connect(DB, connect_timeout=2) as conn:
        conn.execute("SELECT 1")
    return {"status": "ok"}
