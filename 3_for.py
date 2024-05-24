"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

sales_amount =  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
]
def main():
  total_items_sold_4all = 0
  total_counts = 0
  for sales_data in sales_amount:
    total_items_sold = sum(sales_data.get("items_sold"))
    average_items_sold = total_items_sold / len(sales_data.get("items_sold"))
    print (f"Суммарное количество продаж для {sales_data.get("product")} составляет {total_items_sold}")
    print (f"Среднее количество продаж для {sales_data.get("product")} составляет {average_items_sold}")
    total_items_sold_4all +=total_items_sold
    total_counts += len(sales_data.get("items_sold"))
    
  average_total_items_sold_4all = total_items_sold_4all/ total_counts
  print (f"Cуммарное количество продаж всех товаров составляет {total_items_sold_4all}")
  print (f"Cреднее количество продаж всех товаров {average_total_items_sold_4all}")

if __name__ == "__main__":
    main()
