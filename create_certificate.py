# import required classes from modules
from PIL import Image, ImageDraw, ImageFont
import csv
from titlecase import titlecase

fontName = ImageFont.truetype('fonts/monotype corsiva.ttf', size=50)
colorName = 'rgb(0, 0, 0)'
#(x, y) = (550, 285)
(x, y) = (550, 290)

fontDept = ImageFont.truetype('fonts/PT Serif.ttf', size=25)
colorDept = 'rgb(0, 0, 0)' #black colour
(deptX, deptY) = (240, 345)

fontSerial = ImageFont.truetype('fonts/PT Serif.ttf', size=25)
colorSerial = 'rgb(0, 0, 0)' #black colour
(serialX, serialY) = (635, 650)

certificateCount = 0

with open('e-certificate receiver.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    # to remove the header from .csv file
    has_header = csv.Sniffer().has_header(csvFile.read(1024))
    csvFile.seek(0)  # Rewind.
    
    if has_header:
        # go to next row if header is present in the .csv file
        next(reader)

    for row in reader:   
        print(row[0], titlecase(row[1]))
        participentName = titlecase(row[1])
        
        # create Image object with the input image 
        baseImage = Image.open('E-Participation.png')
        # draw the message on the background
        draw = ImageDraw.Draw(baseImage)
        draw.text((x, y), participentName, fill=colorName, font=fontName)

        #to draw the department
        deptName = row[0][row[0].find('/')+len('/'):row[0].rfind('/1')] + ' Department'
        draw.text((deptX, deptY), deptName, fill=colorDept, font=fontDept)

        serialNo = 'SERIAL_NO/'+str(certificateCount).zfill(4)
        draw.text((serialX, serialY), serialNo, fill=colorSerial, font=fontSerial)
        certificateCount+=1
        # save the edited image
        baseImage.save('e-certificate/' + participentName + '-' + row[3] + '.png', optimize=True, quality=100)
           
csvFile.close()


