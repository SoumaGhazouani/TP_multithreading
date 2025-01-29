# TP Multithreading

## Objectif
Ce projet implémente un système de traitement de tâches en utilisant le multithreading avec Python. Il repose sur une architecture où des "minions" exécutent des tâches en parallèle sous la supervision d'un "boss".

Les objectifs spécifiques de ce projet sont :

- Utiliser UV pour gérer un projet et ses dépendances.
- Créer une architecture avec un Queue Manager, un Boss et des Minions pour l'exécution des tâches.
- Utiliser des Minions en Python et C++ afin d'effectuer des mesures de performance.

## Structure et Description du Projet

L'architecture du projet est composée des éléments suivants :

- **Queue Manager (`QueueManager.py`)** : Gère les files de tâches et de résultats.
- **Boss (`Boss.py`)** : Crée les tâches, les ajoute dans la file des tâches et récupère les résultats.
- **Minions** : Récupèrent les tâches, les exécutent et ajoutent les résultats dans la file des résultats.
- **`task.py`** : Définit la classe `Task` qui représente une tâche à exécuter.
- **`README.md`** : Documentation du projet.

### Types de Minions

- **Minion Python (`Minion.py`)** : Minion implémenté en Python.
- **Minion C++ (`low_level.cpp`)** : Communique avec le gestionnaire de queue à l'aide d'un proxy Python (`proxy.py`) pour échanger des données sérialisées.

## Installation et Compilation

### Installer UV

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Cloner le dépôt

```sh
git clone git@github.com:SoumaGhazouani/TP_multithreading.git
cd TP_multithreading
```

### Synchroniser UV

```sh
uv sync
```

## Lancement et Exécution des Tâches

### Lancer les programmes

```sh
uv run manager.py
uv run proxy.py
uv run boss.py
```

Attendez que le boss envoie les tâches, puis exécutez :

```sh
uv run minion.py
```

### Compilation du code C++

Configurer le projet avec CMake (une seule fois) :

```sh
cmake -B build -S .
```

Compiler le projet :

```sh
cmake --build build
```

Exécuter le fichier compilé :

```sh
./build/low_level
```

## Résultats



