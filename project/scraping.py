"""
** La bibliothèque requests est une bibliothèque Python populaire pour envoyer des requêtes HTTP et interagir avec des sites web.
    Elle est très utile pour récupérer des pages web (HTML) que vous pouvez ensuite analyser avec BeautifulSoup.
** BeautifulSoup est une bibliothèque Python utilisée pour parser (analyser) le HTML et XML de manière simple et efficace.
    Elle permet de naviguer dans l'arbre HTML et d'en extraire des informations spécifiques.
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd
import string

# fonction qui retourne le nombre de page d'une lettre
def get_number_of_pages(base_url, letter):
    # Construire l'URL de la première page pour la lettre donnée
    url = base_url.format(1, lettre=letter)
    
    # Récupérer le contenu HTML de la page
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch the page. Status code: {response.status_code}")
    
    # Parser le contenu HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Chercher la balise pagination
    pagination = soup.find('ul', class_='pagination')
    
    # Si la pagination n'existe pas, il y a seulement une page
    if not pagination:
        return 1
    
    # Trouver tous les liens <a> dans la pagination
    page_links = pagination.find_all('a')
    
    # Si les liens <a> sont vides, une seule page est présente
    if not page_links:
        return 1
    
    # Chercher le dernier lien avec un numéro de page
    last_page_link = page_links[-1]
    last_page_url = last_page_link.get('href')
    
    # Extraire le numéro de la dernière page de l'URL
    if "page" in last_page_url:
        last_page_number = int(last_page_url.split('/page/')[1].split('/')[0])
    else:
        last_page_number = 1  # Si aucune pagination détectée, une seule page
    
    return last_page_number

# Liste pour stocker les résultats
data = []

# Liste des lettres à parcourir (A à Z)
lettres = string.ascii_uppercase


for lettre in lettres:
    cpt = 0
    # URL de la page des médicaments
    url_base = f"https://medicament.ma/listing-des-medicaments/page/{{}}/?lettre={lettre}"

    # Vérification de la connexion
    try:
        total_pages = get_number_of_pages(url_base, lettre)
        # Boucle de 1 à total_pages
        for page in range(1, total_pages + 1):
            url = url_base.format(page)  # Génère l'URL de chaque page
            print(f"Scraping page {page}: {url} \n")
            # Envoie de la requête
            response = requests.get(url)

            # Vérification du code de statut HTTP
            response.raise_for_status()  # Lève une exception pour un code de statut >= 400
            if response.status_code == 200:
                print(f"Connexion réussie pour la page {page} ! \n")

            # Parser (analyser) le contenu HTML de la page
            soup = BeautifulSoup(response.content, "html.parser")
            print("Parsing du contenu effectué avec succès ! \n\n")

            # Trouver tous les médicaments dans le tableau
            medicaments = soup.find_all("td")

            # Extraire les informations
            for medicament in medicaments:
                # Extraire le nom du médicament
                nom = medicament.find("span", class_="details")
                cpt += 1
                if nom:
                    nom_medicament = nom.get_text(strip=True)
                    # Extraire les détails et le prix
                    details = nom.find_next("span", class_="small")
                    if details:
                        details_text = details.get_text(strip=True)
                        try:
                            # Supprimer details_text du nom_medicament
                            nom_medicament_sans_details = nom_medicament.replace(details_text, "").strip()
                            # Diviser la partie du nom pour obtenir le nom puis la dose
                            nom_part, dose_part = nom_medicament_sans_details.rsplit(",", 1)
                            # Diviser la partie des détails pour obtenir le format puis le prix
                            forme_part, prix_part = details_text.rsplit("-", 1)
                            data.append([nom_part, dose_part, forme_part, prix_part])
                            #print(f"Nom: {nom_part} *** Dose: {dose_part} *** Format: {forme_part} *** Prix:{prix_part}")
                        except ValueError:
                            # Si '-' n'est pas présent, affecte None et continue
                            #print(f"****************** {nom_part}*********************")
                            nom_part = nom_medicament
                            dose_part = ("None")
                            forme_part = ("None")
                            prix_part = ("None")
                            data.append([nom_part, dose_part, forme_part, prix_part])
        
        # Créer un DataFrame pandas
        df = pd.DataFrame(data, columns=["Nom", "Dose", "Format", "Prix"])

        # Sauvegarder dans un fichier Excel
        fichier_excel = "medicaments__A_Z.xlsx"
        df.to_excel(fichier_excel, index=False, engine='openpyxl')
        #print(f"Les résultats ont été sauvegardés dans le fichier : {fichier_excel}")
        print(f"Total des médicaments extraits : {cpt}")

    except requests.exceptions.HTTPError as http_err:  # Attrape les erreurs HTTP spécifiques (par exemple, 404 Not Found, 500 Internal Server Error)
        print(f"Échec de la connexion. Erreur HTTP : {http_err} - Code de statut : {http_err.response.status_code}")
    except requests.exceptions.RequestException as err:   # Attrape toutes les autres erreurs possibles liées à la requête (problèmes de connexion, URL invalide, etc.)
        print(f"Erreur de connexion : {err}")