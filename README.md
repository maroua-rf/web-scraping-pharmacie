# 💊 Mini-Projet : Web Scraping – Pharmacie Maroc

## 📝 Description
Ce projet a pour objectif d'extraire, nettoyer, analyser et visualiser des données relatives aux médicaments disponibles sur le marché marocain.  
Les données proviennent du site [medicament.ma](https://medicament.ma), une plateforme en ligne dédiée aux informations sur les médicaments au Maroc.  

L'objectif principal est de fournir une **analyse approfondie** des produits pharmaceutiques disponibles, en se concentrant sur des aspects tels que les prix, les dosages et les caractéristiques des médicaments.  
Le projet peut être utile pour les professionnels de santé, les patients et les consommateurs recherchant des informations sur les médicaments.

---

## 🧩 Structure du projet
```
mini-projet-scraping-pharmacie/
├── projet/
│ ├── Scraping.py → collecte les données depuis le site web
│ ├── Nettoyage.py → nettoyage et préparation des données
│ ├── Analyse.py → analyse statistique et extraction d'informations pertinentes
│ └── Visualisation.py → création de graphiques et visualisations
├── medicaments__A_Z.xlsx → fichier Excel avec les données extraites
└── Rapport.pdf → rapport détaillé du projet
```

---

## 🛠️ Outils et Bibliothèques

- **Python**  
- **requests** : pour envoyer des requêtes HTTP et récupérer les pages web  
- **BeautifulSoup4** : pour analyser et extraire des informations depuis le HTML  
- **pandas** : pour le traitement et la manipulation des données  
- **matplotlib** et **seaborn** : pour la visualisation des données  

Pour installer les bibliothèques nécessaires :
```bash
pip install requests beautifulsoup4 pandas matplotlib seaborn
```
---
## 🚀 Exécution du projet
Les scripts doivent être exécutés dans cet ordre :
    python Scraping.py
    python Nettoyage.py
    python Analyse.py
    python Visualisation.py

- Scraping.py : récupère les données de medicament.ma et les enregistre dans un fichier Excel.

- Nettoyage.py : nettoie les données pour garantir leur qualité et leur cohérence (colonnes renommées, suppression des valeurs invalides, formatage).

- Analyse.py : effectue des analyses statistiques (moyennes, écarts-types, top 5 des médicaments les plus chers et moins chers, analyse des dosages).

- Visualisation.py : crée des graphiques (nuage de points, histogrammes, boxplots, barplots des médicaments et mots fréquents).

---
## 📊 Exemple de résultats
- Extraction de toutes les pages du site classées de A à Z

- Nettoyage et structuration des données pour l'analyse

- Graphiques illustrant la distribution des prix, des dosages et des tendances dans les noms de médicaments

- Identification des médicaments les plus chers et les moins chers
---
  
## 👩‍💻 Auteurs
**Rifi Maroua**
**Ougni Imane**
