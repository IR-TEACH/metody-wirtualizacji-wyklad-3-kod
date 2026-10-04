"""Czujnik w sali: co 2 s wysyła losową temperaturę do backendu."""
import json, os, random, sys, time, urllib.request

BACKEND_URL = os.environ.get("BACKEND_URL", "http://host.docker.internal:8000")
SALA = os.environ.get("SALA") or str(random.randint(100, 350))

print(f"Czujnik sali {SALA}, Python {sys.version.split()[0]}", flush=True)
while True:
    temp = round(random.uniform(19, 25), 1)
    body = json.dumps({"sala": SALA, "temp": temp}).encode()
    req = urllib.request.Request(f"{BACKEND_URL}/measurements", data=body,
                                 headers={"Content-Type": "application/json"})
    try:
        urllib.request.urlopen(req, timeout=5)
        print(f"sala {SALA}: {temp} °C -> wysłano", flush=True)
    except Exception as e:
        print(f"sala {SALA}: {temp} °C -> błąd: {e}", flush=True)
    time.sleep(2)
