player = input("Введите операцию:\n")
import random
H = ("Камень\n","Ножницы\n","Бумага\n")
bot = random.choice(H)
print(bot)
A = "Камень"
B = "Ножницы"
C = "Бумага"
if player == bot:
    print("Ничья")
if player == A and bot == B:
    print("Вы победили")
elif player == A and bot == C:
    print("Вы проиграли")
elif player == B and bot == A:
    print("Вы проиграли")
elif player == B and bot == C:
    print("Вы победили")
elif player == C and bot == A:
    print("Вы победили")
elif player == C and bot == B:
    print("Вы проиграли")
# elif operation == A and bot == A:
#     print("Ничья")
# elif operation == B and bot == B:
#     print("Ничья")
# elif operation == C and bot == C:
#     print("Ничья")



    


