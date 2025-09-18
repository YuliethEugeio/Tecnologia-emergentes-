import requests
from bs4 import BeautifulSoup

url = "https://www.icbf.gov.co/noticias"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    noticias = []

    # Buscar cada bloque de noticia
    items = soup.find_all("div", class_="views-row")

    for item in items:
        link_tag = item.find("a")
        if link_tag:
            titulo = link_tag.get_text(strip=True)
            link = "https://www.icbf.gov.co" + link_tag.get("href")
            noticias.append({
                "titulo": titulo,
                "link": link
            })

    if noticias:
        for noticia in noticias:
            print(f"Título: {noticia['titulo']}")
            print(f"Link: {noticia['link']}")
            print("-" * 40)
    else:
        print("No se encontraron noticias.")
else:
    print(f"Error al realizar la solicitud: {response.status_code}")

