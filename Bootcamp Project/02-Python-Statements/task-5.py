## Write a program that prints the integers from 1 to 100. But for multiples of three print
#  "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which 
# are multiples of both three and five print "FizzBuzz".



num = range(1, 100)

for x in num:
    if x %3 == 0 and x %5 == 0:
        print("FizzBuzz")
    elif x %3 == 0:
        print("Buzz")
    elif x %5 == 0:
        print ("Fizz")

    
    
    
    