



# not all pdf  are readable by python or pypdf2

# reading from pdf files

import PyPDF2

f = open('csv_pdfs/Working_Business_Proposal.pdf',mode='rb')

pdf_reader = PyPDF2.PdfReader(f)

res = len(pdf_reader.pages)
print(res)


page_one = pdf_reader.pages[0]
print(page_one.extract_text())

f.close()


f = open('csv_pdfs/Working_Business_Proposal.pdf',mode='rb')


pdf_reader = PyPDF2.PdfReader(f)

pageone = pdf_reader.pages[0]

pdf_writer = PyPDF2.PdfWriter()

pdf_writer.add_page(pageone)

pdf_op = open('csv_pdfs/newfilebi.pdf',mode='wb')

pdf_writer.write(pdf_op)

f.close()
pdf_op.close()