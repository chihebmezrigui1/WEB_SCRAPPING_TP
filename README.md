# 📌 Projet de Web Scraping - Champions de League of Legends

## 📝 Description
Ce projet utilise **Python, Flask et BeautifulSoup** pour scraper les champions du jeu **League of Legends** à partir du site [League of Legends Fandom](https://leagueoflegends.fandom.com/wiki/League_of_Legends_Wiki). Les données des champions sont stockées dans un fichier `champions.json` et affichées sous forme de cartes dans une interface web.

---

## 🚀 Installation et Configuration

### 1️⃣ Prérequis
Assurez-vous d'avoir **Python 3+** installé sur votre machine.

### 2️⃣ Cloner le projet
```bash
 git clone https://github.com/chihebmezrigui1/WEB_SCRAPPING_TP.git
 cd WEB_SCRAPPING_TP
```

### 3️⃣ Créer un environnement virtuel (optionnel mais recommandé)
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate    # Windows
```

### 4️⃣ Installer les dépendances
```bash
pip install -r requirements.txt
```

---

## 🕵️‍♂️ Scraper les champions
Lancez le script pour récupérer les données des champions et les stocker dans `all_champions_stats.json` :
```bash
python scraper/scrape.py
```

---

## 🌍 Démarrer le serveur Flask
Lancez l'application Flask pour afficher les champions dans le navigateur :
```bash
python app.py
```
Puis ouvrez **http://127.0.0.1:5000/** dans votre navigateur.

---

## 📂 Structure du projet
```
/WEB_SCRAPPING_TP
│── templates
│       └── index.html #interface web
│── scraper
    ├── champion.py
    ├── frontend
    │   └── static
    │       └── images
    └── scrape.py
|── all_champions_stats.json
│── app.py  # Application Flask
│── requirements.txt  # Dépendances
│── README.md  # Documentation
```

---

## 📌 Fonctionnalités
✅ **Scraper tous les champions de LoL** (nom, rôle, attaque, sante, armure, image)  
✅ **Stocker les données dans un fichier JSON**  
✅ **Afficher les champions sous forme de cartes**   

---

## 🛠️ Technologies utilisées
- **Python** 🐍
- **Flask** 🌍
- **BeautifulSoup** 🕵️‍♂️
- **HTML/CSS** 🎨

---