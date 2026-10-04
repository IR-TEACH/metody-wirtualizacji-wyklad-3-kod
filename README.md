# Stacja pomiarowa

Aplikacja demo do Wykładu 2 z Metod wirtualizacji. Czujniki (`sensor`) wysyłają temperaturę do `backend`, a strona (`frontend`) pokazuje najnowsze pomiary.

```bash
docker compose up -d --build
```

- Strona: http://localhost:8080
- API: http://localhost:8000/docs

Sprzątanie: `docker compose down`
