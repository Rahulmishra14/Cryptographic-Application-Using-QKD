from flask import Flask
import random,requests
from utils.exchange_keys import sendKeyToBob
from logs.logging_service import generateLogs

def generateQubits(length):
    """Generate a random sequence of bits."""
    key = [random.randint(0, 1) for _ in range(length)]
    bases=generateBases(length)
    generateLogs(f"Key & Bases Generated at Alice","WARNING")
    SECURE_KEYS=sendKeyToBob(key,bases)
    return SECURE_KEYS


def generateBases(length):
    """Randomly choose between two bases, 0 for Z basis and 1 for X basis."""
    return [random.randint(0, 1) for _ in range(length)]
