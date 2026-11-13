# Object-oriented game simulator
# Turid Torheim, NMBU, 2026

import random
import items


class Character:
    """Represents a character in the RPG"""

    def __init__(self, name: str, hp_max: int = 100, damage: int = 10, weapon_name: str = False, weapon_dice: int = 6) -> None:
        """
        Initialise the Character

        Args:
            name (str): The name of the character.
            hp_max (int): Max hit points (default = 100)
            damage (int): Damage delt when character attacks (default = 10)
        """
        self.name = name
        self._hp = hp_max  # Note: _hp indicated private attribute
        self.hp_max = hp_max
        
        if weapon_name is not False:
            self.weapon = items.Weapon(weapon_name, weapon_dice)
            self.damage = 0
            self.wepon_chek=True
            

        else:
            self.damage = damage
            self.wepon_chek=False
            

    def attack(self, target) -> None:
        """Attack and deal damage to target character"""
        print(self.wepon_chek)
        if self.wepon_chek==False:
            target.take_damage(self.damage)
            
            
        else:
            target.take_damage(self.weapon.roll_damage())
            

    def introduce(self) -> None:
        """Creates string that introduces character"""
        print(f"Hi, my name is {self.name}!")

    def __repr__(self) -> str:
        """Representation of character object"""
        return f"<Character name={self.name} hp={self.hp} damage={self.damage}>)"

    def __str__(self) -> str:
        """String representation of character object"""
        return f"Character: {self.name} with {self.hp} HP and {self.damage} damage"

    @property
    def hp(self) -> int:
        """Public read-only property to inspect HP without allowing direct, unsafe edits."""
        return self._hp


    def take_damage(self, damage: int) -> None:
        self._hp -= damage
        self._hp = max(self._hp, 0) 

    def heal(self, amount: int) -> None:
        self._hp += amount
        self._hp = min(self._hp, self.hp_max)

    @property
    def is_alive(self) -> bool:
        if not self._hp > 0:
            return False
        return True




class Dize:
    def __init__(self, sides: int = 6) -> None:
        self.sides = sides

    def roll(self) -> int:
        import random
        return random.randint(1, self.sides)
    def __repr__(self) -> str:
        return f"Dize={self.sides}"

    def __call__(self) -> int:
        return self.roll()


#d6=Dize(6)
#print(d6())

dave=Character("Dave", hp_max=60, damage=15)

peter=Character("Peter", hp_max=70, damage=10, weapon_name="Sword", weapon_dice=8)
print(dave) 
peter.attack(dave)

print(peter) 
print(dave) 
print(peter.is_alive)