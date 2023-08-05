class Scout:
  team = 4099

  def __init__(self, name, subteam):
    self.name = name
    self.subteam = subteam

scout_one = new Scout("John", "strategy")
scout_two = new Scout("Nhoj", "business")

# Instance access
print(scout_one.team) 
print(scout_two.team)
# Class access
print(Scout.team)
