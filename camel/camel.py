def main():
    camel_case = input("Enter the word in camelCase: ")
    result = snake_case(camel_case)
    print(result)

def snake_case(n):
    result = ""
    for char in n:
        if char.isupper():
            result = result+ "_" + char.lower()
        else:
            result =result+ char
    return result

if __name__ == "__main__":
    main()
