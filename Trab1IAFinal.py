import random
import copy

class No():
    def __init__(self, estado = None, caminho = [0]):
        if(estado == None):
            self.estado = Estado()
            self.filhos = []
            self.caminho = caminho
        else:
            self.estado = estado
            self.filhos = []
            self.caminho = caminho
    def __repr__(self):
        return f'{self.estado}'
    def setFilho(self, filho):
        self.filhos.append(filho)
    #tentei fazer em ambas os objetos a copia porem nao funcionou
    def copia(self,estadoCopia):
        self.estado.pilha1 = copy.deepcopy(estadoCopia.estado.pilha1)
        self.estado.pilha2 = copy.deepcopy(estadoCopia.estado.pilha2)
        self.estado.pilha3 = copy.deepcopy(estadoCopia.estado.pilha3)
        self.filhos = copy.deepcopy(estadoCopia.filhos)
        self.caminho = copy.deepcopy(estadoCopia.caminho)

class Estado():
    pilha1 = []
    pilha2 = []
    pilha3 = []
    def __init__(self, pilha1=[], pilha2=[], pilha3=[]):
        self.pilha1 = pilha1
        self.pilha2 = pilha2
        self.pilha3 = pilha3
    def __repr__(self):
        return f'{self.pilha1} \t\t{self.pilha2} \t\t{self.pilha3}\n pilha 1 \t pilha2 \t pilha3 \n'
    def getTamPilha1(self):
        return len(self.pilha1)
    def getTamPilha2(self):
        return len(self.pilha2)
    def getTamPilha3(self):
        return len(self.pilha3)
    #funcao que nao funcionou, esta e a que eu fiz apos a pergunta no whats
    def setPilhas(self,estadoCopia):
        self.pilha1 = copy.deepcopy(estadoCopia.pilha1)
        self.pilha2 = copy.deepcopy(estadoCopia.pilha2)
        self.pilha3 = copy.deepcopy(estadoCopia.pilha3)
    def comparaPilhas(self, estado):
        if(self.pilha1 != estado.pilha1):
            return False
        if(self.pilha2 != estado.pilha2):
            return False
        if(self.pilha3 != estado.pilha3):
            return False
        return True
    #quando uso dentro do objeto ele altera o valor do estado atual e a copia junto
    #entao decidi fazer manualmente(pergunta que fiz para o senhor e uma de suas sujestoes)
    def P1toP2(self):
        if(self.getTamPilha1() > 0):
            self.pilha2.append(self.pilha1.pop())
    def P1toP3(self):
        if(self.getTamPilha1() > 0):
            self.pilha3.append(self.pilha1.pop())
    def P2toP1(self):
        if(self.getTamPilha2() > 0):
            self.pilha1.append(self.pilha2.pop())
    def P2toP3(self):
        if(self.getTamPilha2() > 0):
            self.pilha3.append(self.pilha2.pop())
    def P3toP1(self):
        if(self.getTamPilha3() > 0):
            self.pilha1.append(self.pilha3.pop())
    def P3toP2(self):
        if(self.getTamPilha3() > 0):
            self.pilha2.append(self.pilha3.pop())

def geraAleatorio():
    pilha1 = []
    pilha2 = []
    pilha3 = []
    aux = 0
    for i in range(3):
        aux = random.randint(0,2)
        if aux == 0:
            pilha1.append(i)
        elif aux == 1:
            pilha2.append(i)
        elif aux == 2:
            pilha3.append(i)
    estadoRand = Estado(pilha1,pilha2,pilha3)
    return estadoRand

def novoEstado(noAtual, abertos):
    todosFilhos = []
    noCopia = copy.deepcopy(noAtual)
    x = 0
    if(noCopia.estado.getTamPilha1() > 0):
        popP1 = noCopia.estado.pilha1.pop()
        aux = Estado(noCopia.estado.pilha1, noCopia.estado.pilha2, noCopia.estado.pilha3)
        filho1 = copy.deepcopy(aux)
        filho1.pilha2.append(popP1)
        flag = 0
        for i in abertos:
            if i.comparaPilhas(aux):
                flag = flag + 1
        if flag == 0:
            todosFilhos.append(filho1)
        filho2 = copy.deepcopy(aux)
        filho2.pilha3.append(popP1)
        flag = 0
        for i in abertos:
            if i.comparaPilhas(filho2):
                flag = flag + 1
        if flag == 0:
            todosFilhos.append(filho2)
    noCopia = copy.deepcopy(noAtual)
    if(noCopia.estado.getTamPilha2() > 0):
        popP2 = noCopia.estado.pilha2.pop()
        aux = Estado(noCopia.estado.pilha1, noCopia.estado.pilha2, noCopia.estado.pilha3)  
        filho1 = copy.deepcopy(aux)
        filho1.pilha1.append(popP2)
        flag = 0
        for i in abertos:
            if i.comparaPilhas(filho1):
                flag = flag + 1
        if flag == 0:
            todosFilhos.append(filho1)
        filho2 = copy.deepcopy(aux)
        filho2.pilha3.append(popP2)
        flag = 0
        for i in abertos:
            if i.comparaPilhas(filho2):
                flag = flag + 1
        if flag == 0:
            todosFilhos.append(filho2)   
    noCopia = copy.deepcopy(noAtual)
    if(noCopia.estado.getTamPilha3() > 0):
        popP3 = noCopia.estado.pilha3.pop()
        aux = Estado(noCopia.estado.pilha1, noCopia.estado.pilha2, noCopia.estado.pilha3) 
        filho1 = copy.deepcopy(aux)
        filho1.pilha1.append(popP3)
        flag = 0
        for i in abertos:
            if i.comparaPilhas(filho1):
                flag = flag + 1
        if flag == 0:
            todosFilhos.append(filho1)
        filho2 = copy.deepcopy(aux)
        filho2.pilha2.append(popP3)
        flag = 0
        for i in abertos:
            if i.comparaPilhas(filho2):
                flag = flag + 1
        if flag == 0:
            todosFilhos.append(filho2)
    if(len(todosFilhos) > 0):
        for i in todosFilhos:
            caminho = copy.deepcopy(noCopia.caminho)
            caminho.append(x)
            filho = No(i, caminho)
            noAtual.setFilho(filho)
            x = x + 1

def busca(estadoAtual, meta):
    abertos = [estadoAtual]
    estadoNoAtual = [estadoAtual.estado]
    while len(abertos) != 0:
        aux = abertos.pop(0)
        if(aux.estado.comparaPilhas(meta)):
            global todosCaminho
            todosCaminho = aux.caminho
            return 'Sucesso'
        else:
            novoEstado(aux,estadoNoAtual)
            if len(aux.filhos) > 0:
                for i in aux.filhos:
                    abertos.append(i)
                    estadoNoAtual.append(i.estado)
    return 'Falha'

todosCaminho = []
aux = geraAleatorio()
estadoInit = No(aux, [])
aberto = copy.deepcopy(estadoInit)
print('Estado Inicial:')
print(aux)
meta = Estado([],[2, 1, 0],[])
if(aux.comparaPilhas(meta)):
    print('Estado inicial:\n')
    print(aux)
    print('meta:\n')
    print(meta)
    print('\t Sucesso \n Estado inicial é igual a meta')
else:
    resultBusca = busca(aberto, meta)
    if (resultBusca == 'Sucesso'):
        print('Caminho:')
        for i in todosCaminho:
            aberto = aberto.filhos[i]
            print(aberto)
    else:
        print(resultBusca)