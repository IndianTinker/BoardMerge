import sys

if __name__ == '__main__' and len(sys.argv) > 0 and sys.argv[1][-3:].upper() == 'PDF':
	from pyPdf import PdfFileWriter, PdfFileReader	
	print len(sys.argv)
	#inp[]
	total=len(sys.argv)
	original = sys.argv[1]
	target ='Combine.pdf'
	inp = PdfFileReader(file(sys.argv[1], "rb"))
	page=inp.getPage(0)
	output = PdfFileWriter()
	for i in range(1,total):	
		
		inp = PdfFileReader(file(sys.argv[i], "rb"))	
		page.mergePage(inp.getPage(0))
		
	#numPages = input1.getNumPages()
	# print the title of document1.pdf
	# print "title = %s" % (input1.getDocumentInfo().title)
	#for i in total:
	#       page.mergePage(inp[i].getPage(1))


output.addPage(page)
outputStream = file(target, "wb")
output.write(outputStream)
outputStream.close()
print "DONE !"
