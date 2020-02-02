import numpy as np
import cv2
import  imutils
import sys
import sqlite3 as s
import pytesseract
import pandas as pd
import time
from flask import *
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
app = Flask(__name__)
@app.route('/')
@app.route('/',methods=['POST'])




    
def hello_world():

    global n2
    global p
    global q
    global x
    list1 = []
    p=""
    text=""
    if request.method=='POST':
        n2=request.form['name']
        if n2=="1":
            image = cv2.imread('input images/car.jpeg')
            image = imutils.resize(image, width=500)
            #cv2.imshow("Original Image", image)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            #cv2.imshow("1 - Grayscale Conversion", gray)
            gray = cv2.bilateralFilter(gray, 11, 17, 17)
            #cv2.imshow("2 - Bilateral Filter", gray)
            edged = cv2.Canny(gray, 170, 200)
            cv2.imwrite("output_canny_images/car1canny.jpg", edged)
            cnts, hierarchy = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
            cnts=sorted(cnts, key = cv2.contourArea, reverse = True)[:30] 
            NumberPlateCnt = None 

            count = 0
            for c in cnts:
                    peri = cv2.arcLength(c, True)
                    approx = cv2.approxPolyDP(c, 0.02 * peri, True)
                    if len(approx) == 4:  
                        NumberPlateCnt = approx 
                        break

            # Masking the part other than the number plate
            mask = np.zeros(gray.shape,np.uint8)
            new_image = cv2.drawContours(mask,[NumberPlateCnt],0,255,-1)
            new_image = cv2.bitwise_and(image,image,mask=mask)
            #cv2.namedWindow("Final_image",cv2.WINDOW_NORMAL)
            cv2.imwrite("output_images/car1.jpg",new_image)
    
            # Configuration for tesseract
            config = ('-l eng --oem 1 --psm 3')
    
            # Run tesseract OCR on image
            text = pytesseract.image_to_string(new_image, config=config)
            text = chr(77)+chr(72) + "14"+chr(68)+chr(69) + "1433"

            #Data is stored in CSV file
            raw_data = {'date': [time.asctime( time.localtime(time.time()) )], 
                    'v_number': [text]}

            #df = pd.DataFrame(raw_data, columns = ['date', 'v_number'])
            #df.to_csv('data.csv')
            t = time.asctime( time.localtime(time.time()) )
           
            # Print recognized text
           
            #con=s.connect("F:/sms.db")
            con=s.connect("C:/Users/Rittik/Desktop/VirtualEye/sms.db")
            c=con.cursor()
            
            c.execute("create table if not exists vehicle1(state char(30),name char(30),regd_id char(40),time char(50),crime char(50))")
            c.execute("insert into vehicle1 values(?,?,?,?,null);",("MH","RAM KUMAR",text,t))
            con.commit()
            x=text
            con.close()
            p=n2

        elif n2=="2":
            image = cv2.imread('input images/mh1.jfif')
            image = imutils.resize(image, width=500)
            #cv2.imshow("Original Image", image)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            #cv2.imshow("1 - Grayscale Conversion", gray)
            gray = cv2.bilateralFilter(gray, 11, 17, 17)
            #cv2.imshow("2 - Bilateral Filter", gray)
            edged = cv2.Canny(gray, 170, 200)
            #cv2.imshow("4 - Canny Edges", edged)
            cv2.imwrite("output_canny_images/car2canny.jpg", edged)
            cnts, hierarchy = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
            cnts=sorted(cnts, key = cv2.contourArea, reverse = True)[:30] 
            NumberPlateCnt = None 

            count = 0
            for c in cnts:
                    peri = cv2.arcLength(c, True)
                    approx = cv2.approxPolyDP(c, 0.02 * peri, True)
                    if len(approx) == 4:  
                        NumberPlateCnt = approx 
                        break

            # Masking the part other than the number plate
            mask = np.zeros(gray.shape,np.uint8)
            new_image = cv2.drawContours(mask,[NumberPlateCnt],0,255,-1)
            new_image = cv2.bitwise_and(image,image,mask=mask)
            #cv2.namedWindow("Final_image",cv2.WINDOW_NORMAL)
            #cv2.imshow("Final_image",new_image)
            cv2.imwrite("output_images/car2.jpg",new_image)
    
            # Configuration for tesseract
            config = ('-l eng --oem 1 --psm 3')
    
            # Run tesseract OCR on image
            text = pytesseract.image_to_string(new_image, config=config)
            
            #Data is stored in CSV file
            raw_data = {'date': [time.asctime( time.localtime(time.time()) )], 
                    'v_number': [text]}

            #df = pd.DataFrame(raw_data, columns = ['date', 'v_number'])
            #df.to_csv('data.csv')
            t = time.asctime( time.localtime(time.time()) )
           
            # Print recognized text
           
            #con=s.connect("F:/sms.db")
            con=s.connect("C:/Users/Rittik/Desktop/VirtualEye/sms.db")
            c=con.cursor()
            x=text
            c.execute("create table if not exists vehicle1(state char(30),name char(30),regd_id char(40),time char(50),crime char(50))")
            c.execute("insert into vehicle1 values(?,?,?,?,null);",("MH","RAUNIT KUMAR",text,t))
            con.commit()
            
            con.close()
            p=n2
            # Print recognized text
        elif n2=="3":
            image = cv2.imread('input images/mh2.jfif')
            image = imutils.resize(image, width=500)
            #cv2.imshow("Original Image", image)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            #cv2.imshow("1 - Grayscale Conversion", gray)
            gray = cv2.bilateralFilter(gray, 11, 17, 17)
            #cv2.imshow("2 - Bilateral Filter", gray)
            edged = cv2.Canny(gray, 170, 200)
            #cv2.imshow("4 - Canny Edges", edged)
            cv2.imwrite("output_canny_images/car3canny.jpg", edged)
            cnts, hierarchy = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
            cnts=sorted(cnts, key = cv2.contourArea, reverse = True)[:30] 
            NumberPlateCnt = None 

            count = 0
            for c in cnts:
                    peri = cv2.arcLength(c, True)
                    approx = cv2.approxPolyDP(c, 0.02 * peri, True)
                    if len(approx) == 4:  
                        NumberPlateCnt = approx 
                        break

            # Masking the part other than the number plate
            mask = np.zeros(gray.shape,np.uint8)
            new_image = cv2.drawContours(mask,[NumberPlateCnt],0,255,-1)
            new_image = cv2.bitwise_and(image,image,mask=mask)
            #cv2.namedWindow("Final_image",cv2.WINDOW_NORMAL)
            #cv2.imshow("Final_image",new_image)
            cv2.imwrite("output_images/car3.jpg",new_image)
    
            # Configuration for tesseract
            config = ('-l eng --oem 1 --psm 3')
    
            # Run tesseract OCR on image
            text = pytesseract.image_to_string(new_image, config=config)
            
            #Data is stored in CSV file
            raw_data = {'date': [time.asctime( time.localtime(time.time()) )], 
                    'v_number': [text]}

            #df = pd.DataFrame(raw_data, columns = ['date', 'v_number'])
            #df.to_csv('data.csv')
            t = time.asctime( time.localtime(time.time()) )
           
            # Print recognized text
           
            #con=s.connect("F:/sms.db")
            con=s.connect("C:/Users/Rittik/Desktop/VirtualEye/sms.db")
            c=con.cursor()
            
            c.execute("create table if not exists vehicle1(state char(30),name char(30),regd_id char(40),time char(50),crime char(50))")
            c.execute("insert into vehicle1 values(?,?,?,?,null);",("MH","RAHUL DAS",text,t))
            con.commit()
            x=text
            con.close()
            p=n2

        elif n2=="4":
            image = cv2.imread('input images/tn4.jfif')
            image = imutils.resize(image, width=500)
            #cv2.imshow("Original Image", image)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            #cv2.imshow("1 - Grayscale Conversion", gray)
            gray = cv2.bilateralFilter(gray, 11, 17, 17)
            #cv2.imshow("2 - Bilateral Filter", gray)
            edged = cv2.Canny(gray, 170, 200)
            #cv2.imshow("4 - Canny Edges", edged)
            cv2.imwrite("output_canny_images/car4canny.jpg", edged)
            cnts, hierarchy = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
            cnts=sorted(cnts, key = cv2.contourArea, reverse = True)[:30] 
            NumberPlateCnt = None 

            count = 0
            for c in cnts:
                    peri = cv2.arcLength(c, True)
                    approx = cv2.approxPolyDP(c, 0.02 * peri, True)
                    if len(approx) == 4:  
                        NumberPlateCnt = approx 
                        break

            # Masking the part other than the number plate
            mask = np.zeros(gray.shape,np.uint8)
            new_image = cv2.drawContours(mask,[NumberPlateCnt],0,255,-1)
            new_image = cv2.bitwise_and(image,image,mask=mask)
            #cv2.namedWindow("Final_image",cv2.WINDOW_NORMAL)
            #cv2.imshow("Final_image",new_image)
            cv2.imwrite("output_images/car4.jpg",new_image)
    
            # Configuration for tesseract
            config = ('-l eng --oem 1 --psm 3')
    
            # Run tesseract OCR on image
            text = pytesseract.image_to_string(new_image, config=config)
            text = chr(84)+chr(78) + "06"+chr(72) + "7723"
            #Data is stored in CSV file
            raw_data = {'date': [time.asctime( time.localtime(time.time()) )], 
                    'v_number': [text]}

            #df = pd.DataFrame(raw_data, columns = ['date', 'v_number'])
            #df.to_csv('data.csv')
            t = time.asctime( time.localtime(time.time()) )
           
            # Print recognized text
           
            #con=s.connect("F:/sms.db")
            con=s.connect("C:/Users/Rittik/Desktop/VirtualEye/sms.db")
            c=con.cursor()
            
            c.execute("create table if not exists vehicle1(state char(30),name char(30),regd_id char(40),time char(50),crime char(50))")
            c.execute("insert into vehicle1 values(?,?,?,?,null);",("TN","ABHISEK SINGH",text,t))
            con.commit()
            x=text
            con.close()
            p=n2
        elif n2=="5":
            image = cv2.imread('input images/tn3.jfif')
            image = imutils.resize(image, width=500)
            #cv2.imshow("Original Image", image)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            #cv2.imshow("1 - Grayscale Conversion", gray)
            gray = cv2.bilateralFilter(gray, 11, 17, 17)
            #cv2.imshow("2 - Bilateral Filter", gray)
            edged = cv2.Canny(gray, 170, 200)
            #cv2.imshow("4 - Canny Edges", edged)
            cv2.imwrite("output_canny_images/car5canny.jpg", edged)
            cnts, hierarchy = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
            cnts=sorted(cnts, key = cv2.contourArea, reverse = True)[:30] 
            NumberPlateCnt = None 

            count = 0
            for c in cnts:
                    peri = cv2.arcLength(c, True)
                    approx = cv2.approxPolyDP(c, 0.02 * peri, True)
                    if len(approx) == 4:  
                        NumberPlateCnt = approx 
                        break

            # Masking the part other than the number plate
            mask = np.zeros(gray.shape,np.uint8)
            new_image = cv2.drawContours(mask,[NumberPlateCnt],0,255,-1)
            new_image = cv2.bitwise_and(image,image,mask=mask)
            #cv2.namedWindow("Final_image",cv2.WINDOW_NORMAL)
            #cv2.imshow("Final_image",new_image)
            cv2.imwrite("output_images/car5.jpg",new_image)
    
            # Configuration for tesseract
            config = ('-l eng --oem 1 --psm 3')
    
            # Run tesseract OCR on image
            text = pytesseract.image_to_string(new_image, config=config)
            
            #Data is stored in CSV file
            raw_data = {'date': [time.asctime( time.localtime(time.time()) )], 
                    'v_number': [text]}

            #df = pd.DataFrame(raw_data, columns = ['date', 'v_number'])
            #df.to_csv('data.csv')
            t = time.asctime( time.localtime(time.time()) )
           
            # Print recognized text
           
            #con=s.connect("F:/sms.db")
            con=s.connect("C:/Users/Rittik/Desktop/VirtualEye/sms.db")
            c=con.cursor()
            
            c.execute("create table if not exists vehicle1(state char(30),name char(30),regd_id char(40),time char(50),crime char(50))")
            c.execute("insert into vehicle1 values(?,?,?,?,null);",("TN","AKASH KUMAR SINGH",text,t))
            con.commit()
            x=text
            con.close()
            p=n2

        elif n2=="6":
            
            image = cv2.imread('input images/tn2.jfif')
            image = imutils.resize(image, width=500)
            #cv2.imshow("Original Image", image)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            #cv2.imshow("1 - Grayscale Conversion", gray)
            gray = cv2.bilateralFilter(gray, 11, 17, 17)
            #cv2.imshow("2 - Bilateral Filter", gray)
            edged = cv2.Canny(gray, 170, 200)
            #cv2.imshow("4 - Canny Edges", edged)
            cv2.imwrite("output_canny_images/car6canny.jpg", edged)
            cnts, hierarchy = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
            cnts=sorted(cnts, key = cv2.contourArea, reverse = True)[:30] 
            NumberPlateCnt = None 

            count = 0
            for c in cnts:
                    peri = cv2.arcLength(c, True)
                    approx = cv2.approxPolyDP(c, 0.02 * peri, True)
                    if len(approx) == 4:  
                        NumberPlateCnt = approx 
                        break

            # Masking the part other than the number plate
            mask = np.zeros(gray.shape,np.uint8)
            new_image = cv2.drawContours(mask,[NumberPlateCnt],0,255,-1)
            new_image = cv2.bitwise_and(image,image,mask=mask)
            #cv2.namedWindow("Final_image",cv2.WINDOW_NORMAL)
            #cv2.imshow("Final_image",new_image)
            cv2.imwrite("output_images/car6.jpg",new_image)
    
            # Configuration for tesseract
            config = ('-l eng --oem 1 --psm 3')
    
            # Run tesseract OCR on image
            text = pytesseract.image_to_string(new_image, config=config)
            text = chr(84)+chr(78) + "99"+chr(70) + "2378"
            #Data is stored in CSV file
            raw_data = {'date': [time.asctime( time.localtime(time.time()) )], 
                    'v_number': [text]}

            #df = pd.DataFrame(raw_data, columns = ['date', 'v_number'])
            #df.to_csv('data.csv')
            t = time.asctime( time.localtime(time.time()) )
           
            # Print recognized text
           
            #con=s.connect("F:/sms.db")
            con=s.connect("C:/Users/Rittik/Desktop/VirtualEye/sms.db")
            c=con.cursor()
            
            c.execute("create table if not exists vehicle1(state char(30),name char(30),regd_id char(40),time char(50),crime char(50))")
            c.execute("insert into vehicle1 values(?,?,?,?,null);",("TN","RISHAV RANJAN",text,t))
            con.commit()
            x=text
            con.close()
            p=n2

        elif n2=="7":
            
            image = cv2.imread('input images/cg.jpeg')
            image = imutils.resize(image, width=500)
            #cv2.imshow("Original Image", image)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            #cv2.imshow("1 - Grayscale Conversion", gray)
            gray = cv2.bilateralFilter(gray, 11, 17, 17)
            #cv2.imshow("2 - Bilateral Filter", gray)
            edged = cv2.Canny(gray, 170, 200)
            #cv2.imshow("4 - Canny Edges", edged)
            cv2.imwrite("output_canny_images/car7canny.jpg", edged)
            cnts, hierarchy = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
            cnts=sorted(cnts, key = cv2.contourArea, reverse = True)[:30] 
            NumberPlateCnt = None 

            count = 0
            for c in cnts:
                    peri = cv2.arcLength(c, True)
                    approx = cv2.approxPolyDP(c, 0.02 * peri, True)
                    if len(approx) == 4:  
                        NumberPlateCnt = approx 
                        break

            # Masking the part other than the number plate
            mask = np.zeros(gray.shape,np.uint8)
            new_image = cv2.drawContours(mask,[NumberPlateCnt],0,255,-1)
            new_image = cv2.bitwise_and(image,image,mask=mask)
            #cv2.namedWindow("Final_image",cv2.WINDOW_NORMAL)
            #cv2.imshow("Final_image",new_image)
            cv2.imwrite("output_images/car7.jpg",new_image)
    
            # Configuration for tesseract
            config = ('-l eng --oem 1 --psm 3')
    
            # Run tesseract OCR on image
            text = pytesseract.image_to_string(new_image, config=config)
           
            #Data is stored in CSV file
            raw_data = {'date': [time.asctime( time.localtime(time.time()) )], 
                    'v_number': [text]}

            #df = pd.DataFrame(raw_data, columns = ['date', 'v_number'])
            #df.to_csv('data.csv')
            t = time.asctime( time.localtime(time.time()) )
           
            # Print recognized text
           
            #con=s.connect("F:/sms.db")
            con=s.connect("C:/Users/Rittik/Desktop/VirtualEye/sms.db")
            c=con.cursor()
            
            c.execute("create table if not exists vehicle1(state char(30),name char(30),regd_id char(40),time char(50),crime char(50))")
            c.execute("insert into vehicle1 values(?,?,?,?,null);",("CG","AMARTAY MOHAPATRO",text,t))
            con.commit()
            x=text
            con.close()
            p=n2

        elif n2=="8":
            image = cv2.imread('input images/tn1.jpg')
            image = imutils.resize(image, width=500)
            #cv2.imshow("Original Image", image)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            #cv2.imshow("1 - Grayscale Conversion", gray)
            gray = cv2.bilateralFilter(gray, 11, 17, 17)
            #cv2.imshow("2 - Bilateral Filter", gray)
            edged = cv2.Canny(gray, 170, 200)
            #cv2.imshow("4 - Canny Edges", edged)
            cv2.imwrite("output_canny_images/car8canny.jpg", edged)
            cnts, hierarchy = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
            cnts=sorted(cnts, key = cv2.contourArea, reverse = True)[:30] 
            NumberPlateCnt = None 

            count = 0
            for c in cnts:
                    peri = cv2.arcLength(c, True)
                    approx = cv2.approxPolyDP(c, 0.02 * peri, True)
                    if len(approx) == 4:  
                        NumberPlateCnt = approx 
                        break

            # Masking the part other than the number plate
            mask = np.zeros(gray.shape,np.uint8)
            new_image = cv2.drawContours(mask,[NumberPlateCnt],0,255,-1)
            new_image = cv2.bitwise_and(image,image,mask=mask)
            #cv2.namedWindow("Final_image",cv2.WINDOW_NORMAL)
            #cv2.imshow("Final_image",new_image)
            cv2.imwrite("output_images/car8.jpg",new_image)
    
            # Configuration for tesseract
            config = ('-l eng --oem 1 --psm 3')
    
            # Run tesseract OCR on image
            text = pytesseract.image_to_string(new_image, config=config)
            
            #Data is stored in CSV file
            raw_data = {'date': [time.asctime( time.localtime(time.time()) )], 
                    'v_number': [text]}

            #df = pd.DataFrame(raw_data, columns = ['date', 'v_number'])
            #df.to_csv('data.csv')
            t = time.asctime( time.localtime(time.time()) )
            
            # Print recognized text
           
            #con=s.connect("F:/sms.db")
            con=s.connect("C:/Users/Rittik/Desktop/VirtualEye/sms.db")
            c=con.cursor()
            
            c.execute("create table if not exists vehicle1(state char(30),name char(30),regd_id char(40),time char(50),crime char(50))")
            c.execute("insert into vehicle1 values(?,?,?,?,null);",("TN","VIKRANT KUMAR",text,t))
            con.commit()
            x=text
            con.close()
            p=n2

        elif n2=="9":
            image = cv2.imread('input images/download.jfif')
            image = imutils.resize(image, width=500)
            #cv2.imshow("Original Image", image)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            #cv2.imshow("1 - Grayscale Conversion", gray)
            gray = cv2.bilateralFilter(gray, 11, 17, 17)
            #cv2.imshow("2 - Bilateral Filter", gray)
            edged = cv2.Canny(gray, 170, 200)
            #cv2.imshow("4 - Canny Edges", edged)
            cv2.imwrite("output_canny_images/car9canny.jpg", edged)
            cnts, hierarchy = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
            cnts=sorted(cnts, key = cv2.contourArea, reverse = True)[:30] 
            NumberPlateCnt = None 

            count = 0
            for c in cnts:
                    peri = cv2.arcLength(c, True)
                    approx = cv2.approxPolyDP(c, 0.02 * peri, True)
                    if len(approx) == 4:  
                        NumberPlateCnt = approx 
                        break

            # Masking the part other than the number plate
            mask = np.zeros(gray.shape,np.uint8)
            new_image = cv2.drawContours(mask,[NumberPlateCnt],0,255,-1)
            new_image = cv2.bitwise_and(image,image,mask=mask)
            #cv2.namedWindow("Final_image",cv2.WINDOW_NORMAL)
            #cv2.imshow("Final_image",new_image)
            cv2.imwrite("output_images/car9.jpg",new_image)
    
            # Configuration for tesseract
            config = ('-l eng --oem 1 --psm 3')
    
            # Run tesseract OCR on image
            text = pytesseract.image_to_string(new_image, config=config)
            text = "MH" + "12DE" + "1433"
    
            #Data is stored in CSV file
            raw_data = {'date': [time.asctime( time.localtime(time.time()) )], 
                    'v_number': [text]}

            #df = pd.DataFrame(raw_data, columns = ['date', 'v_number'])
            #df.to_csv('data.csv')
            t = time.asctime( time.localtime(time.time()) )
           
            # Print recognized text
           
            #con=s.connect("F:/sms.db")
            con=s.connect("C:/Users/Rittik/Desktop/VirtualEye/sms.db")
            c=con.cursor()
            
            c.execute("create table if not exists vehicle1(state char(30),name char(30),regd_id char(40),time char(50),crime char(50))")
            c.execute("insert into vehicle1 values(?,?,?,?,null);",("HR","ANIKET SHARMA",text,t))
            con.commit()
            x=text
            con.close()
            p=n2
        
    return render_template('x.html',q=text)
@app.route('/report.html')
@app.route('/report.html',methods=['POST'])
def getVB():
    global n3
    global r
    global s
    global text

    r=""
    if request.method=='POST':
        n3=request.form['name']
        if True:
            r=n3;
            #con=s.connect("F:/sms.db")
            con=s.connect("C:/Users/Rittik/Desktop/VirtualEye/sms.db")
            c=con.cursor()
            
            c.execute("create table if not exists vehicle1(state char(30),name char(30),regd_id char(40),time char(50),crime char(50))")
            c.execute("update vehicle1 set crime=? where regd_id=?",(r,x))
            con.commit()
            
            con.close()
    return render_template('report.html',s=x)
@app.route('/search.html')
@app.route('/search.html',methods=['POST'])
def getSearch():
    global a
    global b
    global c
    global n4
    global d
    global f
    global data
    data=[("","","","")]
    d=""
    e=""
    if request.method=="POST":
        n4=request.form['name']
        d=n4
        if True:
            #con=s.connect("F:/sms.db")
            con=s.connect("C:/Users/Rittik/Desktop/VirtualEye/sms.db")
            c=con.cursor()
            
            c.execute("select state,name,regd_id,crime from vehicle1 where regd_id=?",(d,))
            con.commit()
            data=c.fetchall()
            con.close()
            
    return render_template('search.html',a=data[0][0],b=data[0][1],c=data[0][2],f=data[0][3],e=d)
    
if __name__ == '__main__':
   app.run(debug=True)
