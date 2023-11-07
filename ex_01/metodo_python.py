'''
1) A ModalGR possui um cofre eletrônico que precisa estar protegido por 3 senhas, sendo 
essas criptografadas e armazenadas numa base de dados SQL. Cada uma dessas senhas deve 
possuir uma regra/método de criptografia distinta, mas ambas devem utilizar uma única 
chave secreta. Para isso, você foi escolhido para criar o sistema de criptografia dessas senhas.
Chave secreta:
#modalGR#GPTW#top#maiorEmpresaTecnologia#baixadaSantista

'''



import cryptocode

# criptografando a senha 12345678 e passando a chave secreta para descriptografar
chave = "#modalGR#GPTW#top#maiorEmpresaTecnologia#baixadaSantista"
senha = "12345678"
print(senha)
criptografando = cryptocode.encrypt(senha, chave)
print(criptografando)

descriptografando = cryptocode.decrypt(criptografando, chave)
print(descriptografando)


