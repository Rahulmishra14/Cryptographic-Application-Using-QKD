from flask import Blueprint,Flask,request,jsonify
from utils.match_keys import process_qubits_and_bases
import os
from service.sqlite import get_data_from_db
from utils.match_keys import SHARED_KEY
bob_bp = Blueprint('BOB', __name__)

@bob_bp.route('/api/share-qubits-and-bases', methods=['POST'])
def get_qubits_and_bases():
    data=request.get_json()
    bob_sifted_keys=process_qubits_and_bases(data)
    response={
        "status":"success",
        "data":{
            "sifted_keys":bob_sifted_keys,
            "length":len(bob_sifted_keys)
        }
    }
    return response

@bob_bp.route('/api/get-shared-keys', methods=['GET'])
def get_secure_keys():
    data=get_data_from_db("KEY_STORE")
    response={
        "status":"success",
        "data":{
            "length":len(data[0][0]),
            "key":data[0][0]
        }
    }
    return response
