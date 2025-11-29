import re
import sys


def main():

    print(parse(input("HTML:")))


def parse(link):
    pattern = r'<iframe[^>]+src=["\']https?://(?:www\.)?youtube\.com/embed/([^"\']+)["\']'


    u=re.search(pattern,link,re.IGNORECASE)
    if u:
        extracted_link = f"https://youtu.be/{u.group(1)}"
        return f"{extracted_link}"

    else:
        return None




if __name__ == "__main__":
    main()