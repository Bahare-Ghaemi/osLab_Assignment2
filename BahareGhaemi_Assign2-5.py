second_input = int(input("Enter the second : "))

hour = int(second_input / 3600)
second = second_input % 3600

if second >= 60 :
    minute = int(second / 60)
    second = second % 60
    print(hour,minute,second)
else:
    print(hour,"00",second)