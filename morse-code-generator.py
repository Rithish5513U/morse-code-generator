morse_dict = {    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ' ': '/'}
morse = list(morse_dict.values())
text = list(morse_dict.keys())

def morse_to_text(sample):
    res = ''
    code = sample.split()
    for symbol in code:
        ind = morse.index(symbol)
        res += text[ind]
    return res

def text_to_morse(sample):
    res = ''
    for letter in sample.upper():
        res += morse_dict[letter] + ' '
    return res

while True:
    choice = int(input("Enter your choice : \n 1. Text to Morse Code \n 2. Morse code to Text \n 3. Select any other key to quit \n"))
    if choice == 1:
        x = input("Enter text to be converted to Morse Code : ")
        print("Your generated Morse Code :",text_to_morse(x))
    elif choice == 2:
        x = input("Enter Morse Code to be converted to text : ")
        print("Your decoded Morse Code :",morse_to_text(x))
    else:
        break

