def main():
    entrada_lados = input().split()
    lista = []

    for i in entrada_lados:
        i = float(i)
        lista.append(i)

    lista.sort(reverse=True)
    l1 = lista[0]
    l2 = lista[1]
    l3 = lista[2]

    existe_Ou_nao = condicao_de_existencia_triangulo(l1, l2, l3)
    tipo_do_triangulo(existe_Ou_nao, l1, l2, l3)


def condicao_de_existencia_triangulo(l1, l2, l3):
    existe = True
    if 0 < l1 and 0 < l2 and 0 < l3:
        if l1 >= l2 + l3 or l2 >= l3 + l1 or l3 >= l2 + l1:
            existe = False
            print("NAO FORMA TRIANGULO")
            return existe

        else:
            return existe
    else:
        existe = False
        return existe


def tipo_do_triangulo(existe, l1, l2, l3):
    if existe:
        if l1 ** 2 == (l2 ** 2) + (l3 ** 2):
            print("TRIANGULO RETANGULO")
        elif l1 ** 2 > (l2**2) + (l3**2):
            print("TRIANGULO OBTUSANGULO")
        elif l1**2 < (l2**2) + (l3**2):
            print("TRIANGULO ACUTANGULO")

        if l1 == l2 == l3:
            print("TRIANGULO EQUILATERO")
        elif l1 == l2 and l1 != 3 or l1 == l3 and l1 != l2 or l2 == l1 and l2 != l3 or l2 == l3 and l2 != l1 or l3 == l2 and l3 != l1 or l3 == l1 and l3 != l2:
            print("TRIANGULO ISOSCELES")


main()
