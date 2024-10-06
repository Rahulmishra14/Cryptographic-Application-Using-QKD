from flask import Flask
import random,requests
from utils.exchange_keys import sendKeyToBob
from dotenv import load_dotenv, set_key
import os
from logs.logging_service import generateLogs
from service.sqlite import insert_data,execute_query
SHARED_KEY=None
load_dotenv('.env')

def process_qubits_and_bases(data):
    """Randomly choose between two bases, 0 for Z basis and 1 for X basis."""
    length=data['data']['length']
    alice_qubits=data['data']['qubits']
    alice_bases=data['data']['bases']
    bob_bases= [random.randint(0, 1) for _ in range(length)]
    print("Bob bases",bob_bases)
    bob_sifted_key=measure_keys(alice_qubits,alice_bases,bob_bases)
    return bob_sifted_key

def measure_keys(alice_qubits,alice_bases,bob_bases):
    bob_bits= [alice_qubits[i] if alice_bases[i] == bob_bases[i] else random.randint(0, 1) for i in range(len(alice_qubits))]
    bob_sifted_key = sift_keys(alice_bases, bob_bases, bob_bits)
    return bob_sifted_key

def sift_keys(alice_bases, bob_bases, bob_bits):
    """Sift keys to keep only the bits where Alice and Bob used the same basis."""
    sifted_keys= [bob_bits[i] for i in range(len(bob_bits)) if alice_bases[i] == bob_bases[i]]
    adjusted_keys=adjust_generated_keys(sifted_keys,len(alice_bases))
    return adjusted_keys

def adjust_generated_keys(sifted_keys,length):
    while len(sifted_keys) < length:
        sifted_keys.append(random.randint(0, 1))

    clear_table="DELETE FROM KEY_STORE"
    execute_query(clear_table)
    sifted_key_str = ''.join(map(str, sifted_keys))
    query = f'''INSERT INTO KEY_STORE VALUES("{sifted_key_str}")'''
    insert_data(query)
    # set_key('.env', 'SHARED_KEY', sifted_key_str)
    return sifted_keys


    
