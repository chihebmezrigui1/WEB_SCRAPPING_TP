import requests
from bs4 import BeautifulSoup
import json
import os

URL2 = "https://leagueoflegends.fandom.com/wiki/League_of_Legends_Wiki"

def scrape_champions():
    response = requests.get(URL2)
    soup = BeautifulSoup(response.text, "html.parser")

    # Trouver tous les <span> avec la classe 'grid-icon champion-icon'
    champion_spans = soup.find_all("span", class_="grid-icon champion-icon")

    champions = []

    # Parcourir chaque élément et extraire les données
    for champion_span in champion_spans:
        # Nom du champion
        name = champion_span.get("data-champion", "").strip()

        # Lien vers la page du champion
        link_tag = champion_span.find("a")
        link = "https://leagueoflegends.fandom.com" + link_tag["href"] if link_tag else ""

        # Image du champion
        image_tag = champion_span.find("img")
        image = image_tag["data-src"] if image_tag and "data-src" in image_tag.attrs else ""

        # Limiter le lien à ".png"
        if image:
            image = image.split(".png")[0] + ".png"

        # Ajouter le champion à la liste
        champions.append({
            "name": name,
            "link": link,
            "image": image
        })

    return champions

# Fonction pour récupérer les stats de base d'un champion à partir de sa page
def scrape_champion_stats(champion_url):
    response = requests.get(champion_url)
    soup = BeautifulSoup(response.text, "html.parser")

    champion = []

    # Récupérer la section des stats du champion

    # Attaque du champion
    attack_section = soup.find("div", class_="pi-smart-data-value", attrs={"data-source": "attack damage"})
    if attack_section:
        attack = attack_section.find("span").text.strip()
    else:
        attack = ""

    # Santé du champion
    health_section = soup.find("div", class_="pi-smart-data-value", attrs={"data-source": "health"})
    if health_section:
        health = health_section.find("span").text.strip()
    else:
        health = ""

    # Armure du champion
    armor_section = soup.find("div", class_="pi-smart-data-value", attrs={"data-source": "armor"})
    if armor_section:
        armor = armor_section.find("span").text.strip()
    else:
        armor = ""

    # Role du champion
    position_section = soup.find("div", {"data-source": "position"})
    if position_section:
        lane = position_section.find("div", {"class": "pi-data-value"}).text.strip()
    else:
        lane = ""

    champion.append({
        "attaque" : attack,
        "sante": health,
        # "ressource" : resource_text,
        "armure" : armor,
        "lane" : lane,
    })

    return champion

# Fonction pour télécharger une image
def download_image(url, name):
    if not url:
        print(f"Aucune image pour {name}.")
        return
    # Créer le répertoire pour stocker les images si nécessaire
    os.makedirs("champion_images", exist_ok=True)

    # Définir le chemin de l'image
    file_path = os.path.join("champion_images", f"{name}.png")

    try:
        # Télécharger l'image
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(file_path, "wb") as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            print(f"Image de {name} téléchargée avec succès.")
        else:
            print(f"Échec du téléchargement de l'image pour {name}.")
    except Exception as e:
        print(f"Erreur lors du téléchargement de l'image pour {name}: {e}")

def main():
    # Récupérer la liste de tous les champions et leurs liens
    champions = scrape_champions()
    
    all_champions_data = []

    # print(f"Scraping de {champions[0]['name']}...")
            
    # # Récupérer les stats de base du champion
    # stats = scrape_champion_stats(champions[0]['link'])
    
    # # Ajouter le nom et les stats au champion
    # champion_data = {
    #     "name": champions[0]['name'],
    #     "image": champions[0]['image'],
    #     "stats": stats
    # }

    # Pour chaque champion, récupérer ses stats
    for champion in champions:
        print(f"Scraping de {champion['name']}...")

        download_image(champion["image"], champion["name"])

        # Récupérer les stats de base du champion
        stats = scrape_champion_stats(champion['link'])
        
       # Ajouter le nom et les stats au champion
        champion_data = {
            "name": champion['name'],
            "image": champion['image'],
            "stats": stats
        }

        all_champions_data.append(champion_data)

    # Sauvegarder toutes les données dans un fichier JSON
    with open("all_champions_stats.json", "w") as f:
        json.dump(all_champions_data, f, indent=4)

    print("Scraping terminé et sauvegardé dans 'all_champions_stats.json'.")

if __name__ == "__main__":
    main()
