
import PyPDF2

#┌───────────────┐
#│ NOTE: Reading │
#└───────────────┘
pdf_file = open("d_PdfWordExel/meetingminutes1.pdf")
reader = PyPDF2.PdfFileReader(pdf_file)
reader.numPages
page = reader.getPage(0)       # first page
page.extractText()


#┌────────────────┐
#│ NOTE: Editting │
#└────────────────┘
# You can reorder/delete page and create new pdf
# but cannot change the text on a page/change color/change font/...
pdf1 = open("d_PdfWordExel/meetingminutes1.pdf", "rb")  # read binary mode
pdf2 = open("d_PdfWordExel/meetingminutes2.pdf", "rb")
reader1 = PyPDF2.PdfFileReader(pdf1)
reader2 = PyPDF2.PdfFileReader(pdf2)
writer = PyPDF2.PdfFileWriter()     # create blank pdf on memory
for pagenum in range(reader1.numPages):
    page = reader1.getPage(pagenum)
    writer.addPage(page)
for pagenum in range(reader2.numPages):
    page = reader2.getPage(pagenum)
    writer.addPage(page)

output_file = open("d_PdfWordExel/meetingminutes_combine.pdf", "wb")
writer.write(output_file)
output_file.close()
pdf1.close()
pdf2.close()
