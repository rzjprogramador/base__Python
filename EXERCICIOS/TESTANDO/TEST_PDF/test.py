import PyPDF2

arquivo = r"/pdfs/pdf_1.pdf"
ler_pdf = PyPDF2.PdfFileReader(arquivo)
pagina = ler_pdf.getPage(0)
conteudo = pagina.extractText()
print(conteudo)


'''
pdf_1.pdf
/home/rzj/_noGIT/Python/base__Python/EXERCICIOS/TESTANDO/TEST_PDF/pdfs/

'''
