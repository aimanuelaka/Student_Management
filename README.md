# 🎓 Student Manager – Application Flask de gestion des étudiants

Application web développée avec **Flask** pour gérer :
- 👨‍🎓 Étudiants (CRUD)
- 📚 Matières (CRUD)
- 📝 Notes (CRUD + moyenne automatique)
- 🔐 Utilisateurs avec rôles : `admin` et `standard`
- 💻 Interface responsive en Bootstrap
- ✅ Tests unitaires, d’intégration et de charge

---

## 🚀 Technologies utilisées

- **Python 3.11+**
- [Flask](https://flask.palletsprojects.com/)
- Flask-Login / Flask-WTF / Flask-SQLAlchemy
- [Bootstrap 5](https://getbootstrap.com/)
- [SQLite](https://www.sqlite.org/index.html)
- [Pytest](https://docs.pytest.org/)
- [Locust](https://locust.io/) pour les tests de charge

---

## 📁 Arborescence du projet

```bash
student_manager/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes/
│   │   ├── auth.py
│   │   ├── admin.py
│   │   ├── student.py
│   │   ├── subject.py
│   │   └── note.py
│   ├── templates/
│   └── static/
├── tests/
│   ├── conftest.py
│   ├── test_models.py
│   ├── test_routes.py
│   ├── test_integration.py
│   ├── locustfile.py
│   └── load_test_threaded.py
├── run.py
├── init_users.py
├── requirements.txt
└── run_tests.sh


---

## 👥 Comptes tests préconfigurés
Nom d’utilisateur	Mot de passe	Rôle
admin	admin123	Administrateur
user	user123	Standard

---
## 🚀 Installation et lancement
1. Cloner le projet
```bash
Copier
Modifier
git clone <ton-repo-url>
cd student_manager
2. Créer un environnement virtuel Python et activer
```bash
Copier
Modifier
python3 -m venv venv
source venv/bin/activate       # Linux/macOS
venv\Scripts\activate.bat      # Windows
3. Installer les dépendances
```bash
Copier
Modifier
pip install -r requirements.txt
4. Initialiser la base de données et les comptes
```bash
Copier
Modifier
python init_users.py
5. Lancer le serveur Flask
```bash
Copier
Modifier
python run.py
L’application sera accessible sur http://127.0.0.1:5000

6. Accès
La racine / redirige vers la page de login /auth/login.

Utilise les comptes test pour te connecter.

## 🧪 Lancer les tests
Tests unitaires, fonctionnels et d’intégration
```bash
Copier
Modifier
./run_tests.sh
Tests de charge avec Locust
bash
Copier
Modifier
pip install locust
locust -f tests/locustfile.py
Ouvre http://localhost:8089, indique le nombre d’utilisateurs et démarre.

📝 Notes
Le rôle admin peut gérer tous les comptes, étudiants, matières, notes.

Le rôle standard ne voit que la liste des moyennes.

L’interface est responsive grâce à Bootstrap 5.

Les mots de passe sont stockés hashés avec Werkzeug.

🤝 Contribution
N’hésite pas à faire des PR, ouvrir des issues ou demander des fonctionnalités !
