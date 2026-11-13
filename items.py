
class Weapon:
    def __init__(self, name: str, damage_dice: int):
        self.name = name
        self.damage_dice = damage_dice
    def roll_damage(self) -> int:
        import game_simulator_v1
        return game_simulator_v1.Dize(self.damage_dice).roll() 

    
