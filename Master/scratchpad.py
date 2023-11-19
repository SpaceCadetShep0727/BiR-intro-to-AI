from PIL import Image

im = (Image.open('robot2.png').convert('L'))
im = im.point(lambda x: 0 if x >150 else 0)

im.save('robot2_black.png')
        
        
