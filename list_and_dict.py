def main():
    my_list=[1, "hello", True, 4.5]
    my_dict={"firstname": "David", "lastname": "Granados"}

    super_list=[
        {"firstname": "Israel", "lastname": "Granados"},
        {"firstname": "Liv", "lastname": "Galan"},
        {"firstname": "abigail", "lastname": "Galan"}
    ]

    super_dict={
        "natural_nums":[1,2,3,4,5],
        "integer_nums":[-1,-2,0,1,2],
        "floating_nums":[1.1,4.5,6.45]
    }

    for key, value in super_dict.items():
        print(key, "-", value)

if __name__ == '__main__':
    main()