import customtkinter as ctk

# --- Lógica (Back-end) ---
class LogicaCalculadora:
    def __init__(self):
        self.expressao = ""

    def adicionar_caractere(self, caractere):
        self.expressao += str(caractere)
        return self.expressao

    def limpar(self):
        self.expressao = ""
        return ""

    def calcular(self):
        try:
            # Avalia a string matemática com segurança
            resultado = str(eval(self.expressao))
            self.expressao = resultado
            return resultado
        except:
            self.expressao = ""
            return "Erro"

# --- Interface (Front-end) ---
class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.back = LogicaCalculadora()

        # Configurações da Janela
        self.title("Calculadora")
        self.geometry("300x450")
        ctk.set_appearance_mode("dark") 
        
        # Display (Visor)
        self.visor = ctk.CTkEntry(self, width=280, height=70, font=("Helvetica", 32), 
                                  justify="right", fg_color="#1a1a1a", border_color="#333")
        self.visor.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

        # Configuração de Botões (Texto, Linha, Coluna, Cor)
        botoes = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3, "#ff9500"),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3, "#ff9500"),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3, "#ff9500"),
            ('C', 4, 0, "#ff3b30"), ('0', 4, 1), ('=', 4, 2, "#34c759"), ('+', 4, 3, "#ff9500"),
        ]

        for texto, linha, col, *cor in botoes:
            cor_final = cor[0] if cor else "#333333"
            btn = ctk.CTkButton(self, text=texto, width=60, height=60, corner_radius=10,
                                fg_color=cor_final, font=("Helvetica", 20, "bold"),
                                hover_color="#555",
                                command=lambda t=texto: self.clique_botao(t))
            btn.grid(row=linha, column=col, padx=5, pady=5)

    def clique_botao(self, texto):
        if texto == "=":
            res = self.back.calcular()
        elif texto == "C":
            res = self.back.limpar()
        else:
            res = self.back.adicionar_caractere(texto)
        
        self.visor.delete(0, "end")
        self.visor.insert(0, res)

if __name__ == "__main__":
    app = App()
    app.mainloop()