#atividade2:
    
turno = (input(" Em que turno você estuda? Digite 'm' para manhã, 'v' para tarde, 'n' para noite):"))
if turno == "m":
    print("Bom dia!")
elif turno == "v":
    print("Boa tarde!")
elif turno == "n":
    print("Boa noite!")
else:
    print("Entrada inválida por favor, digite 'm' para turno matutino,'v'para turno vespertino ou 'n' para noturno.")