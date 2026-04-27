import nacl.secret
import nacl.utils

# 1. Génération d'une clé aléatoire sécurisée (32 octets)
key = nacl.utils.random(nacl.secret.SecretBox.KEY_SIZE)
box = nacl.secret.SecretBox(key)

# 2. Message à protéger
message = b"Top Secret avec PyNaCl"

# 3. Chiffrement
encrypted = box.encrypt(message)
print(f"📦 Message chiffré (Hex) : {encrypted.hex()}")

# 4. Déchiffrement
decrypted = box.decrypt(encrypted)
print(f"🔓 Message déchiffré : {decrypted.decode()}")