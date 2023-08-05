class Scout:
  team = 4099

  def __init__(self, name):
    self.name = name

scout_one = new Scout("John")

print(scout_one.team)
print(Scout.team)
