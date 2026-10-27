class Player:
    team_run=0

    def __init__(self,name,run):
        self.name=name
        self.run=run
        
    def hit_Four(self):
        self.run+=4
        Player.team_run+=4

    def hit_Six(self):
        self.run+=6
        Player.team_run+=6  

    def player_details(self):
        print(f"Player Name:{self.name} scored:{self.run}")


#Tester part

Tamim= Player("Tamim",0)
Shakib=Player("Shakib",0)
Tamim.hit_Four()
Tamim.hit_Six()
Tamim.player_details()
Shakib.hit_Four()
Shakib.hit_Six()
Shakib.player_details()
print("Team runs:",Player.team_run)