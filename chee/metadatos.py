# -*- encoding: utf-8 -*-
'''
Notas:
La función "walk" es útil para recorrer todos los ficheros y directorios que se encuentran incluidos en un directorio concreto.
'''

from PyPDF2 import PdfFileReader, PdfFileWriter # importamos modulo y librerias
import os # importamos modulo socket para ir a otras carpetas

def printMeta():
    for dirpath, dirnames, files in os.walk("chee"): # para el diretorio, nombre y archivos en la carpeta docs
        for name in files: # recorremos los posibles fichreos
            ext = name.lower().rsplit('.', 1)[-1]
            if ext in ['pdf']:
                print "[+] Metadata for file: %s " %(dirpath+os.path.sep+name) # pintamos el titulo de metadata for file y el directorio y nombre del documento
                pdfFile = PdfFileReader(file(dirpath+os.path.sep+name, 'rb')) # abrimos el fichero
                docInfo = pdfFile.getDocumentInfo() # creamos un diccionario con la info recolectada
                for metaItem in docInfo:
                    print '[+] ' + metaItem + ':' + docInfo[metaItem]
                print "\n"
printMeta() # invocamos la funcion
