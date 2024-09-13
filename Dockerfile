# Utiliser une image de base Python 3.12 pour notre application
FROM python:3.12-slim

# Installer les bibliothèques système nécessaires
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Installer les dépendances Python, y compris PySide6
RUN pip install --no-cache-dir pyside6

# Copier le code de notre application dans le répertoire de travail
COPY . /app

# Exécuter la commande pour lancer l'application
CMD ["python", "Main.py"]
