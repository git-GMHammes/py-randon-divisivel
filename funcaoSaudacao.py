#
# Criar uma função simples para saudação
#
def saudacao(tratamento='Olá', nome='Desconhecido'):
    return tratamento, nome


print(f'{saudacao()}')
print(f'{saudacao("Ola", "Gustavo")}')
print(f'{saudacao(nome="Orlando", tratamento="Bom dia")}')
