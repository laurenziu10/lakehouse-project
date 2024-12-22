# Datenbankverbindung (z.B. für Delta Lake oder Parquet)
SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/superset.db'

# Verschiedene Superset-Einstellungen
APP_NAME = "Lakehouse Dashboard"
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Sicherheitskonfiguration
SECRET_KEY = 'your_secret_key_here'
SESSION_COOKIE_SECURE = False  # False für lokale Entwicklung
CSRF_ENABLED = True

# Wählen Sie den Authentifizierungsmechanismus
AUTH_TYPE = 1  # 1 = Database authentication
AUTH_USER_REGISTRATION = True  # Benutzerregistrierung aktivieren
AUTH_USER_REGISTRATION_ROLE = "Gamma"  # Rolle der registrierten Benutzer

# Für Delta oder Parquet kannst du SQLAlchemy oder andere Data-Layer verwenden.
# Beispiel: Wenn du Delta mit PySpark verwendest, könntest du eine Verbindung zu einem Delta-Lake-Standort herstellen.
