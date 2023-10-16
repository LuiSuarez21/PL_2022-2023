# Exercício 2 de Processamento de Linguagens
# Elementos do grupo:
# Luis Esteves - 16960;
# Luís Gonçalves - 18851;

import codecs
import Opcs


# Tem o trabalho de ler o ficheiro
def slurp(filename):
    fh = codecs.open(filename, 'rb', encoding='utf-8')
    contents = fh.readlines()
    fh.close()
    documento = ""
    for linha in contents:
        documento = documento + linha
    return documento

def slurp2(filename):
    fh = codecs.open(filename, 'rb', encoding='utf-8')
    contents = fh.readlines()
    fh.close()
    return contents

# Faz split dos tokens encontrados.
def splitF(palavra, money_inserted, id_count, tipo):
    if tipo == 0:
        for letra in palavra:
            if letra == '=':
                p = palavra.split("=")
                palavras_dictionary = {"Produto": p[1].strip(), "Preco": float(p[2].strip()), "Quantidade": p[3].strip()}
                return palavras_dictionary
    if tipo == 1:
        for letra in palavra:
            if letra == '=':
                p = palavra.split("=")
                line = p[1].strip()
                return line
    if tipo == 2:
        ok = 0
        for letra in palavra:
            if letra == ',':
                p = palavra.split(",")
                i = 0
                for n in p:
                    p[i] = clear_letter(p[i])
                    p[i] = p[i].strip()
                    i = i + 1
                money_inserted = money_counter(p, money_inserted, id_count, ok)
                return money_inserted
    if tipo == 3:
        for letra in palavra:
            if letra == '=':
                p = palavra.split("=")
                line = p[1].strip()
                return line
    if tipo == 4:
        ok = 1
        money_inserted = money_counter(palavra, money_inserted, id_count, ok)
        return money_inserted


# Função para tirar os pontos encontrados no final das linhas
def clear_points(line):
    valide = i = 0
    lll = len (line)
    new_line = ""
    for l in line:
        if l == '.' and lll == (i+1):
            valide = 1
        i += 1
    if valide == 1:
        new_line = line.replace('.', "")
        return new_line
    else:
        return line

def found_points_commas(line):
    found = 0
    for digit in line:
        if digit == ',':
            found = 1
    return found


# Função para limpar letras do nosso input
def clear_letter(line):
    digits = ""
    for c in line:
        if c.isdigit():
            digits += c
    return digits


# Função que verifica o tipo de moeda e adiciona a um dicionario no caso de existir a tal moeda
def money_counter(amount_inserted, money_inserted, id_count, ok):
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
    if ok == 1 and int(amount_inserted) == 1:
        money_inserted['1e'] += 1
        money_inserted['id'] = id_count
        return money_inserted
    elif ok == 1 and int(amount_inserted) == 2:
        money_inserted['2e'] += 1
        money_inserted['id'] = id_count
        return money_inserted
    elif ok == 1 and int(amount_inserted) == 5:
        money_inserted['5cent'] += 1
        money_inserted['id'] = id_count
        return money_inserted
    elif ok == 1 and int(amount_inserted) == 10:
        money_inserted['10cent'] += 1
        money_inserted['id'] = id_count
        return money_inserted
    elif ok == 1 and int(amount_inserted) == 20:
        money_inserted['20cent'] += 1
        money_inserted['id'] = id_count
        return money_inserted
    elif ok == 1 and int(amount_inserted) == 50:
        money_inserted['50cent'] += 1
        money_inserted['id'] = id_count
        return money_inserted

    for m in amount_inserted:
        if int(m) == 1:
            money_inserted['1e'] += 1
        elif int(m) == 2:
            money_inserted['2e'] += 1
        elif int(m) == 5:
            money_inserted['5cent'] += 1
        elif int(m) == 10:
            money_inserted['10cent'] += 1
        elif int(m) == 20:
            money_inserted['20cent'] += 1
        elif int(m) == 50:
            money_inserted['50cent'] += 1
    money_inserted['id'] = id_count
    return money_inserted


# Função que soma o total de uma da quantia inserida
def count_money_id(money_inserted):
    euros = 0
    centimos = 0
    total = 0
    iaux = 0
    i = 6
    items = 0
    a = b = c = d = e = f = 0
    while i > 0:
        if int(money_inserted['1e']) != 0 and a == 0:
            v = money_inserted.get('1e')
            a = v
            items += 1 * v
        elif int(money_inserted['2e']) != 0 and b == 0:
            v = money_inserted.get('2e')
            b = v
            items += 1 * v
        elif int(money_inserted['5cent']) != 0 and c == 0:
            v = money_inserted.get('5cent')
            c = v
            items += 1 * v
        elif int(money_inserted['10cent']) != 0 and d == 0:
            v = money_inserted.get('10cent')
            d = v
            items += 1 * v
        elif int(money_inserted['20cent']) != 0 and e == 0:
            v = money_inserted.get('20cent')
            e = v
            items += 1 * v
        elif int(money_inserted['50cent']) != 0 and f == 0:
            v = money_inserted.get('50cent')
            f = v
            items += 1 * v
        i -= 1
        iaux += 1

    a = b = c = d = e = f = iaux = 0
    while items > 0:
        if int(money_inserted['1e']) != 0 and a == 0:
            v = money_inserted.get('1e')
            a = v
            euros += 1 * v
        elif int(money_inserted['2e']) != 0 and b == 0:
            v = money_inserted.get('2e')
            b = v
            euros += 2 * v
        elif int(money_inserted['5cent']) != 0 and c == 0:
            v = money_inserted.get('5cent')
            c = v
            centimos += 5 * v
        elif int(money_inserted['10cent']) != 0 and d == 0:
            v = money_inserted.get('10cent')
            d = v
            centimos += 10 * v
        elif int(money_inserted['20cent']) != 0 and e == 0:
            v = money_inserted.get('20cent')
            e = v
            centimos += 20 * v
        elif int(money_inserted['50cent']) != 0 and f == 0:
            v = money_inserted.get('50cent')
            f = v
            centimos += 50 * v
        items -= 1
        iaux += 1
    while centimos > 100:
        euros += 1
        centimos -= 100
    total += euros
    centimos /= 100
    total += centimos
    return float(total)


def menu(products, total_insertion, desired_product, amounts, prices, money_on_machine):
    numero = 0
    while numero != '6':
        print("------------------------------------")
        print("------------ Vending Machine --------------")
        print("\n1) Mostrar stock existente;")
        print("2) Procurar um produto;")
        print("3) Adicionar uma quantidade nova a um produto já existente;")
        print("4) Consultar compras feitas;")
        print("5) Sair;")
        try:
            numero = input("Digite a opção que deseja:\n")
            if numero.isdigit():
                if numero == '1':
                    Opcs.show_stock()
                if numero == '2':
                    Opcs.search_product(products, amounts)
                elif numero == '3':
                    Opcs.add_product(products, amounts, prices, money_on_machine)
                elif numero == '4':
                    Opcs.buy_items(total_insertion, desired_product, products, prices)
            else:
                print("Erro!Insira um numero entre 1-5.")
        except:
            print("Erro!Digite algum numero por favor.")
