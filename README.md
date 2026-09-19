#tirar os return 

def soma(n1, n2):
    resultado = n1 + n2
    print(f'A soma de {n1} mais {n2} é igual a: {resultado}')

def subtracao(n1, n2):
    resultado = n1 - n2
    print(f'A subtração de {n1} menos {n2} é igual a: {resultado}')

def divisao(n1, n2):
    resultado = n1/n2
    print(f'A divisão de {n1} com {n2} é igual a: {resultado}')

def multiplicacao(n1, n2):
    resultado = n1 * n2
    print(f'A multiplicação de {n1} com {n2} é igual a: {resultado}')

while True:
    opcao = str(input('Digite uma das opções: ( + | - | / | * ) ou digite sair: '))
    match opcao:
        case '+':
            n1 = int(input('Digite o primeiro numero: '))
            n2 = int(input('Digite o segundo numero: '))
            soma(n1, n2)
        case '-':
            n1 = int(input('Digite o primeiro numero: '))
            n2 = int(input('Digite o segundo numero: '))
            subtracao(n1, n2)
        case '/':
            n1 = int(input('Digite o primeiro numero: '))
            n2 = int(input('Digite o segundo numero: '))
            subtracao(n1, n2)
        case '*':
            n1 = int(input('Digite o primeiro numero: '))
            n2 = int(input('Digite o segundo numero: '))
            multiplicacao(n1, n2)
        case 'sair':
            break
        case _:
            print('Digite um opção valida por favor! ')
