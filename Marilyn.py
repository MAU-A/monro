from PIL import Image

image = Image.open("monro.jpg")

red,green,blue = image.split() 
r = red
g = green
b = blue

r = red
monro_left = (50, 0, 596, 522)
monro_left = r.crop(monro_left)

r = red 
monro_red = (25, 0, 596-25, 522)
monro_red = r.crop(monro_red)
img = Image.blend(monro_left, monro_red, 0.5)

b = blue
monro_blue = (0, 0, 596-50, 522)
monro_blue = b.crop(monro_blue)

b = blue
canal_blue = (25, 0, 596-25, 522)
canal_blue = b.crop(canal_blue)
img_2 = Image.blend(monro_blue, canal_blue, 0.5)

g = green
canal_green = (25, 0, 596-25, 522)
canal_green = g.crop(canal_green)

new_image = Image.merge("RGB", (monro_left, canal_green, monro_blue ))


new_image.thumbnail((80, 70))
new_image.save("monro_1.jpg")
