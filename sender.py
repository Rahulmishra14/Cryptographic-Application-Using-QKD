import requests

def get_secure_key(length):
    try:
        api_url='http://127.0.0.1:5500/api/generate_keys'
        data={
            "key_length":length
        }
        response=requests.post(api_url,json=data)
        if response.status_code==200:
            key_data=response.json()
            message = "HELLO World!       h    00112"
            encrypt_data_using_secure_key(key_data['keys']['key'],message)
    except Exception as e:
        print("Error Occurred while requesting key",e)

def string_to_bits(msg):
    # Convert a string to a binary representation
    return ''.join(format(ord(char), '08b') for char in msg)

def xor_strings(s1, s2):
    # XOR two binary strings
    return ''.join(str(int(a) ^ int(b)) for a, b in zip(s1, s2))

def send_encrypted_msg_to_receiver(msg):
    try:
        api_url='http://127.0.0.1:5503/receiver/msg-exchange'
        data={
            "message":msg
        }
        response=requests.post(api_url,json=data)
        if response.status_code==200:
            print("Msg Sent Successfully!!")
    except Exception as e:
        print("Error Occurred while requesting key",e)

def encrypt_data_using_secure_key(secure_key,msg):
    bits_conversion_using_OTP=string_to_bits(msg)
    encrypted_msg=xor_strings(bits_conversion_using_OTP,secure_key)
    print("Key Received from Alice",secure_key)
    print("Encrypted MSG",encrypted_msg)
    send_encrypted_msg_to_receiver(encrypted_msg)


get_secure_key(512)