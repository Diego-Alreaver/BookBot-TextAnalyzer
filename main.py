
def characters_counter(palabras):
    character_counts = {

    }
    for char in palabras:
        if char in character_counts:
            character_counts[char] += 1
        else:
            character_counts[char] = 1
    
    return character_counts

def sort_on(dict):
    return dict["num"]

def print_report(file_path, word_count, character_counts):
    # Convertir el diccionario de caracteres a una lista de diccionarios
    character_list = [{"char": char, "num": num} for char, num in character_counts.items()]
    
    # Ordenar la lista por el número de apariciones de forma descendente
    character_list.sort(reverse=True, key=sort_on)
    
    # Imprimir el informe
    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document\n")
    
    for item in character_list:
        if item["char"].isalpha():  # Filtrar solo caracteres alfabéticos
            print(f"The '{item['char']}' character was found {item['num']} times")
    
    print("--- End report ---")

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

    # Imprimir el informe
    print_report(path_to_file, contador, character_counts)
    

# Llamar a la función main
if __name__ == "__main__":
    main()
