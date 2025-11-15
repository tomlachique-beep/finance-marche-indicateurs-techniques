# Analyse technique de titres boursiers – Projet de Finance de Marché

Ce dépôt présente un projet d'analyse technique réalisé dans le cadre d'un cours de Finance de Marché.  
L'objectif est d'appliquer des indicateurs techniques classiques sur plusieurs actions européennes afin d'illustrer une démarche de data analysis appliquée aux marchés financiers.

##  Objectifs du projet

- Manipuler des séries temporelles de prix boursiers.
- Calculer plusieurs **indicateurs techniques** :
  - Moyennes mobiles (20 et 40 jours)
  - RSI (Relative Strength Index)
  - Indicateur stochastique
  - Bandes de Bollinger
- Mettre en forme les données pour une exploitation en **Python** (pandas / Jupyter).
.

---

##  Données

Les données sont stockées dans le fichier :

data/Finance_de_marche.xlsx

---

##  Indicateurs techniques étudiés

- **Moyennes mobiles (20/40)** : tendance court vs moyen terme.
- **RSI** : zones de surachat / survente.
- **Stochastique** : position du cours dans son range récent.
- **Bandes de Bollinger** : volatilité et excès de prix.

---

## Stack technique

- **Excel** : calculs et structuration des données brutes.
- **Python** (dossier `src/`) :
  - `pandas`, `numpy` pour la manipulation / calcul
  - `matplotlib` pour les graphiques
- **Jupyter Notebook** (dossier `notebooks/`) pour l’analyse exploratoire.

---

## Structure du projet

```text
.
├─ data/
│  └─ Finance_de_marche.xlsx
├─ src/
│  └─ indicators.py
├─ notebooks/
│  └─ 01_exploration_indicateurs_technique.ipynb
├─ README.md
├─ requirements.txt
```

## Compétences mises en avant

- Manipulation de données financières (time series)
- Calcul et interprétation d’indicateurs techniques
- Structuration d’un projet de data analyse (données + code + documentation)
- Maîtrise d’Excel et première utilisation de Python/pandas

---

##  Auteur

Projet réalisé par **Lachique Tom**  
Étudiant en **Master Information, Communication parcours Data analytics et stratégie de l'information** (Université de Toulon)  
À la recherche d’un **stage en data analyst**.

📩 E-mail : tom.lachique.135@gmail.com

🔗 LinkedIn : https://www.linkedin.com/in/tom-lachique-9b969427b/


