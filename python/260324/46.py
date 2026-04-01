class soccer:
    def __init__(self, team, win):
        self.team = team
        self.win = win

    def winner(self, i):
        if i.win >= self.win:
            return i.team
        return None

team, win = map(int, input().split())
info = soccer(team, win)

teams = []

for _ in range(info.team):
    t_name, t_win = input().split()
    teams.append(soccer(t_name, int(t_win)))

for i in range(info.team - 1, -1, -1):
    result = info.winner(teams[i])
    if result:
        print(result)

