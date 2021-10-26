from .interfaces import SkillInterface


class Healer(SkillInterface):

    def __init__(self, level):
        self.level = level

    def behavior(self):
        print("Healer")

    def skill_level(self):
        print(f"Skill Level Healer: {self.level}")
