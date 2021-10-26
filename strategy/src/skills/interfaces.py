from abc import ABC, abstractmethod


class SkillInterface(ABC):

    @abstractmethod
    def behavior(self):
        raise NotImplementedError

    @abstractmethod
    def skill_level(self):
        raise NotImplementedError
