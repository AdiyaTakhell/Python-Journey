import emoji


def main():
    emoji_str = input("Input:")
    result = emoji_converter(emoji_str)
    print(f"Output:{result}")


def emoji_converter(s):
    try:

        converted = emoji.emojize(s, language='alias')


        if converted == s:
            return "Emoji not recognized"
        return  converted
    except Exception as e:
        return f"Error: {e}"


if __name__ == '__main__':
    main()
