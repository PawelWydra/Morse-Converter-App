from morse_data import MORSE_CODE_DICT

print('ℳ𝒪ℛ𝒮ℰ 𝒞𝒪𝒟ℰ 𝒞𝒪𝒩𝒱ℰℛ𝒯ℰℛ')

while should_continue := True:
    string_input = input("Hi, please entry a word to convert into morse code \n")
    morse_code_output = ''
    try:
        for letter in string_input:
            morse_code_output += MORSE_CODE_DICT[letter.capitalize()]

        print(f"Your string was {string_input} and converted successfully into {morse_code_output}")

    except KeyError:
        print("Failed, maybe try with other word.")

    finally:
        if (result := input('Would you like to continue?? Yes/No? \n').lower()) == "No":
            should_continue = False
