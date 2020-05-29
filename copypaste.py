from PIL import Image
#up
im=Image.open('dog2.jpg')


crop=Image.open('googles.jpg').convert('RGB')
im.paste(crop,(0,0))
im.save('cropped.jpg')


#down
height,width=im.size


im=Image.open('dog2.jpg')

im.paste(crop,(0,width-100))
im.save('dpwncrop.jpg')
