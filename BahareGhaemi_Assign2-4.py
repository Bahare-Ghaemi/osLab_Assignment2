totalTime = input("enter time : ")

hour = int(totalTime.split(":")[0])
minute = int(totalTime.split(":")[1])
second = int(totalTime.split(":")[2])

totalSecond = (hour*3600) + (minute*60) + second
print("total second = ",totalSecond)
