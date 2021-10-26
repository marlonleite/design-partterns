from .interfaces import SkillInterface


class ArrowFight(SkillInterface):

    def __init__(self, level):
        self.level = level

    def behavior(self):
        print("Arrow Fight")

    def skill_level(self):
        print(f"Skill Level Arrow: {self.level}")
