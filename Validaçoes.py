def validar_valor():
    while True:
        valor = input("\nDigite o valor disponível para investir: R$ ")
        valor = valor.replace(".", "").replace(",", ".")
        try:
            valor = float(valor)
            if valor <= 0:
                print("\033[31mERRO!! O valor deve ser maior que zero. Digite novamente.\033[0m")
                continue
            return valor
        except ValueError:
            print("\033[31mERRO!! Valor inválido. Digite novamente.\033[0m")

def validar_nome():
    while True:
        nome = input("Digite seu nome: ").strip().lower()
        if nome.replace(" ", "").isalpha():
            return nome.title()
        print("\033[31mERRO!! Digite apenas letras e espaços.\033[0m")



def validar_idade():
    while True:
        idade = input("\nDigite a idade do investidor: ")
        if not idade.isdigit():
            print("\033[31mERRO!! Idade inválida. (Digite apenas números inteiros.)\033[0m")
            continue
        idade = int(idade)
        if idade <= 0:
            print("\033[31mERRO!! A idade deve ser maior que zero. Digite novamente.\033[0m")
            continue
        return idade


def validar_prazo():
    while True:
        prazo = input("\nDigite o prazo máximo do investimento (em anos): ")
        if not prazo.isdigit():
            print("\033[31mERRO!! Prazo inválido. (Digite apenas números inteiros.)\033[0m")
            continue
        prazo = int(prazo)
        if prazo <= 0:
            print("\033[31mERRO!! O prazo deve ser maior que zero. Digite novamente.\033[0m")
            continue
        return prazo
    
def validar_perfilrisco():
    perfis = ["conservador", "moderado", "arrojado"]
    while True:
        perfil = input("\nDigite o seu perfil de risco de investidor: ").strip().lower()
        if perfil in perfis:
            return perfil.capitalize()
        print("\033[31mERRO! Digite um dos perfis disponíveis:\033[0m")
        print("""
        Conservador
        Moderado
        Arrojado
        """)


def validar_cores():
    VERDE = "\033[32m"
    VERMELHO = "\033[31m"
    LARANJA = "\033[33m"
    NEGRITO = "\033[1m"
    RESET = "\033[0m"
    AZUL = "\033[34m"
