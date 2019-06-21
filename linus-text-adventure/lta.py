global can_lick_squirt
can_lick_squirt = True
global need_kevin
need_kevin = True
global need_whitney
need_whitney = True
global whitney_in_living_room
whitney_in_living_room = False
global cid_can_attack
cid_can_attack = True
global current_room


def intro():
    print '''
\t\tLinus: A Text Adventure

You awake from a luxurious nap. You feel refreshed. Except, there's
some noise. It's your stomach. You have a grumbly belly and it's probably
what woke you up.
To help you along your way you can type 'help' at any time for a list of
actions you can take.
Let's go find some food!
'''


def help():
    print '''
Commands:
\tlook
\tlick
\tgo <destination> where <destination> is the name of a room
\tmeow
\tpurr
'''


def default_lick():
    print "lick... lick..."


def default_meow():
    print "meow... nobody cares."


def default_purr():
    print "I don't feel like it. Too hungry."


def default_go(room):
    global current_room
    look, start = room()
    current_room = start
    look()


def go_no_look(room):
    global current_room
    _, start = room()
    current_room = start


def cannot_go():
    print "I can't go there."


def get_command(look,
                go,
                lick=default_lick,
                meow=default_meow,
                purr=default_purr):
        command = raw_input('> ')
        if command == 'help':
            help()
        elif command == 'look':
            look()
        elif 'go ' in command:
            parts = command.split(' ')
            command = parts.pop(0)
            where = ' '.join(parts)
            if command == 'go' and len(where):
                go(where)
            else:
                print "Usage of go: go <location>"
        elif command == 'meow':
            meow()
        elif command == 'purr':
            purr()
        elif command == 'lick':
            lick()
        else:
            print "No."


def bedroom():
    def look():
        print "Your queen size bed, covered in your fur, is calling to you",
        print "to come nap some more. Alas,",
        print "you have a grumbling in your belly."
        if can_lick_squirt:
            print "Your sister, Squirt, is sleeping on your bed."
        print "in front of you is the door to the hallway"

    def go(room):
        if room != 'hallway':
            cannot_go()
        else:
            default_go(hallway)

    def lick():
        global can_lick_squirt
        global cid_can_attack
        if can_lick_squirt:
            can_lick_squirt = False
            cid_can_attack = False
            print '''
You decide to give Squirt a bath.
After about three seconds of nice bath time she gets angry.
You keep licking.  Squirt finally takes a swing at your face.
You dodge it and see she has gotten up to take out her frustration on Cid in
the living room.
You hear a cat fight ensue.
'''
        else:
            default_lick()

    def start():
        get_command(look, go, lick)

    return (look, start)


def hallway():
    def look():
        print '''
You see the bathroom, the bedroom, and the living room.
Where would the food be?
'''

    def go(room):
        if room == 'bedroom':
            default_go(bedroom)
        elif room == 'bathroom':
            default_go(bathroom)
        elif room == 'living room':
            default_go(living_room)
        else:
            cannot_go()

    def start():
        get_command(look, go)

    return (look, start)


def bathroom():
    def look():
        print '''
You see a bunch of things with water.  You hate getting wet.
Better watch out.  Squirt says you can die if your ears get wet.
'''

    def go(room):
        if room == 'hallway':
            default_go(hallway)
        else:
            cannot_go()

    def meow():
        global whitney_in_living_room
        if not whitney_in_living_room:
            whitney_in_living_room = True
            print '''
The accoustics of the bathroom are perfect.
You can't help but think of your meow as amazing.
Apparently one of your people, Whitney, thinks so too!
You hear her door creak open as she leaves her bedroom.
She must have been sleeping.
No time to sleep! You need food!
'''
        else:
            default_meow()

    def start():
        get_command(look, go, meow=meow)

    return (look, start)


def living_room():
    def look():
        global cid_can_attack
        if cid_can_attack:
            cid_attacks()
        else:
            walk_in()

    def cid_attacks():
            print '''
You walk into the living room only to see your arch enemy
Cid! He's lurking under his favorite chair waiting to boop you right on the
snoot. You decide it's safer to move back to hallway...
'''
            go_no_look(hallway)

    def walk_in():
        print '''
You look around the living room as if you own the place.
You see one of your people, Kevin, sitting on the couch next to the cat tree.
He's always on the couch.'''
        global whitney_in_living_room
        global need_whitney
        if whitney_in_living_room and need_whitney:
            print '''Whitney is on the couch.
More importantly her lap is available for snuggles.
'''
        else:
            print '\n',

    def go(room):
        global whitney_in_living_room
        if room == 'hallway':
            default_go(hallway)
        elif room == 'kitchen':
            default_go(kitchen)
        elif room == 'cat tree' or room == 'tree':
            default_go(cat_tree)
        elif ('lap' in room or 'whitney' in room) and whitney_in_living_room:
            default_go(lap)
        else:
            cannot_go()

    def start():
        get_command(look, go)

    return (look, start)


def kitchen():
    def look():
        print '''
This place smells like food!
Your people are always making food in here. You see many things.
But one is special. Behold, the stove.
The magical food cooker of the humans.
'''

    def go(room):
        if room == 'stove':
            print '''
Ouch!!! It's hot. Your tiny cat feet have been badly burned.
Your people hear you yowl and immediately take you to the hospital.
Looks like your gonna be hungry forever.

\t\tGame over.
'''
            exit(1)
        elif room == 'living room':
            default_go(living_room)
        else:
            cannot_go()

    def start():
        get_command(look, go)

    return (look, start)


def cat_tree():
    def look():
        print '''
You can see Cid hiding from Squirt above you on the top of
the tower.  Better not go up or you might get booped.  Still you have a good
view to better see where the food might be.
'''

    def go(room):
        if room == 'living room':
            default_go(living_room)
        else:
            cannot_go()

    def meow():
        global need_kevin
        if need_kevin:
            print '''
You look Kevin right in the eyes and meow.
He puts down his video game and walks over to pick you up.
This is not what you wanted but now you are in his arms.
'''
            go_no_look(kevin_arms)
        else:
            default_meow()

    def start():
        get_command(look, go, meow=meow)

    return (look, start)


def kevin_arms():
    def look():
        print '''
You hate it when Kevin holds you.
He's always rubbing your belly. It's the worst. It looks like you could jump
back to the cat tree if you wiggle a bit.
Or maybe while you're here you can hypnotize him into feeding you?
'''

    def go(room):
        if room == 'cat tree':
            default_go(cat_tree)
        else:
            cannot_go()

    def purr():
        global need_kevin
        need_kevin = False
        global need_whitney
        if need_whitney:
            print '''
Kevin laughs and rubs your belly.
It's not the best thing, but it's still affection. So you'll take it.
You get snuggled a bit more and Kevin puts you back on the cat tree.
'''
            go_no_look(cat_tree)
        else:
            print '''
Kevin sighs. He looks at the clock and realizes it's way
past feeding time. Finally! It looks like all that meowing and purring worked.
Kevin fills your food bowl with glorious kibble bits. You think he's a bit
stingy, but you're too overjoyed by stuffing your face to care.  Maybe you'll
get more next time in another 'Linus: A Text Adventure'!

\t CONGRATULATIONS, YOU FED LINUS! (winning in Linus' eyes)
'''
            exit(0)

    def start():
        get_command(look, go, purr=purr)

    return (look, start)


def lap():
    def look():
        print '''
Ahh, to be in mom's lap. It is superb. Not even Cid can touch
you here.
After a brief rest you realize you're still very hungry.
The living room and your journey awaits.
'''

    def go(room):
        if room == 'living room':
            default_go(living_room)
        else:
            cannot_go()

    def purr():
        global need_kevin
        global need_whitney
        if need_kevin:
            print '''
Whitney smiles and pets you.
She gives you all of her love and then puts you down in the living room.
'''
            need_whitney = False
            go_no_look(living_room)
        else:
            print '''
Whitney says "Have you fed the cats yet?"
Whatever that means.  Kevin shakes his head no.
Whitney gets up and puts you on the ground.  THE TIME HAS COME!!!
Whitney walks over to the food closet and gets your food out.
It was close. Your grumbly belly almost defeated you today.
Let's hope you survive the next close encounter with hunger in
"Linus: A Text Adventure"

\t CONGRATULATIONS, YOU FED LINUS! (winning in Linus' eyes)
'''
            exit(0)

    def start():
        get_command(look, go, purr=purr)

    return (look, start)


look, start = bedroom()
current_room = start
intro()
while True:
    current_room()
