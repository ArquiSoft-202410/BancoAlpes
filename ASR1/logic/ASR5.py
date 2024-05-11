from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.serialization import load_pem_private_key, load_pem_public_key
from cryptography.hazmat.backends import default_backend
from ASR1.models import SignatureKeys
import base64

response, created = SignatureKeys.objects.get_or_create(id=1)
if created:
    newKeys = SignatureKeys.create()
    response.privateKey = newKeys.privateKey
    response.publicKey = newKeys.publicKey
    response.save()

privateKeyData = response.privateKey
publicKeyData = response.publicKey

def generateSignature(data):
    privateKey = load_pem_private_key(
        privateKeyData.encode(),
        password=None,
        backend=default_backend()
    )
    signature = privateKey.sign(
        data.encode(),
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return base64.b64encode(signature).decode('utf-8')

def verifySignature(data, signature):
    publicKey = load_pem_public_key(
        publicKeyData.encode(),
        backend=default_backend()
    )
    try:
        signature_bytes = base64.b64decode(signature)
        publicKey.verify(
            signature_bytes,
            data.encode(),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except Exception as e:
        print(e)
        return False