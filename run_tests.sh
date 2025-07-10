#!/bin/bash

# Aller à la racine du projet (le dossier contenant run.py)
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

# Définir le PYTHONPATH pour que pytest trouve le module app
export PYTHONPATH=.

# Lancer les tests avec affichage clair
echo "📦 Lancement des tests avec pytest..."
pytest tests/ -v --tb=short
