def main():
    user_input=input("Greeting:").lower().replace(" ","")
    result=greet(user_input)
    print(result)

def greet(greeting):
    if "hello" in greeting:
        return f"${0}"
    elif greeting[0] == "h" and greeting != "hello":
        return f"${20}"
    else:
        return f"${100}"


if __name__ == '__main__':
    main()


