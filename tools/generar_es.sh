#!/bin/bash
# Este script busca todos los archivos *.pot en la carpeta translates y crea su correspondiente archivo es.po

find translations -type f -name "*.pot" | while read potfile; do
    # Obtener el directorio y nombre base del archivo .pot
    dir=$(dirname "$potfile")
    base=$(basename "$potfile" .pot)
    
    # Definir el nombre de salida, por ejemplo, base.es.po
    outfile="$dir/es.po"

    if [ -f "$outfile" ]; then
        echo "El archivo $archivo_po ya existe. Se omite la traducción automática."
    else
        echo "Generando traducción para: $potfile"

        # Ejecutar msginit
        msginit --locale=es_ES --input="$potfile" --output-file="$outfile" --no-translator
    
        echo "Archivo generado: $outfile"
    fi
done
