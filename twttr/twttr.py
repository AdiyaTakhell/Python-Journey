def main():
    user_input = input("Input: ")
    result = remove_vowels(user_input)
    print(result)

def remove_vowels(n):
    vowels = "aeiouAEIOU"
    for vowel in vowels:
        n = n.replace(vowel, "")
    return n

main()
