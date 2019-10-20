# -*- encoding: utf-8 -*-
'''
Notas:
La función "walk" es útil para recorrer todos los ficheros y directorios que se encuentran incluidos en un directorio concreto.
'''

from PyPDF2 import PdfFileReader, PdfFileWriter # importamos modulo y librerias
import os # importamos modulo socket para ir a otras carpetas

print "\n"
print "*****************************************"
print "*****************************************"
print "***                                   ***"
print "***  GETTING METADATA FROM PDF FILES  ***"
print "***                                   ***"
print "*****************************************"
print "*****************************************"
print "\n"

def printMeta():
    for dirpath, dirnames, files in os.walk("chee"): # para el diretorio, nombre y archivos en la carpeta docs
        for name in files: # recorremos los posibles ficheros
            ext = name.lower().rsplit('.', 1)[-1]
            if ext in ['pdf']:
		print '==================================================='
                print "File path: %s " %(dirpath+os.path.sep+name) # pintamos el titulo de metadata for file y el directorio y nombre del documento
                pdfFile = PdfFileReader(file(dirpath+os.path.sep+name, 'rb')) # abrimos el fichero
                docInfo = pdfFile.getDocumentInfo() # creamos un diccionario con la info recolectada
		numPages = pdfFile.getNumPages() # Devuelve el número de páginas del documento
                for metaItem in docInfo:
		    print '-------------------------------------'
                    print metaItem + ':' + docInfo[metaItem]
		print '-------------------------------------'
		print "File pages: " + str(numPages)
                print "\n"
    print "Text extracted from first page: \n"
    page = pdfFile.getPage(0)
    print page.extractText()
printMeta() # invocamos la funcion
