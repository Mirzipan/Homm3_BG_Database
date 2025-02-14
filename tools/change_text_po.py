#!/usr/bin/env python3
import polib
import sys
import glob

def update_po_files(search_str, replace_str):
    # Buscar recursivamente archivos es.po en el directorio "translations"
    files = glob.glob("translations/**/es.po", recursive=True)
    if not files:
        print("No se encontraron archivos es.po en 'translations'.")
        return

    for filename in files:
        print(f"Procesando {filename}...")
        po = polib.pofile(filename)
        modified = False
        for entry in po:
            if search_str in entry.msgid:
                 # Verifica si msgstr ya contiene la cadena de reemplazo.
                if replace_str in entry.msgstr:
                    print(f"  Se omite la actualización para: {entry.msgid.strip()} (ya contiene '{replace_str}')")
                    continue
                # Crear la nueva cadena para msgstr reemplazando search_str por replace_str
                new_msgstr = entry.msgid.replace(search_str, replace_str)
                if entry.msgid.endswith('\n') and not new_msgstr.endswith('\n'):
                    new_msgstr += '\n'
                if entry.msgstr != new_msgstr:
                    entry.msgstr = new_msgstr
                    modified = True
                    print(f"  Actualizado: {entry.msgid.strip()}")
        if modified:
            po.save()
            print(f"  Guardados cambios en {filename}")
        else:
            print(f"  No se encontraron entradas para actualizar en {filename}")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Uso: python update_po.py <cadena_a_buscar> <cadena_de_reemplazo>")
        sys.exit(1)
    search_str = sys.argv[1]
    replace_str = sys.argv[2]
    update_po_files(search_str, replace_str)
