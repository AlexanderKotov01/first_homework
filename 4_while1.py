"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""
whats_up = input("Как дела? ")

def hello_user(whats_up):
    whats_up.lower()
    whats_up.capitalize() 
    while whats_up != "Хорошо":
        print ("Как дела? ")

if __name__ == "__main__":
    hello_user(whats_up)
