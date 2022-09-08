def func(a,b):
  return a + b

def funcsub(a,b):
  return a - b

def funcmul(a,b):
  return a * b

def funcdiv(a,b):
  return a / b

print("CALCULATOR")
TO_DO = input("Enter the action to be done : +,-,*,/ : ", )
x = int(input("First : "))
y = int(input("Second : "))

print("Action  : ", TO_DO)
if (TO_DO == '+' ) :
  print("Sum : ", func(x,y))
elif (TO_DO == '-') :
  print("Minus : ", funcsub(x,y))
elif TO_DO == '*':
  print("Mul : ", funcmul(x,y))
elif TO_DO == '/':
  print("Div : ", funcdiv(x,y))
else:
  print("Its not value")
