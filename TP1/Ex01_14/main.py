#Exercício 1 de Processamento de Linguagens
#Elementos do grupo:
#Luis Esteves - 16960;
#Luís Gonçalves - 18851;

import ply.lex as plex

# 1.A -> Definir expressão regular que reconheça constantes com vírgula flutuante
# De salientar que no nosso projecto não aceitamos números como por exemplo "+1.232e2"

expr_reg = "(\-)?[0-9]+\.[0-9]+(e|E)(\-)?[0-9]+"


# 1.B -> Calcular o autómato determinista que implementa o reconhecimento da expressão regular;
#Em "Values" dizemos os valores que são admitidos pela a expressão regular;
#Em "Q" são os estados no nosso autómato, agora já um autómato determinista, explicado no relatório;

Values = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "", "-", "e", "E", "\."}
Q = {"q0", "q1", "q2", "q3", "q4"}

# 1.C -> Defenição da tabela de transição do autómato determinista e testar alguns exemplos
#Agora iremos demonstrar a tabela de transição, replicada nesta lista de estados e os valores que podem ser reconhecidos;


States = {
    "q0": {"-": "q1", "0": "q1", "1": "q1", "2": "q1", "3": "q1", "4": "q1", "5": "q1", "6": "q1", "7": "q1",
           "8": "q1", "9": "q1"},
    "q1": {"0": "q1", "1": "q1", "2": "q1", "3": "q1", "4": "q1", "5": "q1", "6": "q1", "7": "q1", "8": "q1",
           "9": "q1", ".": "q2"},
    "q2": {"0": "q2", "1": "q2", "2": "q2", "3": "q2", "4": "q2", "5": "q2", "6": "q2", "7": "q2", "8": "q2", "9": "q2",
           "e": "q3", "E": "q3"},
    "q3": {"-": "q4", "0": "q4", "1": "q4", "2": "q4", "3": "q4", "4": "q4", "5": "q4", "6": "q4", "7": "q4", "8": "q4",
           "9": "q4"},
    "q4": {"0": "q4", "1": "q4", "2": "q4", "3": "q4", "4": "q4", "5": "q4", "6": "q4", "7": "q4", "8": "q4", "9": "q4",}
    }


#Agora vamos pôr a prova a nossa expressão regular e ver se reconhece ou não correctamente números com vírgula flutoante;
#Função que trata de reconhecer o input introduzido

inicial_State = "q0"
final_State = "q4"
def match(number):
    actual_State = inicial_State
    l = len(number)
    i = 0
    error = 0
    while (i < l) and (error != 1):
        actual_caracter = number[i]
        if (actual_caracter in States[actual_State]):
            actual_State = States[actual_State][actual_caracter]
        else:
            error = 1
        i += 1
    return (actual_State in final_State) and (i == l)

#Menu em que o utilizador pode interagir e testar se é reconhecido ou não constantes com vírgulas flotoantes;
opc = 0;
while int(opc) != 2:
    print("-----------------------------------")
    print("1) Testar expressão regular;");
    print("2) Sair;")
    opc = input("\nInsira a opção que deseja: ")
    if int(opc) > 2 or int(opc) < 1:
        print("\nPor favor insira o valor 1 ou 2!")
    else:
        try:
            if int(opc) == 1:
                number = input("Insira uma constante com vírgula flutoante:");
                print(f"'{number}'\t{match(number)}");
        except:
            print("\nErro desconhecido! Por favor, insira uma constante com vírgula flutuante ou o valor 1 para sair do menu!")


