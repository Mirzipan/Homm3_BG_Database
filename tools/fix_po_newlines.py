#!/usr/bin/env python3
import polib
import sys

def fix_po_newlines(po_file):
    po = polib.pofile(po_file)
    changed = False
    for entry in po:
        # Si el msgid termina con \n pero msgstr no, se agrega \n al final del msgstr.
        if entry.msgid.endswith('\n') and not entry.msgstr.endswith('\n'):
            entry.msgstr += '\n'
            changed = True
        # Si el msgid no termina con \n pero msgstr sí, se quita el salto de línea.
        elif not entry.msgid.endswith('\n') and entry.msgstr.endswith('\n'):
            entry.msgstr = entry.msgstr.rstrip('\n')
            changed = True
    if changed:
        po.save()
        print(f"Se han corregido los saltos de línea en: {po_file}")
    else:
        print(f"No se encontraron problemas de saltos de línea en: {po_file}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Uso: python fix_po_newlines.py <archivo.po>")
        sys.exit(1)
    fix_po_newlines(sys.argv[1])
