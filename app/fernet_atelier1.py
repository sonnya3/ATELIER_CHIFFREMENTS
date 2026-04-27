import os
from cryptography.fernet import Fernet
import sys

def run_atelier():
    # 1. Récupération de la clé dans les variables d'environnement
    key = os.getenv('FERNET_KEY')
    
    if not key:
        print("❌ ERREUR : Le Secret 'FERNET_KEY' est introuvable.")
        sys.exit(1)

    f = Fernet(key.encode())
    
    # Exemple de message
    message = "Ceci est un message protégé par un Secret GitHub !".encode()
    
    # Chiffrement
    token = f.encrypt(message)
    print(f"🔒 Message chiffré : {token.decode()}")
    
    # Déchiffrement
    original = f.decrypt(token).decode()
    print(f"🔓 Message déchiffré : {original}")

if __name__ == "__main__":
    run_atelier()