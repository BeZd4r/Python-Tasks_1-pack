#number to word
def number_to_words(num):
    nums = {0 : "", 1 : "один", 2 : "два" , 3 : "три" , 4 : "четыре", 5 : "пять",
            6 : "шесть", 7 : "семь", 8 : "восемь", 9 : "девять", 10 :  "десять", 12 : "двенадцать",
           40: "сорок",90 : "девяносто"}

    if num < 10:
        return nums[num%10]

    elif num == 10:
        return nums[10]

    elif 10 < num < 20:
        if 11 <= num < 14 and num != 12:
            return nums[num%10] + "надцать"
        elif num == 12:
            return nums[12]
        else:
            return nums[num%10][:-1] + "надцать"

    elif 40 <= num < 50:
        return "сорок " + nums[num%10]

    elif num >= 90:
        return "девяносто " + nums[num%10]

    elif num < 40:
        return nums[num//10]+"дцать " + nums[num%10]

    elif num >= 50:
        return nums[num//10]+"десят " + nums[num%10]

# считываем данные
n = int(input())

# вызываем функцию
print(number_to_words(n))
