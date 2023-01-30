print("Let's solve the equation: aX +b = cX + 2.")
a = input("Integer a:")
a = int(a)

b=int(input("Integer b:"))
c=int(input("Integer c:"))
d=int(input("Integer d:"))

x= (d-b)/(a-c)
print(f"{a}x + {b} = {c}x + {d}")
print(f"x is {x}")