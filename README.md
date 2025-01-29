# TP Multithreading

## Objectif
Ce projet implémente un système de traitement de tâches en utilisant le multithreading avec Python et cpp. Il repose sur une architecture où des "Minions" exécutent des tâches en parallèle sous la supervision d'un "Boss".

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
uv run QueueManager.py
uv run proxy.py
uv run Boss.py
```

Attendez que le boss envoie les tâches, puis exécutez :

```sh
uv run Minion.py
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

Pour évaluer les performances, nous avons résolu des systèmes linéaires de la forme **AX = b**, où **X** est de taille aléatoire. Le boss envoie deux tâches de même taille aux deux minions (Python et C++), puis nous mesurons le temps d'exécution.

### Temps d'exécution pour différentes tailles de tâches

#### Taille `1122`

- **Minion Python** : `0.134559 sec`
- **Minion C++** : `0.43322 sec`

#### Taille `2895`
- **Minion Python** : `3.4403 sec`
- **Minion C++** : `11.415 sec`



### Analyse des performances

Contrairement aux attentes, Python est plus rapide que C++ dans ces tests. Cela est probablement dû à l’optimisation poussée de **NumPy**, qui exploite des bibliothèques sous-jacentes très performantes pour la résolution de systèmes linéaires.

Nous avons tenté d'améliorer les performances du Minion C++ en compilant avec l'option **Release** :

```sh
cmake -B build -S . -DCMAKE_BUILD_TYPE=Release
cmake --build build
```

Cependant, même avec cette optimisation, Python reste plus rapide que C++ dans ce contexte: 

#### Taille `1853`

- **Minion Python** : `0.1249259 sec`
- **Minion C++ avec l'option Release** : `1.08543 sec`

#### Taille `2395`

- **Minion Python** : `5.90942 sec`
- **Minion C++ avec l'option Release** : `6.76766 sec`


Ces résultats montrent que **C++ n'est pas toujours plus rapide que Python**, cela dépend de plusieurs facteurs :

- L'optimisation des bibliothèques utilisées (comme NumPy en Python qui exploite des optimisations bas niveau).
- La gestion de la mémoire et la parallélisation des calculs.
- L'implémentation spécifique des algorithmes dans chaque langage.

### Améliorations possibles

Pour améliorer les performances du Minion C++, nous pourrions explorer d'autres approches :

- **Utilisation d'OpenMP** : OpenMP permet d'exécuter les calculs en parallèle en répartissant les opérations sur plusieurs cœurs du processeur. Cela pourrait être appliqué pour traiter chaque ligne ou case de la matrice simultanément.

- **Optimisation du code C++** : L'utilisation de bibliothèques comme Eigen ou Armadillo permettrait d'exploiter des algorithmes optimisés et une meilleure gestion de la mémoire, offrant ainsi un gain de performance notable.

- **Exploitation du GPU** : CUDA et OpenCL permettent d'utiliser la carte graphique pour accélérer les calculs matriciels en parallèle, ce qui peut être bien plus rapide qu'une exécution sur CPU pour des matrices de grande taille.

## Conclusion

Ce projet illustre l'utilisation du multithreading en Python et C++, permettant d'évaluer l'impact de différentes implémentations sur les performances. L'utilisation de NumPy en Python s'est avérée être une solution plus performante que notre implémentation en C++. Ces résultats soulignent l'importance du choix des bibliothèques et des techniques d'optimisation pour améliorer l'efficacité des calculs. 

---

