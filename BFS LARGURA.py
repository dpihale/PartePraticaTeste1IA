import random
from collections import deque

class Agente:
    def __init__(self, localizacao):
        self.desempenho = 0
        self.localizacao = localizacao

    def programa_reflex(self, percepcao):
        localizacao, estado = percepcao
        if estado == 'vazio':
            return 'encher'
        elif localizacao == 'A':
            return 'direita'
        elif localizacao == 'B':
            return 'esquerda'

class Ambiente:
    def __init__(self):
        self.estado = {'A': random.choice(['cheio', 'vazio']),
                       'B': random.choice(['cheio', 'vazio'])}

    def percepcao(self, agente):
        return (agente.localizacao, self.estado[agente.localizacao])

    def localizacao_default(self):
        return random.choice(['A', 'B'])

    def executar_accao(self, agente, accao):
        if accao == 'esquerda':
            agente.desempenho -= 1
            if agente.localizacao == 'A':
                agente.localizacao = 'B'
        elif accao == 'direita':
            agente.desempenho -= 1
            if agente.localizacao == 'B':
                agente.localizacao = 'A'
        elif accao == 'encher':
            agente.desempenho += 10
            self.estado[agente.localizacao] = 'cheio'

def bfs(ambiente, agente):
    visitados = set()
    fila = deque([(agente.localizacao, tuple(ambiente.estado.values()))])

    while fila:
        estado_atual, estado_baldes = fila.popleft()
        if 'vazio' not in estado_baldes:
            return estado_atual

        visitados.add((estado_atual, estado_baldes))

        for acao in ['encher', 'direita', 'esquerda']:
            ambiente.estado['A'], ambiente.estado['B'] = estado_baldes
            ambiente.executar_accao(agente, acao)
            novo_estado = (agente.localizacao, tuple(ambiente.estado.values()))

            if novo_estado not in visitados:
                fila.append((agente.localizacao, novo_estado[1]))
                visitados.add(novo_estado)

            ambiente.estado['A'], ambiente.estado['B'] = estado_baldes
            agente.localizacao = estado_atual

ambiente = Ambiente()
agente = Agente(ambiente.localizacao_default())

resultado = bfs(ambiente, agente)
print("Resultado da busca em largura:", resultado)
