#!/usr/bin/env python3
"""
Script para corregir los metadatos de los notebooks de Anaconda
y hacerlos compatibles con Google Colab.
"""

import json
import os
from pathlib import Path

def fix_notebook_metadata(notebook_path):
    """Corrige los metadatos de un notebook para que sea compatible con Colab."""
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            notebook = json.load(f)
        
        # Verificar si tiene el problema de conda
        metadata = notebook.get('metadata', {})
        kernelspec = metadata.get('kernelspec', {})
        
        if kernelspec.get('name') == 'conda-base-py':
            # Corregir los metadatos
            kernelspec['name'] = 'python3'
            kernelspec['display_name'] = 'Python 3'
            
            # Asegurar que language_info esté presente y correcto
            if 'language_info' not in metadata:
                metadata['language_info'] = {}
            
            language_info = metadata['language_info']
            language_info.setdefault('name', 'python')
            language_info.setdefault('version', '3')
            language_info.setdefault('nbconvert_exporter', 'python')
            language_info.setdefault('pygments_lexer', 'ipython3')
            language_info.setdefault('file_extension', '.py')
            language_info.setdefault('mimetype', 'text/x-python')
            
            # Guardar el notebook corregido
            with open(notebook_path, 'w', encoding='utf-8') as f:
                json.dump(notebook, f, indent=1, ensure_ascii=False)
            
            return True
        return False
    except Exception as e:
        print(f"Error procesando {notebook_path}: {e}")
        return False

def main():
    """Busca y corrige todos los notebooks en el proyecto."""
    project_root = Path(__file__).parent
    notebooks = list(project_root.rglob('*.ipynb'))
    
    fixed_count = 0
    total_count = len(notebooks)
    
    print(f"Encontrados {total_count} notebooks. Verificando...\n")
    
    for notebook_path in notebooks:
        if fix_notebook_metadata(notebook_path):
            print(f"✓ Corregido: {notebook_path.relative_to(project_root)}")
            fixed_count += 1
    
    print(f"\n{'='*60}")
    print(f"Proceso completado: {fixed_count} de {total_count} notebooks corregidos.")
    print(f"{'='*60}")

if __name__ == '__main__':
    main()

