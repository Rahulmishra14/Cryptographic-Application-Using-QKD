import requests
from logs.logging_service import generateLogs
SECURE_KEY=None


def sendKeyToBob(key,bases):
    try:
        generateLogs("Sending Key To BOB","WARNING")
        api_url='http://127.0.0.1:5501/api/share-qubits-and-bases'
        response={
            "status":"success",
            "data":{
                "module_name":"Alice",
                "qubits":key,
                "bases":bases,
                "length":len(key)
            }
        }
        print("Response",response)
        response=requests.post(api_url,json=response)
        if response.status_code == 200:
            generateLogs("Key Sent Successfully")
            rec=response.json()
            print("Response Rec from BOb",rec)
            global SECURE_KEY
            SECURE_KEY=rec['data']['sifted_keys']
            generateLogs(f"XORED Key Received {SECURE_KEY}")
            return SECURE_KEY
        else:
            generateLogs(f"Failed with status code {response.status_code}","ERROR")
    except Exception as e:
        generateLogs(f"An Unexpected Error Occurred while sending key to bob {e}","ERROR")