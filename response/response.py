from validator_collection import validators,errors

def responsive(input_email):
    try:
        validators.email(input_email)
        return f"Valid"

    except errors.InvalidEmailError:
        return f"Invalid"

def main():

    input_email=input("Enter the email: ")
    print(responsive(input_email))

if __name__ == '__main__':
    main()
