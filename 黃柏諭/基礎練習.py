def max_num(num1,num2,num3):
    if num1 >= num2 and num1>=num3:
        return num1
    elif num2 >= num1 and num2>=num3:
        return num2
    else:
        return num3
alb1 = max_num(30,60,90)
print(alb1)
    
