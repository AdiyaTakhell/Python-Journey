def main():
    user_input=input("What time is it ? ")
    time_in_float=convert(user_input)
    if 7<=time_in_float<8.1:
        print("breakfast time")
    elif 12<=time_in_float<13.1:
        print("lunch time")
    elif 18<time_in_float<19.1:
        print("dinner time")
    else:
        pass


def convert(time):
    hour1,minute1=time.split(":")
    hour=float(hour1)
    minutes=float(minute1)
    after_modify=minutes/60
    result=hour+after_modify
    return round(result,2)




if __name__=="__main__":
    main()





