import pandas as pd

# Charger les données du fichier Excel
fichier_excel = "medicaments__A_Z.xlsx"
df = pd.read_excel(fichier_excel)

# Renommer les colonnes
df.columns = ["Nom medicament", "Dosage", "Forme", "Prix (MAD)"]

# Supprimer les lignes où 'dosage', 'forme', ou 'prix (MAD)' ont la valeur "None"
df_before_none_removal = df.copy()  # Sauvegarder avant suppression
df = df[(df['Dosage'] != "None") & (df['Forme'] != "None") & (df['Prix (MAD)'] != "None")]

# Convertir le champ 'Prix (MAD)' en float
df['Prix (MAD)'] = df['Prix (MAD)'].str.extract(r'(\d+\.?\d*)')[0]  # Extraire les valeurs numériques
df['Prix (MAD)'] = pd.to_numeric(df['Prix (MAD)'], errors='coerce')  # Convertir en float, remplacer erreurs par NaN

# Arrondir à 2 chiffres après la virgule
df['Prix (MAD)'] = df['Prix (MAD)'].round(2)

# Supprimer les lignes où 'prix (MAD)' est NaN après la conversion
df_before_dropna = df.copy()  # Sauvegarder avant suppression
df = df.dropna(subset=['Prix (MAD)'])

# Uniformiser la colonne "Dose" (mettre en minuscule)
df["Dosage"] = df["Dosage"].str.lower().str.replace(r"\[.*?\]", "", regex=True).str.strip()

# Supprimer les espaces inutiles dans les colonnes de type chaîne
df["Nom medicament"] = df["Nom medicament"].str.strip()
df["Dosage"] = df["Dosage"].str.strip()
df["Forme"] = df["Forme"].str.strip()

# Sauvegarder les données nettoyées dans un nouveau fichier Excel
fichier_excel_nettoye = "nettoyage_medicaments.xlsx"
df.to_excel(fichier_excel_nettoye, index=False, engine='openpyxl')

