from flask import Flask, render_template, request

app = Flask(__name__)

# Caesar cipher function
def caesar_cipher(text, shift, decrypt=False):
    result = ""
    if decrypt:
        shift = -shift
    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_amount + shift) % 26 + shift_amount)
        else:
            result += char
    return result

# Vigenere cipher function
def vigenere_cipher(text, key, decrypt=False):
    result = ""
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    text_as_int = [ord(i) for i in text]
    for i in range(len(text_as_int)):
        value = (text_as_int[i] - 65 + (key_as_int[i % key_length] - 65) * (-1 if decrypt else 1)) % 26
        result += chr(value + 65)
    return result

@app.route('/', methods=['GET', 'POST'])
def index():
    caesar_result = None
    vigenere_result = None

    if request.method == 'POST':
        if 'caesar_submit' in request.form:
            text = request.form['caesar_text']
            shift = int(request.form['caesar_shift'])
            operation = request.form['caesar_operation']

            if operation == 'encrypt':
                caesar_result = caesar_cipher(text, shift)
            else:
                caesar_result = caesar_cipher(text, shift, decrypt=True)

        elif 'vigenere_submit' in request.form:
            text = request.form['vigenere_text']
            key = request.form['vigenere_key'].upper()
            operation = request.form['vigenere_operation']

            if operation == 'encrypt':
                vigenere_result = vigenere_cipher(text.upper(), key)
            else:
                vigenere_result = vigenere_cipher(text.upper(), key, decrypt=True)

    return render_template('index.html', caesar_result=caesar_result, vigenere_result=vigenere_result)

if __name__ == '__main__':
    app.run(debug=True)
