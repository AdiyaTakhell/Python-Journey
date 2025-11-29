import re
import sys

def main():
    try:
        ipaddress=sys.argv[1]
        print(validate(ipaddress))
    except Exception as e:
        print(f"{e}")


def validate(ip):
    pattern = r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    valid=re.search(pattern,ip)

    if valid:
        return True
    else:
        return  False

if __name__ == "__main__":
    main()
