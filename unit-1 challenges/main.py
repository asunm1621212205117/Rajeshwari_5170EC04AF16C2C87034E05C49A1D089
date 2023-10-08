def fact(n):
  if n==0 or n==1:
    return 1
  else:
    return n*fact(n-1)
    number=int(input("Enter number to find factorial:"))
    print("The factorial of a {} is {}.".format(number,result))
    