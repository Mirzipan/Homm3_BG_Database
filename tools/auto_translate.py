import polib
from googletrans import Translator
import sys

def traducir_po(archivo_po, destino='es'):
    # Cargar el archivo .po
    po = polib.pofile(archivo_po)
    translator = Translator()
    
    print(f"Procesando: {archivo_po}")
    
    for entry in po:
        # Solo traducir si el msgstr está vacío
        if not entry.msgstr.strip():
            try:
                # Traducir el texto original (msgid) al idioma destino (español)
                traduccion = translator.translate(entry.msgid, dest=destino).text
                entry.msgstr = traduccion
                print(f"Traducido: '{entry.msgid}' -> '{traduccion}'")
            except Exception as e:
                print(f"Error al traducir '{entry.msgid}': {e}")
    
    # Guardar el archivo actualizado
    po.save()
    print(f"Archivo guardado: {archivo_po}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python auto_translate.py <ruta-al-archivo.po>")
    else:
        archivo = sys.argv[1]
        traducir_po(archivo)
