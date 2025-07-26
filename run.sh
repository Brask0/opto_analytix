#!/bin/bash

if [ ! -d "venv"]; then
	echo ">>> L'environnement virtuel n'existe pas, Lance d'abord ./install.sh"
	exit 1
fi

echo ">> Activation de l'environnement virtuel..."
source venv/bin/activate

echo ">>> Lancement du programme..."
python main.py
