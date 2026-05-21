import pyxel
class Enemies:
    """This class store the information that will be common for all the enemies"""
    def __init__(self, x: int, y: int,direc: int):
        """this is the init method where the x is refered to the position in x/y axis and its direction"""

        self.x = x                                          #They all will have in common a position x,y, direccion that will be
        self.y = y                                          #or left with -1 or right with 1,the gravity and sprite that will change if it
        self.direc=direc                                    #is an enemy or another and the atribute air to check if it is in the air
        self.sprite = (0, 0, 24,16,16, 0)
        self.air = False
        self.dy = 0
    @property
    def x(self) -> int:
        return self.__x

    @property
    def y(self) -> int:
        return self.__y

    @x.setter
    def x(self, x:int):
        self.__x = x

    @y.setter
    def y(self, y: int):
        self.__y = y

    @property
    def sprite(self) -> tuple:
        return self.__sprite

    @sprite.setter
    def sprite(self, sprite: tuple):
        self.__sprite = sprite

    @property
    def dy(self) -> int:
        return self.__dy

    @dy.setter
    def dy(self, dy: int):
        self.__dy = dy

    @property
    def air(self) -> bool:
        return self.__air

    @air.setter
    def air(self, air: bool):
        self.__air = air

    @property
    def direc(self) -> int:
        return self.__direc

    @direc.setter
    def direc(self, direc: int):
        self.__direc = direc

    def mover(self, length: int):
        """"this will be the function for the movements of the enemies (really similar to the marios one"""
        if self.x >= 356:                   #This is for the teletransportation and we set the direcion to right
            self.x = 0
            self.direc = 1
        if self.direc == 1:
            self.sprite = (self.sprite[0],0+ 16*(pyxel.frame_count%3), self.sprite[2], -16, self.sprite[4],0)       #Thanks to this the sprite will be changing
        if self.x < -16:                     #Again fot the teleport
            self.x = 350
            self.direc = -1
        if self.direc == -1:
            self.sprite = (self.sprite[0],0 + 16*(pyxel.frame_count%3), self.sprite[2], 16, self.sprite[4],0)       #Again for the direction of the enemy, his sprite
                                                                                                                    #will be changing like it is moving to that direction
        if self.direc == 0:                   #We have done this because is the sprite the enemy will
            self.x = self.x                   #have when it dies
            self.sprite = (0, 112, self.sprite[2], 16, 16, 0)

        self.x += self.direc

class Turtle(Enemies):
    """this is the specific class for the enemy turtle, here we will set its characteristics"""
    def __init__(self, x: int, y: int,direc:int):
        super().__init__(x,y,direc)
        self.sprite = (0, 0, 24,16,16, 0)                   #We will take everything of the enemies class except from the sprite


class Crab(Enemies):
    """this is the specific class for the enemy crab, here we will set its characteristics"""
    def __init__(self, x: int, y: int,direc:int):
        super().__init__(x,y,direc)
        self.sprite = (0, 0, 40,16,16, 0)                   #We will take everything of the enemies class except from the sprite
        self.lifes_crab = 2
    def mover(self, length: int):
        super().mover(length)
        if self.direc == 0:
            self.x = self.x                                     #We will have to change the function move for the enemy crabs because the sprite
            self.sprite = (0, 152, self.sprite[2], 16, 16, 0)   #when its dies is different

class Butter(Enemies):
    """this is the specific class for the enemy fly, here we will set its characteristics"""
    def __init__(self, x: int, y: int,direc:int):
        super().__init__(x,y,direc)
        self.sprite = (0, 0, 56, 16, 16, 0)                 #change again the sprite

    def mover(self,length:int):
        super().mover(length)
        if self.direc == 0:
            self.x = self.x                                 #change again the sprite for the fly when it dies
            self.sprite = (0, 80, 56, 16, 16, 0)

