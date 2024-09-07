

from PIL import Image

mac = Image.open('images_pillow/download.jpeg')

print(type(mac))

# mac.show()

print(mac.size)
print(mac.format_description)


mac.crop((0,0,100//2,100//2))
# x,y, width,height

# mac.show()



# copy and pasting 

comuter = mac.crop()

mac.paste(im=comuter,box=(20,9))

mac.resize((12,12))

mac.rotate(90)

# mac.show()


#### color transparency red green blue aplha

red = Image.open('images_pillow/download.jpeg')

red.putalpha(40) # transparency 
red.show()



