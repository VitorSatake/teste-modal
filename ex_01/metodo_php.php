

<?php
// Chave secreta
$chave_secreta = "#modalGR#GPTW#top#maiorEmpresaTecnologia#baixadaSantista";

// Senha a ser criptografada
$senha = "12345678";

// Algoritmo de criptografia
$algoritmo = 'aes-256-cbc';

// Gerar um vetor de inicialização (IV) aleatório
$iv = openssl_random_pseudo_bytes(openssl_cipher_iv_length($algoritmo));

// Criptografar a senha
$senha_criptografada= openssl_encrypt($senha, $algoritmo, $chave_secreta, 0, $iv);

// Encode o IV em base64 para ser usado na descriptografia
$iv_base64 = base64_encode($iv);

echo "Senha original: $senha\n";
echo "Senha criptografada: $senha_criptografada\n";


// Descriptografar a senha
$senha_decifrada = openssl_decrypt($senha_criptografada, $algoritmo, $chave_secreta, 0, base64_decode($iv_base64));

echo "Senha descriptografada: $senha_decifrada\n";
?>

