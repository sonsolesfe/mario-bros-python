import pyxel
class Plataformas:
    """This class stores the information related to Platforms"""
    def __init__(self, x: int, y: int):
        """ The param x is refered to the x position and the y to the y position"""
        self.x = x                                      #They have a x and y position
        self.y = y
        self.sprite = (0, 170, 136, 85, 7, 0)           #We set the image

    @property
    def x(self) -> int:
        return self.__x

    @x.setter
    def x(self, x: int):
        self.__x = x

    @property
    def y(self) -> int:
        return self.__y

    @y.setter
    def y(self, y: int):
        self.__y = y

    @property
    def sprite(self) -> tuple:
        return self.__sprite

    @sprite.setter
    def sprite(self, sprite: tuple):
        self.__sprite = sprite


class Floor:
    """This class stores the information related to the floor"""
    def __init__(self, x: int, y: int):
        """ The param x is refered to the x position and the y to the y position"""
        self.x = x
        self.y = y
        self.sprite = (0, 120, 176, 16, 16, 0)          #We set the image

    @property
    def x(self) -> int:
        return self.__x

    @property
    def y(self) -> int:
        return self.__y

    @x.setter
    def x(self, x: int):
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
class Pow:
    """This class stores the information related to the block pow"""
    def __init__(self, x: int, y: int):
        """ The param x is refered to the x position and the y to the y position"""
        self.x = x
        self.y = y
        self.sprite = (0, 136, 176, 15, 15, 0)          #We set the image

        self.count_hits = 0                             #Counter for the number of hits

        self.hit1_sprite = (0, 152, 176, 15, 12, 0)     #In this case we create more sprites because the image
        self.hit2_sprite = (0, 168, 176, 15, 8, 0)      #will be changing if mario hits the pow (this is done in the board)

        self.dissapear = False                          #We want that the block dissapear, so we have do it by a bool that will change
                                                        #if  this block is or not in the screen

    @property
    def x(self) -> int:
        return self.__x

    @property
    def y(self) -> int:
        return self.__y

    @x.setter
    def x(self, x: int):
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
    def count_hits(self) -> int:
        return self.__count_hits

    @count_hits.setter
    def count_hits(self, count_hits: int):
        self.__count_hits= count_hits

    @property
    def hit1_sprite(self) -> tuple:
        return self.__hit1_sprite

    @hit1_sprite.setter
    def hit1_sprite(self, hit1_sprite: tuple):
        self.__hit1_sprite = hit1_sprite

    @property
    def hit2_sprite(self) -> tuple:
        return self.__hit2_sprite

    @property
    def dissapear(self) -> bool:
        return self.__dissapear

    @dissapear.setter
    def dissapear(self, dissapear: bool):
        self.__dissapear = dissapear

    @hit2_sprite.setter
    def hit2_sprite(self, hit2_sprite: tuple):
        self.__hit2_sprite = hit2_sprite
class Tuberias:
    """This class stores the information related to the pipes"""
    def __init__(self, x: int, y: int):
        """ The param x is refered to the x position and the y to the y position"""
        self.x = x
        self.y = y
        self.sprite = (0, 32, 187, 47,19,0)             #We set the image

        self.sprite_arriba = (0,64,176,45,30,0)           #There are different types of pipes so the sprite will be
        self.sprite_arriba2 = (0,64,176,-45,30,0)         #different for each of them

    @property
    def x(self) -> int:
        return self.__x

    @property
    def y(self) -> int:
        return self.__y

    @x.setter
    def x(self, x: int):
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
    def sprite_arriba(self) -> tuple:
        return self.__sprite_arriba

    @sprite_arriba.setter
    def sprite_arriba(self, sprite_arriba: tuple):
        self.__sprite_arriba = sprite_arriba

    @property
    def sprite_arriba2(self) -> tuple:
        return self.__sprite_arriba2

    @sprite_arriba2.setter
    def sprite_arriba2(self, sprite_arriba2: tuple):
        self.__sprite_arriba2 = sprite_arriba2
class Coins:
    """This class stores the information related to the coins"""
    def __init__(self, x: int, y: int,direc: int):
        """ The param x is refered to the x position and the y to the y position adnd the direc is the
            direccion that the coin will take when it moves"""

        self.x = x
        self.y = y
        self.sprite = (0, 0, 208, 7, 15, 0)                 #We set the image

        self.dissapear_coin = False                          #For the dissappear of the coins

        self.direc=direc

        self.air = False
        self.dy = 0

    @property
    def x(self) -> int:
        return self.__x

    @property
    def y(self) -> int:
        return self.__y

    @x.setter
    def x(self, x: int):
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
    def dissapear_coin(self) -> bool:
        return self.__dissapear_coin

    @dissapear_coin.setter
    def dissapear_coin(self, dissapear_coin: bool):
        self.__dissapear_coin = dissapear_coin

    @property
    def direc(self) -> int:
        return self.__direc

    @direc.setter
    def direc(self, direc: int):
        self.__direc = direc

    @property
    def air(self) -> bool:
        return self.__air

    @air.setter
    def air(self, air: bool):
        self.__air = air

    @property
    def dy(self) -> int:
        return self.__dy

    @dy.setter
    def dy(self, dy: int):
        self.__dy = dy

    def mover_coins(self, length: int):
        """Function that we will use to move the coins,they will cross the image as same as mario and the enemies,
            and we will receive the length of the length too"""
        if self.x >= 356:               #They will teleport as mario or enemies
            self.x = 0
            self.direc = 1
        if self.direc == 1:
            self.sprite = (self.sprite[0],0+ 8*(pyxel.frame_count%5), self.sprite[2], -8, self.sprite[4], 0)     #We want that it changes meanwhile they are moving
        if self.x < -16:
            self.x = 350                 #They will teleport as mario or enemies
            self.direc = -1
        if self.direc == -1:
            self.sprite = (self.sprite[0],0 + 8*(pyxel.frame_count%5), self.sprite[2], 8, self.sprite[4], 0)     #We want that it changes meanwhile they are moving
        self.x += self.direc

