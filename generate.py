import PIL.Image
from PIL import Image, ImageDraw, ImageFont
import matplotlib.font_manager as fm
import random
import os


class ImageGeneration():

    def __init__(self):

        # words arr
        self.opt_words = []
        self.qual_words = []
        self.thing_words = []
        self.buffer = []
        self.words = []

        # approximate ratio of the word categories
        self.ratio = [12, 70, 18]

        # image generation specifications
        self.fonts = []
        self.sizes = [16, 20, 24] # (pt, px): (12, 16), (15, 20), (18, 24)
        self.rotate = (-15, 15)

        # dataset basic
        self.train_size = 1000 # 1000
        self.test_size = 200 # 200


    def readFile(self):

        # read the word files
        print(" --- start reading --- ")

        with open('Operations.txt', 'r') as f:
            for line in f:
                for word in line.split():
                    if len(word) > 0:
                        self.buffer.append(word[:-1])
        self.opt_words = random.sample(self.buffer, k=self.ratio[0])
        print("Operations: ", len(self.opt_words), "out of", len(self.buffer))

        self.buffer.clear()

        with open('Things.txt', 'r') as f:
            for line in f:
                for word in line.split():
                    if len(word) > 0:
                        self.buffer.append(word[:-1])
        self.thing_words = random.sample(self.buffer, k=self.ratio[1])
        print("Things: ", len(self.thing_words), "out of", len(self.buffer))

        self.buffer.clear()

        with open('Qualities.txt', 'r') as f:
            for line in f:
                for word in line.split():
                    if len(word) > 0:
                        self.buffer.append(word[:-1])
        self.qual_words = random.sample(self.buffer, k=self.ratio[2])
        print("Qualities: ", len(self.qual_words), "out of", len(self.buffer))

        # record the selected words
        words_file = open("words.txt", "w+")
        words_file.write("Operations: ")
        for f in self.opt_words:
            words_file.write(f+",")
        words_file.write("\n")

        words_file.write("Things: ")
        for f in self.thing_words:
            words_file.write(f+",")
        words_file.write("\n")

        words_file.write("Qualities: ")
        for f in self.qual_words:
            words_file.write(f+",")

        words_file.close()

        print(" --- finish reading --- ")


    def fontSetup(self):
        system_fonts = fm.findSystemFonts(fontpaths=None, fontext='ttf')
        self.fonts = random.sample(system_fonts, k=75)
        print("Total Font: ", len(self.fonts))

        # record the selected fonts
        font_file = open("font.txt", "w+")
        for f in self.fonts:
            font_file.write(f+",")
        font_file.close()


    def generateImg(self, text, imgSize=224, bgColor=255):

        # create a new image of size 224*224 in white
        img = PIL.Image.new(mode="RGB", size=(imgSize, imgSize), color=(bgColor, bgColor, bgColor))

        fnt = ImageFont.truetype(random.choice(self.fonts), random.choice(self.sizes))

        # transparent mask
        tim = PIL.Image.new('RGBA', (int(imgSize*1.28), int(imgSize*1.28)), (bgColor, bgColor, bgColor, 0))
        draw = ImageDraw.Draw(tim)
        draw.text((int(imgSize//2), int(imgSize//2)), text, fill=0, align="center", font=fnt)
        tim = tim.rotate(random.randint(-15, 15))
        Image.Image.paste(img, tim, (int(-imgSize*0.14),int(-imgSize*0.14)))
        # img.show()
        return img


    def pipline(self):

        # select 100 words from the 850 basic words and save to words.txt
        self.readFile()

        # randomly select 75 random fonts; print these fonts to font.txt
        self.fontSetup()

        # create a folder for the data
        curr_path = os.getcwd()
        save_path = os.path.join(curr_path, "data")
        os.mkdir(save_path, 0o666)

        for i in range(len(self.qual_words)):
            for j in range(1, self.train_size+self.test_size+1):
                img = self.generateImg(self.qual_words[i])
                img.save(f"{save_path}/"+"qual_"+self.qual_words[i]+"_"+str(j)+".png")

        for i in range(len(self.thing_words)):
            for j in range(1, self.train_size+self.test_size+1):
                img = self.generateImg(self.thing_words[i])
                img.save(f"{save_path}/"+"thing_"+self.thing_words[i]+"_"+str(j)+".png")

        for i in range(len(self.opt_words)):
            for j in range(1, self.train_size+self.test_size+1):
                img = self.generateImg(self.opt_words[i])
                img.save(f"{save_path}/"+"opt_"+self.opt_words[i]+"_"+str(j)+".png")



# execute the whole thing
g = ImageGeneration()
g.pipline()
