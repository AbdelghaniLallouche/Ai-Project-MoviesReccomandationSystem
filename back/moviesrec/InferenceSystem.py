from .facts import *
from aima3.logic import *


def generateLogicConcept(data):
    expression_parts = []
    for key, value in data.items():
        if key in mapper:
            expression_parts.append(str(mapper[key](value)))
    expression = " & ".join(expression_parts) + " ==> Concept(x)"
    return expression


def generateLogicMovie(data):
    expression_parts = []
    for key, value in data.items():
        if key in mapper:
            expression_parts.append(str(mapper[key](value)))
    expression = " & ".join(expression_parts) + " ==> Movie(y)"
    return expression


mapper = {
    'language': lambda val: expr(f'Language({val})'),
    'type': lambda val: expr(f'Type({val})'),
    'time': lambda val: expr(f'Time({val})'),
    'genre': lambda val: expr(f'Genre({val})'),
    'principalactor': lambda val: expr(f'Principalactor({val})'),
    'concept': lambda val: expr(f'Concept({val})'),
}


def final_Movie(input_data, list_data):
    agenda = []
    movies = []
    for key, value in input_data.items():
        if key in mapper:
            agenda.append(expr(str(mapper[key](value))))
    seen = set()
    memory = {}
    while agenda:
        p = agenda.pop(0)
        if p in seen:
            continue
        seen.add(p)
        if fol_fc_ask(movie_kb, p):
            memory[p] = True
        else:
            memory[p] = False
        data_one = {
            'language': list_data[1],
            'type': list_data[2],
            'time': list_data[4],
            'genre': list_data[3],

        }
        if memory.get(expr(f'Language({list_data[1]})'), False) and memory.get(expr(f'Type({list_data[2]})'), False) and memory.get(expr(f'Time({list_data[4]})'), False) and memory.get(expr(f'Genre({list_data[3]})'), False):
            concept = list(fol_fc_ask(movie_kb, expr(generateLogicConcept(data_one))))
            if concept:
                for elem in concept:
                    for value in elem.values():
                        value_concept = value
                        expr_concept = str(expr(f'Concept({value})'))
                        agenda.append(expr(expr_concept))
                        data_two = {
                            'principalactor': list_data[0],
                            'concept': value_concept,
                        }
                        if memory.get(expr(expr_concept), False) and memory.get(expr(f'Budget({list_data[0]})'), False):
                            movie_exp = str(generateLogicMovie(data_two))
                            movies = list(fol_fc_ask(movie_exp, expr(movie_exp)))
                            if movies:
                                for elem in movies:
                                    for value in elem.values():
                                        movies.append(value)
                                        agenda.append(str('movie: ' + value))

    return list(set(movies))