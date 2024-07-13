
def characters_counter(palabras):
    character_counts = {

    }
    for char in palabras:
        if char in character_counts:
            character_counts[char] += 1
        else:
            character_counts[char] = 1
    
    return character_counts



def main():
    # Ruta relativa al archivo
    path_to_file = "books/frankenstein.txt"
    
    # Abrir y leer el archivo
    with open(path_to_file, 'r') as f:
        file_contents = f.read()
    contador = 0
    listalower = []

    # Imprimir el contenido del archivo
    word_counts = file_contents.split()

    for words in word_counts:
        listalower.append(words.lower())
        contador = contador +1
    print(contador)

    character_counts = characters_counter(file_contents.lower())
    print(character_counts)
    
    

# Llamar a la función main
if __name__ == "__main__":
    main()
