import random
import time

def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

names = ["fish", "quickdraw", "Leaf", "Rae", "AAAAAAAAAA", "Air"]
disasters = ["Meteor Shower", "Tsunami", "Laser Beams", "Hail", "Lightning Storm", "Tornado", "Nyan Cat", "Volcano", "Shoop Da Woop", "Earthquake", "Tetris Fall", "Bat Country", "Black Hole", "Geyser"]
maps = ["San fransisco", "Haunted house", "Carrier", "Abandoned factory", "Skyline", "Ruins"]
players = [["quickdraw3243", 255,255,0], ["UniKing", 255,165,0], ["AAAAAAAAA", 210,180,140], ["Rae", 255,165,0], ["Fish", 125, 162, 126], ["Leaf", 255,165,0], ["Air", 125, 162, 126]]
messages = ["Mouth shut", "Close your oral cavity", "Cease the air virations originating from your oral vocal", "Mouth unopen", "Shut mouth", "Waiting for the day Avery becomes sentient", "AVERY \n GET OVER HERE \n LOOK AT THESE PANTS", "Avery you should purchase this", "AVERY BUY THIS"]
while True:
    mapa = maps[random.randint(0,len(maps) - 1)]
    name = names[random.randint(0,len(names) - 1)]
    name2 = names[random.randint(0,len(names) - 1)]
    disaster = disasters[random.randint(0,len(disasters) - 1)]
    deaths = [f"{name} has died to {disaster}!", f"{name} has died to my {disaster}", f"{name} has failed to kill me in time!", f"{name} was killed by the first disaster! \n Which was {disaster}!", f"{name} was killed by {name2}'s {disaster}!", f"{name} has missed their {disaster}!", f"{name} is master on {mapa}!", f"{name}'s {disaster} has killed no one!", f"{name} has failed to kill anyone!"]
    death = deaths[random.randint(0,len(deaths))]
    player = players[random.randint(0,len(players) - 1)]
    message = messages[random.randint(0,len(messages) - 1)]
    print(colored(255,255,0, '[Avery]:') + death)
    time.sleep(random.randint(1,3))
    for fsjhjsldfgsg in range(random.randint(1,3)):
        player = players[random.randint(0,len(players) - 1)]
        message = messages[random.randint(0,len(messages) - 1)]
        print(colored(player[1],player[2],player[3], f"[{player[0]}]:") + message)
        time.sleep(random.randint(1,3))

