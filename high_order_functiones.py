from functools import reduce

def run():
    my_list = [1,4,5,6,9,13,19,21]
    #filter toma cada valor del iterable para comprobar la condicion devolviendo un iterador por lo que creamos una lista para imprimir el iterador
    odd = list(filter(lambda x: x % 2 != 0, my_list))

    print (odd)

    list_two  = [1,2,3,4,5]
    #map toma cada valor del iterable y ejecuta la funcion sobre cada uno de los elementos e igual que filter creamos una lista
    squares = list(map(lambda x: x**2, list_two))

    print (squares)

    list_tree = [2,2,2,2,2]
    #reduce para usarla tenemos que importalo desde functools y tiene los mismos argumantos que los anteriores pero esta funcion recibe dos parametros uno que almacena el resultado(o el primer valor del iterable) y otro que opera con el siguiente valor del iterable
    all_multiplied = reduce(lambda a,b : a*b, list_tree)

    print (all_multiplied)

if __name__ == '__main__':
    run()