
usuarios = {
    "pedro": "admin",
    "maria": "editor",
    "joao": "visualizador"
}

permissoes = {
    "admin": ["ler", "escrever", "deletar"],
    "editor": ["ler", "escrever"],
    "visualizador": ["ler"]
}

nome = input("Digite o nome do usuário: ").lower()
acao = input("Digite a ação desejada (ler, escrever, deletar): ").lower()

if nome in usuarios:
    papel = usuarios[nome]
    if acao in permissoes[papel]:
        print(f"Acesso PERMITIDO ✅ - {nome} pode {acao}")
    else:
        print(f"Acesso NEGADO ❌ - {nome} NÃO pode {acao}")
else:
    print("Usuário não encontrado ❌")