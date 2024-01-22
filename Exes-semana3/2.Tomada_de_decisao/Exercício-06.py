#06 - Crie um programa que solicite ao usuário um login e uma senha. O programa deve permitir o acesso apenas se o usuário for "admin" e a senha for "admin123", caso contrário imprima uma mensagem de erro.

# Defina as credenciais corretas
login_correto = "admin"
senha_correta = "admin123"

# Loop infinito para solicitar login e senha até que as credenciais corretas sejam fornecidas
while True:
    login = input("Digite seu login: ")
    senha = input("Digite sua senha: ")

    if login == login_correto and senha == senha_correta:
        # Se as credenciais forem corretas, saia do loop
        print("Acesso permitido. Bem-vindo, admin!")
        break
    else:
        # Se as credenciais forem incorretas, exiba uma mensagem de erro
        print("Login ou senha incorretos. Tente novamente.")