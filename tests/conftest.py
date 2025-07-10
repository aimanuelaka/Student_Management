import pytest
import os
import tempfile
from app import create_app, db
from app.models import User
from werkzeug.security import generate_password_hash

@pytest.fixture
def app():
    # Crée une app de test avec une base SQLite temporaire
    db_fd, db_path = tempfile.mkstemp()

    app = create_app()
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": f"sqlite:///{db_path}",
        "SQLALCHEMY_TRACK_MODIFICATIONS": False,
        "WTF_CSRF_ENABLED": False,
    })

    with app.app_context():
        db.create_all()

        # Crée les deux comptes uniquement si pas déjà présents
        if not User.query.filter_by(username="admin").first():
            admin = User(username="admin", role="admin", password_hash=generate_password_hash("admin123"))
            db.session.add(admin)

        if not User.query.filter_by(username="user").first():
            user = User(username="user", role="standard", password_hash=generate_password_hash("user123"))
            db.session.add(user)

        db.session.commit()

    yield app

    # Nettoyage à la fin du test
    os.close(db_fd)
    os.unlink(db_path)

@pytest.fixture
def client(app):
    return app.test_client()
