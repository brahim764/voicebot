import os
import pickle
import google.auth.transport.requests
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ["https://www.googleapis.com/auth/calendar"]

flow = InstalledAppFlow.from_client_secrets_file(
    "client_secret.json", SCOPES
)
creds = flow.run_local_server(port=0)

# Sauvegarder le token
with open("token.json", "w") as token:
    token.write(creds.to_json())

print("✅ Token enregistré avec succès.")
