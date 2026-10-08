// ten sam adres co strona: nginx przekazuje /api/ do backendu
const API = "/api";

async function odswiez() {
  const pomiary = await (await fetch(`${API}/measurements`)).json();
  document.getElementById("pomiary").innerHTML = pomiary.reverse()
    .map(p => `<tr><td>${p.sala}</td><td>${p.temp}</td></tr>`).join("");
}

odswiez();
setInterval(odswiez, 2000);  // co 2 s, tak jak wysyła czujnik
