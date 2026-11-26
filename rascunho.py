from rich import print
from rich.panel import Panel
class Gamer:
    def __init__(self,nome,nick):
        self.nome = nome
        self.nick = nick
        self.favoritos = list()


    def add_favoritos(self,jogo):
        self.favoritos.append(jogo)
        self.favoritos.sort(key=str.lower)


    def ficha(self):
        conteudo = f"Nome Real = [blue on white]{self.nome}[/]"
        conteudo += f"\nJogos favoritos:"
        for c in self.favoritos:
            conteudo += f"\n[blue]:video_game: {c}"
        painel = Panel(conteudo,title=f" Jogador <{self.nick}>",width=40)
        print(painel)


j1 = Gamer("Juliano Berdet","Jberdet")
j1.add_favoritos("Red Dead Redemption 2")
j1.add_favoritos("Donkey kong 2")
j1.add_favoritos("Age of Empires 3")
j1.ficha()