from rich import print
from rich.panel import Panel
import sys
class Gamer:
    def __init__(self,nome,nick):
        self.nome = nome
        self.nick = nick
        self.jogo_favorito = list()



    def add_favoritos(self,jogo):
        self.jogo_favorito.append(jogo)
        self.jogo_favorito.sort(key=str.lower) #se o usuario digita tudo fora de ordem ele coloca tudo para lower, e ordena



    def ficha(self):
        conteudo = f"Nome real = [black on blue]{self.nome}[/]"
        conteudo += f"\nJogos favoritos:"
        for c in self.jogo_favorito:
            conteudo += f"\n:video_game: [blue]{c}[/]"

        painel = Panel(conteudo,title=f"Jogador <{self.nick}>",width=35)
        print(painel)


j1 = Gamer("Fabricio da Silva","detonator2026")
j1.add_favoritos("Mario Bros.")
j1.add_favoritos("Sonic")
j1.add_favoritos("God of War")
j1.add_favoritos("Fortnite")
j1.add_favoritos("Among Us")
print()

print('-' * 40)
j2 = Gamer("Olivia Souza","peachraivosa32")
print(f"Olá {j2.nome}! ",end='')
while True:
    try:
        j2.add_favoritos(str(input("Digite um jogo favorito: ")).strip())
        resp = ""
        while resp not in ["S","N"]:
            resp = str(input("Tem mais algum jogo favorito?[S/N] ")).strip().upper()
            if resp != "":
                resp = resp[0]
        print('-' * 40)
        if resp == 'N':
            break
    except KeyboardInterrupt:
        print("[red]O usuário preferiu sair[/]")
        sys.exit()

j1.ficha()
j2.ficha()