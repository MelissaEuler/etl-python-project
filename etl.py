# =========================
# ETL - Projeto de Estudo
# =========================

# 1. EXTRACT - Dados simulados
usuarios = [
    {
        "nome": "Ana",
        "conta": "12345-6",
        "cartao": "1111 2222 3333 4444"
    },
    {
        "nome": "Carlos",
        "conta": "98765-4",
        "cartao": "5555 6666 7777 8888"
    }
]

# 2. TRANSFORM - Criar mensagens personalizadas
mensagens = []

for usuario in usuarios:
    nome = usuario["nome"]
    conta = usuario["conta"]
    cartao = usuario["cartao"][-4:]

    mensagem = f"Olá {nome}! Sua conta {conta} possui um cartão final ****{cartao}."
    mensagens.append(mensagem)

# Visualização das mensagens transformadas
print(mensagens)

# 3. LOAD - Salvar mensagens em arquivo
with open("mensagens.txt", "w", encoding="utf-8") as arquivo:
    for mensagem in mensagens:
        arquivo.write(mensagem + "\n")