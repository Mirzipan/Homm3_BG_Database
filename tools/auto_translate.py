#!/usr/bin/env python3
import polib
from googletrans import Translator
import sys
import re

def should_translate(text):
    """
    Devuelve False si se detecta que el texto contiene etiquetas HTML,
    atributos o elementos de código que no se deben traducir.
    """
    # Expresión regular que busca etiquetas HTML o los caracteres { } / \
    if re.search(r'<[^>]+>|[{}\\/]', text):
        return False
    return True

def traducir_po(archivo_po, destino='es'):
    po = polib.pofile(archivo_po)
    translator = Translator()
    
    print(f"Procesando: {archivo_po}")

    for entry in po:
        # Solo traducir si msgstr está vacío y si se considera traducible
        if not entry.msgstr.strip():
            if should_translate(entry.msgid):
                try:
                    traduccion = translator.translate(entry.msgid, dest=destino).text
                    # Si msgid termina en '\n' y la traducción no, se agrega el salto de línea.
                    if entry.msgid.endswith('\n') and not traduccion.endswith('\n'):
                        traduccion += '\n'
                    entry.msgstr = traduccion
                    print(f"Traducido: '{entry.msgid.strip()}' -> '{entry.msgstr.strip()}'")
                except Exception as e:
                    print(f"Error al traducir '{entry.msgid}': {e}")
            else:
                # Si no se debe traducir, puedes dejar msgstr vacío o copiar msgid
                # En este ejemplo, simplemente se omite la traducción.
                print(f"Se omite la traducción para: {entry.msgid.strip()[:60]}...")
    
    po.save()
    print(f"Archivo guardado: {archivo_po}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Uso: python auto_translate.py <archivo.po>")
    else:
        archivo = sys.argv[1]
        traducir_po(archivo)
