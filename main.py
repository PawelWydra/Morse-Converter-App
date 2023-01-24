from morse_data import MORSE_CODE_DICT


class Coder:
    def __init__(self, string_to_code):
        self.string_to_code = string_to_code
        self.code_output = ""

    def __str__(self):
        return self.code_output

    def decode(self):
        try:
            for letter in self.string_to_code:
                self.code_output += MORSE_CODE_DICT[letter.capitalize()]
                print(MORSE_CODE_DICT[letter.capitalize()])
        except KeyError:
            print("Failed, maybe try with other word.")


print('ℳ𝒪ℛ𝒮ℰ 𝒞𝒪𝒟ℰ 𝒞𝒪𝒩𝒱ℰℛ𝒯ℰℛ')
should_continue = True

while should_continue:
    string_input = input("Hi, please entry a word to convert into morse code \n")
    coder = Coder(string_input)
    coder.decode()
    print(coder.code_output)
    if (result := input('Would you like to continue?? Yes/No? \n').lower()) == "No":
        should_continue = False
