from typing import Type

from .skills import SkillInterface


class Warrior:

    def __init__(self, skill: Type[SkillInterface]):
        self.skill = skill

    def action(self):
        self.skill.behavior()

    def attributes(self):
        self.skill.skill_level()
