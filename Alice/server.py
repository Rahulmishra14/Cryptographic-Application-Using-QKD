from flask import Flask
import random,requests
from utils.generate_key import generateQubits
from logs.logging_service import generateLogs
from routes.apis import alice_bp

app = Flask("Cryptographic Application")
PORT=5500
app.register_blueprint(alice_bp)

if __name__ == '__main__':
    generateLogs(f"Alice Started at {PORT}","INFO")
    generateQubits(32)
    app.run(debug=True, port=PORT,use_reloader=True)
