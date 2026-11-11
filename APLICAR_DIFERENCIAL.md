# Paquete diferencial: tu-primer-sistema-rag

**Este ZIP contiene solamente archivos nuevos o sustituidos** respecto a la rama `main` consultada el 11 de noviembre de 2026. No incluye archivos del motor de slides ni otros archivos preexistentes sin cambios.

## Aplicación sin tocar GitHub automáticamente

1. Descarga el ZIP y extráelo en una carpeta temporal.
2. Descarga/clona **por tu cuenta** `https://github.com/jorgektch/tu-primer-sistema-rag`.
3. Copia **el contenido** de esta carpeta sobre la raíz del repositorio, aceptando sobrescritura exclusivamente para `README.md` y `presentation.config.json`.
4. Conserva el resto de los archivos existentes, especialmente `.github/`, `assets/`, `tools/`, `index.html`, `engine-release.json` y tests originales.
5. Ejecuta `python -m unittest discover -s tests -p 'test_rag.py'`, `node --test tests/rag-demo.test.mjs`, y los tests existentes del repo; prueba en `python -m http.server 8000`.
6. Revisa el diff y decide tú si haces commit/push.

**No hay mutaciones remotas.** La demo estática no contiene un LLM real; el script de Python permite activarlo con una clave propia.

## Archivos modificados
- `README.md` — nueva presentación y documentación principal.
- `presentation.config.json` — nombre y subtítulo del taller.

## Archivos añadidos
- `rag_core.py`, `01_explorar_documentos.py`, `02_busqueda_semantica_aproximada.py`, `03_rag_con_llm.py`, `04_evaluacion_offline.py`
- `data/conocimiento.json`, `demo/*`, `docs/*` (contenidos nuevos), `ejercicios/*`, `tests/test_rag.py`, `tests/rag-demo.test.mjs`, `.env.example`, `requirements.txt`, este archivo.

**Atención:** En el repositorio base existen pruebas de la plantilla que podrían tener expectativas sobre la versión original del README. Revisa sus resultados antes de integrar el diferencial.
