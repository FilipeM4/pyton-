import tkinter as tk
from tkinter import ttk, messagebox


class Pedido:

    def __init__(self, nome, telefone, item, endereco, quantidade,
                 metodo_pagamento, ponto_referencia):
        self.nome = nome
        self.telefone = telefone
        self.item = item
        self.endereco = endereco
        self.quantidade = quantidade
        self.metodo_pagamento = metodo_pagamento
        self.ponto_referencia = ponto_referencia


class PizzariaGUI:

    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Pizzaria Dos Maias")
        self.janela.configure(bg="yellow")

        self.sabores_pizza = [
            "Marguerita", "Calabresa", "Frango com Catupiry", "Portuguesa",
            "Quatro Queijos", "Chocolate com Morango", "Romeu e Julieta",
            "Bacon com Milho", "Vegetariana", "Pepperoni", "Mussarela e bacon",
            "pizza de sorvete", "pizza de baunilha com chocolate"
        ]

        self.tamanhos_pizza = ["Pequena", "Média", "Grande"]

        self.preco_pizza = {
            "Marguerita": {
                "Pequena": 30,
                "Média": 40,
                "Grande": 50
            },
            "Calabresa": {
                "Pequena": 30,
                "Média": 40,
                "Grande": 50
            },
            "Frango com Catupiry": {
                "Pequena": 35,
                "Média": 45,
                "Grande": 55
            },
            "Portuguesa": {
                "Pequena": 35,
                "Média": 45,
                "Grande": 55
            },
            "Quatro Queijos": {
                "Pequena": 35,
                "Média": 45,
                "Grande": 55
            },
            "Chocolate com Morango": {
                "Pequena": 40,
                "Média": 50,
                "Grande": 60
            },
            "Romeu e Julieta": {
                "Pequena": 40,
                "Média": 50,
                "Grande": 60
            },
            "Bacon com Milho": {
                "Pequena": 40,
                "Média": 50,
                "Grande": 60
            },
            "Vegetariana": {
                "Pequena": 45,
                "Média": 55,
                "Grande": 65
            },
            "Pepperoni": {
                "Pequena": 45,
                "Média": 55,
                "Grande": 65
            },
            "Mussarela e bacon": {
                "Pequena": 50,
                "Média": 60,
                "Grande": 70
            },
            "pizza de sorvete": {
                "Pequena": 60,
                "Média": 70,
                "Grande": 80
            },
            "Pizza de baunilha com chocolate": {
                " pequena": 95,
                "Média": 87,
                "Grande": 90
            }
        }

        self.sabores_refri = [
            "Coca-Cola",
            "Guaraná",
            "Fanta",
            "Sprite",
            "Schweppes",
            "Kuat",
            "Sukita",
            "Dolly",
            "Tubaína",
            "Sprite Zero",
            "Água",
        ]

        self.preco_refri = {
            "Coca-Cola": 13,
            "Guaraná": 10,
            "Fanta": 9,
            "Sprite": 10,
            "Schweppes": 8,
            "Kuat": 7,
            "Sukita": 6,
            "Dolly": 5,
            "Tubaína": 8,
            "Sprite Zero": 6,
            "Água": 4
        }

        self.nome_cliente = tk.StringVar()
        self.telefone_cliente = tk.StringVar()
        self.endereco_cliente = tk.StringVar()
        self.ponto_referencia_cliente = tk.StringVar()
        self.sabor_pizza_selecionado = tk.StringVar()
        self.tamanho_pizza_selecionado = tk.StringVar()
        self.quantidade_pizzas = tk.IntVar(value=1)
        self.sabor_refri_selecionado = tk.StringVar()
        self.quantidade_refris = tk.IntVar(value=1)
        self.metodo_pagamento_selecionado = tk.StringVar()

        self.criar_widgets()

    def criar_widgets(self):

        notebook = ttk.Notebook(self.janela)
        notebook.grid(row=0, column=0, padx=5, pady=5, columnspan=2)

        frame_pizzas = tk.Frame(notebook, bg="yellow")
        notebook.add(frame_pizzas, text='Pizzas')

        tk.Label(frame_pizzas, text="Nome:", bg="yellow").grid(row=0,
                                                               column=0,
                                                               padx=5,
                                                               pady=5)
        tk.Entry(frame_pizzas, textvariable=self.nome_cliente).grid(row=0,
                                                                    column=1,
                                                                    padx=5,
                                                                    pady=5)

        tk.Label(frame_pizzas, text="Telefone:", bg="yellow").grid(row=0,
                                                                   column=2,
                                                                   padx=5,
                                                                   pady=5)
        tk.Entry(frame_pizzas, textvariable=self.telefone_cliente).grid(row=0,
                                                                        column=3,
                                                                        padx=5,
                                                                        pady=5)

        tk.Label(frame_pizzas, text="Endereço:", bg="yellow").grid(row=1,
                                                                   column=0,
                                                                   padx=5,
                                                                   pady=5)
        tk.Entry(frame_pizzas, textvariable=self.endereco_cliente).grid(row=1,
                                                                        column=1,
                                                                        padx=5,
                                                                        pady=5)

        tk.Label(frame_pizzas, text="Ponto de Referência:",
                 bg="yellow").grid(row=2, column=0, padx=5, pady=5)
        tk.Entry(frame_pizzas,
                 textvariable=self.ponto_referencia_cliente).grid(row=2,
                                                                  column=1,
                                                                  padx=5,
                                                                  pady=5)

        tk.Label(frame_pizzas, text="Sabor:", bg="yellow").grid(row=3,
                                                                 column=0,
                                                                 padx=5,
                                                                 pady=5)
        tk.OptionMenu(frame_pizzas, self.sabor_pizza_selecionado,
                      *self.sabores_pizza).grid(row=3, column=1, padx=5, pady=5)

        tk.Label(frame_pizzas, text="Tamanho:", bg="yellow").grid(row=4,
                                                                   column=0,
                                                                   padx=5,
                                                                   pady=5)
        tk.OptionMenu(frame_pizzas, self.tamanho_pizza_selecionado,
                      *self.tamanhos_pizza).grid(row=4, column=1, padx=5, pady=5)

        tk.Label(frame_pizzas, text="Quantidade:", bg="yellow").grid(row=5,
                                                                      column=0,
                                                                      padx=5,
                                                                      pady=5)
        tk.Spinbox(frame_pizzas,
                    from_=1,
                    to=10,
                    textvariable=self.quantidade_pizzas).grid(row=5,
                                                              column=1,
                                                              padx=5,
                                                              pady=5)

        frame_refris = tk.Frame(notebook, bg="yellow")
        notebook.add(frame_refris, text='Refrigerantes')

        tk.Label(frame_refris, text="Sabor:", bg="yellow").grid(row=0,
                                                                column=0,
                                                                padx=5,
                                                                pady=5)
        tk.OptionMenu(frame_refris, self.sabor_refri_selecionado,
                      *self.sabores_refri).grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_refris, text="Quantidade:", bg="yellow").grid(row=1,
                                                                     column=0,
                                                                     padx=5,
                                                                     pady=5)
        tk.Spinbox(frame_refris,
                    from_=1,
                    to=10,
                    textvariable=self.quantidade_refris).grid(row=1,
                                                              column=1,
                                                              padx=5,
                                                              pady=5)

        carrinho_frame = tk.Frame(self.janela, bg="yellow")
        carrinho_frame.grid(row=0, column=2, padx=5, pady=5, sticky="nsew")

        tk.Label(carrinho_frame, text="Carrinho de Compras",
                 bg="yellow").grid(row=0, column=0, padx=5, pady=5)

        self.carrinho_listbox = tk.Listbox(carrinho_frame, width=40, height=15)
        self.carrinho_listbox.grid(row=1, column=0, padx=5, pady=5)

        def apagar_item():
            selecionado = self.carrinho_listbox.curselection()
            if selecionado:
                self.carrinho_listbox.delete(selecionado)

        apagar_item_btn = tk.Button(carrinho_frame,
                                    text="Apagar Item",
                                    command=apagar_item)
        apagar_item_btn.grid(row=2, column=0, padx=5, pady=5)

        def editar_item():
            selecionado = self.carrinho_listbox.curselection()
            if selecionado:
                item = self.carrinho_listbox.get(selecionado)

        editar_item_btn = tk.Button(carrinho_frame,
                                    text="Editar Item",
                                    command=editar_item)
        editar_item_btn.grid(row=3, column=0, padx=5, pady=5)

        self.total_label = tk.Label(carrinho_frame,
                                    text="Total: R$ 0.00",
                                    bg="yellow",
                                    font=("Helvetica", 10))
        self.total_label.grid(row=4, column=0, padx=5, pady=5)

        def calcular_preco():
            total = 0
            for item in self.carrinho_listbox.get(0, tk.END):
                preco = float(item.split("R$ ")[1])
                total += preco
            self.total_label.config(text=f"Total: R$ {total:.2f}")

        def adicionar_ao_carrinho(item):
            self.carrinho_listbox.insert(tk.END, item)
            calcular_preco()

        def fazer_pedido():
            nome = app.nome_cliente.get()
            telefone = app.telefone_cliente.get()
            endereco = app.endereco_cliente.get()
            ponto_referencia = app.ponto_referencia_cliente.get()
            sabor_pizza = app.sabor_pizza_selecionado.get()
            tamanho_pizza = app.tamanho_pizza_selecionado.get()
            quantidade_pizzas = app.quantidade_pizzas.get()
            sabor_refri = app.sabor_refri_selecionado.get()
            quantidade_refris = app.quantidade_refris.get()
            metodo_pagamento = app.metodo_pagamento_selecionado.get()

            preco_pizza = self.preco_pizza[sabor_pizza][
                tamanho_pizza] * quantidade_pizzas
            preco_refri = self.preco_refri[sabor_refri] * quantidade_refris
            preco_total = preco_pizza + preco_refri

            pedido = Pedido(
                nome, telefone,
                f"Pizza: {sabor_pizza} ({tamanho_pizza}) x {quantidade_pizzas}, Refri: {sabor_refri} x {quantidade_refris}",
                endereco, quantidade_pizzas + quantidade_refris,
                metodo_pagamento, ponto_referencia)

            adicionar_ao_carrinho(f"{pedido.item} - R$ {preco_total:.2f}")

            messagebox.showinfo(
                "Pedido Realizado",
                f"Pedido realizado com sucesso!\nPreço total: R$ {preco_total:.2f}")

            pedido.hora_saida = time.time()

        fazer_pedido_btn = tk.Button(frame_refris,
                                     text="Fazer Pedido",
                                     command=fazer_pedido)
        fazer_pedido_btn.grid(row=3, column=0, columnspan=2, padx=5, pady=5)


pedidos = []

root = tk.Tk()
app = PizzariaGUI(root)
root.mainloop()
