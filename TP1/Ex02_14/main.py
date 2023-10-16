#Exercício 2 de Processamento de Linguagens
#Elementos do grupo:
#Luis Esteves - 16960;
#Luís Gonçalves - 18851;

import ply.lex as plex
import funcAux

#Tokens que vamos utilizar ao longo do trabalho;
    #products -> Dedicado para ler frases do tipo : PRODUTO=twix=2.3=13.
    #products2 -> Dedicado para ler frases do tipo : PRODUTO=twix.
    #error -> Dedicado para dar erro para quando encontra frases do tipo : QUANTIA c20, c70.
    #money_on_machine -> Dedicado para ler frases do tipo : MOEDEIRO=0.
    #intro_money -> Dedicado para ler frases do tipo : QUANTIA c20, c70.
    #cancel -> Dedicado para ler frases do tipo : CANCELAR
    #skip -> Dedicado para passar \n,\t e \r a frente

tokens = ['PRODUCTS', 'PRODUCTS2', 'MONEY_ON_MACHINE', 'INTRO_MONEY', 'CANCEL', 'ERROR', 'SKIP']

#Inicialiazação das variáveis que vamos utilizar ao longo do programa
    #Dicionários que vão tratar de guardas as nossas frases já com o split feito
    #Produto, Preço e Quantidade
products_dictionary = {}
money_inserted = { '5cent' : 0, '10cent' : 0, '20cent' : 0, '50cent' : 0, '1e' : 0, '2e' : 0, 'total': 0.0, 'id' : 0}

    #Listas que vao guardar cada um dos elementos dos dicionários
products = []
amounts = []
prices = []
total_insertion = []
desired_product = []

    #Outras varíaveis
cancel = ""
money_on_machine = 0
id_count = 0
ok = 0


def t_PRODUCTS(t):
    r"PRODUTO=([a-zA-Z]+[ ]*[a-zA-Z]*)+=[0-9]+(\.)?[0-9]*=[0-9]+\."
    global products_dictionary, products, amounts, prices, ok
    if ok == 0:
        line = t.value
        tp = 0
        products_dictionary = funcAux.splitF(line, money_inserted, id_count, tp)
        l = funcAux.clear_points(products_dictionary["Quantidade"])
        products.append(products_dictionary["Produto"])
        amounts.append(l)
        prices.append(float(products_dictionary["Preco"]))


def t_MONEY_ON_MACHINE(t):
    r"MOEDEIRO[ ]*=[0-9]+\."
    global money_on_machine, money_inserted, ok
    if ok == 0:
        line = t.value
        line = funcAux.clear_points(line)
        tp = 1
        money_on_machine = funcAux.splitF(line, money_inserted, id_count, tp)


def t_INTRO_MONEY(t):
    r"QUANTIA([ ]*(c(5|10|20|50))?(e(1|2))?[ ]*(\,|\.))*"
    global money_inserted, id_count, total_insertion, ok
    money_inserted = {
        '1e': 0,
        '2e': 0,
        '50cent': 0,
        '20cent': 0,
        '10cent': 0,
        '5cent': 0,
        'total': 0.0,
        'id': 0
    }
    if ok == 1:
        line = t.value
        nAux = funcAux.found_points_commas(line)
        if nAux == 0:
            line = funcAux.clear_letter(line)
            tp = 4
            money_inserted = funcAux.splitF(line, money_inserted, id_count, tp)
            total_insertion.append(funcAux.count_money_id(money_inserted))
            id_count += 1
        else:
            tp = 2
            line = funcAux.clear_points(line)
            money_inserted = funcAux.splitF(line, money_inserted, id_count, tp)
            total_insertion.append(funcAux.count_money_id(money_inserted))
            id_count += 1


def t_PRODUCTS2(t):
    r"PRODUTO=([a-zA-Z]+[ ]*[a-zA-Z]*)+(\.)"
    global desired_product, ok
    if ok == 1:
        line = t.value
        line = funcAux.clear_points(line)
        tp = 3
        desired_product.append(funcAux.splitF(line, money_inserted, id_count, tp))

def t_ERROR(t):
    r"Error[0-9]+"
    pass

def t_CANCEL(t):
    r"CANCELAR|cancelar|Cancelar"
    global cancel
    cancel = t.value
    pass

def t_SKIP(t):
    r"\n|\t|\r"
    pass


lexer = plex.lex()
lexer.input(funcAux.slurp("Stock.txt"))
token = lexer.token()
ok = 1
lexer.input(funcAux.slurp("Vending_machine.txt"))
token = lexer.token()
print("------------------------------------------")

#Aqui aparece o menu em que o utizador vai poder análisar o texto como quiser.
funcAux.menu(products, total_insertion, desired_product, amounts, prices, money_on_machine)

