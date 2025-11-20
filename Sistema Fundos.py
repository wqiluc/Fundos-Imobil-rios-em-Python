from Validaçoes import validar_idade
from Validaçoes import validar_nome
from Validaçoes import validar_perfilrisco
from Validaçoes import validar_prazo
from Validaçoes import validar_valor
from Validaçoes import validar_cores
from time import sleep

def menuinicial():
    print("\n Por favor, insira as informaçoes abaixo :")
    print("""\n
    Valor disponível p/ investir (R$);
    Idade do investidor;
    Prazo do investimento (em anos);
    Perfil de risco""""")

VERDE = "\033[32m"
VERMELHO = "\033[31m"
LARANJA = "\033[33m"
NEGRITO = "\033[1m"
RESET = "\033[0m"
AZUL = "\033[34m"

continuar = "s".upper()

while continuar.upper() == "s":
    taxa = 0
    menuinicial()

    valordisponivel = validar_valor()
    nome = validar_nome()
    idade = validar_idade()
    prazo = validar_prazo()
    perfilrisco = validar_perfilrisco()

    banco_de_dados_usuario = {}

    print(f"{VERDE}Dados Coletados! ✅📊{RESET}", "\n")
    banco_de_dados_usuario["Seu Nome"] = nome 
    banco_de_dados_usuario["Valor Disponível"] =valordisponivel
    banco_de_dados_usuario["Idade"] = idade
    banco_de_dados_usuario["Prazo Máximo"] = prazo
    banco_de_dados_usuario["Perfil de Risco"] = perfilrisco

    print(f"{AZUL}", banco_de_dados_usuario, f"{RESET}")

    if idade >= 60 and prazo >= 5 and perfilrisco == "Arrojado":
        print(f"{VERMELHO}Não recomendamos esse cenário para você{RESET}")
    elif idade <= 10 and prazo >= 10:
        print(f"{NEGRITO}PARÁBENS!! você recebeu um bônus de 0.05 de taxa{RESET}")
        taxa += 0.05
    elif perfilrisco == "Conservador" and prazo < 2:
        print(f"{VERMELHO}Não recomendamos esse cenário para você. Rendimento baixíssimo.{RESET}")

    if perfilrisco == "Conservador":
        print("Taxa de 6% ao ano(0.06)")
        taxa += 0.06
    elif perfilrisco == "Moderado":
        print("Taxa de 9% ao ano(0.09)")
        taxa += 0.09
    else:
        print("Taxa de 13% ao ano(0.13)")
        taxa += 0.13

    montantefinal = valordisponivel * (1 + taxa) ** prazo
    print(f"{VERDE}Seu Montante final foi de: R${montantefinal:.2f}00{RESET}")
    print(f"{VERDE}O lucro obtido foi de: R${montantefinal - valordisponivel:.2f}00{RESET}")

    print(f"\n{LARANJA}Vamos agora avaliar seu rendimento..{RESET}")
    sleep(1)

    rentabilidade = ((montantefinal - valordisponivel) / valordisponivel) * 100
    print(f"\n{VERDE}Montante final: R${montantefinal:.2f}00{RESET}")
    print(f"{VERDE}Lucro obtido: R${montantefinal - valordisponivel:.2f}00{RESET}")
    print(f"{VERDE}Rentabilidade: {rentabilidade:.2f}%{RESET}")

    if rentabilidade < 25:
        print(f"{VERDE}Rentabilidade RAZOÁVEL{RESET}")
    elif 25 <= rentabilidade < 80:
        print(f"{VERDE}Rentabilidade BOA{RESET}")
    elif 80 <= rentabilidade < 100:
        print(f"{VERDE}Rentabilidade MUITO BOA{RESET}")
    else:
        print(f"{VERDE}Rentabilidade FANTÁSTICA! ACIMA DE 100%{RESET}")

    continuar = input("\nDeseja realizar outra simulação? (s/n): ").strip().lower()
    if (continuar.lower() == "s"):
        taxa = 0
        valordisponivel = 0
    elif (continuar.lower() == "n"):
        print(f"\n {AZUL} Obrigado(a) por usar nosso sistema🏦🌐\n{RESET} ")
        exit()