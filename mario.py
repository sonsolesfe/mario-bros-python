import pyxel

class Mario:
    """This class stores the information related to mario"""

    def __init__(self, x: int, y: int):
        """ The param x is refered to the x position and the y to the y position"""
        self.x = x
        self.y = y

        self.sprite = (0, 0, 0,16,24, 0)                   #we set the image

        self.lifes = 3                                     #we set the lifes that mario will have

        self.dy = 0                                        #we set the gravity of mario, that is in the y axis

        self.air = False                                   #we have set that the enemy is not in the air, this will be changing
                                                           #when mario is or not in the air
        self.jumpable = True                               #The jump is to control when mario is jumping

    @property
    def x(self) -> int:
        return self.__x

    @property
    def y(self) -> int:
        return self.__y

    @property
    def lifes(self) ->int:
        return self.__lifes

    @property
    def sprite(self) -> tuple:
        return self.__sprite

    @property
    def dy(self) -> int:
        return self.__dy

    @property
    def air(self) -> bool:
        return self.__air

    @air.setter
    def air(self,air:bool):
        self.__air = air
    @dy.setter
    def dy(self, dy: int):
        self.__dy = dy

    @sprite.setter
    def sprite(self,sprite:tuple):
        self.__sprite = sprite
    @x.setter
    def x(self, x:int):
        self.__x = x

    @y.setter
    def y(self, y: int):
        self.__y = y

    @lifes.setter
    def lifes(self, lifes: int):
        self.__lifes = lifes

    @property
    def jumpable(self) -> bool:
        return self.__jumpable

    @jumpable.setter
    def jumpable(self, jumpable: bool):
        self.__jumpable = jumpable
    def move(self, direction: str,length:int):
        """This is the function that we have created for the movement of mario,
        it takes the direction of mario and its length."""

        if direction.lower() == "right":
            self.sprite = (self.sprite[0], 16 + 16 * (pyxel.frame_count%3), self.sprite[2], 16, self.sprite[4])     #We change the sprite pf mario when he moves

            self.dx = 3                                       #The velocity that mario will have

            if self.x >= 356:                                 #The teletransportation of mario when it croos the screen in the rigth side
                self.x = 0

        elif direction.lower() == "left":
            self.dx = -3                                      #The velocity that mario will have, in this case is negatve because it will go to the other side

            self.sprite = (self.sprite[0], 16 + 16 * (pyxel.frame_count%3), self.sprite[2], -16, self.sprite[4])    #We change the sprite pf mario when he moves

            if self.x < -16:                                  #The teletransportation of mario when it croos the screen in the left side
                self.x = 350

        else:
            self.dx = 0
            self.sprite = (0, 0, 0, 16, 24, 0)
        self.x += self.dx

    def jump(self):
        """This is the method we have created for mario to jump"""

        self.air = True                         #We set that mario is in the air

        self.jumpable = False                   #We set that mario is jumping (because we put before that was true)

        self.dy = -10.5                         #This is the velocity that mario have in the y axis (for the gravity),
                                                #it is negative because the velocity when it falls is positive.






