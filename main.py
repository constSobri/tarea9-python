def main():
    paises = input("Introduce una lista de paises separadas por comas:")
    listaPaises = paises.split(", ")
    paisesSet = set(listaPaises)
    lista = list(paisesSet)
    ordenados = sorted(lista)
    print(ordenados)


if __name__ == '__main__':
    main()
