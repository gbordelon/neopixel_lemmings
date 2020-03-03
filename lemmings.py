from PIL import Image
from itertools import chain
from enum import Enum, auto

class LemmingState(Enum):
    ALIVE = auto()
    DEAD = auto()
    DYING = auto()

class LemmingDyingState(Enum):
    PANIC = auto()
    SQUISH = auto()
    DROWN = auto()
    EXPLODE = auto()
    VICTORY = auto()

class LemmingAliveState(Enum):
    WALK = auto()
    QUESTION = auto()
    FALL = auto()
    UMBRELLA = auto()
    BLOCK = auto()
    CLIMB = auto()
    BUILD = auto()
    BASH = auto()
    DIG = auto()
    MINE = auto()

class LemmingDirectionState(Enum):
    NONE = auto()
    LEFT = auto()
    RIGHT = auto()

class LemmingState(object):
    def __init__(self, start_position, direction):
        self.world_position = start_position
        self.life_state = LemmingState.ALIVE
        self.state = LemmingAliveState = FALL
        self.direction = direction
        self.frame_count = 0 # for current state: fall distance, velocity (like walking is faster than bashing)

class Lemming(object):
    def __init__(self, start_position, direction):
        self.state = LemmingState(start_position, direction) # LemmingDirectionState

    """
    each clock tick advance the state based on the current lemming state and the world state
    """
    def increment_state(self, world):
        if self.state.life_state is LemmingState.ALIVE:
            if self.state.state is LemmingAliveState.WALK:
                pass
                #world.collide(self.
            elif self.state.state is LemmingAliveState.QUESTION:
                pass
            elif self.state.state is LemmingAliveState.FALL:
                pass
            elif self.state.state is LemmingAliveState.UMBRELLA:
                pass
            elif self.state.state is LemmingAliveState.BLOCK:
                pass
            elif self.state.state is LemmingAliveState.CLIMB:
                pass
            elif self.state.state is LemmingAliveState.BUILD:
                pass
            elif self.state.state is LemmingAliveState.BASH:
                pass
            elif self.state.state is LemmingAliveState.DIG:
                pass
            elif self.state.state is LemmingAliveState.MINE:
                pass
            else:
                pass
        elif self.state.life_state is LemmingState.DYING:
            if self.state.state is LemmingDyingState.PANIC:
                pass
            elif self.state.state is LemmingDyingState.SQUISH:
                pass
            elif self.state.state is LemmingDyingState.DROWN:
                pass
            elif self.state.state is LemmingDyingState.EXPLODE:
                pass
            elif self.state.state is LemmingDyingState.VICTORY:
                pass
            else:
                pass
        else: # dead so cleanup
            pass

    """
    make a lemming a basher or blocker or whatever
    """
    def change_state(self):
        pass

class Material(Enum):
    EMPTY = 0
    MUTABLE = 1
    IMMUTABLE = 2
    LIQUID = 3

class World(object):
    @staticmethod
    def parse_file(world_file):
        
        return World()

    def __init__(self, dimensions, origin, destination, color_map, material_map):
        pass

class LemmingsAnimation(object):
    walk = [ (2,0), (22,0), (42,0), (62,0), (82, 0), (102, 0), (122, 0), (142, 0), (161, 0) ]
    question = [(182, 0), (202,0), (222, 0), (242, 0), (262, 0), (282, 0), (302, 0), (2,20)]
    victory = [(20,20), (40, 20), (60, 20), (80, 20), (100, 20), (120, 20), (140,20), (160,20)]
    fall = [(1,40), (21, 40), (41, 40), (61, 40)]
    umbrella_open = [(80, 40), (100, 40), (120, 40), (140, 40)]
    umbrella = [(160, 40), (180, 40), (200, 40), (220, 40), (200, 40), (180, 40)]
    block = [(1, 60), (21, 60), (41, 60), (61, 60), (81, 60), (101, 60), (121, 60), (141, 60), (161, 60), (181, 60), (201, 60), (221, 60), (241, 60), (261, 60), (281, 60), (301, 60) ]
    climb = [(0, 80), (20, 80), (40, 80), (60, 80), (80, 80), (100, 80), (120, 80), (140, 80)]
    climb_finish = [(160, 80), (180, 80), (200, 80), (220, 80), (240, 80), (260, 80), (280, 80), (300, 80)]
    build = [(1, 100), (21, 100), (41, 100), (61, 100), (81, 100), (101, 100), (121, 100), (141, 100), (161, 100), (181, 100), (201, 100), (221, 100), (241, 100), (261, 100), (281, 100), (301, 100)]
    bash_1 = [(1, 120), (21, 120), (41, 120), (61, 120), (81, 120), (101, 120), (121, 120), (141, 120), (161, 120), (181, 120), (201, 120), (221, 120), (241, 120), (261, 120), (281, 120), (301, 120)]
    bash_2 = [(1, 140), (21, 140), (41, 140), (61, 140), (81, 140), (101, 140), (121, 140), (141, 140), (161, 140), (181, 140), (201, 140), (221, 140), (241, 140), (261, 140), (281, 140), (301, 140)]
    dig = [(1, 160), (21, 160), (41, 160), (61, 160), (81, 160), (101, 160), (121, 160), (141, 160)]
    mine = [(160, 160), (180, 160), (200, 160), (220, 160), (240, 160), (260, 160), (280, 160), (300, 160), (0, 180), (20, 180), (40, 180), (60, 180), (80, 180), (100, 180), (120, 180), (140, 180), (160, 180), (180, 180), (200, 180), (220, 180), (240, 180), (260, 180), (280, 180), (300, 180),]
    panic = [(1, 200), (21, 200), (41, 200), (61, 200), (81, 200), (101, 200), (121, 200), (141, 200), (161, 200), (181, 200), (201, 200), (221, 200), (241, 200), (261, 200), (281, 200), (301, 200)]
    squish = [(0, 220), (20, 220), (40, 220), (60, 220), (80, 220), (100, 220), (120, 220), (140, 220), (160, 220), (180, 220), (200, 220), (220, 220), (240, 220), (260, 220), (280, 220), (300, 220)]
    drown = [(1, 240), (21, 240), (41, 240), (61, 240), (81, 240), (101, 240), (121, 240), (141, 240), (161, 240), (181, 240), (201, 240), (221, 240), (241, 240), (261, 240), (281, 240), (301, 240)]
    explode = [(0, 260), (20, 260), (40, 260), (60, 260), (80, 260), (100, 260), (120, 260), (140, 260), (160, 260), (180, 260), (200, 260), (260, 260), (220, 260), (240, 260)]

    def __init__(self):
        img = Image.open('./lemming_anim.png').convert('RGB')
        self.sprites = img.load()

    def _anim_helper(self, anim):
        for x,y in anim:
            for _y in range(y, y+16):
                for _x in range(x, x+16):
                    yield _x-x, _y-y, self.sprites[_x,_y]
            yield None, None, None

    def _anim_mirror_helper(self, anim):
        for x,y in anim:
            for _y in range(y, y+16):
                for _x in range(x, x+16,):
                    yield 14-(_x-x), _y-y, self.sprites[_x,_y]
            yield None, None, None

    def animation_pixel_generator(self, state):
        if isinstance(state, LemmingDyingState):
            if state is LemmingDyingState.PANIC:
                return self._anim_helper(LemmingsAnimation.panic)
            elif state is LemmingDyingState.SQUISH:
                return self._anim_helper(LemmingsAnimation.squish)
            elif state is LemmingDyingState.DROWN:
                return self._anim_helper(LemmingsAnimation.drown)
            elif state is LemmingDyingState.EXPLODE:
                return self._anim_helper(LemmingsAnimation.explode)
            elif state is LemmingDyingState.VICTORY:
                return self._anim_helper(LemmingsAnimation.victory)
            else:
                pass
        elif isinstance(state, LemmingAliveState):
            if state is LemmingAliveState.WALK:
                return self._anim_helper(LemmingsAnimation.walk)
            elif state is LemmingAliveState.QUESTION:
                return self._anim_helper(LemmingsAnimation.question)
            elif state is LemmingAliveState.FALL:
                return self._anim_helper(LemmingsAnimation.fall)
            elif state is LemmingAliveState.UMBRELLA:
                return chain(self._anim_helper(LemmingsAnimation.umbrella_open),
                             self._anim_helper(LemmingsAnimation.umbrella))
            elif state is LemmingAliveState.BLOCK:
                return self._anim_helper(LemmingsAnimation.block)
            elif state is LemmingAliveState.CLIMB:
                return self._anim_helper(LemmingsAnimation.climb)
                #return self._anim_helper(LemmingsAnimation.climb_finish)
            elif state is LemmingAliveState.BUILD:
                return self._anim_helper(LemmingsAnimation.build)
            elif state is LemmingAliveState.BASH:
                return self._anim_helper(LemmingsAnimation.bash_1)
                #return self._anim_mirror_helper(LemmingsAnimation.bash_2)
            elif state is LemmingAliveState.DIG:
                return chain(self._anim_helper(LemmingsAnimation.dig), self._anim_mirror_helper(LemmingsAnimation.dig))
            elif state is LemmingAliveState.MINE:
                return self._anim_helper(LemmingsAnimation.mine)
            else:
                pass
        else:
            pass
