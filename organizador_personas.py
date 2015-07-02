# Organizador

metals = ["Gold", "Silver", "Bronze"]

from dumbo import identityreducer
import shlex
from collections import Counter


class ParseDatasetOlimpiadas:
    def __init__(self):
        self.registros_erroneos = 0
        pass

    def __call__(self, key, value):

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

            yield (nombre, pais), medallas + (year, disciplina)

        except:
            # yield "Fila erronea", tokens
            pass



def parse_dataset_olimpiadas(key, value):
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

        yield (nombre, pais), medallas + (year, disciplina)

    except:
        # yield "Fila erronea", tokens
        pass



def agrupar_personas_pais(key, values):

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
        yield key, (oro, plata, bronce, len(years), len(disciplinas))



def agrupar_pais(key, values):
    # pais, (nombre y datos)
    yield key[1], (key[0], values)


def sort_tres_mejores(key, values):

    values = sorted(values, key=lambda x: -x[1][0])

    total_oros=0

    for x in values:
        total_oros += x[1][0]

    for i,x in enumerate(values[0:3]):
         yield "", (key, total_oros, i+1, x[0]) + x[1]

def agrupa_para_sort(key, values):
    yield key, values


def sort_oros(key, values):
    cabecera = ["PAIS", "NUM MEDALLAS PAIS","POSICION","PERSONA", "ORO", "PLATA", "BRONCE", "O.DIFERENTES", "D.DIFERENTES"]
    cabecera = '|'.join(cabecera)
    yield cabecera,
    values = sorted(values, key=lambda x: (-x[1], x[2]))

    for x in values:
        #yield key, x
        yield "|".join(str(s).replace('"', '') for s in x),

    # si ordeno por los tres mejores de oros y luego por el mejor pais con mas oros, la anterior desaparece


if __name__ == "__main__":
    import dumbo

    job = dumbo.Job()
    job.additer(ParseDatasetOlimpiadas, agrupar_personas_pais)
    # job.additer(parse_dataset_olimpiadas, agrupar_personas_pais)
    job.additer(agrupar_pais, sort_tres_mejores)

    opts = [("outputformat", "text"), ]

    job.additer(agrupa_para_sort, sort_oros, opts=opts)
    job.run()
