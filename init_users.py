from app import create_app, db
from app.models import User

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()
    admin = User(username="admin", role="admin")
    admin.set_password("admin123")

    standard = User(username="user", role="standard")
    standard.set_password("user123")

    db.session.add_all([admin, standard])
    db.session.commit()
    print("Utilisateurs admin et standard créés avec succès.")
