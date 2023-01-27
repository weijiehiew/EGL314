from tkinter import *
import time
import sendtopolarizer
from PIL import Image, ImageOps
from student_pub import *
from pydub import AudioSegment
from pydub.playback import play
import threading

storyaudio = AudioSegment.from_wav('/home/pi/TeamD/Resources/s1i1.wav')


def img_change(m):
    ## open image file
        if m == 1:
                img1 = PhotoImage(file="Resources/1.png")
                label.configure(image=img1)
                label.image = img1
                #print(Image)
                myImage = Image.open('/home/pi/TeamD/Resources/1.png')
                ## greyscale image file
                greyImage = ImageOps.grayscale(myImage)
                #greyImage.show()

                ## Limiting to 8 shades of greyscale colour
                greyQuantize = greyImage.quantize(8)
                #greyQuantize.show()

                ## resize to 32 x 32 pixels
                smallImage = greyQuantize.resize((32,32), Image.BILINEAR)
                #smallImage.show()

                ## Blow it back up to original photo size (32 x 32 pixels upscale)
                resultImage = smallImage.resize(myImage.size, Image.NEAREST)
                #resultImage.show()

                ## Write Image to save .png file
                ##resultImage.save('cartoon.png')

                # Retrieving pixel value and formating it into list of list
                x = 32; k = 0; outputValue = [0 for i in range(x)]
                for i in range(x):
                  outputValue[i] = [0 for j in range(x)]
                pixValue = list(smallImage.getdata())

                for i in range(x):
                 for j in range(x):
                        outputValue[i][j] = pixValue[k]
                        k = k + 1;

                print(outputValue)
                pubpic(outputValue)
        elif m ==2:
                img1 = PhotoImage(file="Resources/2.png")
                label.configure(image=img1)
                label.image = img1
                #print(Image)
                myImage = Image.open('/home/pi/TeamD/Resources/2.png')
                ## greyscale image file
                greyImage = ImageOps.grayscale(myImage)
                #greyImage.show()

                ## Limiting to 8 shades of greyscale colour
                greyQuantize = greyImage.quantize(8)
                #greyQuantize.show()

                ## resize to 32 x 32 pixels
                smallImage = greyQuantize.resize((32,32), Image.BILINEAR)
                #smallImage.show()

                ## Blow it back up to original photo size (32 x 32 pixels upscale)
                resultImage = smallImage.resize(myImage.size, Image.NEAREST)
                #resultImage.show()

                ## Write Image to save .png file
                ##resultImage.save('cartoon.png')

                # Retrieving pixel value and formating it into list of list
                x = 32; k = 0; outputValue = [0 for i in range(x)]
                for i in range(x):
                  outputValue[i] = [0 for j in range(x)]
                pixValue = list(smallImage.getdata())

                for i in range(x):
                 for j in range(x):
                        outputValue[i][j] = pixValue[k]
                        k = k + 1;

                print(outputValue)
                pubpic(outputValue)
        elif m ==3:
                img1 = PhotoImage(file="Resources/3.png")
                label.configure(image=img1)
                label.image = img1
                #print(Image)
                myImage = Image.open('/home/pi/TeamD/Resources/3.png')
                ## greyscale image file
                greyImage = ImageOps.grayscale(myImage)
                #greyImage.show()

                ## Limiting to 8 shades of greyscale colour
                greyQuantize = greyImage.quantize(8)
                #greyQuantize.show()

                ## resize to 32 x 32 pixels
                smallImage = greyQuantize.resize((32,32), Image.BILINEAR)
                #smallImage.show()

                ## Blow it back up to original photo size (32 x 32 pixels upscale)
                resultImage = smallImage.resize(myImage.size, Image.NEAREST)
                #resultImage.show()

                ## Write Image to save .png file
                ##resultImage.save('cartoon.png')

                # Retrieving pixel value and formating it into list of list
                x = 32; k = 0; outputValue = [0 for i in range(x)]
                for i in range(x):
                  outputValue[i] = [0 for j in range(x)]
                pixValue = list(smallImage.getdata())

                for i in range(x):
                 for j in range(x):
                        outputValue[i][j] = pixValue[k]
                        k = k + 1;

                print(outputValue)
                pubpic(outputValue)
        elif m ==4:
                img1 = PhotoImage(file="Resources/4.png")
                label.configure(image=img1)
                label.image = img1
                #print(Image)
                myImage = Image.open('/home/pi/TeamD/Resources/4.png')
                ## greyscale image file
                greyImage = ImageOps.grayscale(myImage)
                #greyImage.show()

                ## Limiting to 8 shades of greyscale colour
                greyQuantize = greyImage.quantize(8)
                #greyQuantize.show()

                ## resize to 32 x 32 pixels
                smallImage = greyQuantize.resize((32,32), Image.BILINEAR)
                #smallImage.show()

                ## Blow it back up to original photo size (32 x 32 pixels upscale)
                resultImage = smallImage.resize(myImage.size, Image.NEAREST)
                #resultImage.show()

                ## Write Image to save .png file
                ##resultImage.save('cartoon.png')

                # Retrieving pixel value and formating it into list of list
                x = 32; k = 0; outputValue = [0 for i in range(x)]
                for i in range(x):
                  outputValue[i] = [0 for j in range(x)]
                pixValue = list(smallImage.getdata())

                for i in range(x):
                 for j in range(x):
                        outputValue[i][j] = pixValue[k]
                        k = k + 1;

                print(outputValue)
                pubpic(outputValue)
        elif m ==5:
                img1 = PhotoImage(file="Resources/5.png")
                label.configure(image=img1)
                label.image = img1
                #print(Image)
                myImage = Image.open('/home/pi/TeamD/Resources/5.png')
                ## greyscale image file
                greyImage = ImageOps.grayscale(myImage)
                #greyImage.show()

                ## Limiting to 8 shades of greyscale colour
                greyQuantize = greyImage.quantize(8)
                #greyQuantize.show()

                ## resize to 32 x 32 pixels
                smallImage = greyQuantize.resize((32,32), Image.BILINEAR)
                #smallImage.show()

                ## Blow it back up to original photo size (32 x 32 pixels upscale)
                resultImage = smallImage.resize(myImage.size, Image.NEAREST)
                #resultImage.show()

                ## Write Image to save .png file
                ##resultImage.save('cartoon.png')

                # Retrieving pixel value and formating it into list of list
                x = 32; k = 0; outputValue = [0 for i in range(x)]
                for i in range(x):
                  outputValue[i] = [0 for j in range(x)]
                pixValue = list(smallImage.getdata())

                for i in range(x):
                 for j in range(x):
                        outputValue[i][j] = pixValue[k]
                        k = k + 1;

                print(outputValue)
                pubpic(outputValue)
        elif m ==6:
                img1 = PhotoImage(file="Resources/6.png")
                label.configure(image=img1)
                label.image = img1
                #print(Image)
                myImage = Image.open('/home/pi/TeamD/Resources/6.png')
                ## greyscale image file
                greyImage = ImageOps.grayscale(myImage)
                #greyImage.show()

                ## Limiting to 8 shades of greyscale colour
                greyQuantize = greyImage.quantize(8)
                #greyQuantize.show()

                ## resize to 32 x 32 pixels
                smallImage = greyQuantize.resize((32,32), Image.BILINEAR)
                #smallImage.show()

                ## Blow it back up to original photo size (32 x 32 pixels upscale)
                resultImage = smallImage.resize(myImage.size, Image.NEAREST)
                #resultImage.show()

                ## Write Image to save .png file
                ##resultImage.save('cartoon.png')

                # Retrieving pixel value and formating it into list of list
                x = 32; k = 0; outputValue = [0 for i in range(x)]
                for i in range(x):
                  outputValue[i] = [0 for j in range(x)]
                pixValue = list(smallImage.getdata())

                for i in range(x):
                 for j in range(x):
                        outputValue[i][j] = pixValue[k]
                        k = k + 1;

                print(outputValue)
                pubpic(outputValue)
        elif m ==7:
                img1 = PhotoImage(file="Resources/7.png")
                label.configure(image=img1)
                label.image = img1
                #print(Image)
                myImage = Image.open('/home/pi/TeamD/Resources/7.png')
                ## greyscale image file
                greyImage = ImageOps.grayscale(myImage)
                #greyImage.show()

                ## Limiting to 8 shades of greyscale colour
                greyQuantize = greyImage.quantize(8)
                #greyQuantize.show()

                ## resize to 32 x 32 pixels
                smallImage = greyQuantize.resize((32,32), Image.BILINEAR)
                #smallImage.show()

                ## Blow it back up to original photo size (32 x 32 pixels upscale)
                resultImage = smallImage.resize(myImage.size, Image.NEAREST)
                #resultImage.show()

                ## Write Image to save .png file
                ##resultImage.save('cartoon.png')

                # Retrieving pixel value and formating it into list of list
                x = 32; k = 0; outputValue = [0 for i in range(x)]
                for i in range(x):
                  outputValue[i] = [0 for j in range(x)]
                pixValue = list(smallImage.getdata())

                for i in range(x):
                 for j in range(x):
                        outputValue[i][j] = pixValue[k]
                        k = k + 1;

                print(outputValue)
                pubpic(outputValue)
        elif m ==8:
                img1 = PhotoImage(file="Resources/8.png")
                label.configure(image=img1)
                label.image = img1
                #print(Image)
                myImage = Image.open('/home/pi/TeamD/Resources/8.png')
                ## greyscale image file
                greyImage = ImageOps.grayscale(myImage)
                #greyImage.show()

                ## Limiting to 8 shades of greyscale colour
                greyQuantize = greyImage.quantize(8)
                #greyQuantize.show()

                ## resize to 32 x 32 pixels
                smallImage = greyQuantize.resize((32,32), Image.BILINEAR)
                #smallImage.show()

                ## Blow it back up to original photo size (32 x 32 pixels upscale)
                resultImage = smallImage.resize(myImage.size, Image.NEAREST)
                #resultImage.show()

                ## Write Image to save .png file
                ##resultImage.save('cartoon.png')

                # Retrieving pixel value and formating it into list of list
                x = 32; k = 0; outputValue = [0 for i in range(x)]
                for i in range(x):
                  outputValue[i] = [0 for j in range(x)]
                pixValue = list(smallImage.getdata())

                for i in range(x):
                 for j in range(x):
                        outputValue[i][j] = pixValue[k]
                        k = k + 1;

                print(outputValue)
                pubpic(outputValue)
                
        elif m ==9:
                img1 = PhotoImage(file="Resources/9.png")
                label.configure(image=img1)
                label.image = img1
                #print(Image)
                myImage = Image.open('/home/pi/TeamD/Resources/9.png')
                ## greyscale image file
                greyImage = ImageOps.grayscale(myImage)
                #greyImage.show()

                ## Limiting to 8 shades of greyscale colour
                greyQuantize = greyImage.quantize(8)
                #greyQuantize.show()

                ## resize to 32 x 32 pixels
                smallImage = greyQuantize.resize((32,32), Image.BILINEAR)
                #smallImage.show()

                ## Blow it back up to original photo size (32 x 32 pixels upscale)
                resultImage = smallImage.resize(myImage.size, Image.NEAREST)
                #resultImage.show()

                ## Write Image to save .png file
                ##resultImage.save('cartoon.png')

                # Retrieving pixel value and formating it into list of list
                x = 32; k = 0; outputValue = [0 for i in range(x)]
                for i in range(x):
                  outputValue[i] = [0 for j in range(x)]
                pixValue = list(smallImage.getdata())

                for i in range(x):
                 for j in range(x):
                        outputValue[i][j] = pixValue[k]
                        k = k + 1;

                print(outputValue)
                pubpic(outputValue)
        elif m ==10:
                img1 = PhotoImage(file="Resources/10.png")
                label.configure(image=img1)
                label.image = img1
                #print(Image)
                myImage = Image.open('/home/pi/TeamD/Resources/10.png')
                ## greyscale image file
                greyImage = ImageOps.grayscale(myImage)
                #greyImage.show()

                ## Limiting to 8 shades of greyscale colour
                greyQuantize = greyImage.quantize(8)
                #greyQuantize.show()

                ## resize to 32 x 32 pixels
                smallImage = greyQuantize.resize((32,32), Image.BILINEAR)
                #smallImage.show()

                ## Blow it back up to original photo size (32 x 32 pixels upscale)
                resultImage = smallImage.resize(myImage.size, Image.NEAREST)
                #resultImage.show()

                ## Write Image to save .png file
                ##resultImage.save('cartoon.png')

                # Retrieving pixel value and formating it into list of list
                x = 32; k = 0; outputValue = [0 for i in range(x)]
                for i in range(x):
                  outputValue[i] = [0 for j in range(x)]
                pixValue = list(smallImage.getdata())

                for i in range(x):
                 for j in range(x):
                        outputValue[i][j] = pixValue[k]
                        k = k + 1;

                print(outputValue)
                pubpic(outputValue)
        elif m ==11:
                img1 = PhotoImage(file="Resources/11(1).png")
                label.configure(image=img1)
                label.image = img1
                #print(Image)
                myImage = Image.open('/home/pi/TeamD/Resources/11.png')
                ## greyscale image file
                greyImage = ImageOps.grayscale(myImage)
                #greyImage.show()

                ## Limiting to 8 shades of greyscale colour
                greyQuantize = greyImage.quantize(8)
                #greyQuantize.show()

                ## resize to 32 x 32 pixels
                smallImage = greyQuantize.resize((32,32), Image.BILINEAR)
                #smallImage.show()

                ## Blow it back up to original photo size (32 x 32 pixels upscale)
                resultImage = smallImage.resize(myImage.size, Image.NEAREST)
                #resultImage.show()

                ## Write Image to save .png file
                ##resultImage.save('cartoon.png')

                # Retrieving pixel value and formating it into list of list
                x = 32; k = 0; outputValue = [0 for i in range(x)]
                for i in range(x):
                  outputValue[i] = [0 for j in range(x)]
                pixValue = list(smallImage.getdata())

                for i in range(x):
                 for j in range(x):
                        outputValue[i][j] = pixValue[k]
                        k = k + 1;

                print(outputValue)
                pubpic(outputValue)
        elif m ==12:
                img1 = PhotoImage(file="Resources/12.png")
                label.configure(image=img1)
                label.image = img1
                #print(Image)
                myImage = Image.open('/home/pi/TeamD/Resources/12.png')
                ## greyscale image file
                greyImage = ImageOps.grayscale(myImage)
                #greyImage.show()

                ## Limiting to 8 shades of greyscale colour
                greyQuantize = greyImage.quantize(8)
                #greyQuantize.show()

                ## resize to 32 x 32 pixels
                smallImage = greyQuantize.resize((32,32), Image.BILINEAR)
                #smallImage.show()

                ## Blow it back up to original photo size (32 x 32 pixels upscale)
                resultImage = smallImage.resize(myImage.size, Image.NEAREST)
                #resultImage.show()

                ## Write Image to save .png file
                ##resultImage.save('cartoon.png')

                # Retrieving pixel value and formating it into list of list
                x = 32; k = 0; outputValue = [0 for i in range(x)]
                for i in range(x):
                  outputValue[i] = [0 for j in range(x)]
                pixValue = list(smallImage.getdata())

                for i in range(x):
                 for j in range(x):
                        outputValue[i][j] = pixValue[k]
                        k = k + 1;

                print(outputValue)
                pubpic(outputValue)
        elif m ==13:
                img1 = PhotoImage(file="Resources/13.png")
                label.configure(image=img1)
                label.image = img1
                #print(Image)
                myImage = Image.open('/home/pi/TeamD/Resources/13.png')
                ## greyscale image file
                greyImage = ImageOps.grayscale(myImage)
                #greyImage.show()

                ## Limiting to 8 shades of greyscale colour
                greyQuantize = greyImage.quantize(8)
                #greyQuantize.show()

                ## resize to 32 x 32 pixels
                smallImage = greyQuantize.resize((32,32), Image.BILINEAR)
                #smallImage.show()

                ## Blow it back up to original photo size (32 x 32 pixels upscale)
                resultImage = smallImage.resize(myImage.size, Image.NEAREST)
                #resultImage.show()

                ## Write Image to save .png file
                ##resultImage.save('cartoon.png')

                # Retrieving pixel value and formating it into list of list
                x = 32; k = 0; outputValue = [0 for i in range(x)]
                for i in range(x):
                  outputValue[i] = [0 for j in range(x)]
                pixValue = list(smallImage.getdata())

                for i in range(x):
                 for j in range(x):
                        outputValue[i][j] = pixValue[k]
                        k = k + 1;

                print(outputValue)
                pubpic(outputValue)
        elif m ==14:
                img1 = PhotoImage(file="Resources/14.png")
                label.configure(image=img1)
                label.image = img1
                #print(Image)
                myImage = Image.open('/home/pi/TeamD/Resources/14.png')
                ## greyscale image file
                greyImage = ImageOps.grayscale(myImage)
                #greyImage.show()

                ## Limiting to 8 shades of greyscale colour
                greyQuantize = greyImage.quantize(8)
                #greyQuantize.show()

                ## resize to 32 x 32 pixels
                smallImage = greyQuantize.resize((32,32), Image.BILINEAR)
                #smallImage.show()

                ## Blow it back up to original photo size (32 x 32 pixels upscale)
                resultImage = smallImage.resize(myImage.size, Image.NEAREST)
                #resultImage.show()

                ## Write Image to save .png file
                ##resultImage.save('cartoon.png')

                # Retrieving pixel value and formating it into list of list
                x = 32; k = 0; outputValue = [0 for i in range(x)]
                for i in range(x):
                  outputValue[i] = [0 for j in range(x)]
                pixValue = list(smallImage.getdata())

                for i in range(x):
                 for j in range(x):
                        outputValue[i][j] = pixValue[k]
                        k = k + 1;

                print(outputValue)
                pubpic(outputValue)
        elif m ==15:
                img1 = PhotoImage(file="Resources/15.png")
                label.configure(image=img1)
                label.image = img1
                #print(Image)
                myImage = Image.open('/home/pi/TeamD/Resources/15.png')
                ## greyscale image file
                greyImage = ImageOps.grayscale(myImage)
                #greyImage.show()

                ## Limiting to 8 shades of greyscale colour
                greyQuantize = greyImage.quantize(8)
                #greyQuantize.show()

                ## resize to 32 x 32 pixels
                smallImage = greyQuantize.resize((32,32), Image.BILINEAR)
                #smallImage.show()

                ## Blow it back up to original photo size (32 x 32 pixels upscale)
                resultImage = smallImage.resize(myImage.size, Image.NEAREST)
                #resultImage.show()

                ## Write Image to save .png file
                ##resultImage.save('cartoon.png')

                # Retrieving pixel value and formating it into list of list
                x = 32; k = 0; outputValue = [0 for i in range(x)]
                for i in range(x):
                  outputValue[i] = [0 for j in range(x)]
                pixValue = list(smallImage.getdata())

                for i in range(x):
                 for j in range(x):
                        outputValue[i][j] = pixValue[k]
                        k = k + 1;

                print(outputValue)
                pubpic(outputValue)
        elif m ==16:
                img1 = PhotoImage(file="Resources/16.png")
                label.configure(image=img1)
                label.image = img1
                #print(Image)
                myImage = Image.open('/home/pi/TeamD/Resources/16.png')
                ## greyscale image file
                greyImage = ImageOps.grayscale(myImage)
                #greyImage.show()

                ## Limiting to 8 shades of greyscale colour
                greyQuantize = greyImage.quantize(8)
                #greyQuantize.show()

                ## resize to 32 x 32 pixels
                smallImage = greyQuantize.resize((32,32), Image.BILINEAR)
                #smallImage.show()

                ## Blow it back up to original photo size (32 x 32 pixels upscale)
                resultImage = smallImage.resize(myImage.size, Image.NEAREST)
                #resultImage.show()

                ## Write Image to save .png file
                ##resultImage.save('cartoon.png')

                # Retrieving pixel value and formating it into list of list
                x = 32; k = 0; outputValue = [0 for i in range(x)]
                for i in range(x):
                  outputValue[i] = [0 for j in range(x)]
                pixValue = list(smallImage.getdata())

                for i in range(x):
                 for j in range(x):
                        outputValue[i][j] = pixValue[k]
                        k = k + 1;

                print(outputValue)
                pubpic(outputValue)
        else:
                img1 = PhotoImage(file="Resources/blank.png")
                label.configure(image=img1)
                label.image = img1

def startshow():
        pictures = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19']

    
        audio = threading.Thread(target=play, args=(storyaudio,))

        for i in range(16):
            path3 = '/home/pi/TeamD/Resources/' + pictures[i] + '.png'
            #path2 = Image.open(path3)
            sendtopolarizer.middleman(Images = path3)
            #path2 = Image.open('cartoon.png')
            print(path3)
            time.sleep(5)

            if i == 1:
                time.sleep(10)
            elif i == 8:
                time.sleep(10)
            elif i == 13:
                time.sleep(10)
            elif i == 19:
                time.sleep(10)
            else:
                time.sleep(15)
        


main = Tk()
main.title("Group D's Story Telling Show")
main.config(bg="skyblue")

bgimg = PhotoImage(file="Resources/mainbg.png")
limg= Label(main, image=bgimg)
limg.place(x=0, y=0)


#image
frame1 = Frame(main, width=650, height=400, bg='grey') 
frame1.grid(row=0, column=0, padx=10, pady=5)

#startshowbtn
frame2 = Frame(main, width=650, height=400, highlightbackground="grey", highlightthickness=5) 
frame2.grid(row=0, column=1, padx=10, pady=5)
bgimg2 = PhotoImage(file="Resources/framebg.png")
limg2= Label(frame2, image=bgimg2)
limg2.place(x=0, y=0)

#allimagebuttons
frame3 = Frame(main, width=100, height=400, bg="grey")
frame3.grid(row=1, columnspan=2, padx=10, pady=5) 


#open images
pic1 = PhotoImage(file="Resources/1.png")
pic2 = PhotoImage(file="Resources/2.png")
pic3 = PhotoImage(file="Resources/3.png")
pic4 = PhotoImage(file="Resources/4.png")
pic5 = PhotoImage(file="Resources/5.png")
pic6 = PhotoImage(file="Resources/6.png")
pic7 = PhotoImage(file="Resources/7.png")
pic8 = PhotoImage(file="Resources/8.png")
pic9 = PhotoImage(file="Resources/9.png")
pic10 = PhotoImage(file="Resources/10.png")
pic11 = PhotoImage(file="Resources/11(1).png")
pic12 = PhotoImage(file="Resources/12.png")
pic13 = PhotoImage(file="Resources/13.png")
pic14 = PhotoImage(file="Resources/14.png")
pic15 = PhotoImage(file="Resources/15.png")
pic16 = PhotoImage(file="Resources/16.png")

#resize the images
image1 = pic1.subsample(6, 6)
image2 = pic2.subsample(6, 6)
image3 = pic3.subsample(7, 7)
image4 = pic4.subsample(6, 6)
image5 = pic5.subsample(6, 6)
image6 = pic6.subsample(6, 6)
image7 = pic7.subsample(5, 5)
image8 = pic8.subsample(6, 6)
image9 = pic9.subsample(6, 6)
image10 = pic10.subsample(6, 6)
image11 = pic11.subsample(6, 6)
image12 = pic12.subsample(6, 6)
image13 = pic13.subsample(7, 7)
image14 = pic14.subsample(7, 7)
image15 = pic15.subsample(6, 6)
image16 = pic16.subsample(6, 6)

#imageshowonebyone
img1 = PhotoImage(file="Resources/blank.png")
label=Label(frame1, image=img1, bg="grey")
label.grid(row=0, column=0, padx=5, pady=5)


image1button = Button(frame2, image=image1, command=lambda m=1:img_change(m))
image1button.grid(row=0, column=0, padx=10, pady=15)
label1 = Label(frame2, text="Image 1",font=("Calibri, 8"))
label1.place(x=50, y=144)

image2button = Button(frame2, image=image2, command=lambda m=2:img_change(m))
image2button.grid(row=0, column=1, padx=10, pady=15)
label2 = Label(frame2, text="Image 2",font=("Calibri, 8"))
label2.place(x=198, y=144)

image3button = Button(frame2, image=image3, command=lambda m=3:img_change(m))
image3button.grid(row=0, column=2, padx=10, pady=15)
label3 = Label(frame2, text="Image 3",font=("Calibri, 8"))
label3.place(x=328, y=144)

image4button = Button(frame2, image=image4, command=lambda m=4:img_change(m))
image4button.grid(row=0, column=3, padx=10, pady=15)
label4 = Label(frame2, text="Image 4",font=("Calibri, 8"))
label4.place(x=472, y=128)

image5button = Button(frame2, image=image5, command=lambda m=5:img_change(m))
image5button.grid(row=1, column=0, padx=10, pady=15)
label5 = Label(frame2, text="Image 5",font=("Calibri, 8"))
label5.place(x=50, y=300)

image6button = Button(frame2, image=image6, command=lambda m=6:img_change(m))
image6button.grid(row=1, column=1, padx=10, pady=15)
label6 = Label(frame2, text="Image 6",font=("Calibri, 8"))
label6.place(x=198, y=300)

image7button = Button(frame2, image=image7, command=lambda m=7:img_change(m))
image7button.grid(row=1, column=2, padx=10, pady=15)
label7 = Label(frame2, text="Image 7",font=("Calibri, 8"))
label7.place(x=328, y=295)

image8button = Button(frame2, image=image8, command=lambda m=8:img_change(m))
image8button.grid(row=1, column=3, padx=10, pady=15)
label8 = Label(frame2, text="Image 8",font=("Calibri, 8"))
label8.place(x=472, y=305)

image9button = Button(frame2, image=image9, command=lambda m=9:img_change(m))
image9button.grid(row=2, column=0, padx=10, pady=15)
label9 = Label(frame2, text="Image 9",font=("Calibri, 8"))
label9.place(x=50, y=455)

image10button = Button(frame2, image=image10, command=lambda m=10:img_change(m))
image10button.grid(row=2, column=1, padx=10, pady=15)
label10 = Label(frame2, text="Image 10",font=("Calibri, 8"))
label10.place(x=190, y=463)

image11button = Button(frame2, image=image11, command=lambda m=11:img_change(m))
image11button.grid(row=2, column=2, padx=10, pady=15)
label11 = Label(frame2, text="Image 11",font=("Calibri, 8"))
label11.place(x=322, y=467)

image12button = Button(frame2, image=image12, command=lambda m=12:img_change(m))
image12button.grid(row=2, column=3, padx=10, pady=15)
label12 = Label(frame2, text="Image 12",font=("Calibri, 8"))
label12.place(x=472, y=455)

image13button = Button(frame2, image=image13, command=lambda m=13:img_change(m))
image13button.grid(row=3, column=0, padx=10, pady=20)
label13 = Label(frame2, text="Image 13",font=("Calibri, 8"))
label13.place(x=50, y=616)

image14button = Button(frame2, image=image14, command=lambda m=14:img_change(m))
image14button.grid(row=3, column=1, padx=10, pady=20)
label14 = Label(frame2, text="Image 14",font=("Calibri, 8"))
label14.place(x=190, y=616)

image15button = Button(frame2, image=image15, command=lambda m=15:img_change(m))
image15button.grid(row=3, column=2, padx=10, pady=20)
label15 = Label(frame2, text="Image 15",font=("Calibri, 8"))
label15.place(x=322, y=622)

image16button = Button(frame2, image=image16, command=lambda m=16:img_change(m))
image16button.grid(row=3, column=3, padx=10, pady=20)
label16 = Label(frame2, text="Image 16",font=("Calibri, 8"))
label16.place(x=472, y=622)


start = Button(frame3, text="Start Show!",font=("Calibri, 12"), bg='pink', width=13, height=2, command=startshow)
start.grid(rowspan =1 , columnspan = 4)

main.mainloop()
