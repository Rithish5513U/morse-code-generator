# Morse Code Generator

A simple Python console-based Morse Code Generator that converts text to Morse code and vice versa.

## Overview

This project provides a basic Morse code generator written in Python. It allows users to input text and receive the corresponding Morse code output, as well as input Morse code and receive the decoded text.

## Features

- Converts text to Morse code
- Decodes Morse code to text
- User-friendly console interface

## Usage

1. Run the Python script `morse-code-generator.py`.
2. Enter the text you want to convert to Morse code or vice versa.
3. Follow the prompts to see the generated Morse code or decoded text.
4. Type any key to quit the program.

## Morse Code Reference

The program uses the standard Morse code representation for letters A-Z and numbers 0-9. Spaces between words are represented by '/'. 

```python
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ' ': '/'
}
