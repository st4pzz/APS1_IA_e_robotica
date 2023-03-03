from aigyminsper.search.SearchAlgorithms import BuscaLargura
from aigyminsper.search.SearchAlgorithms import BuscaProfundidade
from aigyminsper.search.SearchAlgorithms import BuscaProfundidadeIterativa
from aigyminsper.search.Graph import State
from datetime import datetime

class SumOne(State):

    def __init__(self, n, op, g):
        self.operator = op
        self.number = n
        self.goal = g

    def sucessors(self):
        sucessors = []
        if self.number < self.goal:
            sucessors.append(SumOne(self.number+1, "+1 ", self.goal))
            sucessors.append(SumOne(self.number+2, "+2 ", self.goal))
        return sucessors

    def is_goal(self):
        if self.goal == self.number:
            return True
        return False

    def description(self):
        return "Este é um agente simples que sabe somar 1 e 2"

    def cost(self):
        return 1

    def env(self):
        return self.number

def largura():
    dici_largura = {}
    objetivo = []
    algoritmo = []
    tempos = []
    for i in range(1,51):
        print(i)
        state = SumOne(1, '', i)
        algorithm = BuscaLargura()
        start_time = datetime.now()
        result = algorithm.search(state)
        if result != None:
            end_time = datetime.now()
            algoritmo.append("Busca em Largura")
            objetivo.append(i)
            tempos.append({end_time - start_time})

        else:
            algoritmo.append("Busca em Largura")
            objetivo.append(i)
            tempos.append("...")

    dici_largura["Algoritmo"] = algoritmo
    dici_largura["Objetivo"] = objetivo
    dici_largura["Tempo de Processamento"] = tempos
    return dici_largura


def profundidade():
    dici_profundidade = {}
    objetivo = []
    algoritmo = []
    tempos = []
    for i in range(1,51):
        
        state = SumOne(0, '', i)
        algorithm = BuscaProfundidade()
        start_time = datetime.now()
        result = algorithm.search(state,m=10)
        if result != None:
            end_time = datetime.now()
            algoritmo.append("Busca em Profundidade")
            objetivo.append(i)
            tempos.append({end_time - start_time})

        else:
            algoritmo.append("Busca em Profundidade")
            objetivo.append(i)
            tempos.append("...")

    for i in range(1,51):
        
        state = SumOne(0, '', i)
        algorithm = BuscaProfundidade()
        start_time = datetime.now()
        result = algorithm.search(state,m=100)
        if result != None:
            end_time = datetime.now()
            algoritmo.append("Busca em Profundidade")
            objetivo.append(i)
            tempos.append({end_time - start_time})
        else:
            algoritmo.append("Busca em Profundidade")
            objetivo.append(i)
            tempos.append("...")

    dici_profundidade["Algoritmo"] = algoritmo
    dici_profundidade["Objetivo"] = objetivo
    dici_profundidade["Tempo de Processamento"] = tempos

    return dici_profundidade

def profundidade_iterativa():
    dici_profundidade_iterativa = {}
    objetivo = []
    algoritmo = []
    tempos = []
    
    for i in range(1,51):
        
        state = SumOne(0, '', i)
        algorithm = BuscaProfundidadeIterativa()
        start_time = datetime.now()
        result = algorithm.search(state)
        if result != None:
            end_time = datetime.now()
            algoritmo.append("Busca em Profundidade Iterativa")
            objetivo.append(i)
            tempos.append({end_time - start_time})
        else:
            algoritmo.append("Busca em Profundidade Iterativa")
            objetivo.append(i)
            tempos.append(0)
    
    dici_profundidade_iterativa["Algoritmo"] = algoritmo
    dici_profundidade_iterativa["Objetivo"] = objetivo
    dici_profundidade_iterativa["Tempo de Processamento"] = tempos

    return dici_profundidade_iterativa
    
