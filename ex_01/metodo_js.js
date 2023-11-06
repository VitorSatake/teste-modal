/*
1) A ModalGR possui um cofre eletrônico que precisa estar protegido por 3 senhas, sendo 
essas criptografadas e armazenadas numa base de dados SQL. Cada uma dessas senhas deve 
possuir uma regra/método de criptografia distinta, mas ambas devem utilizar uma única 
chave secreta. Para isso, você foi escolhido para criar o sistema de criptografia dessas senhas.
Chave secreta:
#modalGR#GPTW#top#maiorEmpresaTecnologia#baixadaSantista
*/


const CryptoJS = require("crypto-js");

// Chave secreta 
const chave = "#modalGR#GPTW#top#maiorEmpresaTecnologia#baixadaSantista";

// Função para criptografar um texto
function encrypt(senha) {
  const metodo = CryptoJS.AES.encrypt(senha, chave).toString();
  return metodo;
}

// Função para descriptografar um texto criptografado
function decrypt(metodo) {
  const bytes = CryptoJS.AES.decrypt(metodo, chave);
  const original = bytes.toString(CryptoJS.enc.Utf8);
  return original;
}

// Criptografando e Descriptografando
const senha = "12345678";
const senhaCriptografada = encrypt(senha);
console.log("Senha Criptografada:", senhaCriptografada);

const senhaDescriptografada = decrypt(senhaCriptografada);
console.log("Senha Descriptografada:", senhaDescriptografada);


