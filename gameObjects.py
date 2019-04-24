import gameRun
invObject = []
objectList = []
envObject = []
useSelfList = []
useOnOtherList = []

class roomObject:
    def __init__(self, name, description, pickup, useSelf):
        self.name = name
        self.description = description
        self.pickup = pickup
        if useSelf:
            useSelfList.append(self)
        objectList.append(self)
        envObject.append(self)

    def lookAt(self):
        if self in envObject:
            print "It's a " + self.description
        else:
            print "It's a " + self.description + ". You're holding it"
        gameRun.doSomething()


bed = roomObject('BED', 'filthy bed', False, True)
window = roomObject('WINDOW', 'barred window', False, True)
door = roomObject('DOOR', 'locked door', False, True)
jar = roomObject('JAR', 'cracked jar', True, False)
ball = roomObject('BALL', 'rubber ball', True, False)
table = roomObject('TABLE', 'slightly burnt square table.', False, False)

pairedItems = []

def pairedObjects(first, second, locationFirst, locationSecond):
    #if first.location and second.location == true, return result of using objects correctly
    pair = [{first:locationFirst}, {second:locationSecond}]
    pairedItems.append(pair)
    print pairedItems

pairedObjects(bed, jar, 'env', 'inv')


#envUsePairsList = [[jar, bed]]
#invUsePairsList = [[jar, ball]]
