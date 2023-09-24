class mask:

    def __init__(self, data, nome, valor, desc, status, entrega):
        
        self.data = data
        self.nome = nome
        self.valor = valor
        self.descricao = desc
        self.status = status
        self.entrega = entrega
        
    def getData(self):
        return self.data

    def getNome(self):
        return self.nome

    def getValor(self):
        return self.valor

    def getDesc(self):
        return self.descricao

    def getStatus(self):
        return self.status

    def getEntrega(self):
        return self.entrega
    
    #SETS
    def setData(self, data):
        self.data = data

    def setNome(self, nome):
        self.nome = nome

    def setValor(self, valor):
        self.valor = valor

    def setDesc(self, desc):
        self.descricao = desc

    def setStatus(self, status):
        self.status = status

    def setEntrega(self, entrega):
        self.entrega = entrega

    def dadosPedidos(self):
        return [self.getData(), 
                self.getNome(),
                self.getValor(),
                self.getDesc(),
                self.getStatus(),
                self.getEntrega()]
