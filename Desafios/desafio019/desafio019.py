from rich import print
import time
class Livro:
    def __init__(self,titulo,paginas):
        self.titulo = titulo
        self.total_paginas = paginas
        self.pagina_atual = 1
        print(f":open_book:[blue] Você acabou de abrir o livro '[red]{self.titulo}[/]'"
               f" que tem [green]{self.total_paginas} páginas[/] no total."
               f" Você agora está na [yellow]pagina {self.pagina_atual}[/][blue/]")


    def Avancar_Paginas(self,qtd = 1):
        cont = 0
        for c in range(0, qtd, 1):
            if not self.Fim_do_Livro():
                self.pagina_atual +=1
                print(f"Pag{self.pagina_atual} :play_button: ",end='')
                time.sleep(0.2)
                cont += 1
        if self.Fim_do_Livro():
            print(f":closed_book: [red]Você chegou ao final do livro '{self.titulo}'[/]")
        print(f"[blue]Você avançou {cont} Páginas e está na [yellow]Página {self.pagina_atual}[/]")

    def Fim_do_Livro(self) -> bool:
        return True if self.pagina_atual == self.total_paginas else False


l1 = Livro("10 coisas que aprendi", 20)
l1.Avancar_Paginas(5)
l1.Avancar_Paginas(10)
l1.Avancar_Paginas(10)
