import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

def get_secure_key():
    try:
        api_url='http://127.0.0.1:5501/api/get-shared-keys'
        response=requests.get(api_url)
        data=response.json()
        print("Key Received from Bob",data)
        return data['data']['key']
    except Exception as e:
        print("Error Occurred while requesting key",e)

def bits_to_string(b):
    # Convert a binary string back to a regular string
    chars = [b[i:i+8] for i in range(0, len(b), 8)]
    return ''.join(chr(int(char, 2)) for char in chars)

def xor_strings(s1, s2):
    # XOR two binary strings
    return ''.join(str(int(a) ^ int(b)) for a, b in zip(s1, s2))


@app.route('/receiver/msg-exchange', methods=['POST'])
def msg_handler():
    data=request.get_json()
    secure_key=get_secure_key()
    xored_msg=xor_strings(data['message'],secure_key)
    decrypted_msg=bits_to_string(xored_msg)
    print("Msg FRom ALICE is",decrypted_msg)
    return "Success"


if __name__ == '__main__':
    app.run(port=5503)