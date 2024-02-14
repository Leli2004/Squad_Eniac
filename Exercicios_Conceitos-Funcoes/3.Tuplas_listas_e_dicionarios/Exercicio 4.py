contatos = {
    'Lucas': '87878787',
    'Jessica': '545454545',
    'Tadeu': '445454',
    'Claudia': '55454545554'
}
def busca_contato(nome):
    if nome in contatos:
        return f"O número de telefone de {nome} é: {contatos[nome]}"
    else:
        return f"Contato {nome} não encontrado."


pesquisa = input("Digite o nome do contato que você deseja procurar: ")


resultado = busca_contato(pesquisa)
print(resultado)
