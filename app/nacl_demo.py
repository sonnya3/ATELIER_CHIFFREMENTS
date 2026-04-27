import nacl.secret
import nacl.utils

key = nacl.utils.random(nacl.secret.SecretBox.KEY_SIZE)
box = nacl.secret.SecretBox(key)
message = b"Top Secret avec PyNaCl"
encrypted = box.encrypt(message)

print(f"🔒 Message chiffre (Hex) : {encrypted.hex()}")
print(f"🔓 Message dechiffre : {box.decrypt(encrypted).decode()}")
