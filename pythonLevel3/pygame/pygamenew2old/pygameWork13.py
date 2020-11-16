# 趣味性，AI

from pythonLevel3.pygame.pygamenew2old.pygameWork10 import Vector2
import pygame

# 游戏实体类
class GameEntity(object):
    def __init__(self, world, name, image):
        self.world = world
        self.name = name
        self.image = image
        self.location = Vector2(0, 0)
        self.destination = Vector2(0, 0)
        self.speed = 0.
        self.brain = StateMachine()
        self.id = 0
    def render(self, surface):
        x, y = self.location
        w, h = self.image.get_size()
        surface.blit(self.image, (x-w/2, y-h/2))
    def process(self, time_passed):
        self.brain.think()
        if self.speed > 0 and self.location != self.destination:
            vec_to_destination = self.destination - self.location
            distance_to_destination = vec_to_destination.get_length()
            heading = vec_to_destination.get_normalized()
            travel_distance = min(distance_to_destination, time_passed * self.speed)
            self.location += travel_distance * heading


class StateMachine():
    def __init__(self):
        pass
    def think(self):
        pass


class World(object):
    def __init__(self):
        self.entities = {} # Store all the entities
        self.entity_id = 0 # Last entity id assigned
        # 画一个圈作为蚁穴
        self.background = pygame.surface.Surface(pygame.SCREEN_SIZE).convert()
        self.background.fill((255, 255, 255))
        pygame.draw.circle(self.background, (200, 255, 200), pygame.NEST_POSITION, int(pygame.NEST_SIZE))
    def add_entity(self, entity):
        # 增加一个新的实体
        self.entities[self.entity_id] = entity
        entity.id = self.entity_id
        self.entity_id += 1
    def remove_entity(self, entity):
        del self.entities[entity.id]
    def get(self, entity_id):
        # 通过id给出实体，没有的话返回None
        if entity_id in self.entities:
            return self.entities[entity_id]
        else:
            return None
    def process(self, time_passed):
        # 处理世界中的每一个实体
        time_passed_seconds = time_passed / 1000.0
        for entity in self.entities.itervalues():
            entity.process(time_passed_seconds)
    def render(self, surface):
        # 绘制背景和每一个实体
        surface.blit(self.background, (0, 0))
        for entity in self.entities.values():
            entity.render(surface)
    def get_close_entity(self, name, location, range=100.):
        # 通过一个范围寻找之内的所有实体
        location = Vector2(*location)
        for entity in self.entities.values():  #self.entities.values()代表所有存在游戏实体
            if entity.name == name:
                distance = location.get_distance_to(entity.location)
                if distance < range:  #其距离小于判断range的游戏实体就是我需要的。
                    return entity
        return None