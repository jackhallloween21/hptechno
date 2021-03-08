print(  "Welcome to Jumanji, A Game For Those Who Seek To Find A Way To Leave Their World Behind.Think Once, Think Twice, Before Paying The Price. Abandon Your Fear And Enter Here. You have TWO lives. Once you lose your lives game over. You will collect points after every obstacle you overcome. Collect as many points as possible.")
player = (input("Choose you player: Smolder Bravestone, Ruby Roundhouse, Franklin Mouse Finbar, or Shelly Oberon. First name only:  "))

if player == "Smolder":
  print ("You have chosen Smolder Bravestone. Your strengths are speed, climbing, boomerang, strength, smoldering intensity, and fearlessness. Your weakness is your archnemisis Switchblade.")
  points = 0
  lives = 2
  if lives == 0:
    print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER. You collected", points," XP.")
if player == "Ruby":
  print ("You have chosen Ruby Roundhouse. Your strengths are acrobatics, karate, aikido, tai'chi, dance fighting, and nunchucks. Your weakness is venom.")
  points = 0
  lives = 2
  if lives == 0:
    print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER. You collected", points," XP.")
if player == "Franklin":
  print ("You have chosen Franklin Mouse Finbar. Your strengths are zoology, weapons valet, linguistics, and cranial assault. Your weaknesses are cake, speed, and strength.")
  points = 0
  lives = 2
  if lives == 0:
    print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER. You collected", points," XP.")
if player == "Shelly":
  print ("You have chosen Shelly Oberon. Your strengths are cartology, archeology, palaeontology, and geometry. Your weaknesses are endurance, sun, heat, and sand.")
  points = 0
  lives = 2
  if lives == 0:
    print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER. You collected", points," XP.")


import random
obstacle = random.randint (1,4) 
direction = input("Choose a direction: north, east, south, or west? ") 
if direction == "east":
  print("You are now in the swamp. Watch your surroundings.")
  import random
  obstacle = random.randint (1,3) 
if direction == "north":
  print("You are now in the desert. Watch your surroundings.")
  import random
  obstacle = random.randint (1,3)
if direction == "west":
  print("You are now in the beach. Watch your surroundings.")
  import random
  obstacle = random.randint (1,3)
if direction == "south":
  print("You are now in the rainforest. Watch your surroundings.")
  import random
  obstacle = random.randint (1,2)


while player == "Smolder" and direction == "east" and obstacle == 1:
  choice = input ("Oh no there's deadly mosquitos! Do you want to RUN or SWAT? ")
  if choice == "RUN":
    import random
    one = random.randint (1,2)
    while one == 2:
      print("Oops, you didn't run fast enough. You were stung to death by the mosquitos. You have lost one life.")
      lives = lives -1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You escaped those pesky bugs! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)

  if choice == "SWAT":
    import random
    two = random.randint (1,3)
    while two == 2:
      print("Oops, you didn't swat hard enough. You were stung to death by the mosquitos. You have lost one life.")
      lives= lives-1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You escaped those pesky bugs! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)
while player == "Smolder" and direction == "east" and obstacle == 2:
  print ("Oh no the murky water is too high!")
  choice = input("Do you want to SWIM or SMOLDER?")
  if choice == "SWIM":
    import random
    three = random.randint (1,2)
    while three ==1:
      print("Oops, you didn't swim fast enough. You drowned. You have lost one life.")
      lives = lives -1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER. You collected", points," XP.")
    else:
      print("Yay! You you swam fast enough to get to the edge! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)

  if choice == "SMOLDER":
    import random
    four = random.randint (1,4)
    while four == 1 or four == 2 or four == 3:
      print("Oops, you didn't smolder hard enough. You drowned to death. You have lost one life.")
      lives = lives-1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER. You collected", points," XP.")
    else:
      print("Yay! You smoldered that swamp hard enough it drained! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)
while player == "Smolder" and direction == "east" and obstacle == 3:
  print ("Oh no there's an alligator!")
  choice = input("Do you want to RUN or BOOMERANG?")
  if choice == "RUN":
    import random
    five = random.randint (1,2)
    while five == 1:
      print("Oops, you didn't run fast enough. You were eaten by the alligator. You have lost one life.")
      lives = lives-1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER. You collected", points," XP.")
    else:
      print("Yay! You escaped that overgrown    reptile! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)

  if choice == "BOOMERANG":
    import random
    six = random.randint (1,3)
    while six == 1:
      print("Oops, you didn't throw the boomerang quick enough. You were eaten by the alligator. You have lost one life.")
      lives = lives - 1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER. You collected", points," XP.")
    else:
      print("Yay! You escaped that overgrown reptile! +20 XP")
      points = points + 20
      if points ==points:
        break
  obstacle = random.randint (1,3)
while player == "Smolder" and direction == "north" and obstacle == 1:
  choice = input ("Oh no! Quicksand! Do you want to RUN or CLIMB? ")
  if choice == "RUN":
    import random
    one = random.randint (1,3)
    while one == 2 or one == 1:
      print("Oops, you didn't run fast enough. You were buried by the sand. You have lost one life.")
      lives = lives -1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You escaped the sand! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)

  if choice == "CLIMB":
    import random
    two = random.randint (1,2)
    while two == 2:
      print("Oops, you didn't climb hard enough. You were buried alive. You have lost one life.")
      lives= lives-1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You escaped the dreaded sand! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)
while player == "Smolder" and direction == "north" and obstacle == 2:
  choice = input ("Uh oh. Bounty hunters! The probably work for that slimy Switchblade. Do you want to RUN, BOOMERANG, or FIGHT? ")
  if choice == "RUN":
    import random
    one = random.randint (1,2)
    while one == 2:
      print("Oops, you didn't run fast enough. You were ran over by their wrangler. You have lost one life.")
      lives = lives -1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You escaped those stinky hunters! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)

  if choice == "BOOMERANG":
    import random
    two = random.randint (1,3)
    while two == 2:
      print("Oops, you didn't throw the boomerang quick enough. You were shot. You have lost one life.")
      lives= lives-1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You escaped those no-good scoundrels! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)
  
  if choice == "FIGHT":
    import random
    two = random.randint (1,3)
    while two == 1:
      print("Oops, you are not Bruce Lee. You were pummeled to death. You have lost one life.")
      lives= lives-1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You escaped those no-good scoundrels! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)
while player == "Smolder" and direction == "north" and obstacle == 3:
  choice = input ("Uh oh. Scorpions! Beware of their stingers. Do you want to RUN or SMOLDER? ")
  if choice == "RUN":
    import random
    one = random.randint (1,2)
    while one == 2:
      print("Oops, you didn't run fast enough. You were stung to death. You have lost one life.")
      lives = lives -1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You escaped those pesky bugs! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)

  if choice == "SMOLDER":
    import random
    two = random.randint (1,3)
    while two == 2 or two == 1:
      print("Oops, you didn't smolder hard enough. You were stung. Venom slowly coursed through your veins until you died. You have lost one life.")
      lives= lives-1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You smoldered the pants off those scorpions! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)
while player == "Smolder" and direction == "west" and obstacle == 1:
  choice = input ("Uh oh. There's a tsunami! Do you want to RUN or CLIMB? ")
  if choice == "RUN":
    import random
    one = random.randint (1,2)
    while one == 2:
      print("Oops, you didn't run fast enough. You drowned. You have lost one life.")
      lives = lives -1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You escaped that salty water! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)

  if choice == "CLIMB":
    import random
    two = random.randint (1,2)
    while two == 2:
      print("Oops, you didn't climb high enough. You were shot. You have lost one life.")
      lives= lives-1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You escaped the water! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)
while player == "Smolder" and direction == "west" and obstacle == 2:
  choice = input ("Ugh. Jellyfish?! Do you want to RUN, KICK, or SMOLDER? ")
  if choice == "RUN":
    import random
    one = random.randint (1,2)
    while one == 2:
      print("Oops, you didn't run fast enough. You were stung by the tentacles. You have lost one life.")
      lives = lives -1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You escaped those bottom feeders! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)

  if choice == "KICK":
    import random
    two = random.randint (1,3)
    while two == 2:
      print("Oops, you didn't kick hard enough. You were shot. You have lost one life.")
      lives= lives-1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You escaped those overgrown fish! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)
  if choice == "SMOLDER":
    import random
    two = random.randint (1,3)
    while two == 2 or two == 1:
      print("Oops, you didn't smolder good enough. You were stung. You have lost one life.")
      lives= lives-1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You escaped those overgrown fish! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)
while player == "Smolder" and direction == "west" and obstacle == 3:
  choice = input ("Uh oh. The bartender sticked your punch! He probably works for Switchblade! Do you want to RUN or FIGHT? ")
  if choice == "RUN":
    import random
    one = random.randint (1,2)
    while one == 2:
      print("Rats! You didn't run fast enough. You passed out and were turned in to Switchblade. You have lost one life.")
      lives = lives -1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You escaped that sneaky fox! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)

  if choice == "FIGHT":
    import random
    two = random.randint (1,2)
    while two == 2:
      print("Oops, you were to delirious to put up a fight. You were kidnapped. You have lost one life.")
      lives= lives-1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You escaped that punch-spiking bum! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)
while player == "Smolder" and direction == "south" and obstacle == 1:
  choice = input ("Uh oh. SNAKES! Do you want to RUN or CLIMB? ")
  if choice == "RUN":
    import random
    one = random.randint (1,2)
    while one == 2:
      print("Oops, you didn't run fast enough. You were bitten. You have lost one life.")
      lives = lives -1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You escaped that serpent! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)

  if choice == "CLIMB":
    import random
    two = random.randint (1,2)
    while two == 2:
      print("Oops, you didn't climb high enough. You were bitten. You have lost one life.")
      lives= lives-1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You escaped the slithering slimeball! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)
while player == "Smolder" and direction == "south" and obstacle == 2:
  choice = input ("Uh oh. Mandrill monkeys are heading this way! One bite and they'll impale you. Do you want to RUN, BOOMERANG, or CLIMB? ")
  if choice == "RUN":
    import random
    one = random.randint (1,2)
    while one == 2:
      print("Oops, you didn't run fast enough. You were bitten. You have lost one life.")
      lives = lives -1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You escaped those dumb monkeys! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)

  if choice == "CLIMB":
    import random
    two = random.randint (1,2)
    while two == 2:
      print("Oops, you didn't climb high enough. You were dragged and bitten. You have lost one life.")
      lives= lives-1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You escaped the hairy beast! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)
  if choice == "BOOMERANG":
    import random
    two = random.randint (1,2)
    while two == 2:
      print("Oops, your boomerang was ineffective and you were bitten. You have lost one life.")
      lives= lives-1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You escaped the hairy beast! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)


while player == "Ruby" and direction == "east" and obstacle == 1:
  choice = input ("Oh no there's deadly mosquitos! Do you want to RUN or KARATE? ")
  if choice == "RUN":
    import random
    one = random.randint (1,2)
    while one == 2:
      print("Oops, you didn't run fast enough. You were stung to death by the mosquitos. You have lost one life.")
      lives = lives -1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You escaped those pesky bugs! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)

  if choice == "KARATE":
    import random
    two = random.randint (1,3)
    while two == 2:
      print("Oops, Mr. Miyagi didn't train you well enough. You were stung to death by the mosquitos. You have lost one life.")
      lives= lives-1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You escaped those pesky bugs! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)
while player == "Ruby" and direction == "east" and obstacle == 2:
  print ("Oh no the murky water is too high!")
  choice = input("Do you want to SWIM or DANCE?")
  if choice == "SWIM":
    import random
    three = random.randint (1,2)
    while three ==1:
      print("Oops, you didn't swim fast enough. You drowned. You have lost one life.")
      lives = lives -1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER. You collected", points," XP.")
    else:
      print("Yay! You you swam fast enough to get to the edge! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)

  if choice == "DANCE":
    import random
    four = random.randint (1,4)
    while four == 1 or four == 2 or four == 3:
      print("Uh oh, Dance Revolution doesn't work in real life situations. You drowned to death. You have lost one life.")
      lives = lives-1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER. You collected", points," XP.")
    else:
      print("Yay! You danced so hard it drained! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)
while player == "Ruby" and direction == "east" and obstacle == 3:
  print ("Oh no there's an alligator!")
  choice = input("Do you want to RUN or NUNCHUCKS?")
  if choice == "RUN":
    import random
    five = random.randint (1,2)
    while five == 1:
      print("Oops, you didn't run fast enough. You were eaten by the alligator. You have lost one life.")
      lives = lives-1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER. You collected", points," XP.")
    else:
      print("Yay! You escaped that overgrown    reptile! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)

  if choice == "NUNCHUCKS":
    import random
    six = random.randint (1,3)
    while six == 1:
      print("Oops, you dropped the nunchucks in the filthy water. You were eaten by the alligator. You have lost one life.")
      lives = lives - 1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER. You collected", points," XP.")
    else:
      print("Yay! You escaped that overgrown reptile! +20 XP")
      points = points + 20
      if points ==points:
        break
  obstacle = random.randint (1,3)
while player == "Ruby" and direction == "north" and obstacle == 1:
  choice = input ("Oh no! Quicksand! Do you want to RUN or CLIMB? ")
  if choice == "RUN":
    import random
    one = random.randint (1,3)
    while one == 2 or one == 1:
      print("Oops, you didn't run fast enough. You were buried by the sand. You have lost one life.")
      lives = lives -1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You escaped the sand! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)

  if choice == "CLIMB":
    import random
    two = random.randint (1,2)
    while two == 2:
      print("Oops, you didn't climb hard enough. You were buried alive. You have lost one life.")
      lives= lives-1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You escaped the dreaded sand! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)
while player == "Ruby" and direction == "north" and obstacle == 2:
  choice = input ("Uh oh. Bounty hunters! The probably work for that slimy Switchblade. Do you want to RUN, NUNCHUCKS, or TAICHI? ")
  if choice == "RUN":
    import random
    one = random.randint (1,2)
    while one == 2:
      print("Oops, you didn't run fast enough. You were ran over by their wrangler. You have lost one life.")
      lives = lives -1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You escaped those stinky hunters! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)

  if choice == "NUNCHUCKS":
    import random
    two = random.randint (1,3)
    while two == 2:
      print("Oops, you didn't swing the nunchucks quick enough. You were shot. You have lost one life.")
      lives= lives-1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You escaped those no-good scoundrels! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)
  
  if choice == "TAICHI":
    import random
    two = random.randint (1,3)
    while two == 1:
      print("Oops, you are not Bruce Lee. You were pummeled to death. You have lost one life.")
      lives= lives-1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You escaped those no-good scoundrels! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)
while player == "Ruby" and direction == "north" and obstacle == 3:
  choice = input ("Uh oh. Scorpions! Beware of their stingers. Do you want to RUN or ACROBATICS? ")
  if choice == "RUN":
    import random
    one = random.randint (1,2)
    while one == 2:
      print("Oops, you didn't run fast enough. You were stung to death. You have lost one life.")
      lives = lives -1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You escaped those pesky bugs! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)

  if choice == "ACROBATICS":
    import random
    two = random.randint (1,3)
    while two == 2 or two == 1:
      print("Oops, your flexibility didn't impress the scorpions. You were stung. Venom slowly coursed through your veins until you died. You have lost one life.")
      lives= lives-1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You flipped the pants off those scorpions! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)
while player == "Ruby" and direction == "west" and obstacle == 1:
  choice = input ("Uh oh. There's a tsunami! Do you want to RUN or CLIMB? ")
  if choice == "RUN":
    import random
    one = random.randint (1,2)
    while one == 2:
      print("Oops, you didn't run fast enough. You drowned. You have lost one life.")
      lives = lives -1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You escaped that salty water! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)

  if choice == "CLIMB":
    import random
    two = random.randint (1,2)
    while two == 2:
      print("Oops, you didn't climb high enough. You were shot. You have lost one life.")
      lives= lives-1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You escaped the water! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)
while player == "Ruby" and direction == "west" and obstacle == 2:
  choice = input ("Ugh. Jellyfish?! Do you want to RUN, AIKIDO, or DANCE? ")
  if choice == "RUN":
    import random
    one = random.randint (1,2)
    while one == 2:
      print("Oops, you didn't run fast enough. You were stung by the tentacles. You have lost one life.")
      lives = lives -1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You escaped those bottom feeders! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)

  if choice == "AIKIDO":
    import random
    two = random.randint (1,3)
    while two == 2:
      print("Oops, you didn't kick hard enough. You were shot. You have lost one life.")
      lives= lives-1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You escaped those overgrown fish! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)
  if choice == "DANCE":
    import random
    two = random.randint (1,3)
    while two == 2 or two == 1:
      print("Oops, you didn't dance good enough. You were stung. You have lost one life.")
      lives= lives-1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You escaped those overgrown fish! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)
while player == "Ruby" and direction == "west" and obstacle == 3:
  choice = input ("Uh oh. The bartender sticked your punch! He probably works for Switchblade! Do you want to RUN or KARATE? ")
  if choice == "RUN":
    import random
    one = random.randint (1,2)
    while one == 2:
      print("Rats! You didn't run fast enough. You passed out and were turned in to Switchblade. You have lost one life.")
      lives = lives -1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You escaped that sneaky fox! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)

  if choice == "KARATE":
    import random
    two = random.randint (1,2)
    while two == 2:
      print("Oops, you were to delirious to put up a fight. You were kidnapped. You have lost one life.")
      lives= lives-1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You escaped that punch-spiking bum! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)
while player == "Ruby" and direction == "south" and obstacle == 1:
  choice = input ("Uh oh. SNAKES! Do you want to RUN or CLIMB? ")
  if choice == "RUN":
    import random
    one = random.randint (1,2)
    while one == 2:
      print("Oops, you didn't run fast enough. You were bitten. You have lost one life.")
      lives = lives -1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You escaped that serpent! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)

  if choice == "CLIMB":
    import random
    two = random.randint (1,2)
    while two == 2:
      print("Oops, you didn't climb high enough. You were bitten. You have lost one life.")
      lives= lives-1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You escaped the slithering slimeball! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)
while player == "Ruby" and direction == "south" and obstacle == 2:
  choice = input ("Uh oh. Mandrill monkeys are heading this way! One bite and they'll impale you. Do you want to RUN, NUNCHUCKS, or CLIMB? ")
  if choice == "RUN":
    import random
    one = random.randint (1,2)
    while one == 2:
      print("Oops, you didn't run fast enough. You were bitten. You have lost one life.")
      lives = lives -1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You escaped those dumb monkeys! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)

  if choice == "CLIMB":
    import random
    two = random.randint (1,2)
    while two == 2:
      print("Oops, you didn't climb high enough. You were dragged and bitten. You have lost one life.")
      lives= lives-1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You escaped the hairy beast! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)
  if choice == "NUNCHUCKS":
    import random
    two = random.randint (1,2)
    while two == 2:
      print("Oops, your nunchucks were ineffective and you were bitten. You have lost one life.")
      lives= lives-1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You escaped the hairy beast! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)


while player == "Franklin" and direction == "east" and obstacle == 1:
  choice = input ("Oh no there's deadly mosquitos! Do you want to RUN or REASON? ")
  if choice == "RUN":
    import random
    one = random.randint (1,2)
    while one == 2:
      print("Oops, you didn't run fast enough. You were stung to death by the mosquitos. You have lost one life.")
      lives = lives -1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You escaped those pesky bugs! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)

  if choice == "REASON":
    import random
    two = random.randint (1,3)
    while two == 2:
      print("Oops, you couldn't come to an agreement. You were stung to death by the mosquitos. You have lost one life.")
      lives= lives-1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You escaped those pesky bugs! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)
while player == "Franklin" and direction == "east" and obstacle == 2:
  print ("Oh no the murky water is too high!")
  choice = input("Do you want to SWIM or SPEAK?")
  if choice == "SWIM":
    import random
    three = random.randint (1,4)
    while three ==1 or three==2 or three == 3:
      print("Oops, you didn't swim fast enough. You drowned. You have lost one life.")
      lives = lives -1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER. You collected", points," XP.")
    else:
      print("Yay! You you swam fast enough to get to the edge! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)

  if choice == "SPEAK":
    import random
    four = random.randint (1,4)
    while four == 1 or four == 2 or four == 3:
      print("Oops, you didn't convince the swamp. You drowned to death. You have lost one life.")
      lives = lives-1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER. You collected", points," XP.")
    else:
      print("Yay! You and the swamp came to a mutual agreement! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)
while player == "Franklin" and direction == "east" and obstacle == 3:
  print ("Oh no there's an alligator!")
  choice = input("Do you want to RUN or CAKE?")
  if choice == "RUN":
    import random
    five = random.randint (1,2)
    while five == 1:
      print("Oops, you didn't run fast enough. You were eaten by the alligator. You have lost one life.")
      lives = lives-1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER. You collected", points," XP.")
    else:
      print("Yay! You escaped that overgrown    reptile! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)

  if choice == "CAKE":
    import random
    six = random.randint (1,3)
    while six == 1:
      print("Oops, you ate the cake before you gave it to the alligator. You were eaten by the alligator. You have lost one life.")
      lives = lives - 1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER. You collected", points," XP.")
    else:
      print("Yay! You must've been Patty Cake in your past life! You escaped that overgrown reptile! +20 XP")
      points = points + 20
      if points ==points:
        break
  obstacle = random.randint (1,3)
while player == "Franklin" and direction == "north" and obstacle == 1:
  choice = input ("Oh no! Quicksand! Do you want to RUN or CLIMB? ")
  if choice == "RUN":
    import random
    one = random.randint (1,3)
    while one == 2 or one == 1:
      print("Oops, you didn't run fast enough. You were buried by the sand. You have lost one life.")
      lives = lives -1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You escaped the sand! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)

  if choice == "CLIMB":
    import random
    two = random.randint (1,3)
    while two == 2 or two == 1:
      print("Oops, you didn't climb hard enough. You were buried alive. You have lost one life.")
      lives= lives-1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You escaped the dreaded sand! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)
while player == "Franklin" and direction == "north" and obstacle == 2:
  choice = input ("Uh oh. Bounty hunters! The probably work for that slimy Switchblade. Do you want to RUN, CRANIAL, or FIGHT? ")
  if choice == "RUN":
    import random
    one = random.randint (1,3)
    while one == 2 or one==1:
      print("Oops, you didn't run fast enough. You were ran over by their wrangler. You have lost one life.")
      lives = lives -1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You escaped those stinky hunters! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)

  if choice == "CRANIAL":
    import random
    two = random.randint (1,3)
    while two == 2 or two== 1:
      print("Oops, you didn't get close enough to attack. You were shot. You have lost one life.")
      lives= lives-1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You escaped those no-good scoundrels! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)
  
  if choice == "FIGHT":
    import random
    two = random.randint (1,3)
    while two == 1 or two == 2:
      print("Oops, you are not Bruce Lee. You were pummeled to death. You have lost one life.")
      lives= lives-1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You escaped those no-good scoundrels! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)
while player == "Franklin" and direction == "north" and obstacle == 3:
  choice = input ("Uh oh. Scorpions! Beware of their stingers. Do you want to RUN or ZOOLOGY? ")
  if choice == "RUN":
    import random
    one = random.randint (1,2)
    while one == 2:
      print("Oops, you didn't run fast enough. You were stung to death. You have lost one life.")
      lives = lives -1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You escaped those pesky bugs! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)

  if choice == "ZOOLOGY":
    import random
    two = random.randint (1,3)
    while two == 2 or two == 1:
      print("Oops, you couldn't remember enough about the scorpions. You were stung. Venom slowly coursed through your veins until you died. You have lost one life.")
      lives= lives-1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! Your brains payed off. +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)
while player == "Franklin" and direction == "west" and obstacle == 1:
  choice = input ("Uh oh. There's a tsunami! Do you want to RUN or CLIMB? ")
  if choice == "RUN":
    import random
    one = random.randint (1,2)
    while one == 2:
      print("Oops, you didn't run fast enough. You drowned. You have lost one life.")
      lives = lives -1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You escaped that salty water! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)

  if choice == "CLIMB":
    import random
    two = random.randint (1,2)
    while two == 2:
      print("Oops, you didn't climb high enough. You were shot. You have lost one life.")
      lives= lives-1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You escaped the water! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)
while player == "Franklin" and direction == "west" and obstacle == 2:
  choice = input ("Ugh. Jellyfish?! Do you want to RUN, KICK, or CAKE? ")
  if choice == "RUN":
    import random
    one = random.randint (1,2)
    while one == 2:
      print("Oops, you didn't run fast enough. You were stung by the tentacles. You have lost one life.")
      lives = lives -1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You escaped those bottom feeders! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)

  if choice == "KICK":
    import random
    two = random.randint (1,3)
    while two == 2:
      print("Oops, you didn't kick hard enough. You were shot. You have lost one life.")
      lives= lives-1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You escaped those overgrown fish! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)
  if choice == "CAKE":
    import random
    two = random.randint (1,3)
    while two == 2 or two == 1:
      print("Oops, you didn't give them enough cake. You were stung. You have lost one life.")
      lives= lives-1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You escaped those overgrown fish! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)
while player == "Franklin" and direction == "west" and obstacle == 3:
  choice = input ("Uh oh. The bartender sticked your punch! He probably works for Switchblade! Do you want to RUN or FIGHT? ")
  if choice == "RUN":
    import random
    one = random.randint (1,2)
    while one == 2:
      print("Rats! You didn't run fast enough. You passed out and were turned in to Switchblade. You have lost one life.")
      lives = lives -1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You escaped that sneaky fox! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)

  if choice == "FIGHT":
    import random
    two = random.randint (1,2)
    while two == 2:
      print("Oops, you were to delirious to put up a fight. You were kidnapped. You have lost one life.")
      lives= lives-1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You escaped that punch-spiking bum! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)
while player == "Franklin" and direction == "south" and obstacle == 1:
  choice = input ("Uh oh. SNAKES! Do you want to RUN or CLIMB? ")
  if choice == "RUN":
    import random
    one = random.randint (1,2)
    while one == 2:
      print("Oops, you didn't run fast enough. You were bitten. You have lost one life.")
      lives = lives -1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You escaped that serpent! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)

  if choice == "CLIMB":
    import random
    two = random.randint (1,2)
    while two == 2:
      print("Oops, you didn't climb high enough. You were bitten. You have lost one life.")
      lives= lives-1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You escaped the slithering slimeball! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)
while player == "Franklin" and direction == "south" and obstacle == 2:
  choice = input ("Uh oh. Mandrill monkeys are heading this way! One bite and they'll impale you. Do you want to RUN, CRANIAL, or CLIMB? ")
  if choice == "RUN":
    import random
    one = random.randint (1,2)
    while one == 2:
      print("Oops, you didn't run fast enough. You were bitten. You have lost one life.")
      lives = lives -1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You escaped those dumb monkeys! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)

  if choice == "CLIMB":
    import random
    two = random.randint (1,2)
    while two == 2:
      print("Oops, you didn't climb high enough. You were dragged and bitten. You have lost one life.")
      lives= lives-1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You escaped the hairy beast! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)
  if choice == "CRANIAL":
    import random
    two = random.randint (1,2)
    while two == 2:
      print("Oops, your attacks were ineffective and you were bitten. You have lost one life.")
      lives= lives-1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You escaped the hairy beast! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)


while player == "Shelly" and direction == "east" and obstacle == 1:
  choice = input ("Oh no there's deadly mosquitos! Do you want to RUN or PALAEONTOLOGY? ")
  if choice == "RUN":
    import random
    one = random.randint (1,2)
    while one == 2:
      print("Oops, you didn't run fast enough. You were stung to death by the mosquitos. You have lost one life.")
      lives = lives -1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You escaped those pesky bugs! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)

  if choice == "PALAEONTOLOGY":
    import random
    two = random.randint (1,3)
    while two == 2:
      print("Oops, your knowledge of fossils did not help you. You were stung to death by the mosquitos. You have lost one life.")
      lives= lives-1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You escaped those pesky bugs! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)
while player == "Shelly" and direction == "east" and obstacle == 2:
  print ("Oh no the murky water is too high!")
  choice = input("Do you want to SWIM or PALAEONTOLOGY?")
  if choice == "SWIM":
    import random
    three = random.randint (1,4)
    while three ==1 or three==2 or three == 3:
      print("Oops, you didn't swim fast enough. You drowned. You have lost one life.")
      lives = lives -1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER. You collected", points," XP.")
    else:
      print("Yay! You you swam fast enough to get to the edge! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)

  if choice == "PALAEONTOLOGY":
    import random
    four = random.randint (1,4)
    while four == 1 or four == 2 or four == 3:
      print("Oops, the fossils couldn't save you. You drowned to death. You have lost one life.")
      lives = lives-1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER. You collected", points," XP.")
    else:
      print("Yay! You found a stable ribcage to ride until the end of the stream! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)
while player == "Shelly" and direction == "east" and obstacle == 3:
  print ("Oh no there's an alligator!")
  choice = input("Do you want to RUN or SWIM?")
  if choice == "RUN":
    import random
    five = random.randint (1,3)
    while five > 1:
      print("Oops, you didn't run fast enough. You were eaten by the alligator. You have lost one life.")
      lives = lives-1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER. You collected", points," XP.")
    else:
      print("Yay! You escaped that overgrown    reptile! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)

  if choice == "RUN":
    import random
    six = random.randint (1,3)
    while six > 1:
      print("Oops, the alligator ate you before you got a chance. You have lost one life.")
      lives = lives - 1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER. You collected", points," XP.")
    else:
      print("Yay! You must've been Patty Cake in your past life! You escaped that overgrown reptile! +20 XP")
      points = points + 20
      if points ==points:
        break
  obstacle = random.randint (1,3)
while player == "Shelly" and direction == "north" and obstacle == 1:
  choice = input ("Oh no! Quicksand! Do you want to RUN or CLIMB? ")
  if choice == "RUN":
    import random
    one = random.randint (1,3)
    while one == 2 or one == 1:
      print("Oops, you didn't run fast enough. You were buried by the sand. You have lost one life.")
      lives = lives -1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You escaped the sand! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)

  if choice == "CLIMB":
    import random
    two = random.randint (1,3)
    while two == 2 or two == 1:
      print("Oops, you didn't climb hard enough. You were buried alive. You have lost one life.")
      lives= lives-1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You escaped the dreaded sand! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)
while player == "Shelly" and direction == "north" and obstacle == 2:
  choice = input ("Uh oh. Bounty hunters! The probably work for that slimy Switchblade. Do you want to RUN, GEOMETRY, or FIGHT? ")
  if choice == "RUN":
    import random
    one = random.randint (1,3)
    while one == 2 or one==1:
      print("Oops, you didn't run fast enough. You were ran over by their wrangler. You have lost one life.")
      lives = lives -1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You escaped those stinky hunters! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)

  if choice == "GEOMETRY":
    import random
    two = random.randint (1,3)
    while two == 2 or two== 1:
      print("Oops, you didn't finish your math problems in time. No gold star for you. You were shot. You have lost one life.")
      lives= lives-1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You dodged those bullets and escaped those no-good scoundrels! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)
  
  if choice == "FIGHT":
    import random
    two = random.randint (1,3)
    while two == 1 or two == 2:
      print("Oops, you are not Bruce Lee. You were pummeled to death. You have lost one life.")
      lives= lives-1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You escaped those no-good scoundrels! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)
while player == "Shelly" and direction == "north" and obstacle == 3:
  choice = input ("Uh oh. Scorpions! Beware of their stingers. Do you want to RUN or ZOOLOGY? ")
  if choice == "RUN":
    import random
    one = random.randint (1,2)
    while one == 2:
      print("Oops, you didn't run fast enough. You were stung to death. You have lost one life.")
      lives = lives -1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You escaped those pesky bugs! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)

  if choice == "ZOOLOGY":
    import random
    two = random.randint (1,3)
    while two == 2 or two == 1:
      print("Oops, you couldn't remember enough about the scorpions. You were stung. Venom slowly coursed through your veins until you died. You have lost one life.")
      lives= lives-1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! Your brains payed off. +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)
while player == "Shelly" and direction == "west" and obstacle == 1:
  choice = input ("Uh oh. There's a tsunami! Do you want to RUN or CLIMB? ")
  if choice == "RUN":
    import random
    one = random.randint (1,2)
    while one == 2:
      print("Oops, you didn't run fast enough. You drowned. You have lost one life.")
      lives = lives -1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You escaped that salty water! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)

  if choice == "CLIMB":
    import random
    two = random.randint (1,2)
    while two == 2:
      print("Oops, you didn't climb high enough. You were shot. You have lost one life.")
      lives= lives-1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You escaped the water! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)
while player == "Shelly" and direction == "west" and obstacle == 2:
  choice = input ("Ugh. Jellyfish?! Do you want to RUN, KICK, or CAKE? ")
  if choice == "RUN":
    import random
    one = random.randint (1,2)
    while one == 2:
      print("Oops, you didn't run fast enough. You were stung by the tentacles. You have lost one life.")
      lives = lives -1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You escaped those bottom feeders! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)

  if choice == "KICK":
    import random
    two = random.randint (1,3)
    while two == 2:
      print("Oops, you didn't kick hard enough. You were shot. You have lost one life.")
      lives= lives-1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You escaped those overgrown fish! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)
  if choice == "CAKE":
    import random
    two = random.randint (1,3)
    while two == 2 or two == 1:
      print("Oops, you didn't give them enough cake. You were stung. You have lost one life.")
      lives= lives-1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You escaped those overgrown fish! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)
while player == "Shelly" and direction == "west" and obstacle == 3:
  choice = input ("Uh oh. The bartender sticked your punch! He probably works for Switchblade! Do you want to RUN or FIGHT? ")
  if choice == "RUN":
    import random
    one = random.randint (1,2)
    while one == 2:
      print("Rats! You didn't run fast enough. You passed out and were turned in to Switchblade. You have lost one life.")
      lives = lives -1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You escaped that sneaky fox! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)

  if choice == "FIGHT":
    import random
    two = random.randint (1,2)
    while two == 2:
      print("Oops, you were to delirious to put up a fight. You were kidnapped. You have lost one life.")
      lives= lives-1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You escaped that punch-spiking bum! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)
while player == "Shelly" and direction == "south" and obstacle == 1:
  choice = input ("Uh oh. SNAKES! Do you want to RUN or CLIMB? ")
  if choice == "RUN":
    import random
    one = random.randint (1,2)
    while one == 2:
      print("Oops, you didn't run fast enough. You were bitten. You have lost one life.")
      lives = lives -1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You escaped that serpent! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)

  if choice == "CLIMB":
    import random
    two = random.randint (1,2)
    while two == 2:
      print("Oops, you didn't climb high enough. You were bitten. You have lost one life.")
      lives= lives-1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You escaped the slithering slimeball! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)
while player == "Shelly" and direction == "south" and obstacle == 2:
  choice = input ("Uh oh. Mandrill monkeys are heading this way! One bite and they'll impale you. Do you want to RUN, CARTOLOGY, or CLIMB? ")
  if choice == "RUN":
    import random
    one = random.randint (1,2)
    while one == 2:
      print("Oops, you didn't run fast enough. You were bitten. You have lost one life.")
      lives = lives -1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You escaped those dumb monkeys! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)

  if choice == "CLIMB":
    import random
    two = random.randint (1,2)
    while two == 2:
      print("Oops, you didn't climb high enough. You were dragged and bitten. You have lost one life.")
      lives= lives-1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You escaped the hairy beast! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)
  if choice == "CARTOLOGY":
    import random
    two = random.randint (1,2)
    while two == 2:
      print("Oops, your attacks were ineffective and you were bitten. You have lost one life.")
      lives= lives-1
      break
      if lives == 0:
        print("YOU HAVE LOST ALL OF YOUR LIVES. GAME OVER")
        print("You collected", points," XP.")
    else:
      print("Yay! You escaped the hairy beast! +20 XP")
      points = points + 20
      if points ==points:
        break
    obstacle = random.randint (1,3)







