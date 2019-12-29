from PIL import Image, ImageDraw, ImageEnhance


def dark(phot, st):  # затемнение
    """
        Takes a picture and the degree of effect (recommended value [1 - 10])
        From the original picture makes a picture with reduced brightness and saves it under the name 'gotovo1.jpg'
        """

    photo = Image.open(phot)
    sch = photo.size[0]
    long = photo.size[1]
    photo_zagr = photo.load()
    draw = ImageDraw.Draw(photo)
    st = st
    for i in range(sch):
        for j in range(long):
            c1 = photo_zagr[i, j][0]
            c2 = photo_zagr[i, j][1]
            c3 = photo_zagr[i, j][2]
            c1 = c1 - st * 10
            c2 = c2 - st * 10
            c3 = c3 - st * 10
            if c1 < 0:
                c1 = 0
            if c2 < 0:
                c2 = 0
            if c3 < 0:
                c3 = 0
            draw.point((i, j), (c1, c2, c3))
    photo.save('gotovo.jpg', "JPEG")
    return Image.open('gotovo.jpg')


def light(phot, st):  # яркость
    """
        Takes a picture and the degree of effect (recommended value [1 - 10])
        From the original picture makes a picture with increased brightness and saves it under the name 'gotovo1.jpg'
        """
    photo = Image.open(phot)
    sch = photo.size[0]
    long = photo.size[1]
    draw = ImageDraw.Draw(photo)
    photo_zagr = photo.load()
    st = st
    for i in range(sch):
        for j in range(long):
            c1 = photo_zagr[i, j][0]
            c2 = photo_zagr[i, j][1]
            c3 = photo_zagr[i, j][2]
            c1 = c1 + st * 10
            c2 = c2 + st * 10
            c3 = c3 + st * 10
            if c1 > 255:
                c1 = 255
            if c2 > 255:
                c2 = 255
            if c3 > 255:
                c3 = 255
            draw.point((i, j), (c1, c2, c3))
    photo.save("gotovo.jpg", "JPEG")
    return Image.open('gotovo.jpg')

def black_white(phot):  # черно-белое
    """
        Takes a picture and the degree of effect
        From the original picture makes a black-and-white picture and saves it under the name 'gotovo1.jpg'
        """
    photo = Image.open(phot)
    sch = photo.size[0]
    long = photo.size[1]
    draw = ImageDraw.Draw(photo)
    photo_zagr = photo.load()
    for i in range(sch):
        for j in range(long):
            c1 = photo_zagr[i, j][0]
            c2 = photo_zagr[i, j][1]
            c3 = photo_zagr[i, j][2]
            if (c1 + c2 + c3) > 382.5:
                draw.point((i, j), (255, 255, 255))
            if (c1 + c2 + c3) < 382.5:
                draw.point((i, j), (0, 0, 0))
    photo.save("gotovo.jpg", "JPEG")
    return Image.open('gotovo.jpg')

def gray(phot):  # серое
    """
        Takes a picture and the degree of effect
        From the original picture makes a gray picture and saves it under the name 'gotovo1.jpg'
        """
    photo = Image.open(phot)
    sch = photo.size[0]
    long = photo.size[1]
    photo_zagr = photo.load()
    draw = ImageDraw.Draw(photo)
    for i in range(sch):
        for j in range(long):
            c1 = photo_zagr[i, j][0]
            c2 = photo_zagr[i, j][1]
            c3 = photo_zagr[i, j][2]
            T = (c1 + c2 + c3) // 3
            draw.point((i, j), (T, T, T))
    photo.save("gotovo.jpg", "JPEG")
    return Image.open('gotovo.jpg')


def red(phot, st):  # красное
    """
        Takes a picture and the degree of effect (recommended value [1 - 10])
        From the original picture makes a picture with a red tone and saves it under the name 'gotovo1.jpg'
        """
    photo = Image.open(phot)
    sch = photo.size[0]
    long = photo.size[1]
    photo_zagr = photo.load()
    draw = ImageDraw.Draw(photo)
    st = st
    for i in range(sch):
        for j in range(long):
            c1 = photo_zagr[i, j][0]
            c2 = photo_zagr[i, j][1]
            c3 = photo_zagr[i, j][2]
            c1 = c1 + st * 5
            if c1 > 255:
                c1 = 255
            draw.point((i, j), (c1, c2, c3))
    photo.save("gotovo.jpg", "JPEG")
    return Image.open('gotovo.jpg')


def green(phot, st):
    """
        Takes a picture and the degree of effect (recommended value [1 - 10])
        From the original picture makes a picture with a green tone and saves it under the name 'gotovo1.jpg'
        """
    photo = Image.open(phot)
    sch = photo.size[0]
    long = photo.size[1]
    photo_zagr = photo.load()
    draw = ImageDraw.Draw(photo)
    st = st
    for i in range(sch):
        for j in range(long):
            c1 = photo_zagr[i, j][0]
            c2 = photo_zagr[i, j][1]
            c3 = photo_zagr[i, j][2]
            c2 = c2 + st * 5
            if c2 > 255:
                c2 = 255
            draw.point((i, j), (c1, c2, c3))
    photo.save("gotovo.jpg", "JPEG")
    return Image.open('gotovo.jpg')


def blue(phot, st):
    """
        Takes a picture and the degree of effect (recommended value [1 - 10])
        From the original picture makes a picture with a blue tone and saves it under the name 'gotovo1.jpg'
        """
    photo = Image.open(phot)
    sch = photo.size[0]
    long = photo.size[1]
    photo_zagr = photo.load()
    draw = ImageDraw.Draw(photo)
    st = st
    for i in range(sch):
        for j in range(long):
            c1 = photo_zagr[i, j][0]
            c2 = photo_zagr[i, j][1]
            c3 = photo_zagr[i, j][2]
            c3 = c3 + st * 10
            if c3 > 255:
                c3 = 255
            draw.point((i, j), (c1, c2, c3))
    photo.save("gotovo.jpg", "JPEG")
    return Image.open('gotovo.jpg')


def sepia(phot, st):  # сепия
    """
        Takes a picture and the degree of effect
        From the original picture makes a picture with Sepia effect and saves it under the name 'gotovo1.jpg'
        """
    photo = Image.open(phot)
    sch = photo.size[0]
    long = photo.size[1]
    photo_zagr = photo.load()
    draw = ImageDraw.Draw(photo)
    st = st
    for i in range(sch):
        for j in range(long):
            c1 = photo_zagr[i, j][0]
            c2 = photo_zagr[i, j][1]
            c3 = photo_zagr[i, j][2]
            T = (c1 + c2 + c3) // 3
            c1 = T + (30 + 3 * st) * 2
            c2 = T + (30 + 3 * st)
            c3 = T
            if c1 > 255:
                c1 = 255
            if c2 > 255:
                c2 = 255
            if c3 > 255:
                c3 = 255
            draw.point((i, j), (c1, c2, c3))
    photo.save("gotovo.jpg", "JPEG")
    return Image.open('gotovo.jpg')


def noise(phot, st):  # noise
    """
        Takes a picture and the degree of effect (recommended value [1 - 10])
        From the original picture makes a picture with a noise effect and saves it under the name 'gotovo1.jpg'
        """
    import random
    photo = Image.open(phot)
    sch = photo.size[0]
    long = photo.size[1]
    photo_zagr = photo.load()
    draw = ImageDraw.Draw(photo)
    st = st
    for i in range(sch):
        for j in range(long):
            c1 = photo_zagr[i, j][0]
            c2 = photo_zagr[i, j][1]
            c3 = photo_zagr[i, j][2]
            c1 = c1 + int(random.uniform(-st * 8, st * 8))
            c2 = c2 + int(random.uniform(-st * 8, st * 8))
            c3 = c3 + int(random.uniform(-st * 8, st * 8))
            if c1 > 255:
                c1 = 255
            if c2 > 255:
                c2 = 255
            if c3 > 255:
                c3 = 255
            if c1 < 0:
                c1 = 0
            if c2 < 0:
                c2 = 0
            if c3 < 0:
                c3 = 0
            draw.point((i, j), (c1, c2, c3))
    photo.save("gotovo.jpg", "JPEG")
    return Image.open('gotovo.jpg')


def negativ(phot):  # negativ
    """
        Takes a picture and the degree of effect
        From the original picture makes a picture with a negative effect and saves it under the name 'gotovo1.jpg'
        """
    photo = Image.open(phot)
    sch = photo.size[0]
    long = photo.size[1]
    photo_zagr = photo.load()
    draw = ImageDraw.Draw(photo)
    for i in range(sch):
        for j in range(long):
            c1 = photo_zagr[i, j][0]
            c2 = photo_zagr[i, j][1]
            c3 = photo_zagr[i, j][2]
            c1 = 255 - c1
            c2 = 255 - c2
            c3 = 255 - c3
            draw.point((i, j), (c1, c2, c3))
    photo.save("gotovo.jpg", "JPEG")
    return Image.open('gotovo.jpg')


def kontrast(phot, st):  # kontrast
    """
        Takes a picture and the degree of effect
        From the original picture makes a picture with increased contrast and saves it under the name 'gotovo1.jpg'
        """
    photo = Image.open(phot)
    contrast = ImageEnhance.Contrast(photo)
    photo = contrast.enhance(1 + st * 0.1)
    photo.save("gotovo.jpg", "JPEG")
    return Image.open('gotovo.jpg')

