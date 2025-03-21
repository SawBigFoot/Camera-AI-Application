import base64
import os
from cryptography.fernet import Fernet

# Funksjon for å lage en langsom hash med PBKDF2
def hash_key_with_slowing(key: bytes) -> str:
    """
    Tar nøkkelen, lager et salt, og hasher den med PBKDF2 (langsom hash).
    Flere iterasjoner gjør det langsommere (jo flere, jo tregere).
    """
    from hashlib import pbkdf2_hmac
    
    # Lag et tilfeldig salt (32 bytes)
    salt = os.urandom(32)
 
    # PBKDF2 med 100,000 iterasjoner for å gjøre det langsommere
    hashed_key = pbkdf2_hmac('sha256', key, salt, 100000)
 
    # Konverter hash til heksadesimal streng
    hashed_key_hex = hashed_key.hex()
 
    # Skriver ut salt og den hashede nøkkelen (til debug)
    print(f"Salt (hex): {salt.hex()}")
    print(f"Hashed nøkkel: {hashed_key_hex}")
 
    return hashed_key_hex, salt
 
def load_key():
    """Laster den tidligere genererte Fernet-nøkkelen fra fil."""
    return open("crypt_.key", "rb").read()
 
def save_key_to_():
    """Genererer og lagrer en ny Fernet-nøkkel til fil."""
    key = Fernet.generate_key()
    with open('crypt_.key', 'wb') as crypt_:
        crypt_.write(key)
    return key
 
def encrypt_data(data):
    """Krypterer den gitte dataen og koder den for lagring i JSON."""
    key = load_key()  # Laster Fernet-nøkkelen
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data.encode())  # Krypterer dataen
    # Koder til Base64 for JSON-kompatibilitet
    return base64.urlsafe_b64encode(encrypted_data).decode()
 
def decrypt_data(encrypted_data):
    """Dekoder Base64-data og dekrypterer den gitte dataen."""
    key = load_key()  # Laster Fernet-nøkkelen
    fernet = Fernet(key)
    # Dekoder fra Base64 tilbake til bytes
    encrypted_data = base64.urlsafe_b64decode(encrypted_data)
    decrypted_data = fernet.decrypt(encrypted_data).decode()  # Dekrypterer dataen
    return decrypted_data
 
def main():
    # Genererer en Fernet-nøkkel og hasher den med PBKDF2 for å gjøre den langsom
    key = save_key_to_()  # Lagre Fernet-nøkkelen til fil
    hashed_key, salt = hash_key_with_slowing(key)  # Hash og salt nøkkelen
 
    # Du kan lagre den hashede nøkkelen og saltet på et trygt sted
    with open('crypt__salted.key', 'w') as crypt__salted:
        crypt__salted.write(f"Hashed key: {hashed_key}\nSalt: {salt.hex()}")
 
    # Krypter og dekrypter en melding som et eksempel
    data_to_encrypt = "Sensitive Data"
    
    print(f"Original Data: {data_to_encrypt}")
    
    # Krypter dataen
    encrypted_data = encrypt_data(data_to_encrypt)
    print(f"Kryptert Data: {encrypted_data}")
    
    # Dekrypter dataen
    decrypted_data = decrypt_data(encrypted_data)
    print(f"Dekryptert Data: {decrypted_data}")
 
if __name__ == "__main__":
    main()
 