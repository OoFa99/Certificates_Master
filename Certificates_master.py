from PIL import Image, ImageDraw, ImageFont

font = ImageFont.truetype('your font file', size=140) #you can change the size
color = 'rgb(0, 0, 0)' # black color

image = Image.open('My template path')
imageWidth = image.width
imageHeight = image.height

names = list()
names= [file.rstrip('\n') for file in open('the names CSV file path')]

for name in names:
    nameSize = font.getsize(name)
    image = Image.open('The name of the template along with its format')
    draw = ImageDraw.Draw(image)

    w, h = font.getsize(name)
    pos = ((imageWidth - w)/2, (imageHeight - h)/2)
    #draw the message on the background
    draw.text(pos, name, fill=color, font=font)

    # save the edited image
    image.save('Certificate_' + name + '.png')
