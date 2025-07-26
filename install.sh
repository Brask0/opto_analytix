#!/bin/bash

echo ">> Création de l'environnementvirtuel..."
python3 -m venv venv


echo "> Activation de l'environnement"
source venv/bin/activate

echo ">> Instalation des dépendances..."
pip install --upgrade pip
pip install -r requirements.txt

echo "> Instalation terminé!"
echo ">>> Active l'environnement avec: source venv/bin/activate"
