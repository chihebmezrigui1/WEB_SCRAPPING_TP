import requests
from bs4 import BeautifulSoup
import json
import os

URL = "https://leagueoflegends.fandom.com/wiki/List_of_champions"

def scrape_champions():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")

    champions = []
    table = soup.find("table", {"class": "article-table"})

    for row in table.find_all("tr")[1:]:  # Ignorer l'en-tête
        columns = row.find_all("td")
        if len(columns) < 2:
            continue

        name_tag = columns[0].find("span", class_="champion-icon")
        name = name_tag["data-champion"] if name_tag else ""

        image_tag = columns[0].find("img")
        image = image_tag["data-src"] if image_tag and "data-src" in image_tag.attrs else ""

        role_tag = columns[1]
        role = role_tag.text.strip()

        champion_url = columns[0].find("a")["href"]

        champions.append({
            "name": name,
            "role": role,
            "image": image,
            "url": "https://leagueoflegends.fandom.com" + champion_url  # Lien vers la page détaillée
        })

    return champions

def scrape_champion_details(champion):
    response = requests.get(champion["url"])
    soup = BeautifulSoup(response.text, "html.parser")

    # Récupérer les données supplémentaires pour chaque champion
    details = {}

    # Nom du champion
    details["name"] = champion["name"]

    # Image du champion
    image_tag = soup.find("img", class_="champion-icon")
    details["image"] = image_tag["src"] if image_tag else champion["image"]

    # Mana, Dégâts d’attaque, Lane (exemples d'attributs à scraper)
    info_table = soup.find("table", class_="champion-stats")
    if info_table:
        rows = info_table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if len(cells) == 2:
                label = cells[0].text.strip()
                value = cells[1].text.strip()
                if "Mana" in label:
                    details["mana"] = value
                if "Dégâts d’attaque" in label:
                    details["attack_damage"] = value
                if "Lane" in label:
                    details["lane"] = value

    return details

def main():
    champions_data = scrape_champions()

    # Scraper les détails pour chaque champion
    detailed_champions = []
    for champion in champions_data:
        details = scrape_champion_details(champion)
        detailed_champions.append(details)

    # Sauvegarder les données détaillées dans un fichier JSON
    with open("detailed_champions.json", "w") as f:
        json.dump(detailed_champions, f, indent=4)

    print(f"Scraping terminé, {len(detailed_champions)} champions trouvés.")

if __name__ == "__main__":
    main()
