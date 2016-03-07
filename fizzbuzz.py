# I read about the little "fizzbuzz" thing so I had to have a go.
# If I recall correctly the problem was just to print 1 to 100
# if divisible by 3 print "fizz" and if divisible by 5 print "buzz"
for i in range(1, 100):
    if i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)