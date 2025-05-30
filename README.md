# SignalWire Webhook - Clinique

Application Flask minimale pour répondre à un appel SignalWire avec un message vocal en français.

## Fonctionnement

Quand un appel arrive, SignalWire interroge l'URL `/webhook`. Cette app répond avec un document XML (SWML) contenant :

> Bonjour, vous êtes bien à la clinique.

## Déploiement sur Render

1. Créez un dépôt GitHub avec ce code.
2. Sur [Render.com](https://render.com), créez un **Web Service** connecté à ce dépôt.
3. Render détectera Python automatiquement :
   - Build Command : `pip install -r requirements.txt`
   - Start Command : `gunicorn app:app`
4. Une fois déployé, copiez l’URL Render (ex. `https://voicebot-clinic.onrender.com`).

## Configuration SignalWire

- Allez dans **Phone Numbers > [votre numéro]**
- Choisissez : `Handle using SWML Script`
- Dans **FETCH MAIN SWML FROM URL** :  
  👉 `https://voicebot-clinic.onrender.com/webhook`
- Méthode : `POST`
