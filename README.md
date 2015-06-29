Datos de Olimpiadas

#### Organizador_pais

Organiza el fichero datasetOlimpiadas.csv organizado por el siguiente estilo:
PAIS, NUMERO DE OROS, NUMERO DE PLATAS, NUMERO DE BRONCES, NUMERO DE AÑOS DISTINTOS, NUMERO DE PERSONAS DISTINTAS, NUMERO DE HOMBRES, NUMERO DE MUJERES

Para grabar los resultados en el fichero resultados:
```
dumbo start organizador_pais.py -input datasetOlimpiadas.csv -output resultados -overwrite yes
```




#### Organizador_personas

Organiza el fichero datasetOlimpiadas.csv organizado por el siguiente estilo:
PERSONA, PAIS, NUMERO DE OROS, NUMERO DE PLATAS, NUMERO DE BRONCES, AÑOS DISTINTOS, DISCIPLINAS DISTINTAS

Para grabar los resultados en el fichero resultados:
```
dumbo start organizador_personas.py -input datasetOlimpiadas.csv -output resultados_personas -overwrite yes
```



Para mostrar resultados:
```
more resultados
```
