from PIL import Image, ImageFilter
import os
def pug1():
    nach = 'D:/Чикурова Александра 1-МД-4'
    obrabot = 'D:/Чикурова Александра 1-МД-4/pupug'
    if not os.path.exists(  obrabot):
        os.makedirs(  obrabot)

    supported_extensions = ('.jpg','.png')

    for filename in os.listdir(nach):
        # Проверяем, является ли файл изображением с нужным расширением
        if filename.lower().endswith(supported_extensions):
            image_path = os.path.join(nach, filename)
            image = Image.open(image_path)
            # Применяем фильтр к изображению
            image_filtered = image.filter(ImageFilter.CONTOUR)
            # Создаем новое имя файла с префиксом 'filtered_'
            new_image_name = 'filtered_' + filename
            image_filtered.save(os.path.join(obrabot, new_image_name))

    print("Обработка изображений завершена.")
def pug2():
    import csv
    total = 0
    list = []
    csvfile = open("Покупочки.csv", 'w', encoding="utf-8", newline='')
    reader = csv.reader(csvfile)
    for row in reader:
        product, quantity, price = row
        product = product.strip().replace('"', '')
        quantity = int(quantity)
        price = int(price.strip().replace('"', ''))
        total += quantity * price
        list.append(f'{product} - {quantity} шт. за {price} руб.')
    print("Нужно купить:")
    for item in list:
        print(item)
    print(f"Итоговая сумма: {total} руб.")

while True:
    print('1. список')
    print('2. добавка')
    print('3. Выход')
    a = int(input('Выберите действие: '))
    if a == 1:
        pug1()
    elif a == 2:
        pug2()
    elif a == 3:
        break
    else:
        print('Неверное действие')