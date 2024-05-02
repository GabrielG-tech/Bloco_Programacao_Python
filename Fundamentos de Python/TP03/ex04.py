# Decodificador de Código Morse
# Implemente um programa que traduza uma string de código Morse para texto e vice-versa.

Dicionario_Codigo_Morse = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.',
    ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-',
    '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.'
}

def text_to_morse(text):
    """
    Converte texto para código Morse.

    Argumentos:
    text (str): O texto a ser convertido.

    Retorna:
    str: O texto convertido para código Morse.
    """
    morse_code = []
    for char in text.upper():
        if char in Dicionario_Codigo_Morse:
            morse_code.append(Dicionario_Codigo_Morse[char])
        else:
            morse_code.append(char)
    return ' '.join(morse_code)

def morse_to_text(morse_code):
    """
    Converte código Morse para texto.

    Argumentos:
    morse_code (str): O código Morse a ser convertido.

    Retorna:
    str: O código Morse convertido para texto.
    """
    text = []
    morse_words = morse_code.split(' ')
    for morse_word in morse_words:
        if morse_word in Dicionario_Codigo_Morse.values():
            text.append(list(Dicionario_Codigo_Morse.keys())[list(Dicionario_Codigo_Morse.values()).index(morse_word)])
        else:
            text.append(morse_word)
    return ''.join(text)

def menu():
    """
    Exibe o menu de opções para o usuário e realiza a conversão de acordo com a escolha feita.
    """
    opcao = input("Digite '1' para converter texto para código Morse ou '2' para converter código Morse para texto: ")
    if opcao == '1':
        texto = input("Digite o texto a ser convertido para código Morse: ")
        morse = text_to_morse(texto)
        print("Código Morse:", morse)
    elif opcao == '2':
        morse = input("Digite o código Morse a ser convertido para texto: ")
        texto = morse_to_text(morse)
        print("Texto:", texto)
    else:
        print("Opção inválida.")

menu()
