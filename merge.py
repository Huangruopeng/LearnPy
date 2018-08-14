from PyPDF2 import PdfFileMerger,PdfFileReader
merger = PdfFileMerger()
input1=open("1.0-第1周辅学内容.pdf","rb")
input2=open("1.1-程序设计基本方法.pdf","rb") 
merger.append(fileobj=input1,pages=(0,3))
merger.merge(position=2,fileobj=input2,pages=(0,1))
output=open("merge1.pdf","wb")
merger.write(output)
