// JS działa w przeglądarce na hoście, więc woła backend przez port hosta :8000
const API = `http://${location.hostname}:8000`;

async function odswiez() {
  const pomiary = await (await fetch(`${API}/measurements`)).json();
  document.getElementById("pomiary").innerHTML = pomiary.reverse()
    .map(p => `<tr><td>${p.sala}</td><td>${p.temp}</td></tr>`).join("");
}

odswiez();
setInterval(odswiez, 2000);  // co 2 s, tak jak wysyła czujnik
