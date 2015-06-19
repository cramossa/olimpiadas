# Organizador

metals = ["Gold", "Silver", "Bronze"]

from dumbo import identityreducer
import shlex
from collections import Counter


def parse_dataSetOlimpiadas(key,value):
    tokens0 = value.split(',')
    splitter = shlex.shlex(value.replace('""', '-'))
    splitter.whitespace = ','
    splitter.whitespace_split = True
    splitter.escapedquotes = '"'

    tokens = list(splitter)



    try:
        year = tokens[1]
        pais = tokens[5]
        disciplina = tokens[3]
        sexo = tokens[6]
        nombre = tokens[4]

        year = int(year)
        medallas = tuple(int(x in tokens[9]) for x in metals)

        yield pais , medallas + (year, nombre, sexo)

    except:
        #yield "Fila erronea", tokens
        pass



def agrupar_pais_medallas(key,values):

    years = Counter()
    nombres = Counter()
    hombres = Counter()
    mujeres = Counter()

    oro = 0
    plata = 0
    bronce = 0

    for v in values:
        oro += v[0]
        plata += v[1]
        bronce += v[2]

        years[v[3]] += 1
        nombres[v[4]] += 1
        if(v[5] == 'Men'):
            hombres[v[5]] += 1
        if(v[5] == 'Women'):
            mujeres[v[5]] += 1

    yield key ,(oro, plata, bronce, len(years), len(nombres), sum(hombres.values()), sum(mujeres.values()))

def agrupa_para_sort(key,value):
    yield " ", (key,) + value


def sort_oros(key,values):
    values = list(values)
    yield key, sorted(values, key=lambda x: -x[1])


if __name__ == "__main__":
    import dumbo

    job = dumbo.Job()
    job.additer(parse_dataSetOlimpiadas, agrupar_pais_medallas)
    job.additer(agrupa_para_sort,sort_oros)
    job.run()
