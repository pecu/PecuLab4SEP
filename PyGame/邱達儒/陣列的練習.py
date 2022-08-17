

numbers = [0.1,0.2,0.3]
長度 = len(numbers)
最大值 = max(numbers)
最小值 =  min(numbers) 
最大值位置 = numbers  .index(最大值)
if 長度 != 1:
  numbers.remove (max(numbers))#刪最大值1
最大值2 = max(numbers)
if 長度 != 1:
  if 最大值2 == 最大值:
    print(最小值) 
if 最大值2 != 最大值:
  print(最大值) 
if 長度 == 1:
  print(最小值 )
