from SaveBD import *
import os

class vendaMascaras:

    def __init__(self):
        
        #SESSÃO DE BANCO DE DADOS
        self.cliente = saveBD()

        # ------------------------------ INFORMAÇÕES EM LISTA PRE DEFINIDAS ------------------------------

        self.estampasMascaras = [   'PRETA', 
                                    'BRANCA', 
                                    'VERMELHA', 
                                    'AZUL', 
                                    'ROSA',
                                    'PESSEGO',
                                    'VINHO',
                                    'CINZA',
                                    'BOLINHA PRETA',
                                    'SURF',
                                    'DOCES',
                                    'CAVEIRA PRETA',
                                    'EXCERCITO',
                                    'CAVEIRA AZUL',
                                    'ZIGZAG CINZA',
                                    'FLOR',
                                    'SOLDADINHOS',
                                    'FLAMINGO',
                                    'COROA AZUL GRANDE',
                                    'COROA AZUL PEQUENA',
                                    'COROA BEGE GRANDE',
                                    'COROA BEGE PEQUENA'
                                    'URSINHO',
                                    'COROA VERMELHA',
                                    'PARIS'
                                    ]

        self.tamanhosMascaras = ['PP', 'M', 'G', 'GG']
        self.vendedores =       ['ELLEN', 'CLAUDETE', 'HIOLANDA']
        self.entrega    =       ['OK', 'EM ESPERA']
        self.pagamento  =       ['PG', 'EM ESPERA']
        self.elastico   =       ['ORELHA', 'CABEÇA', 'GRANDE']

        while True:
            
            self.clearScreen()

            print('             --------------- MENU ---------------\n')
            print('                 --> [1] CADASTRAR VENDA')
            print('                 --> [2] EXIBIR VENDAS')
            print('                 --> [3] BUSCAR POR VENDEDOR')
            print('                 --> [4] BUSCAR POR DATA')
            print('                 --> [5] BUSCAR POR DATA E VENDEDOR')
            print('                 --> [6] EDITAR VENDA')
            print('                 --> [7] SAIR\n')
            
            opc = int(input('             --> SELECIONAR OPÇÃO: '))

            #SELEÇÃO DE OPÇÕES
            if opc == 1:
                #cadastrar venda
                self.cadastrarVenda()

            elif opc == 2:
                #exibir todas as vendas
                self.exibirTodasVendas()

            elif opc == 3:
                #exibir vendas por vendedor
                self.exibirVendasVendedor()

            elif opc == 4:
                #exibir por vendas e datas
                self.exibirVendasDatas()

            elif opc == 5:
                #exibir por vendedor e data
                self.exibirDataVendedor()

            elif opc == 6:
                self.editarVendas()
            
            elif opc == 7:
                exit()

            elif opc == 8:
                print(self.cliente.printValorVendedor())
                a = input('')
            else:
                print('OPS !')

    def clearScreen(self):
        os.system('clear')

    # ------------------------------ EXIBIR INFORMAÇÕES EM LISTA PRE DEFINIDAS ------------------------------
    def exibirEstampas(self):

        for pos,i in enumerate(self.estampasMascaras):
            print('                 >> [{}] = {}'.format(pos, i))

    def exibirTamanhos(self):

        for pos,i in enumerate(self.tamanhosMascaras):
            print('                 >> [{}] = {}'.format(pos, i))

    def exibirVendedor(self):

        for pos,i in enumerate(self.vendedores):
            print('                 >> [{}] = {}'.format(pos, i))

    def exibirEntrega(self):

        for pos,i in enumerate(self.entrega):
            print('                 >> [{}] = {}'.format(pos, i))

    def exibirPagamento(self):

        for pos,i in enumerate(self.pagamento):
            print('                 >> [{}] = {}'.format(pos, i))

    def exibirTamanhoElastico(self):

        for pos,i in enumerate(self.elastico):
            print('                 >> [{}] = {}'.format(pos, i))

    # ------------------------------ CADASTRAR VENDAS ------------------------------
    def cadastrarVenda(self):
        self.clearScreen()

        dia = int(input('             --> DATA                : '))
        mes = int(input('             --> MES                 :  '))
        data = '{}/{}'.format(dia, mes)

        nome = input('             --> NOME                :  ')
        valor = float(input('             --> VALOR               :  '))

        #exibir vendedor
        self.exibirVendedor()
        vendedor = int(input('             --> VENDEDOR            :  '))

        #status de pagamentos
        self.exibirPagamento()
        statusPagamento = int(input('             --> STATUS DE PAGAMENTO :  '))

        #status de entrega
        self.exibirEntrega()
        statusEntrega = int(input('             --> STATUS DE ENTREGA   :  '))

        #estampas disponiveis
        self.exibirEstampas()
        mascara1 = int(input('             --> MASCARA 1           :  '))
        mascara2 = int(input('             --> MASCARA 2           :  '))
        mascara3 = int(input('             --> MASCARA 3           :  '))

        #tamanhos de elastico
        self.exibirTamanhoElastico()
        tamanhoElastico = int(input('             --> TAMANHO ELASTICO    :  '))

        #tamanhos de mascasras disponiveis
        self.exibirTamanhos()
        tamanhoMascara = int(input('             --> TAMANHO MASCARA     :  '))

        # --------------------------- SALVAR NO BANCO DE DADOS ---------------------------
        self.cliente.inserirDados(  
                                    data, 
                                    nome.upper(),
                                    valor, 
                                    self.vendedores[vendedor], 
                                    self.pagamento[statusPagamento], 
                                    self.entrega[statusEntrega], 
                                    self.estampasMascaras[mascara1],
                                    self.estampasMascaras[mascara2],
                                    self.estampasMascaras[mascara3],
                                    self.elastico[tamanhoElastico],
                                    self.tamanhosMascaras[tamanhoMascara]
                                    )

    # --------------------------- EXIBIR TODOS OS DADOS ---------------------------
    def exibirTodasVendas(self):

        self.clearScreen()
        print(' ---------------------------------- EXIBIR TODOS OS DADOS ----------------------------------\n')

        self.cliente.buscarTodasVendas()

        #pausa
        pause = input('Press Enter ...')

    # --------------------------- EXIBIR TODOS OS DADOS POR CADA VENDEDOR ---------------------------
    def exibirVendasVendedor(self):

        self.clearScreen()
        print(' ---------------------------------- EXIBIR POR VENDEDORES ----------------------------------\n')

        #exibir vendedores
        self.exibirVendedor()

        v = int(input('\n         --> SELECIONE O VENDEDOR: '))
        
        #exibir lista de venda de cada vendedor
        self.cliente.buscarVendedor(self.vendedores[v])
        
        #pausa
        pause = input('Press Enter ...')

     # --------------------------- EXIBIR VENAS POR DATAS ---------------------------
    def exibirVendasDatas(self):

        self.clearScreen()
        print(' ---------------------------------- EXIBIR POR DATAS ----------------------------------\n')

        dia = int(input('\n                         --> DATA: '))
        mes = int(input('\n                         --> MES : '))
        
        #exibir lista de venda de cada vendedor
        self.cliente.buscarData('{}/{}'.format(dia,mes))
        
        #pausa
        pause = input('Press Enter ...')

     # --------------------------- EXIBIR POR DATA E VENDEDOR ---------------------------
    def exibirDataVendedor(self):
        
        self.clearScreen()
        print(' ---------------------------------- EXIBIR POR DATA E VENDEDOR ----------------------------------\n')

        #exibir vendedores
        self.exibirVendedor()

        v = int(input('\n                         --> SELECIONE O VENDEDOR: '))

        dia = int(input('\n                         --> DATA: '))
        mes = int(input('\n                         --> MES : '))

        #Exibir busca por DATA e VENDEDOR
        self.cliente.buscarDataVendedor('{}/{}'.format(mes,dia), self.vendedores[v])

        #pausa
        pause = input('Press Enter ...')



    # -------------------------------------------------------------- SETOR DE EDIÇÕES --------------------------------------------------------------

    def editarVendas(self):

        while True:
            
            self.clearScreen()

            print('             --------------- MENU DE EDIÇÕES---------------\n')
            print('                 --> [1] EDITAR PAGAMENTO')
            print('                 --> [2] EDITAR ENTREGA')
            print('                 --> [3] EDITAR NOME')
            print('                 --> [4] EDITAR DATA')
            print('                 --> [5] EDITAR VALOR')
            print('                 --> [6] EDITAR MASCARA 1')
            print('                 --> [7] EDITAR MASCARA 2')
            print('                 --> [8] EDITAR MASCARA 3')
            print('                 --> [9] EDITAR TAMANHO ELASTICO')
            print('                 --> [10] EDITAR TAMANHO MASCARA')
            print('                 --> [11] SAIR\n')
            
            opc = int(input('             --> SELECIONAR OPÇÃO: '))

            if opc != 11:
                #pegar o id do cliente para editar
                idCliente = int(input('             --> DIGITAR ID:       '))

                #limpar tela
                self.clearScreen()

                #exibir informações do ID para edição
                self.cliente.buscarID(idCliente)

            if opc == 1:
                self.editarPagamento(idCliente)

            elif opc == 2:
                self.editarEntrega(idCliente)

            elif opc == 3:
                self.editarNome(idCliente)

            elif opc == 4:
                self.editarData(idCliente)
            
            elif opc == 5:
                self.editarValor(idCliente)

            elif opc == 6:
                self.editarMascara1(idCliente)

            elif opc == 7:
                self.editarMascara2(idCliente)

            elif opc == 8:
                self.editarMascara3(idCliente)

            elif opc == 9:
                self.editarTamanhoElastico(idCliente)

            elif opc == 10:
                self.editarTamanhoMascara(idCliente)

            elif opc == 11:
                break      

            #limpar tela
            self.clearScreen()  

            try:
                #exibir informações do ID para edição
                self.cliente.buscarID(idCliente)

            except:
                pass

            #pasue
            pause = input('...')
    
    # ------------------------------------------------------------ FUNÇÕES PARA REALIZAR UPDATES NO BD ------------------------------------------------------------            
    def editarPagamento(self, idCliente):

        #exibir opcoes
        self.exibirPagamento()
        
        opc = int(input('             --> SELECIONAR OPÇÃO: '))

        #commitar alterações
        self.cliente.changeStatusPagamento(idCliente, self.pagamento[opc])

    def editarEntrega(self, idCliente):
        
        #exibir opcoes
        self.exibirEntrega()
        
        opc = int(input('             --> SELECIONAR OPÇÃO: '))

        #commitar alterações
        self.cliente.changeStatusEntrega(idCliente, self.entrega[opc])

    def editarNome(self, idCliente):
        
        nome = input('             --> NOME: ')

        #commitar alterações
        self.cliente.changeNome(idCliente, nome.upper())

    def editarData(self, idCliente):

        dia = int(input('             --> DATA:   '))
        mes = int(input('             --> MES :   '))

        #commitar alterações
        self.cliente.changeData(idCliente, '{}/{}'.format(dia, mes))

    def editarValor(self, idCliente):
        
        valor = float(input('             --> VALOR: '))

        #commitar alterações
        self.cliente.changeValor(idCliente, valor)

    def editarMascara1(self, idCliente):

        #estampas
        self.exibirEstampas()

        mask = int(input('             --> MASCARA 1: '))

        #commitar alterações
        self.cliente.changeMascara1(idCliente, self.estampasMascaras[mask])

    def editarMascara2(self, idCliente):

        #estampas
        self.exibirEstampas()

        mask = int(input('             --> MASCARA 2: '))

        #commitar alterações
        self.cliente.changeMascara2(idCliente, self.estampasMascaras[mask])

    def editarMascara3(self, idCliente):

        #estampas
        self.exibirEstampas()
        
        mask = int(input('             --> MASCARA 3: '))

        #commitar alterações
        self.cliente.changeMascara3(idCliente, self.estampasMascaras[mask])

    def editarTamanhoElastico(self, idCliente):
        
        #exibir opcoes
        self.exibirTamanhoElastico()
        
        elastico = int(input('             --> SELECIONAR OPÇÃO: '))

        #commitar alterações
        self.cliente.changeTamanhoElastico(idCliente, self.elastico[elastico])

    def editarTamanhoMascara(self, idCliente):
        
        #exibir opcoes
        self.exibirTamanhos()
        
        mask = int(input('             --> SELECIONAR OPÇÃO: '))

        #commitar alterações
        self.cliente.changeTamanhoMascara(idCliente, self.tamanhosMascaras[mask])


vendaMascaras()