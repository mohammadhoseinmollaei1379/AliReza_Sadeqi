class Football:
    def __init__(self,first_team,second_team):
        self.first_team = first_team
        self.second_team = second_team
    def shoot(self):
        print(f"goal({self.first_team},{self.second_team})")


goal = Football(3,0)
goal.shoot()
