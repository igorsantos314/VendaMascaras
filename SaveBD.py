import sqlite3
import os

class saveBD:

    def __init__(self):
        #novo caminho
        path = os.getcwd() 
        db_name = 'DataBase.db'

        #acessar base de dados
        self.connection = sqlite3.connect(f"{path}/{db_name}")
        self.cur = self.connection.cursor()

    # --------------- PEGAR O ID ATUAL ---------------
    def getLastID(self):
        show = "SELECT * FROM kitMascaras"
        self.cur.execute(show)

        listCompra = self.cur.fetchall()

        #retorna o proximo indice
        return listCompra[-1][0] + 1

    # --------------- INSERIR DADOS NA TABELA MATERIAL COMPRADO  ---------------
    def inserirGastos(self, valorCompra):

        #inserir dados
        table = "INSERT INTO materialComprado (valorCompra) VALUES ({})".format(valorCompra)
        self.cur.execute(table)

        #consolidar base de dados
        self.connection.commit()

    def getGastos(self):

        #somar todos os gastos
        show = "SELECT * FROM materialComprado"
        self.cur.execute(show)

        #salvar saida em uma lista
        listaGastos = self.cur.fetchall()

        #pegar o valor de cada tupla
        gastosTotais = sum([i[0] for i in listaGastos])

        return gastosTotais

    # --------------- INSERIR DADOS NA TABELA KITMASCARAS  ---------------
    def inserirDados(self, data, nome, valor, vendedor, status_pagamento, status_entrega, mascara1, mascara2, mascara3, tamanho_elastico, tamanho_mascara):
        id = self.getLastID()
        
        #inserir dados
        table = "INSERT INTO kitMascaras (id, data, nome, valor, vendedor, status_pagamento, status_entrega, mascara1, mascara2, mascara3, tamanho_elastico, tamanho_mascara) VALUES({}, '{}', '{}', {}, '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(id, data, nome, valor, vendedor, status_pagamento, status_entrega, mascara1, mascara2, mascara3, tamanho_elastico, tamanho_mascara)
        self.cur.execute(table)

        #consolidat base de dados
        self.connection.commit()

    # --------------- BUSCAR POR TODOS  ---------------
    def buscarTodasVendas(self):
        show = "SELECT * FROM kitMascaras"
        self.cur.execute(show)

        listCompra = self.cur.fetchall()  

        return listCompra
        #self.printAll(listCompra) 

    # --------------- BUSCAR POR PAGAMENTO ---------------
    def buscarPagamento(self, Status):
        show = "SELECT * FROM kitMascaras WHERE status_pagamento = '{}'".format(Status)
        self.cur.execute(show)

        listCompra = self.cur.fetchall()  
        return listCompra

    # --------------- BUSCAR POR ENTREGA ---------------
    def buscarEntrega(self, Status):
        show = "SELECT * FROM kitMascaras WHERE status_entrega = '{}'".format(Status)
        self.cur.execute(show)

        listCompra = self.cur.fetchall()  
        return listCompra

    # --------------- BUSCAR POR ID  ---------------
    def buscarID(self, idCliente):
        show = "SELECT * FROM kitMascaras WHERE id = '{}'".format(idCliente)
        self.cur.execute(show)

        listCompra = self.cur.fetchall()  
        self.printAll(listCompra) 

    # --------------- BUSCAR POR VENDEDOR  ---------------
    def buscarVendedor(self, nomeVendedor):
        #busca
        show = "Select * FROM kitMascaras WHERE vendedor = '{}'".format(nomeVendedor)

        #executar linha de comando
        self.cur.execute(show)

        #pegar saida de dados
        listCompra = self.cur.fetchall()  

        return listCompra

    # --------------- BUSCAR POR DATA  ---------------
    def buscarData(self, data):
        #busca
        show = "Select * FROM kitMascaras WHERE data = '{}'".format(data)

        self.cur.execute(show)

        listCompra = self.cur.fetchall()  
        self.printAll(listCompra)

    # --------------- BUSCAR POR DATA E VENDEDOR  ---------------
    def buscarDataVendedor(self, data, vendedor):

        show = "Select * FROM kitMascaras WHERE data = '{}' AND vendedor = '{}'".format(data, vendedor)

        self.cur.execute(show)

        listCompra = self.cur.fetchall()  
        self.printAll(listCompra)

    # --------------- BUSCAR O VALOR TOTAL DAS VENDAS QUE ESTÃO EM ESPERA  ---------------
    def buscarValorEspera(self):

        show = "Select valor FROM kitMascaras WHERE status_pagamento = 'EM ESPERA'"
        self.cur.execute(show)

        listCompra = self.cur.fetchall()
        valores = [i[0] for i in listCompra]

        #Retorna a soma dos valores
        return sum(valores)

    # --------------- BUSCAR POR PERIODO  ---------------
    def buscarVendasPeriodo(self, diaInicial, mesInicial, diaFinal, mesFinal):
        
        intervaloInicialFinal = 0
        listaDatasFinal = []

        if mesInicial == mesFinal:
            intervaloInicialFinal = diaFinal

        else:
            intervaloInicialFinal = 32
            listaDatasFinal = ['{}/{}'.format(i, mesFinal) for i in range(1, (diaFinal+1))]

        #lista de datas iniciais e finais
        listaDatasInicial = ['{}/{}'.format(i, mesInicial) for i in range(diaInicial, intervaloInicialFinal)]

        #adcionar lista de datas
        listaDatas = listaDatasInicial + listaDatasFinal

        listaCompras = []

        #busca
        for i in listaDatas:
            show = "Select * FROM kitMascaras WHERE data = '{}'".format(i)

            self.cur.execute(show)
            listCompra = self.cur.fetchall()  

            #adicionar a lista geral
            listaCompras.append(listCompra)

        #lista com todas as tuplas
        listaTratada = []
        
        for matriz in listaCompras:
            for tupla in matriz:
                listaTratada.append(tupla)

        return listaTratada

    # --------------- EXIBIÇÃO DOS DADOS  ---------------
    def printAll(self, listCompra):
        
        #print('     ID   DATA   NOME   VALOR   VENDEDOR   STATUS PAGAMENTO   STATUS ENTREGA   MASCARA 1   MASCARA 2:   MASCARA 3   TAMANHO ELASTICO   TAMANHO MASCARA\n')

        #varrer lista e imprimir 25
        for compra in listCompra:
            print('ID:                     {}\nDATA:                   {}\nNOME:                   {}\nVALOR:                  {}\nVENDEDOR:               {}\nSTATUS PAGAMENTO:       {}\nSTATUS ENTREGA:         {}\nMASCARA 1:              {}\nMASCARA 2:              {}\nMASCARA 3:              {}\nTAMANHO ELASTICO:       {}\nTAMANHO MASCARA:        {}\n'.format(compra[0], compra[1], compra[2], compra[3], compra[4], compra[5], compra[6], compra[7], compra[8], compra[9], compra[10], compra[11]))
            #print('     {}   {}   {}   {}   {}   {}   {}   {}   {}   {}   {}   {}\n'.format(compra[0], compra[1], compra[2], compra[3], compra[4], compra[5], compra[6], compra[7], compra[8], compra[9], compra[10], compra[11]))
    
    def printValorVendedor(self):

        matrizDados = []

        #procurar pelos vendedores
        for i in ['ELLEN', 'CLAUDETE', 'HIOLANDA', 'KIL']:

            #varrer vendedores
            show = "Select * FROM kitMascaras WHERE vendedor = '{}'".format(i)

            #saida do acesso ao banco de dados
            self.cur.execute(show)
            listCompra = self.cur.fetchall()

            #valor das vendas
            valorVendas = 0

            for i in listCompra:
                valorVendas += i[3]

            matrizDados.append([len(listCompra), valorVendas])

        return matrizDados

    # -----------------------------------------------        ATUALIZAÇÕES DA TABELA         -----------------------------------------------

    # --------------- ATUALIZAR STATUS DE PAGAMENTO  ---------------
    def changeStatusPagamento(self, id, status_pagamento):
        show = ('UPDATE kitMascaras SET status_pagamento = "{}" WHERE id= "{}"'.format(status_pagamento, id))
        self.cur.execute(show)

        #consolidaR base de dados
        self.connection.commit()

    # --------------- ATUALIZAR STATUS DE ENTREGA  ---------------
    def changeStatusEntrega(self, id, status_entrega):
        show = ('UPDATE kitMascaras SET status_entrega = "{}" WHERE id = "{}"'.format(status_entrega, id))
        self.cur.execute(show)

        self.connection.commit()

    # --------------- ATUALIZAR DATA  ---------------
    def changeData(self, id, data):
        show = ('UPDATE kitMascaras SET data = "{}" WHERE id = "{}"'.format(data, id))
        self.cur.execute(show)

        self.connection.commit()

    # --------------- ATUALIZAR NOME  ---------------
    def changeNome(self, id, nome):
        show = ('UPDATE kitMascaras SET nome = "{}" WHERE id = "{}"'.format(nome, id))
        self.cur.execute(show)

        self.connection.commit()

    # --------------- ATUALIZAR VALOR  ---------------
    def changeValor(self, id, valor):
        show = ('UPDATE kitMascaras SET valor = "{}" WHERE id = "{}"'.format(valor, id))
        self.cur.execute(show)

        self.connection.commit()

    # --------------- ATUALIZAR MASCARA 1  ---------------
    def changeMascara1(self, id, mascara1):
        show = ('UPDATE kitMascaras SET mascara1 = "{}" WHERE id = "{}"'.format(mascara1, id))
        self.cur.execute(show)

        self.connection.commit()

    # --------------- ATUALIZAR MASCARA 2  ---------------
    def changeMascara2(self, id, mascara2):
        show = ('UPDATE kitMascaras SET mascara2 = "{}" WHERE id = "{}"'.format(mascara2, id))
        self.cur.execute(show)

        self.connection.commit()

    # --------------- ATUALIZAR MASCARA 3  ---------------
    def changeMascara3(self, id, mascara3):
        show = ('UPDATE kitMascaras SET mascara3 = "{}" WHERE id = "{}"'.format(mascara3, id))
        self.cur.execute(show)

        self.connection.commit()

    # --------------- ATUALIZAR TAMANHO ELASTICO  ---------------
    def changeTamanhoElastico(self, id, tamanho_elastico):
        show = ('UPDATE kitMascaras SET tamanho_elastico = "{}" WHERE id = "{}"'.format(tamanho_elastico, id))
        self.cur.execute(show)

        self.connection.commit()
    
    # --------------- ATUALIZAR TAMANHO MASCARA  ---------------
    def changeTamanhoMascara(self, id, tamanho_mascara):
        show = ('UPDATE kitMascaras SET tamanho_mascara = "{}" WHERE id = "{}"'.format(tamanho_mascara, id))
        self.cur.execute(show)

        self.connection.commit()


#                                                   --- TESTES ---
a = saveBD()
#a.buscarVendasPeriodo(1, 7, 5, 7)
#a.inserirDados(0, '19/06', 'joao', 10, 'claudete', 'espera', 'espera', 'bolinhha', 'listra', 'exercicito', 'normal', 'G')
#a.inserirDados('19/06', 'joao', 10, 'claudete', 'espera', 'espera', 'bolinhha', 'listra', 'exercicito', 'normal', 'G')
#a.inserirDados('19/06', 'maria', 10, 'ellen', 'espera', 'espera', 'bolinhha', 'listra', 'exercicito', 'normal', 'G')
#a.inserirDados('25/5', 'maria', 10, 'ellen', 'espera', 'espera', 'bolinhha', 'listra', 'exercicito', 'normal', 'G')
#a.inserirDados('15/5', 'joana', 10, 'ellen', 'espera', 'espera', 'bolinhha', 'listra', 'exercicito', 'normal', 'G')
#a.inserirDados('15/5', 'maria', 10, 'ellen', 'PG', 'OK', 'bolinhha', 'listra', 'exercicito', 'normal', 'G')
#a.inserirDados('19/06', 'jose', 10, 'hiolanda', 'espera', 'espera', 'bolinhha', 'listra', 'exercicito', 'normal', 'G')
#a.inserirDados('19/06', 'zacarias', 10, 'claudete', 'espera', 'espera', 'bolinhha', 'listra', 'exercicito', 'normal', 'G')
#a.buscarTodasVendas()

#a.changeStatusEntrega(3, 'OK')
#a.changeStatusPagamento(3, 'PG')
#a.changeNome(3, 'santos')
#a.changeValor(3, 12)

#a.buscarData('25/5')

#a.buscarDataVendedor('0/5', 'ellen')