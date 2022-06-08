from fpdf import FPDF
from os import listdir
import time
import random


class jpg2pdf:
    def __init__(self):
        self.jpg = []
        self.extensions = ('.jpg', '.png', '.gif' , '.jpeg')
        self.name = 'eng_yazeed' + str(random.randint(1,10000)) + '.pdf'

    def get_files(self):
        jj = listdir()
        for x in jj:
            for w in self.extensions:
                if x.endswith(w):
                    self.jpg.append(x)
                else:
                    pass

    def xpdf(self):
        
        pdf = FPDF()
       
        for f in self.jpg:
            pdf.add_page()

            pdf.image(f, x=0, y=0, w=210,
                      h=297)  
        pdf.output(self.name, "F")
        print('Done ...')


if __name__ == '__main__':
    c = jpg2pdf()
    c.get_files()
    c.xpdf()
