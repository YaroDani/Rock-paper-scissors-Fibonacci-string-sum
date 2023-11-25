from random import randint
i=0
h=0
while True:
    a=randint(1,3)
    if a ==1:
        a="камінь"
    if a ==2:
        a="папір"
    if a ==3:
        a="ножиці"
    b=input("камінь ножиці папір")
    if b == "камінь" and a == "ножиці":
        i+=1
        print("Ти переміг!")
    if b == "камінь" and a == "папір":
        h+=1
        print("Бот переміг!")
    elif b == "камінь" and a == "камінь":
        print("Нічия")
    if b == "ножиці" and a == "папір":
        i+=1
        print("Ти переміг!")
    if b == "ножиці" and a == "камінь":
        h+=1
        print("Бот переміг!")
    elif b == "ножиці" and a == "ножиці":
        print("Нічия")
    if b == "папір" and a == "камінь":
        i+=1
        print("Ти переміг!")
    if b == "папір" and a == "ножиці":
        h+=1
        print("Бот переміг!")
    elif b == "папір" and a == "папір":
        print("Нічия")
        
    if i ==3:
        print("Ти переміг!")
        break
    
    if h ==3:
        print("Бот переміг!")
        break