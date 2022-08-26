class Player:
    def __init__(self, name, old, scores):
        self.name, self.old, self.scores = name, old, scores

    # def __len__(self):
    #     print("__len__")
    #     return 1 if self.scores > 0 else 0
    def __str__(self):
        return f'{self.name}; {self.old}; {self.scores}'
    def __bool__(self):
        print("__bool__")
        return bool(self.scores)



lst_in = ['Балакирев; 34; 2048',
'Mediel; 27; 0',
'Влад; 18; 9012',
'Nina P; 33; 0']
players = []
for x in lst_in:
    name, old, scores = x.split('; ')
    new_obj = Player(name, old, int(scores))
    players.append(new_obj)

a = players[0]
print(bool(a))
# print("len x = ", len(a))

players_filtered = list(filter(bool, players))
print(players_filtered)
for x in players_filtered:
    print(x)
