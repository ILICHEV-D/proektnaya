import PySimpleGUI as sg
from PIL import Image
import proekt

k, l1 = 0, 0


def proverka(k):
    """
        Checks whether the photo is processed at the time of execution of the function
        """
    if k == 0:
        photo = 'image.jpeg'
        k = k + 1
    else:
        photo = 'gotovo.jpg'
    return photo, k


def preobraz():
    nach = Image.open('nach.png')
    im = Image.open('image.jpeg')
    width = 300
    height = 300
    nach = nach.resize((width, height), Image.ANTIALIAS)
    im = im.resize((width, height), Image.ANTIALIAS)
    nach = nach.convert('RGB').convert('P', palette=Image.ADAPTIVE)
    im = im.convert('RGB').convert('P', palette=Image.ADAPTIVE)
    nach.save('nach1.png')
    im.save('tmp.png')
    """
        Adapts the original images for correct display in the application window
        """


preobraz()
layout = [[sg.Image(filename="tmp.png", visible=True), sg.Image(filename="nach1.png", key='kl', visible=True)],
          [sg.Text('Эффекты')],
          [sg.Button('Черно-белый'), sg.Button('Серый'), sg.Button('Негатив'), sg.Button('Сброс'),
           sg.Button('Применить')],

          [sg.Text('Затемнение'), sg.Slider((0, 10), key='x4', enable_events=True, orientation='horizontal'),
           sg.Text('Яркость'), sg.Slider((0, 10), key='x5', enable_events=True, orientation='horizontal')],
          [sg.Text('Красный оттенок'), sg.Slider((0, 10), key='x6', enable_events=True, orientation='horizontal'),
           sg.Text('Зелёный оттенок'), sg.Slider((0, 10), key='x7', enable_events=True, orientation='horizontal')],
          [sg.Text('Синий оттенок'), sg.Slider((0, 10), key='x8', enable_events=True, orientation='horizontal'),
           sg.Text('Сепия'), sg.Slider((0, 10), key='x9', enable_events=True, orientation='horizontal')],
          [sg.Text('Шумы'), sg.Slider((0, 10), key='x10', enable_events=True, orientation='horizontal'),
           sg.Text('Контраст'), sg.Slider((0, 10), key='x11', enable_events=True, orientation='horizontal')]]

window = sg.Window('Редактор', layout)


def rrr():
    """
        Update the final image after applying the effect
        Insert the optimized image into a special window
        """
    nach = Image.open('gotovo.jpg')
    width = 300
    height = 300
    nach = nach.resize((width, height), Image.ANTIALIAS)
    nach = nach.convert('RGB').convert('P', palette=Image.ADAPTIVE)
    nach.save('nach1.png')
    window['kl'].Update('nach1.png')


while True:
    event, values = window.read()
    if l1 != 0:
        photo = Image.open('image.jpeg')
        photo.save("gotovo.jpg", "JPEG")
    if event == 'Сброс':  # Insert a blank image into the application after clicking "Сброс"
        k = 0
        nach = Image.open('nach10.png')
        width = 300
        height = 300
        nach = nach.resize((width, height), Image.ANTIALIAS)
        nach = nach.convert('RGB').convert('P', palette=Image.ADAPTIVE)
        nach.save('nach1.png')
        window['kl'].Update('nach1.png')
    if event == 'Черно-белый':
        photo = 'image.jpeg'
        k = 0
        proekt.black_white(photo)
        rrr()
    if event == 'Серый':
        photo = 'image.jpeg'
        k = 0
        proekt.gray(photo)
        rrr()
    if event == 'Негатив':
        print(k)
        photo = 'image.jpeg'
        k = 0
        proekt.negativ(photo)
        rrr()
    if event == 'Применить':
        if int(values['x4']) != 0:  # Read the data from the slider. If the value is positive, we use the effect "dark"
            y = int(values['x4'])
            photo, k = proverka(y)
            proekt.dark(photo, y)
            rrr()
        if int(values['x5']) != 0:  # Read the data from the slider. If the value is positive, we use the effect "light"
            y = int(values['x5'])
            photo, k = proverka(y)
            proekt.light(photo, y)
            rrr()
        if int(values['x6']) != 0:  # Read the data from the slider. If the value is positive, we use the effect "red"
            y = int(values['x6'])
            photo, k = proverka(y)
            proekt.red(photo, y)
            rrr()
        if int(values['x7']) != 0:  # Read the data from the slider. If the value is positive, we use the effect "green"
            y = int(values['x7'])
            photo, k = proverka(y)
            proekt.green(photo, y)
            rrr()
        if int(values['x8']) != 0:  # Read the data from the slider. If the value is positive, we use the effect "blue"
            y = int(values['x8'])
            photo, k = proverka(y)
            proekt.blue(photo, y)
            rrr()
        if int(values['x9']) != 0:  # Read the data from the slider. If the value is positive, we use the effect "sepia"
            y = int(values['x9'])
            photo, k = proverka(y)
            proekt.sepia(photo, y)
            rrr()
        if int(values['x10']) != 0:  # Read the data from the slider.If the value is positive, we use the effect "noise"
            y = int(values['x10'])
            photo, k = proverka(y)
            proekt.noise(photo, y)
            rrr()
        if int(values['x11']) != 0:  # Read the data from the slider.If the value is positive, we use effect "kontrast"
            y = int(values['x11'])
            photo, k = proverka(y)
            proekt.kontrast(photo, y)
            rrr()
    l1 = l1 + 1
    if event in (None, 'Выйти'):  # if user closes window or clicks cancel
        break

window.close()
