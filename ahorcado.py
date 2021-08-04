import random 
import os

def open_file():
    works=[]
    with open("./archivos/palabras.txt", "r", encoding="utf-8") as f:
        for line in f:
            works.append(line.strip().upper())
    return works

def run():
    data = open_file()
    chosen_word = random.choice(data)
    word_list = [letter for letter in chosen_word]
    list_underscores = ["_"] * len(word_list)
    letter_index_dict = {}
    for idx, letter in enumerate(chosen_word):
        if not letter_index_dict.get(letter): 
            letter_index_dict[letter] = []
        letter_index_dict[letter].append(idx)
    
    while True:
        os.system("clear") 
        print("Adivina la palabra!")
        for element in list_underscores:
            print(element + " ", end="")
        print("\n")

        letter = input("Ingresa una letra: ").strip().upper()
        assert letter.isalpha(), "Solo puedes ingresar letras"

        if letter in word_list:
            for idx in letter_index_dict[letter]:
                list_underscores[idx] = letter
        
        if "_" not in list_underscores:
            os.system("clear") 
            print("Ganaste! La palabra era", chosen_word)
            break

if __name__ == '__main__':
    run()