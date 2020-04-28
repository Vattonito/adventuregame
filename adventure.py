class Parser:
    def __init__(self, list_of_commands, list_of_nouns):
        self.phrase = None
        self.noun = None
        self.verb = None
        self.command_list = list_of_commands
        self.noun_list = list_of_nouns

    def parse(self, phrase):
        self.phrase = phrase
        self.verb = None
        self.noun = None
        the_phrase_as_a_list = self.phrase.split()
        if len(the_phrase_as_a_list) > 2:
            print("Unable to parse your command")
            return
        self.verb = the_phrase_as_a_list[0]
        if self.verb not in self.command_list:
            print("Unknonwn command/verb ", self.verb)
            self.verb = None
            return
        if len(the_phrase_as_a_list) > 1:
            self.noun = the_phrase_as_a_list[1]
            if self.noun not in self.noun_list:
                print("Unknown noun: ", self.noun)
                self.verb = None
                self.noun = None
        else:
            self.noun = None

    def get_verb(self):
        return self.verb

    def get_noun(self):
        return self.noun


class Room:
    def __init__(self, name, description):
        self.description = description
        self.name = name
        self.up = None
        self.down = None
        self.left = None
        self.right = None
        self.inventory = []

    def put_item(self, Item):
        self.inventory.append(Item)

    def call_inventory(self):
        for item in self.inventory:
            print(item.name)

    def look(self):
        print("You See", self.inventory)


class Item:
    def __init__(self, name):
        self.name = name


kitchen = Room("Kitchen", "You see a white counter-top with dim light and tile floor")
basement = Room("Basement", "The basement is dark but you see a key")
bedroom = Room("Bedroom", "You see a large bed, and clothes on the floor a cellphone sits on the nightstand")
closet = Room("Closet", "There is a lot of toilet paper")
kitchen.up = bedroom
kitchen.down = basement
kitchen.left = closet
basement.up = kitchen
bedroom.down = kitchen
cellphone = Item("Cell Phone")
key = Item("Key")
bedroom.put_item(cellphone)
basement.put_item(key)
backpack = []


def main():
    command_parser = Parser(['go', 'exit', 'look', 'take'], ['up', 'left', 'right', 'down', 'in', 'out'])
    current_room = kitchen
    print("You are in", current_room.name)
    while command_parser.get_verb() != "exit":
        instruction = input('Enter your instructions here: ')
        command_parser.parse(instruction)
        print('Original phrase: ', command_parser.phrase)
        if command_parser.verb == "take":
            backpack.append(Item)
            print("you take the", Item)
        if command_parser.verb == "look" and command_parser.noun == None:
            print(current_room.description)
        elif command_parser.verb == "go":
            if command_parser.noun == "up":
                if current_room.up != None:
                    current_room = current_room.up
                else:
                    print("There is no room")
            if command_parser.noun == "down":
                if current_room.down != None:
                    current_room = current_room.down
                else:
                    print("There is no room")
            if command_parser.noun == "right":
                if current_room.right != None:
                    current_room = current_room.right
                else:
                    print("There is no room")
            if command_parser.noun == "left":
                if current_room.left != None:
                    current_room = current_room.left
                else:
                    print("There is no room")
            print("You are in", current_room.name)
        elif command_parser.verb == "exit":
            print("You have escaped!!! Goodbye")
        else:
            print("wrong command, please try again")


main()
