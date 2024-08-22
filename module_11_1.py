import PIL.Image
import requests
from matplotlib import pyplot
import PIL

r = requests.get('https://www.twitch.tv/?lang=ru') # запрашиваем ресурс
print(r.status_code) # Выводим статус ресурса. Например, 200 == существует/ 404 == не существует
v = requests.post('https://www.twitch.tv/?lang=ru', params='Параметры') # передаем какие то параметры на сайт



x = [1, 2, 3, 4, 5]
y = [25, 32, 34, 20, 25]
#Рисуем обыкновенный линейный график
pyplot.plot(x, y)
pyplot.show()


x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [25, 32, 34, 20, 25, 23, 21, 33, 19, 28]
#Рисуем диаграмму рассеивания
pyplot.scatter(x, y)
pyplot.show()

with PIL.Image.open('ptitca-kartinka-06 (1).jpg') as im:
    im = im.resize((800, 600)) # Меняем размер
    im = im.convert('L') # Меняем цвет
    im.save('ptitca-kartinka-06.jpg')