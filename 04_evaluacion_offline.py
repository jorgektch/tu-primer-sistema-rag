from rag_core import retrieve
cases=[('¿Qué plazo tengo para cambiar un producto?','DOC-01'),('¿Cuál es el costo de envío a Lima?','DOC-02'),('¿Cuánto dura la garantía del marco?','DOC-03'),('¿Qué recomienda la guía de seguridad vial?','DOC-04'),('¿Hay descuento para estudiantes en accesorios?','DOC-06'),('¿Quién ganó la copa del mundo en 1990?',None)]
passed=0
for query,expected in cases:
    found=retrieve(query,k=3)
    ok=(expected in {x['documento_id'] for x in found}) if expected else not found
    passed+=ok
    print(('OK' if ok else 'REVISAR'),query,'=>',[x['documento_id'] for x in found])
print(f'Casos correctos: {passed}/{len(cases)}')
