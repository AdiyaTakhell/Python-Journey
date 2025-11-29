def main():
    user_input = input("Input: ")
    result = shorten(user_input)
    print(result)


def shorten(word):
    vowels = "aeiouAEIOU"
    for vowel in vowels:
        word= word.replace(vowel, "")
    return word
if __name__ == "__main__":
    main()
