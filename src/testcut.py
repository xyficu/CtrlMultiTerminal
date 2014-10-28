# from fits_cut_to_png import FitsCutToPng
import pyfits
import f2n
import sys
import Image
import os
from _mysql import NULL
import pyfits

# FitsCutToPng("20131203_m06-0848+50_1053.fit", "output1.png", 400, 500, 200)

# fgImg=Image.new("RGB", (300,300), (0,255,0))
# bgImg=Image.new("RGB", (500,500), (100,100,100))
# 
# bgImg.paste(fgImg,(20,20))
# bgImg.save("bgImg.png", "PNG")

# print(FitsCutToPng.version)
    tmpImage = f2n.fromfits("20131203_m06-0848+50_1053.fit")
    print "-----"
    print tmpImage.numpyarray[left:right, top:bottom]
    print "-----"

pfile = pyfits.open("20131203_m06-0848+50_1053.fit")

pfile.info()

print pfile[0].header.keys

# pfile.writeto('new.fit')
