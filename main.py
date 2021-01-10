from tkinter import *
from tkinter import filedialog
import pickle
from textwrap import wrap


def main():
    class Window(Frame):
        def __init__(self, master=None):
            Frame.__init__(self, master=None)
            self.master = master

    root = Tk()
    application = Window(root)
    root.title("Cipher")
    root.call('wm', 'attributes', '.', '-topmost', '1')
    root.geometry("700x250")
    root.wm_iconbitmap("Icon.ico")

    def encrypt(event=None):
        filepath = cypher_box.get(1.0, "end-1c")
        with open(filepath, "rb+") as cipher_file:
            cipher = pickle.load(cipher_file)
            print(cipher)
            text = input_box.get(1.0, "end-1c")
            text = list(text)
            for character in text:
                text[text.index(character)] = cipher[character]
        output_box.delete(1.0, "end-1c")
        output_box.insert(INSERT, "".join(text))

    def decrypt(event=None):
        filepath = cypher_box.get(1.0, "end-1c")
        with open(filepath, "rb+") as cipher_file:
            cipher = pickle.load(cipher_file)
            text = input_box.get(1.0, "end-1c")
            text = wrap(text, cipher["complexity"])
            for character in text:
                for key in cipher.keys():
                    if cipher[key] == character:
                        text[text.index(character)] = key
        output_box.delete(1.0, "end-1c")
        output_box.insert(INSERT, "".join(text))

    def select_file(event=None):
        filepath = filedialog.askopenfilename()
        cypher_box.delete(1.0, "end-1c")
        cypher_box.insert(INSERT, filepath)

    generate_key_button = Button(
        master=root,
        text='Select Cipher',
        command=select_file,
        width=10,
        height=1
    )

    generate_key_button.grid(column=0, row=2)

    cypher_box = Text(
        master=root,
        width=75,
        height=1
    )

    cypher_box.grid(column=1, row=2)

    input_box = Text(
        master=root,
        width=75,
        height=5
    )

    input_box.grid(column=1, row=3)

    output_box = Text(
        master=root,
        width=75,
        height=5
    )

    output_box.grid(column=1, row=11)

    encrypt_button = Button(
        master=root,
        text='Encrypt',
        command=encrypt,
        width=10,
        height=1
    )

    encrypt_button.grid(column=0, row=3)

    decrypt_button = Button(
        master=root,
        text='Decrypt',
        command=decrypt,
        width=10,
        height=1
    )

    decrypt_button.grid(column=0, row=4)

    root.mainloop()


if __name__ == '__main__':
    main()
