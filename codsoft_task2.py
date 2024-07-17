print("Please choose from the below options what opertation you want to perform: ")
print("Type 1 for addition.")
print("Type 2 for subtraction.")
print("Type 3 for multiplication.")
print("Type 4 for division.")
print("Type 5 for finding exponents.")
y=int(input("Enter 1,2,3,4,5 according to your choice: "))
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))

if y==1:
    sum= a+b
    print("The sum of",a,"and", b, "is",sum )
elif y==2:
        if a>b:
            diff=a-b
        else:
            diff=b-a
        print("The difference of",a,"and", b, "is",diff )
elif y==3:
        prod=a*b
        print("The product of",a,"and", b, "is",prod )
elif y==4:
        div=a/b
        print("The quotient of",a,"and", b, "is",div )
elif y==5:
        exp=a**b
        print(a,"raised to the power of",b, "is", exp)
else:
        print("Wrong Choice.")
