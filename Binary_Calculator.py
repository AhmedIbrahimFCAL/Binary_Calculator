# Author: Ahmad Ibrahim Ahmad Mohammed
# Under the supervision: Dr. Manar_Elkady & eng: Mira_Raheem



###Definition The Functions.
#____The entrance type to function is string____

#Chick binary or not.
"""
This function chicks binary or not by passing each bit.
"""
def chick_binary(num):
    if num=="":
        print("Please, don't leave it empty.")
        return True
    for i in num:
        if  i!= "0" and i!="1":
            print("Please, the binary number doesn't include '"+i+"'.")
            return True

#Convert to one's complement
"""
This function does one's complement by fliping 1 to 0 and 0 to 1. 
"""
def ones_complement(num):
    sum = ""
    for i in num:
        if i=="0":
            sum+="1"
        else:
            sum+="0"
    return sum

#Convert to two's complement.
"""
This function does two's complement by from right to left 
and stays first 1 and flips for the rest of bits.
"""
def twos_complement(num):
    if "1" in num:
        sum=""
        num=num[::-1]
        for i in range(len(num)):
            if num[i] =="1":
                break
        for x in range(0,i+1):
            sum+=num[x]
        i+=1
        for y in range(i,len(num)):
            if num[y]=="0":
                sum+="1"
            else:
                sum+="0"
        sum=sum[::-1]
        return sum
    else:
        return num

#Performing the ADDition.
"""
This function does addtion to two binary numbers with the same traditional concept
and we inserted variable for rest called 'rest' .
"""
def add(num1,num2):
# We have reversed the order to make it easier ti deal with numbers.
    num1 = num1[::-1]
    num2 = num2[::-1]
# We added "0" left to the original two numbers avoid overflow.
    num1+="0"
    num2+="0"
# The following two conditions equal number of bits to the two numbers,
    if len(num1)>len(num2):
        x=len(num1)-len(num2)
        for i in range(x):
            num2+="0"
    if len(num2)>len(num1):
        d=len(num2)-len(num1)
        for j in range(d):
            num1+="0"
# This part from code is performing the addition by the traditional way.
    rest = "0"
    sum = ""
    for i in range(len(num1)):
        if num1[i] != num2[i] and rest[i] == "0":
            sum += "1"
            rest += "0"
        elif num1[i] != num2[i] and rest[i] == "1":
            sum += "0"
            rest += "1"
        elif num1[i] == num2[i] == "0" and rest[i] == "0":
            sum += "0"
            rest += "0"
        elif num1[i] == num2[i] == "0" and rest[i] == "1":
            sum += "1"
            rest += "0"
        elif num1[i] == num2[i] == "1" and rest[i] == "1":
            sum += "1"
            rest += "1"
        elif num1[i] == num2[i] == "1" and rest[i] == "0":
            sum += "0"
            rest += "1"
    sum = sum[::-1]
    if sum[0]=="0":
        sum=sum[1:]
# We have reversed the order to be a correct result avoid logic errors.
    return sum

#performing the SUbtraction
"""
This function does subtraction to two binary numbers by two's complement for the second numnber.
"""
def sub(num1, num2):
# We have symbolized the result by result.
    result = ""
    if (int(num1) != 0 or int(num2) != 0) and int(num1) != int(num2):
# We have reversed the order to make it easier ti deal with numbers.
        num1 = num1[::-1]
        num2 = num2[::-1]
# We added "0" left to the original two numbers avoid overflow in the case number of bits for two numbers equal.
        num1 += "0"
        num2 += "0"
        if len(num1) > len(num2):
            x = len(num1) - len(num2)
            for i in range(x):
                num2 += "0"
        if len(num2) > len(num1):
            d = len(num2) - len(num1)
            for i in range(d):
                num1 += "0"
# We have reversed the order to avoid logic errors calling the funcion.
        num1 = num1[::-1]
        num2 = num2[::-1]
        num2 = twos_complement(num2)
        result = add(num1, num2)
# We performed addition as in two's complement.
# these conditions avoid logic errors.
        if len(result) > len(num1) and int(result[1:]) != 0:
            x = len(result) - len(num1)
            result = result[x:]
        if int(result[1:]) == 0:
            result = result[1:]
            result += "1"
        if result[0] == "0":
            result = result[1:]
# We did this process so that the 0utput bits would be the numbers of bits the largest number of bits.
# in the case of two numbers are zero.
    else:
        a = len(num1)
        if len(num2) > len(num1):
            a = len(num2)
        for i in range(a):
            result += "0"
    return result

#Performing the MULTIplication.
"""
This function does multiplication to two binary numbers with the same traditional concept.
"""
def multi(num1,num2):
    res="0"
    if int(num1)!=0 and int(num2)!=0:
        for i in range(len(num2)):
            i=(-(i+1))
            if num2[i]=="1":
                res=add(res,(num1))
            num1+="0"
    return res


###Main Program.
#Display Minu1.
# We have symbolized the intrance latter by sel,sel2.
while True:
    sel = input("\n\n**Binary Calculator**\n  A) Insert new numbers\n  B) Exit\nPlease, select A or B : ").strip()
    while sel.upper()!="A" and sel.upper()!="B":
        sel = input("\nPlease, select a vaild choice.\n**Binary Calculator**\n  A) Insert new numbers\n  B) Exit\nPlease, select A or B : ").strip()
    if sel.upper()=="B":
        break
#Display Minu2
# We have symbolized the intrance numbers by num1,num2
    if sel.upper()=="A":
    # Read the first Binary number
        num1 = input("\nPlease, enter a binary number: ").strip()
        while chick_binary(num1):
            num1 = input("Please, insert a vaild binary number.\nPlease, enter a binary number (Including 1's and 0's only.) : ").strip()
    # Read the operation
        sel2=input("\n**Please, select the operation**\n  A) Compute one's complement\n  B) Compute two's complement\n  c) Addition\n  D) Subtraction\n  E) Multiplication\nplease, select A, B, C, D, or E : ").strip()
        while sel2.upper()!="A" and sel2.upper()!="B" and sel2.upper()!="C" and sel2.upper()!="D" and sel2.upper()!="E":
            sel2 = input("\nPlease, select a vaild choice.\n**Please, select the operation**\n  A) Compute one's complement\n  B) Compute two's complement\n  c) Addition\n  D) Subtraction\n  E) Multiplication\nPlease, select A, B, C, D, or E : ").strip()
    # get the one's complement and print it
        if sel2.upper()=="A":
            print("The ons's complement for",num1,"is",ones_complement(num1))
    # get the one's complement and print it
        elif sel2.upper()=="B":
            print("The two's complement for",num1,"is",twos_complement(num1))
    # If the sellection is not A nor B ,then we need the second number
        elif sel2.upper()=="C":

            num2=input("Please, enter the second binary number: ").strip()
            while chick_binary(num2):
                num2 = input("Please, insert a vaild binary number.\nPlease, enter the second binary number (Including 1's and 0's only.) : ").strip()
            print(num1,"+",num2,"=",add(num1, num2))

        elif sel2.upper()=="D":
            num2 = input("Please, enter the second binary number: ").strip()
            while chick_binary(num2):
                num2 = input("Please, insert a vaild binary number.\nPlease, enter the second binary number (Including 1's and 0's only.) : ").strip()

            while int(num2)>int(num1):
                num2=input("The result is a negative number.\nPlease, enter a number which is less than or equal "+num1+" : ").strip()
            print(num1,"-",num2,"=",sub(num1,num2))
        # Then The selection is multiplication
        else:
            num2 = input("Please, enter the second binary number: ").strip()
            while chick_binary(num2):
                num2 = input("Please, insert a vaild binary number.\nPlease, enter the second binary number (Including 1's and 0's only.) : ").strip()
            print(num1,"*",num2,"=",multi(num1, num2))

print("\nThanks for using my program. See You Soon!")
# Thanks for reading my code.