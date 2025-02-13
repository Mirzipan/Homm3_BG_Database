#!/bin/bash
# Este script busca todos los archivos *.pot en la carpeta translations y crea su correspondiente archivo es.po

# Buscar todos los archivos .pot en la carpeta "translations"
find translations -type f -name "*.pot" | while IFS= read -r potfile; do
    # Obtener el directorio y nombre base del archivo .pot
    dir=$(dirname "$potfile")
    base=$(basename "$potfile" .pot)
    
    # Definir el nombre de salida, por ejemplo, base.es.po
    outfile="$dir/es.po"

    # Verificar si el archivo de traducción ya existe
    if [ -f "$outfile" ]; then
        echo "El archivo $outfile ya existe. Se omite la traducción automática."
    else
        echo "Generando traducción para: $potfile"

        # Ejecutar msginit
        if msginit --locale=es_ES --input="$potfile" --output-file="$outfile" --no-translator; then
            echo "Archivo generado: $outfile"
        else
            echo "Error al generar $outfile"
        fi
    fi
done
