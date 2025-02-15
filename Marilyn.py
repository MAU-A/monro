from PIL import Image


image_1 = Image.open("foto_red.jpg")
image_2 = Image.open("foto_green.jpg")
image_3 = Image.open("foto_blue.jpg")


new_image = Image.merge("RGB", (image_1, image_2, image_3 ))
new_image.save("monro_overlay.jpg")


image = Image.open("monro_overlay.jpg")
image.thumbnail((80, 70)) 
image.save("new_foto_monro.jpg")


