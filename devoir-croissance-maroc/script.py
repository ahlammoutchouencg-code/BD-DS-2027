import pandas as pd
import matplotlib.pyplot as plt

# 1. Import des données
df = pd.read_csv("dataset.csv")

fig, ax = plt.subplots(1, 3, figsize=(17, 5))
x = range(len(df))
w = 0.38

# Graphique 1 : PIB vs agriculture
ax[0].bar([i - w/2 for i in x], df["croissance_pib"], w, label="PIB", color="#1f4e79")
ax[0].bar([i + w/2 for i in x], df["croissance_agricole"], w, label="Agriculture", color="#c0392b")
ax[0].set_xticks(list(x))
ax[0].set_xticklabels(df["annee"])
ax[0].axhline(0, color="grey", linewidth=0.8)
ax[0].set_title("Croissance : PIB vs agriculture (%)")
ax[0].legend()

# Graphique 2 : chômage
ax[1].plot(df["annee"], df["chomage"], marker="o", label="Ensemble")
ax[1].plot(df["annee"], df["chomage_jeunes"], marker="o", label="Jeunes 15-24 ans")
ax[1].plot(df["annee"], df["chomage_diplomes"], marker="o", label="Diplômés")
ax[1].set_title("Taux de chômage (%)")
ax[1].set_xticks(df["annee"])
ax[1].legend()

# Graphique 3 : investissement vs épargne (2025)
last = df.iloc[-1]
ax[2].bar(["Investissement", "Épargne", "Besoin de\nfinancement"],
          [last["investissement_pct_pib"], last["epargne_pct_pib"], last["besoin_financement_pct_pib"]],
          color=["#1f4e79", "#27ae60", "#c0392b"])
ax[2].set_title("2025 : investissement vs épargne (% du PIB)")

plt.tight_layout()
plt.savefig("graphique.png", dpi=150)
plt.show()
