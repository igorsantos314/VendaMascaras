from tkinter import *
from tkinter import ttk 
from tkinter import messagebox
from datetime import date
from os import system, popen
import _thread as th
from time import sleep

from SaveBD import *

class interfaceMascaras:

    def __init__(self):
        
        #bjeto de salvamento em banco de dados
        self.cliente = saveBD()

        self.windowMenu()

    def windowMenu(self):
        
        self.window = Tk()
        self.window.geometry("450x350")
        self.window.title("Venda de Mascara - CHOCHÊ MÃE & FILHA")
        
        #lista de dados da venda
        self.listaCadastro = []

        self.cadastrarVenda = Button(text='CADASTRAR VENDA', width=25, height=2, command=self.Cadastro)
        self.cadastrarVenda.place(x=120, y=20)

        self.exibirTodos = Button(text='CONSULTAR VENDAS', width=25, height=2, command=self.printAll)
        self.exibirTodos.place(x=120, y=80)

        self.sair = Button(text='CONTABILIDADE', width=25, height=2, command= self.Contabilidade)
        self.sair.place(x=120, y=140)

        self.sair = Button(text='GASTOS', width=25, height=2, command= self.gerenciarGastos)
        self.sair.place(x=120, y=200)

        self.sair = Button(text='BACKUP DIÁRIO', width=25, height=2, command= lambda:  th.start_new_thread(self.realizarBackup, ()))
        self.sair.place(x=120, y=260)

        self.tuplaModelosMascaras = (    'NENHUMA',
                                    'PRETA', 
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
                                    'C. AZUL GRANDE',
                                    'C. AZUL PEQUENA',
                                    'C. BEGE GRANDE',
                                    'C. BEGE PEQUENA'
                                    'URSINHO',
                                    'C. VERMELHA',
                                    'PARIS' )

        self.window.mainloop()

    def realizarBackup(self):
        
        #inicia thread de contagem
        th.start_new_thread(self.cronometro, (30,))

        # --------------------------------- BACKUP DIARIO ---------------------------------
        try:
            system('~/.dropbox-dist/dropboxd')
            messagebox.showinfo('AGUARDE', 'Backup Realizado com Sucesso')

        except:
            messagebox.showerror('OPS :(', 'Ocorreu um erro ...')

    def cronometro(self, segs):
        sleep(segs)
        system('dropbox stop')

    def gerenciarGastos(self):
        # --------------------------------- GASTOS DE MATERIAIS ---------------------------------
        #DESTRUIR JANELA
        self.window.destroy()

        self.windowGerenciarGastos = Tk()
        self.windowGerenciarGastos.title('GERENCIAR GASTOS')

        lbl = Label(text='Adicionar Compra de Materiais')
        lbl.pack()
        
        #valor digitado pelo User
        et = Entry()
        et.pack()

        def Adicionar():
            #pegar valor e inserir no BD
            self.cliente.inserirGastos(float(et.get()))
            et.delete(0, END)

            messagebox.showinfo('Pronto', 'Valor Adicionado com Sucesso')

        #adcionar investimento
        btAdd = Button(text='Adicionar', command=Adicionar)
        btAdd.pack()

        lblSeparator = Label(text='________________________________________________')
        lblSeparator.pack()

        def gastosTotais():
            #exibir gastos totais
            messagebox.showinfo('Total', 'Investimento: {}'.format(self.cliente.getGastos()))

        #botão de gastos totais
        btGastosTotais = Button(text='GASTOS TOTAIS', command=gastosTotais)
        btGastosTotais.pack()

        lblSeparator = Label(text='________________________________________________')
        lblSeparator.pack()

        self.windowGerenciarGastos.mainloop()

        #voltar para o menu
        self.windowMenu()
    
    def Cadastro(self):

        #objeto de data
        data_atual = date.today()

        #fonte padrao
        fonteCombos = 'Arial 12 bold'

        #armazenamento dos combobox
        dia = StringVar()
        mes = StringVar()
        data = '{}/{}'.format(dia, mes)

        vendedor = StringVar()

        pag = StringVar()
        entrega = StringVar()
        valor = StringVar()

        mask1 = StringVar()
        mask2 = StringVar()
        mask3 = StringVar()

        tamanhoElastico = StringVar()
        tamanhoMascara = StringVar()


        #destroi janela anterior
        self.window.destroy()

        self.windowCadastro = Tk()
        self.windowCadastro.title('Cad. Vendas')

        #Menu
        myMenu = Menu(self.windowCadastro, tearoff=0)

        #Menu de vendedores
        fileMenuSalvar = Menu(myMenu)
        fileMenuSalvar.add_command(label='SALVAR', command=lambda:salvarDadosBD(1))

        #Adicionar fileMenus de Salvamento
        myMenu.add_cascade(label='File', menu=fileMenuSalvar, font='Arial 9')

        #Menu de Macro
        fileMenuMacro = Menu(myMenu)
        fileMenuMacro.add_command(label='2', command=lambda:salvarDadosBD(2))
        fileMenuMacro.add_command(label='3', command=lambda:salvarDadosBD(3))
        fileMenuMacro.add_command(label='4', command=lambda:salvarDadosBD(4))
        fileMenuMacro.add_command(label='5', command=lambda:salvarDadosBD(5))
        fileMenuMacro.add_command(label='10', command=lambda:salvarDadosBD(10))
        fileMenuMacro.add_command(label='15', command=lambda:salvarDadosBD(15))
        fileMenuMacro.add_command(label='20', command=lambda:salvarDadosBD(20))
        fileMenuMacro.add_command(label='25', command=lambda:salvarDadosBD(25))
        fileMenuMacro.add_command(label='30', command=lambda:salvarDadosBD(30))
        fileMenuMacro.add_command(label='35', command=lambda:salvarDadosBD(35))
        fileMenuMacro.add_command(label='40', command=lambda:salvarDadosBD(40))
        fileMenuMacro.add_command(label='45', command=lambda:salvarDadosBD(45))
        fileMenuMacro.add_command(label='50', command=lambda:salvarDadosBD(50))

        #Adicionar fileMenus de Salvamento
        myMenu.add_cascade(label='Macro', menu=fileMenuMacro, font='Arial 9')

        #Data
        self.textoData = Label(self.windowCadastro, text='Dia:')
        self.textoData.pack() 
        
        comboDia = ttk.Combobox(self.windowCadastro, width = 27, textvariable = dia, font= fonteCombos) 

        comboDia['values'] = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31') 
        comboDia.current(data_atual.day-1)
        comboDia.pack()

        #Mes
        self.textoData = Label(self.windowCadastro, text='Mês:')
        self.textoData.pack()

        comboMes = ttk.Combobox(self.windowCadastro, width = 27, textvariable = mes, font= fonteCombos) 

        comboMes['values'] = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12') 
        comboMes.current(data_atual.month-1)
        comboMes.pack()

        #Nome
        self.texto = Label(self.windowCadastro, text='Cliente:')
        self.texto.pack()

        self.nomeCliente = Entry(self.windowCadastro)
        self.nomeCliente.pack()

        #valor
        self.texto = Label(self.windowCadastro, text='Valor:')
        self.texto.pack()

        comboValor = ttk.Combobox(self.windowCadastro, width = 27, textvariable = valor, font= fonteCombos) 

        comboValor['values'] = ('4', '5', '10', '12', '14') 
        comboValor.current(2)
        comboValor.pack()

        #vendedor
        self.texto = Label(self.windowCadastro, text='Vendedor:')
        self.texto.pack()

        comboVendedor = ttk.Combobox(self.windowCadastro, width = 27, textvariable = vendedor, font= fonteCombos) 

        comboVendedor['values'] = ('ELLEN', 'CLAUDETE', 'HIOLANDA', 'KIL') 
        comboVendedor.current(0)
        comboVendedor.pack()

        #status de pagamento
        self.texto = Label(self.windowCadastro, text='Status de Pagamento:')
        self.texto.pack()

        comboPag = ttk.Combobox(self.windowCadastro, width = 27, textvariable = pag, font= fonteCombos) 

        comboPag['values'] = ('PG', 'EM ESPERA')
        comboPag.current(1) 
        comboPag.pack()

        #status de entrega
        self.texto = Label(self.windowCadastro, text='Status de Entrega:')
        self.texto.pack()

        comboEntrega = ttk.Combobox(self.windowCadastro, width = 27, textvariable = entrega, font= fonteCombos) 

        comboEntrega['values'] = ('OK', 'EM ESPERA') 
        comboEntrega.current(1)
        comboEntrega.pack()

        #mascara 1
        self.texto = Label(self.windowCadastro, text='MASCARA 1:')
        self.texto.pack()

        comboMask1 = ttk.Combobox(self.windowCadastro, width = 27, textvariable = mask1, font= fonteCombos) 

        comboMask1['values'] = self.tuplaModelosMascaras
        comboMask1.current(0)
        comboMask1.pack()

        #mascara 2
        self.texto = Label(self.windowCadastro, text='MASCARA 2:')
        self.texto.pack()

        comboMask2 = ttk.Combobox(self.windowCadastro, width = 27, textvariable = mask2, font= fonteCombos) 

        comboMask2['values'] = self.tuplaModelosMascaras
        comboMask2.current(0)
        comboMask2.pack()
        
        #mascara 3
        self.texto = Label(self.windowCadastro, text='MASCARA 3:')
        self.texto.pack()

        comboMask3 = ttk.Combobox(self.windowCadastro, width = 27, textvariable = mask3, font= fonteCombos) 

        comboMask3['values'] = self.tuplaModelosMascaras
                                    
        comboMask3.current(0)
        comboMask3.pack()

        #Tamanho elastico
        self.texto = Label(self.windowCadastro, text='Tamanho Elástico:')
        self.texto.pack()

        comboElastico = ttk.Combobox(self.windowCadastro, width = 27, textvariable = tamanhoElastico, font= fonteCombos) 

        comboElastico['values'] = ('ORELHA', 'CABEÇA', 'GRANDE') 
        comboElastico.current(0)
        comboElastico.pack()

        #Tamanho Mascara
        self.texto = Label(self.windowCadastro, text='Tamanho Mascara:')
        self.texto.pack()

        comboMascara = ttk.Combobox(self.windowCadastro, width = 27, textvariable = tamanhoMascara, font= fonteCombos) 

        comboMascara['values'] = ('PP', 'M', 'G', 'GG') 
        comboMascara.current(2)
        comboMascara.pack()

        def salvarDadosBD(quantidadeMacro):
            
            #tentar subir no banco de dados
            try:
                #criar N quantidade de kit
                for i in range(quantidadeMacro):
                
                    # --------------------------- SALVAR NO BANCO DE DADOS ---------------------------
                    self.cliente.inserirDados(  
                                            '{}/{}'.format(comboDia.get(), comboMes.get()), 
                                            self.nomeCliente.get().upper(),
                                            comboValor.get(), 
                                            comboVendedor.get(), 
                                            comboPag.get(), 
                                            comboEntrega.get(), 
                                            comboMask1.get(),
                                            comboMask2.get(),
                                            comboMask3.get(),
                                            comboElastico.get(), 
                                            comboMascara.get()
                                            )

                messagebox.showinfo('','CADASTRO REALIZADO COM SUCESSO :)')

            except:
                messagebox.showerror('','OCOURREU UM ERRO :(')

        #configurar file menu
        self.windowCadastro.config(menu=myMenu)

        self.windowCadastro.mainloop()

        #voltar para o menu
        self.windowMenu()

    def Contabilidade(self):

        self.window.destroy()

        self.windowContabilidade = Tk()
        self.windowContabilidade.geometry('500x500')
        
        dados = self.cliente.printValorVendedor()

        #quantidade total
        qtdTotal   = [i[0] for i in dados]
        valorTotal = [i[1] for i in dados]

        #titulo
        titulo = Label(text='Nome                       Kits                        Valor R$', font='Arial 15 bold')
        titulo.pack()

        #Ficha de Ellen
        texto = Label(text='ELLEN')
        texto.place(x=22, y=50)

        qtd = Label(text='{}'.format(dados[0][0]))
        qtd.place(x=220, y=50)

        valor = Label(text='{}'.format(dados[0][1]))
        valor.place(x=400, y=50)

        #Ficha de Claudete
        texto = Label(text='CLAUDETE')
        texto.place(x=22, y=100)

        qtd = Label(text='{}'.format(dados[1][0]))
        qtd.place(x=220, y=100)

        valor = Label(text='{}'.format(dados[1][1]))
        valor.place(x=400, y=100)

        #Ficha de Hiolanda
        texto = Label(text='HIOLANDA')
        texto.place(x=22, y=150)

        qtd = Label(text='{}'.format(dados[2][0]))
        qtd.place(x=220, y=150)

        valor = Label(text='{}'.format(dados[2][1]))
        valor.place(x=400, y=150)

        #Ficha de Kil
        texto = Label(text='KIL')
        texto.place(x=22, y=200)

        qtd = Label(text='{}'.format(dados[3][0]))
        qtd.place(x=220, y=200)

        valor = Label(text='{}'.format(dados[3][1]))
        valor.place(x=400, y=200)

        #quantidade total vendida
        texto = Label(text='KITS VENDIDOS: ')
        texto.place(x=20, y=400)

        lblQtd = Label(text='{}'.format(sum(qtdTotal)), font = 'Arial 20 bold', fg='green')
        lblQtd.place(x=150, y=390)

        #valor total vendido
        texto = Label(text='TOTAL VENDIDO: ')
        texto.place(x=20, y=450)

        texto = Label(text='R$ {}'.format(sum(valorTotal)), font = 'Arial 20 bold', fg='green')
        texto.place(x=150, y=440)

        self.windowContabilidade.mainloop()

        #voltar para o menu
        self.windowMenu()

    def printAll(self):
        
        #destruir menu
        self.window.destroy()

        self.windowPrintAll = Tk()
        self.windowPrintAll.geometry('1200x400')
        self.windowPrintAll.title("TODAS AS VENDAS")

        #Menu
        myMenu = Menu(self.windowPrintAll, tearoff=0)

        #Menu de vendedores
        fileMenuVendedor = Menu(myMenu)

        fileMenuVendedor.add_command(label='ELLEN', command=lambda:inserirDadosListBox(1))
        fileMenuVendedor.add_command(label='CLAUDETE', command=lambda:inserirDadosListBox(2))
        fileMenuVendedor.add_command(label='HIOLANDA', command=lambda:inserirDadosListBox(3))
        fileMenuVendedor.add_command(label='KIL', command=lambda:inserirDadosListBox(4))
        fileMenuVendedor.add_command(label='TODOS', command=lambda:inserirDadosListBox(5))
        #Adicionar fileMenus de Vendedores
        myMenu.add_cascade(label='VENDEDOR', menu=fileMenuVendedor)

        #Menu de STATUS PAGAMENTO
        fileMenuStatusPagamento = Menu(myMenu)
        fileMenuStatusPagamento.add_command(label='EM ESPERA', command=lambda:exibirPor(0))
        fileMenuStatusPagamento.add_command(label='PG', command=lambda:exibirPor(1))

        #Adicionar fileMenus de Edição
        myMenu.add_cascade(label='STS PAG.', menu=fileMenuStatusPagamento)

        #Menu de STATUS Entrega
        fileMenuStatusEntrega = Menu(myMenu)
        fileMenuStatusEntrega.add_command(label='EM ESPERA', command=lambda:exibirPor(2))
        fileMenuStatusEntrega.add_command(label='OK', command=lambda:exibirPor(3))

        #Adicionar fileMenus de Edição
        myMenu.add_cascade(label='STS ENT.', menu=fileMenuStatusEntrega)

        #Menu de Edicao
        fileMenuEdicao = Menu(myMenu)
        fileMenuEdicao.add_command(label='VALOR', command=lambda:editar(0))
        fileMenuEdicao.add_command(label='STATUS PAGAMENTO', command=lambda:editar(1))
        fileMenuEdicao.add_command(label='STATUS ENTREGA', command=lambda:editar(2))
        fileMenuEdicao.add_command(label='MASCARA 1', command=lambda:editar(3))
        fileMenuEdicao.add_command(label='MASCARA 2', command=lambda:editar(4))
        fileMenuEdicao.add_command(label='MASCARA 3', command=lambda:editar(5))
        fileMenuEdicao.add_command(label='TAMANHO ELASTICO', command=lambda:editar(6))
        fileMenuEdicao.add_command(label='TAMANHO MASCARA', command=lambda:editar(7))
        fileMenuEdicao.add_separator()
        fileMenuEdicao.add_command(label='UPDATE TABLE', command=lambda:atualizarPlanilha())
        fileMenuEdicao.add_separator()
        fileMenuEdicao.add_command(label='DELETAR VENDA', command='')

        #Adicionar fileMenus de Edição
        myMenu.add_cascade(label='EDITAR VENDA', menu=fileMenuEdicao)

        #Menu de valor total em ESPERA
        fileMenuValorEspera = Menu(myMenu)
        fileMenuValorEspera.add_command(label='CALCULAR', command=lambda:valorEspera())
        fileMenuValorEspera.add_command(label='VENDAS POR INTERVALO', command=self.intervalo)

        #Adicionar fileMenus de Edição
        myMenu.add_cascade(label='RECEITAS', menu=fileMenuValorEspera)

        #all products
        self.scrollbar = Scrollbar(self.windowPrintAll)
        self.scrollbar.pack(side="right", fill="y")

        self.listbox = Listbox(self.windowPrintAll, height=22, width=145, yscrollcommand=self.scrollbar.set, font='Courier 10', bg='LemonChiffon')
        self.listbox.place(x=10, y=15)

        def atualizarPlanilha():
            #limpar e inserir dados no listbox
            inserirDadosListBox(5)

        #inserir na listbox
        def inserirDadosListBox(vendedor):  
            
            self.listbox.delete(0,'end')

            #sequencia de dados 
            self.listbox.insert("end", 'ID   DATA    NOME           VAL     VEND        STS PAG.    STS ENT.    M.1               M.2               M.3               ELAST.    MASC.')
            
            #DEFINIR LISTA DE VENDAS
            listaVendas = []

            if vendedor == 5:
                listaVendas = self.cliente.buscarTodasVendas()
            
            else:
                vendedores = ['ELLEN', 'CLAUDETE', 'HIOLANDA', 'KIL']
                listaVendas = self.cliente.buscarVendedor(vendedores[vendedor-1])

            #chamar exibicao
            exibicaoDados(listaVendas)

        def exibirPor(tipo):
            self.listbox.delete(0,'end')

            #lista de opcoes
            listaDeOpcoes = ['EM ESPERA','PG', 'EM ESPERA', 'OK']
            listaVendas = []

            if tipo == 0 or tipo == 1:
                listaVendas = self.cliente.buscarPagamento(listaDeOpcoes[tipo])
            
            elif tipo == 2 or tipo == 3:
                listaVendas = self.cliente.buscarEntrega(listaDeOpcoes[tipo])


            #chamar exibicao
            exibicaoDados(listaVendas)

        def editar(tipo):
            try:

                #pega o indice do listbox selecionado
                indice = self.listbox.curselection()[0]
                texto = self.listbox.get(indice)

                #pegar apenas o indice da tupla de dados
                posicaoFinal = 0

                for pos,i in enumerate(texto):
                    if i == ' ':
                        posicaoFinal = pos
                        break
                    
                #id da venda
                id = texto[0:posicaoFinal]

                if tipo == 0:
                    #abrir edicao
                    self.editarValor(id)

                elif tipo == 1:
                    #abrir edicao
                    self.editarStatusPagamento(id)

                elif tipo == 2:
                    #abrir edicao
                    self.editarStatusEntrega(id)

                elif tipo == 3:
                    #abrir edicao
                    self.editarMascara1(id)

                elif tipo == 4:
                    #abrir edicao
                    self.editarMascara2(id)

                elif tipo == 5:
                    #abrir edicao
                    self.editarMascara3(id)

                elif tipo == 6:
                    #abrir edicao
                    self.editarTamanhoElastico(id)

                elif tipo == 7:
                    #abrir edicao
                    self.editarTamanhoMascara(id)

            except:
                pass
        
        def exibicaoDados(listaVendas):

            for pos,i in enumerate(listaVendas):

                #tratamento de dados
                id = "{}".format(i[0])
                id = "{}{}".format(i[0], " " * (5 - len(id)))

                data = "{}{}".format(i[1], " " * (8 - len(i[1])))
                nome = "{}{}".format(i[2], " " * (15 - len(i[2])))

                valor = "{}".format(i[3])
                valor = "{}{}".format(valor, " " * (8 - len(valor)))

                vendedor  = "{}{}".format(i[4], " " * (12 - len(i[4])))
                statusPag = "{}{}".format(i[5], " " * (12 - len(i[5])))
                statusEnt = "{}{}".format(i[6], " " * (12 - len(i[6])))

                m1 = "{}{}".format(i[7], " " * (18 - len(i[7])))
                m2 = "{}{}".format(i[8], " " * (18 - len(i[8])))
                m3 = "{}{}".format(i[9], " " * (18 - len(i[9])))

                tamanhoElastico = "{}{}".format(i[10], " " * (10 - len(i[10])))
                tamanhoMascara  = "{}{}".format(i[11], " " * (5 - len(i[11])))

                #inserção na tabela
                self.listbox.insert("end", "{}{}{}{}{}{}{}{}{}{}{}{}".format(id, data, nome, valor, vendedor, statusPag, statusEnt, m1, m2, m3, tamanhoElastico, tamanhoMascara))

        def valorEspera():
            #pegar o valor total da divida do BD
            v = self.cliente.buscarValorEspera()

            #exibir valor
            messagebox.showinfo('', 'VALOR A RECEBER [ R$ {} ]'.format(v))

        #chamar inserção de dados
        inserirDadosListBox(5)

        #configuração de scrollbar
        self.scrollbar.config(command=self.listbox.get)

        #configurar file menu
        self.windowPrintAll.config(menu=myMenu)

        self.windowPrintAll.mainloop()

        #voltar para o menu
        self.windowMenu()

    # ------------------------------------------------------------------ SETOR DE INTERVALO DE VENDAS ------------------------------------------------------------------
    def intervalo(self):

        #objeto de data
        data_atual = date.today()

        self.windowGetIntervalo = Tk()
        self.windowGetIntervalo.title("Informe o Intervalo de Vendas")

        #informar a data inicial da venda
        lblDI = Label(self.windowGetIntervalo, text='DIA INICIAL')
        lblDI.pack()

        comboDiaInicial = ttk.Combobox(self.windowGetIntervalo, width = 27) 

        comboDiaInicial['values'] = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31') 
        comboDiaInicial.current(data_atual.day-1)
        comboDiaInicial.pack()

        lblMI = Label(self.windowGetIntervalo, text='MES INICIAL')
        lblMI.pack()

        comboMesInicial = ttk.Combobox(self.windowGetIntervalo, width = 27) 

        comboMesInicial['values'] = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12') 
        comboMesInicial.current(data_atual.month-1)
        comboMesInicial.pack()

        #informar a data final da venda
        lblDF = Label(self.windowGetIntervalo, text='DIA FINAL')
        lblDF.pack()

        comboDiaFinal = ttk.Combobox(self.windowGetIntervalo, width = 27) 

        comboDiaFinal['values'] = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31') 
        comboDiaFinal.current(data_atual.day-1)
        comboDiaFinal.pack()


        lblMF = Label(self.windowGetIntervalo, text='MES FINAL')
        lblMF.pack()

        comboMesFinal = ttk.Combobox(self.windowGetIntervalo, width = 27) 

        comboMesFinal['values'] = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12') 
        comboMesFinal.current(data_atual.month-1)
        comboMesFinal.pack()

        btGetIntervalo = Button(self.windowGetIntervalo, text='CONSULTAR VENDAS', command=lambda: varrerDatas())
        btGetIntervalo.pack()

        def varrerDatas():
            
            #pegar os valores de dia e datas informadas
            di = int(comboDiaInicial.get())
            mi = int(comboMesInicial.get())

            df = int(comboDiaFinal.get())
            mf = int(comboMesFinal.get())

            #retorna a lista de venda por este periodo
            listaVendas = self.cliente.buscarVendasPeriodo(di, mi, df, mf)

            #pegar o valor de cada venda
            valor = 0

            for elemento in listaVendas: 
                valor += elemento[3]

            #exibir
            self.printVendasIntervalo(di, mi, df, mf, listaVendas, valor)

        #
        self.windowGetIntervalo.mainloop()

    def printVendasIntervalo(self, di, mi, df, mf, listaVendas, valor):
        
        self.windowIntervalo = Tk()
        self.windowIntervalo.title("{} do {} à {} do {} -- R$ {}".format(di, mi, df, mf, valor))

        self.scrollbar = Scrollbar(self.windowIntervalo)
        self.scrollbar.pack(side="right", fill="y")

        self.listboxIntervalo = Listbox(self.windowIntervalo, height=22, width=145, yscrollcommand=self.scrollbar.set, font='Courier 10', bg='LemonChiffon')
        self.listboxIntervalo.pack()

        def exibicaoDados():
            for pos, i in enumerate(listaVendas):

                #if pos != (len(listaVendas)-1):
                #tratamento de dados
                id = "{}".format(i[0])
                id = "{}{}".format(i[0], " " * (5 - len(id)))

                data = "{}{}".format(i[1], " " * (8 - len(i[1])))
                nome = "{}{}".format(i[2], " " * (15 - len(i[2])))

                valor = "{}".format(i[3])
                valor = "{}{}".format(valor, " " * (8 - len(valor)))

                vendedor  = "{}{}".format(i[4], " " * (12 - len(i[4])))
                statusPag = "{}{}".format(i[5], " " * (12 - len(i[5])))
                statusEnt = "{}{}".format(i[6], " " * (12 - len(i[6])))

                m1 = "{}{}".format(i[7], " " * (18 - len(i[7])))
                m2 = "{}{}".format(i[8], " " * (18 - len(i[8])))
                m3 = "{}{}".format(i[9], " " * (18 - len(i[9])))

                tamanhoElastico = "{}{}".format(i[10], " " * (10 - len(i[10])))
                tamanhoMascara  = "{}{}".format(i[11], " " * (5 - len(i[11])))

                #inserção na tabela
                self.listboxIntervalo.insert("end", "{}{}{}{}{}{}{}{}{}{}{}{}".format(id, data, nome, valor, vendedor, statusPag, statusEnt, m1, m2, m3, tamanhoElastico, tamanhoMascara))
                
        #configuração de scrollbar
        self.scrollbar.config(command=self.listbox.get)

        #chamar função para exibir a lista de vendas
        exibicaoDados()

        self.windowIntervalo.mainloop()

    # ------------------------------------------------------------------ SETOR DE EDICAO ------------------------------------------------------------------
    def editarValor(self, id):

        windowValor = Tk()
        windowValor.title('ID: {}'.format(id))

        lbl = Label(windowValor, text='VALOR DO KIT')
        lbl.pack()

        comboValor = ttk.Combobox(windowValor, width = 27, font= 'Arial 12') 
        comboValor['values'] = ('4', '5', '10', '12', '14') 
        comboValor.current(0)
        comboValor.pack()

        def atualizarBD():
            try:
                #commitar alterações
                self.cliente.changeValor(id, int(comboValor.get()))

                messagebox.showinfo('', 'EDITADO COM SUCESSO :)')
                windowValor.destroy()

            except:
                messagebox.showerror('', 'NÃO FOI POSSÍVEL ATUALIZAR OS DADOS !')

        bt = Button(windowValor, text='SALVAR', command=atualizarBD)
        bt.pack()

        windowValor.mainloop()

    def editarStatusEntrega(self, id):

        windowStatusEntrega = Tk()
        windowStatusEntrega.title('ID: {}'.format(id))

        lbl = Label(windowStatusEntrega, text='STATUS ENTREGA')
        lbl.pack()

        comboEntrega = ttk.Combobox(windowStatusEntrega, width = 27, font= 'Arial 12') 
        comboEntrega['values'] = ('OK', 'EM ESPERA') 
        comboEntrega.current(0)
        comboEntrega.pack()

        def atualizarBD():
            try:
                #commitar alterações
                self.cliente.changeStatusEntrega(id, comboEntrega.get())

                messagebox.showinfo('', 'EDITADO COM SUCESSO :)')
                windowStatusEntrega.destroy()

            except:
                messagebox.showerror('', 'NÃO FOI POSSÍVEL ATUALIZAR OS DADOS !')

        bt = Button(windowStatusEntrega, text='SALVAR', command=atualizarBD)
        bt.pack()

        windowStatusEntrega.mainloop()

    def editarStatusPagamento(self, id):

        windowStatusPagamento = Tk()
        windowStatusPagamento.title('ID: {}'.format(id))

        lbl = Label(windowStatusPagamento, text='STATUS PAGAMENTO')
        lbl.pack()

        comboPag = ttk.Combobox(windowStatusPagamento, width = 27, font= 'Arial 12') 
        comboPag['values'] = ('PG', 'EM ESPERA') 
        comboPag.current(0)
        comboPag.pack()

        def atualizarBD():
            try:
                #commitar alterações
                self.cliente.changeStatusPagamento(id, comboPag.get())

                messagebox.showinfo('', 'EDITADO COM SUCESSO :)')
                windowStatusPagamento.destroy()

            except:
                messagebox.showerror('', 'NÃO FOI POSSÍVEL ATUALIZAR OS DADOS !')

        #salvar edicao
        bt = Button(windowStatusPagamento, text='SALVAR', command=atualizarBD)
        bt.pack()

        windowStatusPagamento.mainloop()

    def editarMascara1(self, id):
        
        windowMascara = Tk()
        windowMascara.title('ID: {}'.format(id))

        lbl = Label(windowMascara, text='MASCARA 1')
        lbl.pack()

        comboMask = ttk.Combobox(windowMascara, width = 27) 

        comboMask['values'] = self.tuplaModelosMascaras
        comboMask.current(0)
        comboMask.pack()

        def atualizarBD():
            try:
                #commitar alterações
                self.cliente.changeMascara1(id, comboMask.get())

                messagebox.showinfo('', 'EDITADO COM SUCESSO :)')
                windowMascara.destroy()

            except:
                messagebox.showerror('', 'NÃO FOI POSSÍVEL ATUALIZAR OS DADOS !')

        #salvar edicao
        bt = Button(windowMascara, text='SALVAR', command=atualizarBD)
        bt.pack()

        windowMascara.mainloop()

    def editarMascara2(self, id):
        
        windowMascara = Tk()
        windowMascara.title('ID: {}'.format(id))

        lbl = Label(windowMascara, text='MASCARA 2')
        lbl.pack()

        comboMask = ttk.Combobox(windowMascara, width = 27) 

        comboMask['values'] = self.tuplaModelosMascaras
        comboMask.current(0)
        comboMask.pack()

        def atualizarBD():
            try:
                #commitar alterações
                self.cliente.changeMascara2(id, comboMask.get())

                messagebox.showinfo('', 'EDITADO COM SUCESSO :)')
                windowMascara.destroy()

            except:
                messagebox.showerror('', 'NÃO FOI POSSÍVEL ATUALIZAR OS DADOS !')

        #salvar edicao
        bt = Button(windowMascara, text='SALVAR', command=atualizarBD)
        bt.pack()

        windowMascara.mainloop()

    def editarMascara3(self, id):
        windowMascara = Tk()
        windowMascara.title('ID: {}'.format(id))

        lbl = Label(windowMascara, text='MASCARA 3')
        lbl.pack()

        comboMask = ttk.Combobox(windowMascara, width = 27) 

        comboMask['values'] = self.tuplaModelosMascaras
        comboMask.current(0)
        comboMask.pack()

        def atualizarBD():
            try:
                #commitar alterações
                self.cliente.changeMascara3(id, comboMask.get())

                messagebox.showinfo('', 'EDITADO COM SUCESSO :)')
                windowMascara.destroy()

            except:
                messagebox.showerror('', 'NÃO FOI POSSÍVEL ATUALIZAR OS DADOS !')

        #salvar edicao
        bt = Button(windowMascara, text='SALVAR', command=atualizarBD)
        bt.pack()

        windowMascara.mainloop()

    def editarTamanhoElastico(self, id):
        windowTamanhoElastico = Tk()
        windowTamanhoElastico.title('ID: {}'.format(id))

        lbl = Label(windowTamanhoElastico, text='TAMANHO ELASTICO')
        lbl.pack()

        comboT = ttk.Combobox(windowTamanhoElastico, width = 27) 

        comboT['values'] = ['ORELHA', 'CABEÇA']
        comboT.current(0)
        comboT.pack()

        def atualizarBD():
            try:
                #commitar alterações
                self.cliente.changeTamanhoElastico(id, comboT.get())

                messagebox.showinfo('', 'EDITADO COM SUCESSO :)')
                windowTamanhoElastico.destroy()

            except:
                messagebox.showerror('', 'NÃO FOI POSSÍVEL ATUALIZAR OS DADOS !')

        #salvar edicao
        bt = Button(windowTamanhoElastico, text='SALVAR', command=atualizarBD)
        bt.pack()

        windowTamanhoElastico.mainloop()

    def editarTamanhoMascara(self, id):

        windowTamanhoMascara = Tk()
        windowTamanhoMascara.title('ID: {}'.format(id))

        lbl = Label(windowTamanhoMascara, text='TAMANHO MASCARA')
        lbl.pack()

        comboT = ttk.Combobox(windowTamanhoMascara, width = 27) 

        comboT['values'] = ['PP', 'M', 'G', 'GG']
        comboT.current(0)
        comboT.pack()

        def atualizarBD():
            try:
                #commitar alterações
                self.cliente.changeTamanhoMascara(id, comboT.get())

                messagebox.showinfo('', 'EDITADO COM SUCESSO :)')
                windowTamanhoMascara.destroy()

            except:
                messagebox.showerror('', 'NÃO FOI POSSÍVEL ATUALIZAR OS DADOS !')

        #salvar edicao
        bt = Button(windowTamanhoMascara, text='SALVAR', command=atualizarBD)
        bt.pack()

        windowTamanhoMascara.mainloop()

a = interfaceMascaras()