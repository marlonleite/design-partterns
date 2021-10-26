from .interfaces import SkillInterface


class SwordFight(SkillInterface):

    def __init__(self, level):
        self.level = level

    def behavior(self):
        print("Sword Fight")

    def skill_level(self):
        print(f"Skill Level Sword: {self.level}")
