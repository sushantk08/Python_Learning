n=int(input("Enter a number: "))

def fact(n):
  if n<2:
    return 1
  else:
    return n*fact(n-1)
  
result=fact(n)
print(f"The factorial of {n} is {result}")