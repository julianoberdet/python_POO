from rich import print
import time
class Livro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.total_paginas = paginas
        self.pagina_atual = 1
        print(f":open_book:[blue] Você acabou de abrir o livro '[red]{self.titulo}[/]'"
               f" que tem [green]{self.total_paginas} páginas[/] no total."
               f" Você agora está na [yellow]pagina {self.pagina_atual}[/][blue/]")

    def analisar_paginas(self,qtd):
        cont = 0
        for c in range(0,qtd, 1):
            if not self.fim_do_livro():
                self.pagina_atual += 1
                print(f"Pag {self.pagina_atual} :arrow_forward: ",end='')
                time.sleep(0.3)
                cont += 1
        if self.fim_do_livro():
            print(f":closed_book: [red]Você chegou ao final do livro '{self.titulo}'[/]")
        print(f"[blue]Você agora avançou {cont} páginas está na [yellow]pagina {self.pagina_atual}[/][blue/]")

    def fim_do_livro(self):
        return True if self.pagina_atual == self.total_paginas else False

l1 = Livro("10 coisas que aprendi",20)
l1.analisar_paginas(5)
l1.analisar_paginas(30)
l1.analisar_paginas(12)
l1.analisar_paginas(19)