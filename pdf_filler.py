from PyPDF2 import PdfFileWriter, PdfFileReader
import io, time
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
packet = io.BytesIO()

# introduction
print('This program generates filled multipage PDF patient orders')
print('Enter requested information')
print(' ')

# information
# Physician name and pager
physician = input(' Physician initials ')
namedict = {
    "BB":"B___ B___, MD",
    "CC":"C___ C___, DO"
}
mdname = namedict.get(physician)
pagerdict = {
    "BB":"1234",
    "CC":"4567"
}
pager = pagerdict.get(physician)

# dates
date1 = input(' Date #1 ')
date2 = input(' Date #2 ')
date3 = input(' Date #3 ')
# times
time1 = input(' Time #1 ')
time2 = input(' Time #2 ')
time3 = input(' Time #3 ')
# name
names = input(' Patient name ')
# dob
dob = input(' Patient date of birth ')
# mrn
mrn = input(' Patient MRN ')
# weight
wght = input(' Patient weight ')
# height
hght = input(' Patient height ')

# allergy
allergy = input(' Patient allergies ')

# locations
x_loc = 146
y_loc = 585

# canvas to define locations
can = canvas.Canvas(packet, pagesize=letter)
can.setFont('Helvetica',9)
can.drawString(x_loc+165, y_loc-475, mdname)
can.setFont('Helvetica',10)
can.drawString(x_loc, y_loc, date1)
can.drawString(x_loc+152, y_loc, date2)
can.drawString(x_loc+309, y_loc, date3)
can.drawString(x_loc+80, y_loc, time1)
can.drawString(x_loc+228, y_loc, time2)
can.drawString(x_loc+383, y_loc, time3)
can.setFont('Helvetica',12)
can.drawString(x_loc+182, y_loc+140, names)
can.drawString(x_loc+182, y_loc+130, dob)
can.drawString(x_loc+182, y_loc+120, mrn)
can.setFont('Helvetica',10)
can.drawString(x_loc-80, y_loc+34, wght)
can.drawString(x_loc-80, y_loc+24, hght)
can.drawString(x_loc-53, y_loc+24, 'cm')
can.drawString(x_loc+20, y_loc+34, allergy)
can.drawString(x_loc+165, y_loc-490, pager)
can.drawString(x_loc+370, y_loc-474, time.strftime("%H:%M"))
can.drawString(x_loc+280, y_loc-475, time.strftime("%m/%d/%Y"))
can.save()

packet.seek(0)
new_pdf = PdfFileReader(packet)

# read existing PDF
existing_pdf = PdfFileReader(open("document.pdf", "rb"))
output = PdfFileWriter()

# add text
for page_num in range(7):
    page = existing_pdf.getPage(page_num)
    page.mergePage(new_pdf.getPage(0))
    output.addPage(page)

# write output
outputname = names + " " + format(time.strftime("%m-%d-%Y")) + ".pdf"
outputStream = open(outputname, "wb")
output.write(outputStream)
outputStream.close()
