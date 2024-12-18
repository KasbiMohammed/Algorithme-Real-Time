# Algorithmes Temps Réel - Simulation en Python

Ce projet implémente et simule six algorithmes de planification en temps réel : **FCFS (First Come, First Served)**, **SJF (Shortest Job First)**, **RM (Rate Monotonic)**, **DM (Deadline Monotonic)**, **LLF (Least Laxity First)** et **EDF (Earliest Deadline First)**.

## Objectifs
Le but de ce projet est d'explorer, comparer et analyser les performances des algorithmes de planification temps réel pour des systèmes embarqués ou des applications critiques où le respect des délais est essentiel.

## Fonctionnalités
- Simulation des algorithmes FCFS, SJF, RM, DM, LLF et EDF.
- Visualisation des résultats et des métriques de performance.
- Interfaces interactives via **Streamlit**, **Flask**, ou **Django**.
- Analyse comparative entre les algorithmes.
- Facilité d’extension pour tester d’autres tâches ou algorithmes.

## Technologies Utilisées
- **Python** : Langage principal pour l'implémentation.
- **Matplotlib** : Visualisation des résultats.
- **Streamlit** : Interface utilisateur simple et interactive.
- **Flask** : API RESTful pour interagir avec les simulations.
- **Django** : Portail complet pour gérer les simulations et leurs résultats.

## Installation
1. Clonez le dépôt GitHub :
    ```bash
    git clone https://github.com/KasbiMohammed/Algorithme-Real-Time.git
    cd Algorithme-Real-Time
    ```

2. Installez les dépendances :
    ```bash
    pip install -r requirements.txt
    ```

## Instructions pour chaque framework

### Utilisation avec Streamlit
Streamlit fournit une interface simple et rapide :
1. Lancez l'application :
    ```bash
    streamlit run streamlit_app.py
    ```
2. Ouvrez [http://localhost:8501](http://localhost:8501) pour utiliser l'interface.

### Utilisation avec Flask
Flask expose une API RESTful :
1. Lancez le serveur :
    ```bash
    python flask_app.py
    ```
2. Accédez à l'API à [http://127.0.0.1:5000](http://127.0.0.1:5000).

### Utilisation avec Django
Django fournit une solution web robuste :
1. Initialisez la base de données :
    ```bash
    python manage.py migrate
    ```
2. Lancez le serveur :
    ```bash
    python manage.py runserver
    ```
3. Accédez à [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Utilisation
1. Configurez les tâches dans `tasks.json` ou via les interfaces utilisateur.
2. Sélectionnez un algorithme pour simuler et obtenir des résultats graphiques ou métriques.


