"""Backend Stacji: przyjmuje pomiary od czujników i oddaje je stronie (REST API)."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Stacja pomiarowa")
# CORS: strona z :8080 może czytać odpowiedzi z :8000
app.add_middleware(CORSMiddleware, allow_origins=["http://localhost:8080"])

pomiary = []  # w pamięci: znikają razem z kontenerem


class Pomiar(BaseModel):
    sala: str
    temp: float


@app.post("/measurements", status_code=201)
def dodaj(pomiar: Pomiar):
    pomiary.append(pomiar)
    return pomiar


@app.get("/measurements")
def lista():
    return pomiary[-20:]  # 20 najnowszych
