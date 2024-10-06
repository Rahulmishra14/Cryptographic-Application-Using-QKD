import requests
from logs.logging_service import generateLogs
XORED_KEY=None


def sendKeyToBob(key,bases):
    try:
        generateLogs("Sending Key To BOB","WARNING")
        api_url='http://127.0.0.1:5501/api/get-key'
        response={
            "status":"success",
            "data":{
                "module_name":"Alice",
                "qubits":key,
                "bases":bases
            }
        }
        print("Response",response)
        response=requests.post(api_url,json=response)
        if response.status_code == 200:
            generateLogs("Key Sent Successfully")
            rec=response.json()
            global XORED_KEY
            XORED_KEY=rec['message']['XORED_KEY']
            generateLogs(f"XORED Key Received {XORED_KEY}")
        else:
            generateLogs(f"Failed with status code {response.status_code}","ERROR")
    except Exception as e:
        generateLogs(f"An Unexpected Error Occurred while sending key to bob {e}","ERROR")