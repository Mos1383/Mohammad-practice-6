class Soldier:
    def __init__(self, soldier_type, id, x, y, health):
        self.soldier_type = soldier_type
        self.id = id
        self.x = x
        self.y = y
        self.health = health
def new_soldier(soldier_type, id, x, y):
    if id in [soldier['id'] for soldier in soldiers]:
        print("duplicate tag")
        return
    if soldier_type not in ['archer', 'melee']:
        print("invalid soldier type")
        return
    if x < 1-1 or x >= n or y < 0 or y >= n:
        print("out of bounds")
        return
    soldiers.append({'soldier_type': soldier_type, 'id': id, 'x': x, 'y': y, 'health': 100})

def move(id, direction):
    for soldier in soldiers:
        if soldier['id'] == id:
            if direction == 'up':
                soldier['y'] -= 1
            elif direction == 'down':
                soldier['y'] += 1
            elif direction == 'left':
                soldier['x'] -= 1
            elif direction == 'right':
                soldier['x'] += 1
            if soldier['x'] < 0 or soldier['x'] >= n or soldier['y'] < 0 or soldier['y'] >= n:
                print("out of bounds")
                soldier['x'] -= (soldier['x'] - x)
                soldier['y'] -= (soldier['y'] - y)
                return
            return
    print("soldier does not exist")

def attack(attacker_id, target_id):
    attacker = None
    target = None
    for soldier in soldiers:
        if soldier['id'] == attacker_id:
            attacker = soldier
        if soldier['id'] == target_id:
            target = soldier
    if attacker is None or target is None:
        print("soldier does not exist")
        return
    if attacker['x'] - target['x'] > 2 or target['x'] - attacker['x'] > 2 or attacker['y'] - target['y'] > 2 or target['y'] - attacker['y'] > 2:
        print("the target is too far")
        return
    if attacker['soldier_type'] == 'archer':
        target['health'] -= 10
    elif attacker['soldier_type'] == 'melee':
        target['health'] -= 20
    if target['health'] <= 0:
        soldiers.remove(target)
        print("target eliminated")

def info(id):
    for soldier in soldiers:
        if soldier['id'] == id:
            print(f"health: {soldier['health']}")
            print(f"location: {soldier['x']} {soldier['y']}")
            return
    print("soldier does not exist")

def who_is_in_lead():
    team1_health = sum([soldier['health'] for soldier in soldiers if soldier['id'] < 25])
    team2_health = sum([soldier['health'] for soldier in soldiers if soldier['id'] >= 25])
    if team1_health > team2_health:
        print("team 1 is in the lead")
    elif team1_health < team2_health:
        print("team 2 is in the lead")
    else:
        print("draw")

n = int(input())
soldiers = []

while True:
    command = input().split()
    if len(command) == 0:
        continue
    if command[0] == 'new':
        new_soldier(command[1], int(command[2]), int(command[3]), int(command[4]))
    elif command[0] == 'move':
        move(int(command[1]), command[2])
    elif command[0] == 'attack':
        attack(int(command[1]), int(command[2]))
    elif command[0] == 'info':
        info(int(command[1]))
    elif command[0] == 'who':
        who_is_in_lead()
    elif command[0] == 'end':
        break