def main():
    # Ruta relativa al archivo
    path_to_file = "books/frankenstein.txt"
    
    # Abrir y leer el archivo
    with open(path_to_file, 'r') as f:
        file_contents = f.read()
    contador = 0
    # Imprimir el contenido del archivo
    word_counts = file_contents.split()
    for words in word_counts:
        contador = contador +1
    print(contador)
    

# Llamar a la función main
if __name__ == "__main__":
    main()
