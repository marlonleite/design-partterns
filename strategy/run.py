from src import Warrior
from src.skills import SwordFight, ArrowFight, Healer

knight = Warrior(SwordFight(6))
arrow = Warrior(ArrowFight(9))
healer = Warrior(Healer(11))

knight.action()
arrow.action()

arrow.action()
arrow.attributes()

healer.action()
healer.attributes()