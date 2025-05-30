from flask import Flask, Response

app = Flask(__name__)

@app.route("/webhook", methods=["GET", "POST"])
def handle_webhook():
    swml = """<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Say voice="Polly.Celine" language="fr-FR">Bonjour, vous êtes bien à la clinique.</Say>
    <Hangup/>
</Response>"""
    return Response(swml, mimetype='application/xml')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
