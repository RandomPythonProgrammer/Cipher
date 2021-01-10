import pickle
from tkinter import *
import random

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

characters = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "|", ",", ".", "<", ">", "'", '"',
              " ", "?", "`", "~", ":", ";", "\n", "{", "}", "[", "]"]


def main():
    class Window(Frame):
        def __init__(self, master=None):
            Frame.__init__(self, master=None)
            self.master = master

    root = Tk()
    include_numbers = IntVar()
    include_characters = IntVar()
    application = Window(root)
    root.title("Cipher Builder")
    root.call('wm', 'attributes', '.', '-topmost', '1')
    root.geometry("250x150")
    root.wm_iconbitmap("Icon.ico")

    def build():
        name = name_box.get(1.0, "end-1c")
        with open(f"Created Ciphers/{name}.pkl", "x") as cipher_file:
            pass
        with open(f"Created Ciphers/{name}.pkl", "wb+") as cipher_file:
            cipher = {}
            for letter in letters:
                code = create_code()
                while not check_code(cipher, code):
                    code = create_code()
                cipher[letter] = code
            for number in numbers:
                code = create_code()
                while not check_code(cipher, code):
                    code = create_code()
                cipher[number] = code
            for upper_letter in [letter.upper() for letter in letters]:
                code = create_code()
                while not check_code(cipher, code):
                    code = create_code()
                cipher[upper_letter] = code
            for character in characters:
                code = create_code()
                while not check_code(cipher, code):
                    code = create_code()
                cipher[character] = code
            cipher["complexity"] = int(number_box.get(1.0, "end-1c"))
            pickle.dump(cipher, cipher_file)

    def create_code():
        code = []
        if include_characters.get() == 1 and include_numbers.get() == 1:
            for number in range(int(number_box.get(1.0, "end-1c"))):
                code.append(random.choice(random.choice([letters, [letter.upper() for letter in letters], numbers, characters])))
        elif include_characters.get() == 1:
            for number in range(int(number_box.get(1.0, "end-1c"))):
                code.append(random.choice(random.choice([letters, [letter.upper() for letter in letters], characters])))
        elif include_numbers.get() == 1:
            for number in range(int(number_box.get(1.0, "end-1c"))):
                code.append(random.choice(random.choice([letters, [letter.upper() for letter in letters], numbers])))
        else:
            for number in range(int(number_box.get(1.0, "end-1c"))):
                code.append(random.choice(random.choice([letters, [letter.upper() for letter in letters]])))
        return "".join(code)

    def check_code(cipher, code):
        for key in cipher.keys():
            if cipher[key] == code:
                return False
        return True

    name_label = Label(
        master=root,
        width=15,
        height=1,
        text="Name",
    )

    name_label.grid(column=0, row=0)

    number_label = Label(
        master=root,
        width=15,
        height=1,
        text="Complexity (int)",
    )

    number_label.grid(column=0, row=1)

    build_button = Button(
        master=root,
        width=15,
        height=1,
        text="build",
        command=build
    )

    build_button.grid(column=0, row=3)

    name_box = Text(
        master=root,
        width=15,
        height=1
    )

    name_box.grid(column=1, row=0)

    number_box = Text(
        master=root,
        width=15,
        height=1
    )

    number_box.grid(column=1, row=1)

    number_check = Checkbutton(
        root,
        text="Numbers",
        variable=include_numbers,
        height=5,
        width=10,
        onvalue=True,
        offvalue=False
    )

    number_check.grid(column=0, row=2)

    characters_check = Checkbutton(
        root,
        text="S. Characters",
        variable=include_characters,
        height=5,
        width=10,
        onvalue=True,
        offvalue=False
    )

    characters_check.grid(column=1, row=2)

    root.mainloop()


if __name__ == '__main__':
    main()
