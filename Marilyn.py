from PIL import Image

image = Image.open("monro.jpg")
red, green, blue = image.split()


image_1 = Image.open("foto_red.jpg")
monro_left = (51, 0, 696-50, 522)
monro_left = image_1.crop(monro_left)

image_2 = Image.open("foto_blue.jpg")
monro_middle = (0, 0, 696-51, 522)
monro_middle = image_2.crop(monro_middle)


img1 = image_1
img2 = image_2

img = Image.blend(img1,img2, 0.5)

image_3 = Image.open("foto_green.jpg")
green = (51, 0, 696-50, 522)
green = image_3.crop(green)


new_image = Image.merge("RGB", (image_1, image_3, image_2 ))


image = Image.open("monro_overlay.jpg")
image.thumbnail((80, 70)) 
image.save("new_foto1_monro.jpg")
