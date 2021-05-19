# a="JainAbraham"
# b=input("enter the character:")
# flag=0
# for i in a:
#     if i==b:
#         flag=1
# if flag==1:
#     print("present")
# else:
#     print("not present")


# a="abcdefg"
# b="asdfghjkl"
# for i in a:
#     if i not in b:
#         print(i)


# a="akkadbakkadbambebo"
# b=""
# for i in a: #
#     if i not in b:
#       b+=i #
# print(b,end="")


# a="umbrella"
# b=input("enter the element")
# count=0
# for i in a:
#     if i in b:
#         count+=1
# print(count)


#count the vowels

# a=input("enter the string")
# b="aeiou"
# count=0
# for i in a:
#     if i in b:
#        count+=1
# print(count)

#print without punctuations

# a="abcdefghijklmnopqrstuvwxyz"
# b="hello::{ wo,:ld>]};"
# count=" "
# for i in b:
#     if i in a:
#      count+=i
# print(count)


#calculator

print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
choice=int(input("enter the operator number"))
num1=float(input("enter the first number"))
num2=float(input("enter the second number"))


if choice==1:
    sum = num1 + num2
    print("The sum is ", sum)

elif choice==2:
    diff = num1 - num2
    print("the difference is ", diff)

elif choice==3:
    product = num1 * num2
    print("The product is ", product)

elif choice==4:
    div = num1 / num2
    print("The quotient is ", div)

else:
    print("no such operator")







