import inflect
p=inflect.engine()
word="Adieu, adieu, to"
item=[]
while True:
    try:
        name=input("Name: ").title()

        if name:
            item.append(name)



    except EOFError:
        break
print(f"{word} {p.join(item)}")

