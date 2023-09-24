
class SaveData:

    def __init__(self):
        
        self.caminhoDefault = "/home/igor/Área de Trabalho/Códigos Ellen/"
        self.caminhos = ["{}Ellen/ELLEN.txt".format(self.caminhoDefault), "{}Claudete/CLAUDETE.txt".format(self.caminhoDefault), "{}Hiolanda/HIOLANDA.txt".format(self.caminhoDefault)]
    
    #caminho padrao
    def getCaminhoDefault(self):
        return self.caminhoDefault

    #pegar o vendedor pelo indice da lista
    def getVendedor(self, idVendedor):
        return self.caminhos[idVendedor]

    #acessar todas as vendas
    def acessarVendas(self, idVendedor):
        
        arq = open(self.getVendedor(idVendedor), 'r')

        for i in arq:
            print(i)

    def getIdCompra(self, idVendedor):

        arq = open('{}'.format(self.getCaminhoDefault()))

        arq.close()

    def addVenda(self, dadosVenda):

        for pos,i in dadosVenda:

            if pos == 3:
                pass
            
    def salvarDadosVenda(self, idVendedor, dataString):

        with open(self.getVendedor(idVendedor), 'a') as arquivo:
            arquivo.write('{}\n'.format(dataString))

a = SaveData()
a.salvarDadosVenda(0, '123')
a.salvarDadosVenda(0, '456')
a.acessarVendas(0)