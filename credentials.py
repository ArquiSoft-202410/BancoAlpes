from BancoAlpes import settings
import json

data = {
    "type": "service_account",
    "project_id": settings.PROJECT_ID,
    "private_key_id": settings.PRIVATE_KEY_ID,
    "private_key": settings.PRIVATE_KEY,
    "client_email": settings.CLIENT_EMAIL,
    "client_id": settings.CLIENT_ID,
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/749913748910-compute@developer.gserviceaccount.com",
    "universe_domain": "googleapis.com"
}

with open('ASR2/static/json/credentials.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)
