from Lions import database, app
from Lions.models import Usuario, Foto


with app.app_context():
    database.create_all()