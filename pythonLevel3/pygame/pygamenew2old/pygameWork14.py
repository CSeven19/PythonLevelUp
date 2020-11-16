# ai

from pythonLevel3.pygame.pygamenew2old.pygameWork10 import Vector2
from pythonLevel3.pygame.pygamenew2old.pygameWork13 import GameEntity,World

class Ant(GameEntity):
    def __init__(self, world, image):
        # 执行基类构造方法
        GameEntity.__init__(self, world, "ant", image)
        # 创建各种状态
        exploring_state = AntStateExploring(self)
        seeking_state = AntStateSeeking(self)
        delivering_state = AntStateDelivering(self)
        hunting_state = AntStateHunting(self)
        self.brain.add_state(exploring_state)
        self.brain.add_state(seeking_state)
        self.brain.add_state(delivering_state)
        self.brain.add_state(hunting_state)
        self.carry_image = None
    def carry(self, image):
        self.carry_image = image
    def drop(self, surface):
        # 放下carry图像
        if self.carry_image:
            x, y = self.location
            w, h = self.carry_image.get_size()
            surface.blit(self.carry_image, (x-w, y-h/2))
            self.carry_image = None
    def render(self, surface):
        # 先调用基类的render方法
        GameEntity.render(self, surface)
        # 额外绘制carry_image
        if self.carry_image:
            x, y = self.location
            w, h = self.carry_image.get_size()
            surface.blit(self.carry_image, (x-w, y-h/2))

class State():
    def __init__(self, name):
        self.name = name
    def do_actions(self):
        pass
    def check_conditions(self):
        pass
    def entry_actions(self):
        pass
    def exit_actions(self):
        pass

class StateMachine():
    def __init__(self):
        self.states = {}    # 存储状态
        self.active_state = None    # 当前有效状态
    def add_state(self, state):
        # 增加状态
        self.states[state.name] = state
    def think(self):
        if self.active_state is None:
            return
        # 执行有效状态的动作，并做转移检查
        self.active_state.do_actions()
        new_state_name = self.active_state.check_conditions()
        if new_state_name is not None:
            self.set_state(new_state_name)
    def set_state(self, new_state_name):
        # 更改状态，执行进入/退出动作
        if self.active_state is not None:
            self.active_state.exit_actions()
        self.active_state = self.states[new_state_name]
        self.active_state.entry_actions()