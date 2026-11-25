from operator import itemgetter

from rich import print
from rich.panel import Panel

class Gamer:
    def __init__(self,nome,nick):
        self.nome = nome
        self.nick = nick

    def add_favoritos(self,jogo):
        lista = list()
        self.jogo = jogo
        self.lista = lista
        self.lista.append(self.jogo)
        self.lista.sort()
        return self.lista



    def ficha(self):
        conteudo = f"Nome real = {self.nome}"
        conteudo += f"\nJogos favoritos:"
        for c in self.add_favoritos(self.jogo):
            conteudo += f"\n:video_game: [blue]{c}[/]"

        painel = Panel(conteudo,title=f"Jogador <{self.nick}>",width=35)
        print(painel)


j1 = Gamer("Fabricio da Silva","detonator2026")
j1.add_favoritos("Mario Bros.")
j1.add_favoritos("Sonic")
j1.add_favoritos("God of War")
j1.add_favoritos("Fortnite")
j1.ficha()

