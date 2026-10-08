# Stacja pomiarowa (W3)

Aplikacja demo do Wykładu 3 z Metod wirtualizacji. Czujniki (`sensor`) wysyłają temperaturę do `backend`, który zapisuje ją w PostgreSQL (`db`). Strona (`frontend`, nginx) pokazuje najnowsze pomiary i przekazuje `/api/` do backendu.

```bash
cp .env.example .env
docker compose up -d --build
```

- Strona: http://localhost:8080
- API: http://localhost:8080/api/docs

Sprzątanie: `docker compose down` (dane zostają) lub `docker compose down -v` (usuwa też dane).

Stan kodu po każdym warsztacie: `git checkout warsztat-1` (2, 3); początek zajęć: `git checkout start`.
