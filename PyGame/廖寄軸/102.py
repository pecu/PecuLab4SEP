import random
神秘數字= random.randint(1, 99)#  電腦選的數字
猜測數字  = 0                                    #  玩家猜的數字
嘗試次數= 0                                    #  記綠猜的次數
print("請在1和99之間選個數字.你可以嘗試6次!")

#可以猜6次
while 嘗試次數 < 6:
     猜測數字= int(input("請輸入數字:"))
    if  猜測數字 < 神秘數字:
                print ("你的數字太小")
    elif  猜測數字 > 神秘數字:
                print ("你的數字太大")
    else:
            break
    嘗試次數 = 嘗試次數 +  1

# 顯示最後結果
if 猜測數字 == 神秘數字:
    print("讚!你猜對了!")
else:
    print("不能再猜了!")
    print("神秘數字是", 神秘數字)
