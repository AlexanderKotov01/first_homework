questions_and_answers = {
    "Как дела?": "Хорошо!",
    "Что делаешь?": "Программирую",
    "Сколько время?": "Я не знаю...",
    "Куда пойдем?": "В кино"
}
"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""
def ask_user(answers_dict):
    while whats_up.lower().capitalize() != "Хорошо":
      whats_up = input("Как дела? ")
      break

if __name__ == "__main__":
    ask_user(questions_and_answers)




