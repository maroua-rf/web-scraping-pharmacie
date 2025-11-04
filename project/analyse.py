import pandas as pd

# Chargement des données depuis le fichier Excel
df = pd.read_excel("nettoyage_medicaments.xlsx")

# Statistiques de base
print(df["Prix (MAD)"].describe())

# Afficher les 5 médicaments les plus chers
print("Les 5 médicaments les plus chers :")
top_5_chers = df.sort_values(by="Prix (MAD)", ascending=False).head(5)
print(top_5_chers[["Nom medicament", "Prix (MAD)"]])

# Afficher les 5 médicaments les moins chers
print("\nLes 5 médicaments les moins chers :")
top_5_moins_chers = df.sort_values(by="Prix (MAD)", ascending=True).head(5)
print(top_5_moins_chers[["Nom medicament", "Prix (MAD)"]])

# Afficher les 5 dosages les plus fréquents
print("\nLes 5 dosages les plus fréquents :")
top_5_dosages = df['Dosage'].value_counts().head(5)
print(top_5_dosages)