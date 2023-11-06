
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


