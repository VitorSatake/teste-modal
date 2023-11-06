import cryptocode

# criptografando a senha 12345678 e passando a chave secreta para descriptografar
chave = "#modalGR#GPTW#top#maiorEmpresaTecnologia#baixadaSantista"
criptografando = cryptocode.encrypt("12345678", chave)
print(criptografando)

descriptografando = cryptocode.decrypt(criptografando, chave)
print(descriptografando)












'''
import os
from Cryptodome.Protocol.KDF import PBKDF2
chave_secreta = b'#modalGR#GPTW#top#maiorEmpresaTecnologia#baixadaSantista'  # Substitua pela sua chave secreta
salt = os.urandom(16)
senha = "123456".encode()
chave_derivada = PBKDF2(senha, salt, dkLen=32, count=100000)
print(senha)





import bcrypt
chave_secreta = "#modalGR#GPTW#top#maiorEmpresaTecnologia#baixadaSantista"
senha = "11111".encode()
senha_hashed = bcrypt.hashpw(senha, chave_secreta)

'''
