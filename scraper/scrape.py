import requests
from bs4 import BeautifulSoup
import json
import os

BASE_URL = "https://leagueoflegends.fandom.com/wiki/List_of_champions"

def scrape_champions():
    response = requests.get(BASE_URL)
    soup = BeautifulSoup(response.content, "html.parser")
    champions = []

    # Sélectionner les champs à scraper
    for champ in soup.select("table.wikitable tbody tr"):
        cells = champ.find_all("td")
        if len(cells) < 2:  # Ignorer les lignes sans données
            continue

        name = cells[0].get_text(strip=True)
        image_url = cells[0].find("img")["src"] if cells[0].find("img") else ""
        role = cells[1].get_text(strip=True)

        champions.append({
            "name": name,
            "role": role,
            "image_url": image_url
        })

    # Sauvegarder les données dans un fichier JSON
    with open("scraper/champions.json", "w", encoding="utf-8") as f:
        json.dump(champions, f, ensure_ascii=False, indent=4)

    print(f"Scraping terminé : {len(champions)} champions récupérés.")

def save_images(folder="frontend/static/images"):
    os.makedirs(folder, exist_ok=True)
    with open("scraper/champions.json", encoding="utf-8") as f:
        champions = json.load(f)

    for champ in champions:
        if champ["image_url"]:
            img_data = requests.get(champ["image_url"]).content
            with open(os.path.join(folder, f"{champ['name']}.jpg"), "wb") as f:
                f.write(img_data)

if __name__ == "__main__":
    scrape_champions()
    save_images()
