from flask import Flask
import random,requests
# from utils.match_keys import generateBases
from logs.logging_service import generateLogs
from routes.apis import bob_bp
from service.sqlite import setup_db

app = Flask("Cryptographic Application")
PORT=5501
app.register_blueprint(bob_bp)

if __name__ == '__main__':
    generateLogs(f"BOB Started at {PORT}","INFO")
    setup_db()
    # generateBases(32)
    app.run(debug=True, port=PORT,use_reloader=True)
