# Continuidad con la ruta de talleres

Repositorios consultados **solo en lectura** el 11-11-2026:

- https://github.com/jorgektch/tu-primer-agente-de-ia: herramienta, agente, evaluaciones y demo offline.
- https://github.com/jorgektch/tu-primer-agente-de-ia-con-mcp: servidor de catálogo con herramientas de stock/precio/cotización, `smolagents.MCPClient` y `ToolCallingAgent`.
- https://github.com/jorgektch/tu-primer-sistema-rag: plantilla README to Slides, sin implementación previa de RAG en la rama principal.

**Diseño de integración recomendado:** este taller utiliza la *misma narrativa de tienda ficticia* y agrega una base de políticas, garantías y logística. Las preguntas sobre políticas las resuelve recuperación documental; stock y precios se delegan al catálogo MCP. No se copian ni modifican módulos MCP. Esta carpeta **no implementa integración end-to-end** con los otros repositorios.

## Taller posterior: "Tu primer agente con MCP + RAG"

1. Integrar un servidor/herramienta `buscar_conocimiento(pregunta, k)` que encapsule `rag_core.retrieve` y devuelva snippets + IDs.
2. Exponer `consultar_stock`, `consultar_precio`, `cotizar_producto` del servidor MCP anterior sin cambiar sus validaciones.
3. Introducir router de intención: políticas -> RAG; datos transaccionales -> tools; mixtos -> ambos.
4. Devolver respuesta unificada con fuentes de documento y resultados de herramientas claramente separados.
5. Evaluar 4 casos: política, stock, consulta mixta y prompt injection dentro de documento.

**Fronteras de confianza:** no aceptar órdenes de documentos como instrucciones del agente; no exponer API keys al navegador; controlar acceso a documentos y herramientas en el servidor; no convertir recomendaciones del LLM en acciones autorizadas.

**Archivos de motor preservados:** no se incluyen parches para `assets/js/*`, `assets/theme.css`, `index.html`, `engine-release.json`, workflows, ni utilidades del motor. Solo se modifica contenido del taller y configuración visual.
