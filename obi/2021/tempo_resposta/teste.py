eventos = int(input())

class Usuario():

    def __init__(self, nome):
        self.registros = ''
        self.bloco = {}
        self.nome = nome
        self.tempo_total = 0
        self.count_tick = 0
        self.resposta_pendente = False
        self.last_update = 0

    def increase_tick(self,tick, tempo = 1):
        if tick == self.last_update:
            return
        if self.registros == 'R':
            self.count_tick += tempo 

    def adicionar_registro(self,tick,registro, bloco):
        self.registros = registro
        if self.registros == 'E':
            if self.last_update == tick + 1:
                self.tempo_total += 1
                self.count_tick += 0
            else:
                self.tempo_total += self.count_tick
                self.count_tick = 0
        try:
            self.bloco[bloco] += 1
        except:
            self.bloco[bloco] = 1
        self.last_update = tick

    def retornar_bloco(self,bloco):
        try:
            return self.bloco[bloco]
        except:
            return 0

    def retornar_total_registros(self):
        return self.registros

bloco_atual = 0
usuarios = {}

for i in range(eventos):
    evento = input()
    registro , nome = evento.split()
    if registro != 'T':
        if nome not in usuarios:
            usuarios[nome] = Usuario(nome)
            usuarios[nome].adicionar_registro(i, registro, bloco_atual)
        else:
            usuarios[nome].adicionar_registro(i, registro, bloco_atual)
        for j in usuarios:
            usuarios[j].increase_tick(i)
    else:
        for j in usuarios:
            usuarios[j].increase_tick(i,int(nome))

        bloco_atual += 1


for j in usuarios:
    print(usuarios[j].nome, usuarios[j].tempo_total)


