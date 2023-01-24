from morse_data import MORSE_CODE_DICT


class Coder:
    def __init__(self, string_to_code):
        self.string_to_code = string_to_code
        self.code_output = ""

    def __str__(self):
        return self.code_output

    def code(self):
        for letter in self.string_to_code:
            self.code_output += MORSE_CODE_DICT[letter.capitalize()]


print('ℳ𝒪ℛ𝒮ℰ 𝒞𝒪𝒟ℰ 𝒞𝒪𝒩𝒱ℰℛ𝒯ℰℛ')
should_continue = True

while should_continue:
    string_input = input("Hi, please entry a word to convert into morse code \n")
    try:
        coder = Coder(string_input)
        coder.code()
        print(f"Your string was {string_input} and converted successfully into {coder}")

    except KeyError:
        print("Failed, maybe try with other word.")

    if (result := input('Would you like to continue?? Yes/No? \n').lower()) == "no":
        should_continue = False
