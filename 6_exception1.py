"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""
whats_up = input("Как дела? ")

def hello_user(whats_up):
    try:
       while whats_up.lower().capitalize() != "Хорошо":
          whats_up = input("Как дела? ")
          break
    except KeyboardInterrupt:
         print ('Пока! ')
  
if __name__ == "__main__":
    hello_user(whats_up) 
   