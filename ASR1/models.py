from django.db import models
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

class DatosPersonales(models.Model):
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    pais = models.CharField(max_length=15)
    ciudad = models.CharField(max_length=20)
    numero = models.CharField(max_length=10)
    email = models.EmailField()
    firma = models.TextField()

class SignatureKeys(models.Model):
    privateKey = models.TextField()
    publicKey = models.TextField()

    @classmethod
    def create(cls):
        privateKey = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        publicKey = privateKey.public_key()
        pemPrivateKey = privateKey.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        ).decode('utf-8')
        pemPublicKey = publicKey.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ).decode('utf-8')
        return cls(privateKey=pemPrivateKey, publicKey=pemPublicKey)