import random
number = random.randint(1,3)
k = 0
player = int(input("Угадай число от 1 до 20\n"))
while player != number:
    k += 1
    player = int(input("Угадай число от 1 до 20\n"))
    while player != number:
        k += 1
        player = int(input("Угадай число от 1 до 20\n"))
        while player != number:
            k += 1
            player = int(input("Угадай число от 1 до 20\n"))
    if player == number:
        break 
print(f"Верное число {player}")
print(f"Количество попыток {k}")