#!/usr/bin/python -tt

from tank import Tank

tanks  = { ('r': Tank( 'Rutgers') ), ('p': Tank( 'Princeton') ), ('n' : Tank( 'NJIT') ) }
alive_tanks = len(tanks)

while alive_tanks > 1 :

  print 
  for tank_name in sorted( tanks.keys()):
    print tank_name, tanks[tank_name]

  attacker = raw_input("Who fires ? ").lower()
  target = raw_input("Who gets hit ? ").lower()

  try :
    attacker_tank = tanks[attacker]
    target_tank = tanks[target]
  except KeyError, name:
    print "Tank id not found in dictionary !" ,name
    continue

  if not attacker_tank.alive or not target_tank.alive:
    print "One of the tanks in combat are already dead!"
    continue

  print 
  print "*" * 30

  attacker_tank.fires_at(tarket_tank)
  
  if not target_tank.alive:
    alive_tanks -= 1
  
  print "*" * 30

for tank in tanks.values():
  if tank.alive:
    print tank.name, "has survive the battle!"
    break

