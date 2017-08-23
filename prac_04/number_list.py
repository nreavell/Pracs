
list = []
average = 0

for i in range(0,5):
    number = int(input("Number:"))
    list.append(number)

average = sum(list) / len(list)

print("The lowest number is {}".format(min(list)))
print("The highest number is {}".format(max(list)))
print("The first number is {}".format((list[0])))
print("The last number is {}".format((list[4])))
print("The number average is {}".format(average))