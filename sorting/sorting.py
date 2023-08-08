class Scout:
  team = 4099
  def __init__(self, name, subteam):
    self.name = name
    self.subteam = subteam
  def display():
    print(f"{self.name} is a scout.")

class PitScout(Scout):
  def __init__(self, name, subteam, group):
    super().__init__(name, subteam)
    self.group = group
  def display(): # Overriden
    print(f"{self.name} is a pit scout.")

scout_one = new Scout("John", "strategy")
scout_two = new Scout("Nhoj", "business")
