#coding:utf-8
import os,sys

#return item list
def getAllItem(path, itemtype='jpg'):
	L = []
	for file in os.listdir(path): 
		if os.path.splitext(file)[1][1:] == itemtype:  
			L.append(os.path.join(path, file))
	return L

def png2pdf(path, width, heigth, itemtype):
	from fpdf import FPDF
	items = getAllItem(path, itemtype=itemtype)
	pdf = FPDF(unit="pt", format=[width, heigth]) ## Choose your width and heigth of your Images
	for item in items:
	    pdf.add_page()
	    pdf.image(item,x=0,y=0,w=0, h=0) ## Images are placed at the top left corner
	    
	pdf.output("result.pdf",'F') ## output(name,File to local storage)

def pdf2png(pdfname, itemtype):
	from wand.image import Image
	from wand.color import Color

	os.mkdir('png')
	page_number = 0
	with Image(filename=pdfname, resolution=300) as img:
		for page in img.sequence:
			with Image(width=img.width, height=img.height, background=Color("white")) as bg:
				bg.composite(page, 0, 0)
				bg.save(filename="./png/{}.{}".format(page_number, itemtype))
				page_number += 1

if __name__ == '__main__':
	func = sys.argv[1]
	if func ==  'png2pdf':
		path = sys.argv[2]
		width = int(sys.argv[3])
		heigth = int(sys.argv[4])
		itemtype = sys.argv[5]
		png2pdf(path, width, heigth, itemtype)
	elif func == 'pdf2png':
		pdfname = sys.argv[2]
		itemtype = sys.argv[3]
		pdf2png(pdfname, itemtype)
