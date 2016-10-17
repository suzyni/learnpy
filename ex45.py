from sys import exit
import scene

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map
    
    def play(self):
        current_scene = self.scene_map.opening_scene()
        
        while True:
            print "\n---------"
            next_scene_name = current_scene.enter()
            if next_scene_name == 'finished':
                exit(0)
            else:
                current_scene = self.scene_map.next_scene(next_scene_name)

class Death(scene.Scene):

    def enter(self):
        print "You died."
        exit(1)
        
class CentralCorridor(scene.Scene):

    def enter(self):
        print "You have entered Central Corridor."
        action = raw_input("> ")
        if action == "1":
            return 'death'
        elif action == "2":
            return 'laser_weapon_armory'
        else:
            print "DOES NOT COMPUTE!"
            return 'central_corridor'

class LaserWeaponArmory(scene.Scene):

    def enter(self):
        print "You have entered Laser Weapon Armory."
        action = raw_input("> ")
        if action == "1":
            return 'death'
        elif action == "2":
            return 'the_bridge'
        else:
            print "DOES NOT COMPUTE!"
            return 'laser_weapon_armory'

class TheBridge(scene.Scene):

    def enter(self):
        print "You have entered The Bridge."
        action = raw_input("> ")
        if action == "1":
            return 'death'
        elif action == "2":
            return 'escape_pod'
        else:
            print "DOES NOT COMPUTE!"
            return 'the_bridge'
        
class EscapePod(scene.Scene):

    def enter(self):
        print "You have entered Escape Pod."
        action = raw_input("> ")
        if action == "1":
            return 'death'
        elif action == "2":
            print "You won!"
            return 'finished'
        else:
            print "DOES NOT COMPUTE!"
            return 'escape_pod'

class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death()
    }
    
    def __init__(self, start_scene):
        self.start_scene = start_scene
    
    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)
    
    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()