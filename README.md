# Analyse technique de titres boursiers – Projet de Finance de Marché

Dans le cadre de mon cours de Finance de Marché à l'Université de Toulon, j'y présente un projet d'analyse technique que j'ai réalisé.
Mon but était d'utiliser des indicateurs techniques traditionnels sur diverses actions européennes. C'était pour moi l'opportunité d'appliquer une approche intégrale d'analyse des données dans le contexte des marchés financiers.

##  Objectifs du projet

Dans le cadre de ce projet, j'ai d'abord pris le temps de me familiariser avec la gestion des séries temporelles liées aux prix boursiers.

Par la suite, j'ai déterminé et mis en œuvre divers indicateurs techniques majeurs, y compris les moyennes mobiles (sur 20 et 40 jours), le RSI, l'indicateur stochastique ainsi que les bandes de Bollinger.

Finalement, l'un des buts principaux était d'organiser les données de manière à ce qu'elles puissent être traitées efficacement en Python, en utilisant pandas et Jupyter.


---

##  Données

Les données que j'ai utilisées sont stockées dans le fichier data/Finance_de_marche.xlsx. Je les ai récupérées manuellement depuis le site ABC Bourse pour les besoins de cet exercice académique.

---

##  Indicateurs techniques étudiés

- **Moyennes mobiles (20/40)** : tendance court vs moyen terme.
- **RSI** : zones de surachat / survente.
- **Stochastique** : position du cours dans son range récent.
- **Bandes de Bollinger** : volatilité et excès de prix.

---
## Exemple de graphique produit avec Python

![Graphique BMW](Figure_1.png)

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






