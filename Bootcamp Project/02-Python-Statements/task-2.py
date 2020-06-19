## Use range() to print all the even numbers from 0 to 10.

num = range(1, 11)

#print(type(num))

for x in num:
    if (x%2) == 0:
        print (x)
        