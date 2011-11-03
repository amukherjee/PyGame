class Tank(object):

  def __init__(self, name):
    
    self.name = name
    self.alive  = True
    self.ammo = 5
    self.armor = 100

  def __str__(self):

    if self.alive:
      return "%s (%i armor, %i shells)" % (self.name, self.armor, self.ammo)
    else
      return "%s (DEAD)" % self.name

  def fire_at(self, enemy):

    if self.ammo >=1:
      self.ammo -=1
      print self.name, "fires on ", enemy.name
    else:
      print self.name, "is out of ammo !"


