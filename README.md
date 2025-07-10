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
