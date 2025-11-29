modify_input=input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
user_input=modify_input.lower().replace("-","").replace(" ","")


if user_input =="42" or user_input=="fortytwo":
    print("yes")
else:
    print("no")

