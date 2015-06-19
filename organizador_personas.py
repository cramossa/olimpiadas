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

        yield (nombre , pais), medallas + (year,) + (disciplina,)

    except:
        #yield "Fila erronea", tokens
        pass



def agrupar_personas_pais(key,values):

    years = Counter()
    disciplinas = Counter()

    oro = 0
    plata = 0
    bronce = 0

    for v in values:
        oro += v[0]
        plata += v[1]
        bronce += v[2]

        years[v[3]] += 1
        disciplinas[v[4]] += 1

    if(len(years) > 2):
        yield key ,(oro, plata, bronce, len(years), len(disciplinas))


def agrupa_para_sort(key,value):
    yield " ", (key,) + value


def sort_oros(key,values):
    values = list(values)
    yield key, sorted(values, key=lambda x: -x[1])


if __name__ == "__main__":
    import dumbo

    job = dumbo.Job()
    job.additer(parse_dataSetOlimpiadas, agrupar_personas_pais)
    job.additer(agrupa_para_sort,sort_oros)
    job.run()
