import PyPDF2

with open('dictionary.txt') as file_object:
	contents = file_object.read()

words = contents.split('\n')

pdf = open('encrypted.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(pdf)
pdf_writer = PyPDF2.PdfFileWriter()

for word in words:
    print('Trying to break in with ' + word + '...')
    try:
        if pdf_reader.decrypt(word) == 1:
            print('The password is', word)
            break
        elif pdf_reader.decrypt(word.lower()) == 1:
            print('The password is', word)
            break
    except:
        print('Password not found.')

for num_page in range(pdf_reader.numPages):
    page_obj = pdf_reader.getPage(num_page)
    pdf_writer.addPage(page_obj)

new_pdf = open('password.pdf', 'wb')
pdf_writer.write(new_pdf)
new_pdf.close()
pdf.close()
