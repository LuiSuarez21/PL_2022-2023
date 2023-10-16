import funcAux
import codecs

#Opção 1
#Mostrar stock existente
def show_stock():
    documento = funcAux.slurp("Stock.txt")
    if documento != "":
        print("\n--------------------------------")
        print("Stock existente:\n")
        print(documento)


#Opção 2
#Algoritmo para encontrar um dado produto
def search_product(products, amounts):
    print("\n--------------------------------")
    validate = 0
    i = 0
    try:
        product = input("Digite o produto que deseja:")
        for p in products:
            if p == product:
                print(f"\nProduto encontrado: PRODUTO={product} com a QUANTIDADE={amounts[i]};")
                validate = 1
            i = i + 1
        if validate == 0:
            print("Produto Indisponível!")
    except:
        print("Erro na digitaçáo. Repita por favor.")
        print("------------------------------------------")


#Opção 3
#Algoritmo para encontrar um dado produto e adicionar ao stock
def add_product(products, amounts, prices, money):
    print("\n--------------------------------")
    try:
        product = input("Digite o produto que deseja:")
        new_quant = input("Digite a quantidade que quer inserir:")
        i = 0
        valide = 0
        iaux = 0
        f = 0
        for p in products:
            if p == product:
                fh = codecs.open("Stock.txt", 'w', encoding='utf-8')
                i = iaux
                valide = 1
                for p in products:
                    if (p == product):
                        fh.write(f"\nPRODUTO={product}={prices[i]}={int(new_quant)+int(amounts[i])}.")
                    else:
                        fh.write(f"\nPRODUTO={products[f]}={prices[f]}={amounts[f]}.")
                    f = f + 1
                fh.write(f"\nMOEDEIRO={money}.")
                fh.close()
            iaux = iaux + 1
            if iaux == len(amounts) and valide != 1 and valide != 2:
                print("\nProduto não existente!")
            elif valide != 2:
                print("\nInserção completa!")
                valide = 2
    except:
        print("Erro na digitaçáo. Repita por favor.")
        print("------------------------------------------")


#Opção 4
def buy_items(total_insertion, desired_product, products, price):
    print("\n--------------------------------")
    i = 0
    f = 0
    content = funcAux.slurp2("Vending_machine.txt")
    for line in content:
        if "QUANTIA" in line:
            print(line)
            print(f"\t -> valor inserido: €{total_insertion[f]} (saldo: €{total_insertion[f]}) ")
            f = i
            i += 1
        if "PRODUTO" in line:
            print(line)
            print(f"\t -> produto selecionado: {desired_product[i]} , preço: €{price[i]}")
            if float(price[i]) <= float(total_insertion[f]):
                print(f"\t -> compra bem sucedida! Troco: {total_insertion[f] - price[i]}")
            else:
                print(f"\tpreço: €{price[i]} (quantia insuficiente) (saldo: €{total_insertion[i]})")
            i = i + 1
        if '\n' in line or '\r' in line or '\t' in line:
            i = i


#Opção 5
#No caso de encontrar cancelar
def cancel(line, money_on_machine):
    if line != "":
        print(f"\n-> Compra cancelada! Devolvemos {money_on_machine}€.")