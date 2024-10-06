from flask import Blueprint,Flask,request,jsonify
from utils.generate_key import generateQubits
alice_bp = Blueprint('ALICE', __name__)

@alice_bp.route('/api/generate_keys', methods=['POST'])
def get_qubits_and_bases():
    data=request.get_json()
    key_length=int(data['key_length'])
    SECURE_KEY=generateQubits(key_length)
    sifted_key_str = ''.join(map(str, SECURE_KEY))
    response={
        "status":"success",
        "keys":{
            "length":len(sifted_key_str),
            "key":sifted_key_str
        }
    }
    return response
