import gameObjects

print gameObjects.useOnOtherList
def doSomething():
        action = raw_input('What do you want to do?: ').upper()
        print action
        if 'LOOK' in action:
            if len(action.split()) == 1:
                roomDesc()
            else:
                print 'OwO'
                lookInit(action)
        elif 'GET' in action or 'TAKE' in action or 'PICK' in action:
            print 'Grabby'
            pickUpInit(action)
        elif 'USE' in action:
            useInit(action)
        elif 'EXIT' in action:
            print 'Alright then. Bye'
            exit()

        else:
            print 'What did you mean exactly?'
            return doSomething()

def lookInit(action):
    action = action.split()
    for thing in gameObjects.objectList:
        for word in action:
            if word in thing.name:
                return thing.lookAt()
    print 'Look at what?'
    return doSomething()


def roomDesc():
    roomDescText = ['You are stood in a cold, dark, cell. Surrounded by stone on all sides. There is little here for you '\
                   'beyond a bed and a table. ', 'A cracked jar sits atop the table. It seems lonely. ', 'A dim light pours through your window. The door has not been opened in days. ',\
                    'A small rubber ball rests in the corner betwixt the door and window. ']
    for thing in gameObjects.objectList:
        if thing not in gameObjects.envObject:
            for line in roomDescText:
                searchWords = line.upper()
                if thing.name in searchWords:
                    roomDescText.remove(line)
    print ''.join(roomDescText)
    doSomething()

def pickUpInit(action):
    action = action.split()
    for knownObj in gameObjects.objectList:
        for word in action:
            if word in knownObj.name:
                if knownObj in gameObjects.envObject and knownObj.pickup:
                    print 'You picked up the ' + knownObj.description
                    gameObjects.invObject.append(knownObj)
                    gameObjects.envObject.remove(knownObj)
                    return doSomething()
                elif knownObj.pickup == False:
                    print "You cant't pick that up"
                    return doSomething()
                else:
                    print "You're already holding that"
                    return doSomething()
    print 'Get/Pick up what?'
    return doSomething()

def useInit(action):
    action = action.split()
    envCount = 0
    invCount = 0
    objectsFound = []
    for word in action:
        for thing in gameObjects.envObject:
            if word in thing.name:
                envCount += 1
                objectsFound.append(thing)
        for thing in gameObjects.invObject:
            if word in thing.name:
                invCount += 1
                objectsFound.append(thing)
    if invCount == 1 and envCount == 1:
        return useInvOnEnv(objectsFound)
    elif invCount == 1 or invCount == 2:
        print str(objectsFound) + ' one or two inventory items'
        useInv(objectsFound)
    elif envCount == 1:
        print 'woo'
    else:
        print 'Uh, try something else'

    return doSomething()

def useInvOnEnv(objectsFound):
    if objectsFound in gameObjects.pairedItems:
        print objectsFound
    else:
        print objectsFound
        print gameObjects.pairedItems
        print "Well, that did nothing"
    doSomething()


def useInv(objectsFound):
    if len(objectsFound) == 1:
        pass