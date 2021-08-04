def divisores(num):
    try:
        if num < 0:
            raise ValueError("Ingrese un número positivo")
        divisor =[i for i in range(1,num+1) if num % i == 0]
        return divisor
    except ValueError as e:
        print(e)
        return False

def run():
    num = input("Ingrese un número: ")
    assert num.isnumeric(), "Ingrese un número"
    print(divisores(int(num)))
    print("El programa termino")

if __name__ == '__main__':
    run()