a = float(input("Enter the 1st number:"))
b = float(input("Enter the 2nd number:"))

print(f"Addition : {a+b}")
print(f"Subtraction : {a-b}")
print(f"Multiplication : {a*b}")

if(b==0):
    print("Division : Invalid!")
else:
    print(f"Division : {a/b}")