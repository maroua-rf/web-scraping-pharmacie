import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import re
import seaborn as sns
import pandas as pd

# Chargement des données depuis le fichier Excel
df = pd.read_excel("nettoyage_medicaments.xlsx")

# Créer un graphique de nuage de points des prix
plt.figure(figsize=(10, 6))
sns.scatterplot(x=df.index, y=df['Prix (MAD)'], color='blue', alpha=0.6)

# Ajouter des labels
plt.title('Nuage des Prix des Médicaments')
plt.xlabel('Index')
plt.ylabel('Prix (DH)')

# Afficher le graphique
plt.show()

# 1. Distribution des prix des médicaments
plt.figure(figsize=(10, 6))
plt.hist(df['Prix (MAD)'], bins=20, color='skyblue', edgecolor='black')
plt.title('Distribution des prix des médicaments')
plt.xlabel('Prix')
plt.ylabel('Nombre de médicaments')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# 2. boxplot (ou boîte à moustaches)
plt.figure(figsize=(10, 6))
sns.boxplot(x=df['Prix (MAD)'])
plt.title('Boxplot des prix des médicaments')
plt.xlabel('Prix')
plt.show()

# Les 5 médicaments les plus chers
top_5_chers = df.sort_values(by='Prix (MAD)', ascending=False).head(5)

plt.figure(figsize=(10, 6))
sns.barplot(x='Prix (MAD)', y='Nom medicament', data=top_5_chers, palette='viridis')
plt.title('Top 5 des médicaments les plus chers')
plt.xlabel('Prix')
plt.ylabel('Nom du médicament')
plt.show()

# 3. Les 5 médicaments les moins chers
top_5_moins_chers = df.sort_values(by='Prix (MAD)', ascending=True).head(5)

plt.figure(figsize=(10, 6))
sns.barplot(x='Prix (MAD)', y='Nom medicament', data=top_5_moins_chers, palette='coolwarm')
plt.title('Top 5 des médicaments les moins chers')
plt.xlabel('Prix')
plt.ylabel('Nom du médicament')
plt.show()

# 4. Fréquence des mots dans les noms des médicaments
# Combiner tous les noms des médicaments
all_names = ' '.join(df['Nom medicament'].astype(str))

# Nettoyer les noms : suppression des caractères spéciaux et passage en minuscule
cleaned_names = re.sub(r'[^a-zA-ZÀ-ÿ\s]', '', all_names).lower()

# Diviser les mots
word_list = cleaned_names.split()

# Compter la fréquence des mots
word_counts = Counter(word_list)

# Afficher les 10 mots les plus fréquents
print("Les 10 mots les plus fréquents dans les noms des médicaments :")
for word, count in word_counts.most_common(10):
    print(f"{word} : {count}")

# 5. Visualisation des mots les plus fréquents (optionnel)
top_words = dict(word_counts.most_common(10))
plt.figure(figsize=(10, 6))
plt.bar(top_words.keys(), top_words.values(), color='lightgreen')
plt.title("Top 10 des mots les plus fréquents dans les noms des médicaments")
plt.xticks(rotation=45)
plt.ylabel("Fréquence")
plt.show()