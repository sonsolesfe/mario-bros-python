import pyxel
from mario import Mario
from plataformas import Plataformas
from plataformas import Tuberias
from plataformas import Coins
from enemies import Turtle, Crab,Butter
from plataformas import Pow
from plataformas import Floor

class Board:
    def __init__(self, width: int, length: int):
        """This is the init method in which we need a width and a length as atributes"""
        self.width = width
        self.length = length

        pyxel.init(self.width, self.length, title="Mario Bros", fps=30, display_scale=3)
        pyxel.load("dibus/resources.pyxres")
        pyxel.playm(0)

        #We create all the list in wich the enemies platforms... will be stored
        #In many times we will go througth the proper list

        self.__mario = Mario(0, 180)

        self.__floor = []
        for x in range(0, 357, 16):
            self.__floor.append(Floor(x, 210))

        self.__plataformas = [Plataformas(0,165),Plataformas(271,165),Plataformas(-35,120),
                              Plataformas(300,120),Plataformas(90,100),Plataformas(175,100),
                              Plataformas(0,48),Plataformas(272,48),Plataformas(42,165),Plataformas(229,165)]

        self.__pow = Pow(170,155)

        self.__tuberias= [Tuberias(0,188),Tuberias(309,188),Tuberias(0,13),Tuberias(310,13)]

        self.score = 0

        self.__enemies = []

        self.__coins = []

        pyxel.run(self.update, self.draw)

        self.current_platform = None
        self.current_floor = None

    @property
    def width(self) -> int:
        return self.__width

    @property
    def length(self) -> int:
        return self.__length

    @width.setter
    def width(self, width: int):
        self.__width = width

    @length.setter
    def length(self, length: int):
        self.__length = length

    @property
    def floor(self) -> list:
        return self.__floor

    @floor.setter
    def floor(self, floor: list):
        self.__floor = floor

    @property
    def plataformas(self) -> list:
        return self.__plataformas

    @plataformas.setter
    def plataformas(self, plataformas: list):
        self.__plataformas = plataformas

    @property
    def tuberias(self) -> list:
        return self.__tuberias

    @tuberias.setter
    def tuberias(self, tuberias: list):
        self.__tuberias = tuberias

    @property
    def enemies(self) -> list:
        return self.__enemies

    @enemies.setter
    def enemies(self, enemies: list):
        self.__enemies = enemies

    @property
    def coins(self) -> list:
        return self.__enemies

    @coins.setter
    def coins(self, coins: list):
        self.__coins = coins

    @property
    def score(self) -> int:
        return self.__score

    @score.setter
    def score(self, score: int):
        self.__score = score


    def update(self):
        """The update is the function that will be constantly invoked because it is invoked in each frame"""
        if pyxel.btnp(pyxel.KEY_Q):             #When we press the letter Q the game will finish
            pyxel.quit()
        elif pyxel.btn(pyxel.KEY_RIGHT):        #When we press the letter right mario will move to the right
                self.__mario.move('right', self.width)
        elif pyxel.btn(pyxel.KEY_LEFT):         #When we press the letter left mario will move to the left
                self.__mario.move('left', self.width)
        if pyxel.btnp(pyxel.KEY_UP) and  self.__mario.jumpable == True:    #When we press the letter up mario will move to the right
                self.__mario.jump()

        #We have used the frame count (that is something from pyxel)
        if pyxel.frame_count % 400 == 0:             #This is how we create the coins, they will appearing with the rest of the division frame and 400 is 0
            self.__coins.append(Coins(150,50,1))
        if pyxel.frame_count % 200 == 0:             #This is how we create the turtles, they will appearing with the rest of the division frame and 200 is 0
            self.__enemies.append(Turtle(60 , 68, -1))
        if pyxel.frame_count % 300 == 0:             #This is how we create the crabs, they will appearing with the rest of the division frame and 300 is 0
            self.__enemies.append(Crab(25, 180, 1))
        if pyxel.frame_count % 550 == 0:             #This is how we create the flies (named by butter), they will appearing with the rest of the division frame and 500 is 0
            self.__enemies.append(Butter(80,100,-1))


        #This to for loops have been created to apply to each enemy of the list the function of movement

        for enemy in self.__enemies:
            enemy.mover(self.length)

        for coin in self.__coins:
            coin.mover_coins(self.length)


        #This if will be constantly generating (because it is inside the update method)
        if self.__mario.air:                        #This is the way we manage mario to appply the gravity if he is in the air
            self.__mario.dy += 1                    #(because he has jumped or because he fall of a platforma)
            self.__mario.y += self.__mario.dy
            if self.__mario.y >= 200:
                self.__mario.air = False
                self.__mario.dy = 0
                self.__mario.y = 200
        if self.__mario.y < 200:
                self.__mario.air = True


        # We have done the same for the enemies, the way we manage to solve the problem is really similar
        for enemy in self.__enemies:
            if enemy.air:
                enemy.dy += 1
                enemy.y += enemy.dy
                if enemy.y >= 200:
                    enemy.air = False
                    enemy.dy = 0
                    enemy.y = 200
            if enemy.y < 200:
                    enemy.air = True


        # We have done the same for the coins, the way we manage to solve the problem is really similar
        for coin in self.__coins:
            if coin.air:
                coin.dy += 1
                coin.y += coin.dy
                if coin.y > 200:
                    coin.air = False
                    coin.dy = 0
                    coin.y = 200
            if coin.y < 200:
                    coin.air = True


        #In the following lines we are invoking the functions
        self.position_collision_plataformas(self.__mario)
        for enemy in self.__enemies:
            self.position_collision_plataformas(enemy)
        for coin in self.__coins:
            self.position_collision_plataformas(coin)

        self.position_collision_floor(self.__mario)
        for enemy in self.__enemies:
            self.position_collision_floor(enemy)
        for coin in self.__coins:
            self.position_collision_floor(coin)

        self.position_mario_collision_pow()
        self.mario_collision_tuberias()
        self.enemy_collision_tuberias()
        self.enemies_collision_enemies()
        self.mario_collision_enemies()
        self.coin_mario_collision()


    def collision_floor(self, object):
        """This function have been created to check if mario has touched the floor"""
        for floor in self.__floor:
            if (object.y + 24 > floor.y and object.y < floor.y + 8):            #If this conditions are satisfied, the function will return above
                    object.current_floor = floor
                    if object.dy > 0:
                        return "above"
    def position_collision_floor(self,object):
        """This function have been created to put the object that has touch the floor in a specific position,
        this is the way we manage if the return of the previous function was above"""
        if object == self.__mario:
            if self.collision_floor(object) == "above" and object.current_floor:
                    object.y = 210 -24
                    object.dy = 0
                    object.air = False                                #Thi is the position mario will take if it touches it
                    object.jumpable = True
        for enemy in self.__enemies:
            if object== enemy:
                if self.collision_floor(object) == "above" and object.current_floor:
                        object.y = 210 -16                      #We will change the position of the enemy
                        object.dy = 0                           #(that will be different from mario, because of the sprite)
                        object.air = False

        for coin in self.__coins:
            if object == coin:
                if self.collision_floor(object) == "above" and object.current_floor:
                        object.y = 210 -16                        #We have done the same with the coins
                        object.dy = 0
                        object.air = False

    def mario_collision_enemies(self):
        """This function is for the collision of mario with the enemies, we will check the entire list
        of the enemies"""
        for enemy in self.__enemies:
            if (enemy.x + 16 > self.__mario.x and enemy.x < self.__mario.x + 16
                and enemy.y + 16 > self.__mario.y and enemy.y < self.__mario.y + 24 and enemy.direc !=0):
                self.__mario.lifes -= 1
                self.__mario.x = 175                                  #If an enemy and mario has the same exact position that means that they are being in contact so
                self.__mario.y = 25                                   #we will rest a life of mario and we will teleport him to the top of the sreen

                if self.__mario.lifes == 0:
                    pyxel.quit()                         #If mario has no lifes we will finish the program

            elif enemy.direc == 0:              #This means that an enemy is dead
                if (enemy.x + 16 > self.__mario.x and enemy.x < self.__mario.x + 16
                        and enemy.y + 16 > self.__mario.y and enemy.y < self.__mario.y + 24):
                    self.__enemies.remove(enemy)                #If mario has the same position as a dead enemy, that enemy will dissapear from the list
                    self.score += 500                           #Moreover, we will add 500 points
    def enemies_collision_enemies(self):
        """This method is for the collision between enemies"""
        for i in range(len(self.__enemies)):
            for j in range(i + 1, len(self.__enemies)):   #We will go throught all the list and if they have the same position the are in contact
                enemy1 = self.__enemies[i]
                enemy2 = self.__enemies[j]
                if (enemy1.x + 16 > enemy2.x and enemy1.x < enemy2.x + 16
                        and enemy1.y + 24 > enemy2.y and enemy1.y < enemy2.y + 24):

                        enemy1.direc *= -1                 #Changing the direction of the enemy each one to a different one
                        enemy2.direc *= -1
    def collision_plataformas(self, object):
        """This function will check if the object is touching the platform from above or below"""
        for platform in self.__plataformas:
            if (object.y + 24 > platform.y and object.y < platform.y + 8):
                if(object.x +16 > platform.x and object.x < platform.x + 85):           #We go througth all the list of platforms
                    object.current_platform = platform                                  #If the object has positive gravity that means that is above
                    if object.dy > 0:                                                   #If the object has negative gravity that means that is below
                        return "above"
                    elif object.dy < 0:
                        return "below"

    def position_collision_plataformas(self, object):
        """This function have been created to put the object that has touch the platform in a specific position,
        this is the way we manage if the return of the previous function was above or below"""
        if object == self.__mario:
            if self.collision_plataformas(object) == "above" and object.current_platform:       #If this conditions are satisfied, mario will take a position above the platform
                    object.y = object.current_platform.y -24
                    object.dy = 0                                       #He will have no gravity and we have to put that he is not in the air
                    object.air = False
                    object.jumpable = True
            elif self.collision_plataformas(object) == "below" and object.current_platform:     #If this conditions are satisfied, mario will take the other one
                    object.y = object.current_platform.y +24
                    object.dy = 0                                       #Mario now has gravity because he is below
                    object.air = True
                    for enemy in self.__enemies:
                        if (enemy.x +16 > self.__mario.x and enemy.x < self.__mario.x +16
                            and enemy.y in range(self.__mario.y -40, self.__mario.y)) and enemy.direc != 0:    #For killing the enemies, if there is an enemy above the platform and
                            if not isinstance(enemy, Crab):                                                    #mario have touched the platform from below it will die (direction equal to 0)
                                enemy.direc = 0
                            if isinstance(enemy, Crab):
                                enemy.lifes_crab -=1
                                if enemy.lifes_crab == 0:
                                    enemy.direc = 0

                        elif (enemy.x +16 > self.__mario.x and enemy.x < self.__mario.x +16 and
                              enemy.y in range(self.__mario.y -40, self.__mario.y)) and enemy.direc == 0:
                            enemy.direc = -1                                                                #If there is an enemy already dead (direc = 0) and you kick it againg,
                            enemy.lifes_crab = 1                                                            #it will revive, we have added a life to the crabs


        for enemy in self.__enemies:
            if object== enemy:
                if self.collision_plataformas(object) == "above" and object.current_platform:
                        object.y = object.current_platform.y -16                                #If the enemies touched the platform (the onbly posibility is above)
                        object.dy = 0
                        object.air = False

        for coin in self.__coins:
            if object== coin:
                if self.collision_plataformas(object) == "above" and object.current_platform:       #If the coins touched the platform (the onbly posibility is above)
                        object.y = object.current_platform.y -16
                        object.dy = 0
                        object.air = False

    def coin_mario_collision(self):
        """method which handles collision of Mario with coins"""
        for coin in self.__coins:  # What we have done first is to go
            if (coin.x + 8 > self.__mario.x and coin.x < self.__mario.x + 16  # through the list of the coins and
                    and coin.y + 8 > self.__mario.y and coin.y < self.__mario.y + 24):  # check if Mario touches them, if this happens(conditions) they
                self.__coins.remove(coin)  # will disappear and the score will increased
                self.score += 500

    def mario_collision_tuberias(self):
        """This method handles collision between Mario and pipes"""
        for tuberia in self.__tuberias:
            if ( self.__mario.x + 16 > tuberia.x and self.__mario.x < tuberia.x + 47 and  # Here is done the same as in the method below
                    self.__mario.y + 24 > tuberia.y and self.__mario.y < tuberia.y + 19):
                if self.__mario.x > 175 and self.__mario.y > 150:
                    self.__mario.x = tuberia.x - 16
                if self.__mario.x < 175 and self.__mario.y > 150:
                    self.__mario.x = tuberia.x + 47

    def enemy_collision_tuberias(self):
        """This method handles collision between enemies and pipes"""
        for enemy in self.__enemies:  # With a for loop we have gone through the list of enemies
            if enemy.x > 298 and enemy.y > 180:  # checking if they collide with the pipes, and if this
                enemy.x = 51  # happened the enemies teleport.
                enemy.y = 25
            if enemy.x < 50 and enemy.y > 180:
                enemy.x = 305
                enemy.y = 25

    def mario_collision_pow(self):
        """This method handles collision between Mario and pow"""
        if (self.__mario.y + 24 > self.__pow.y and self.__mario.y < self.__pow.y + 17):
            if (self.__mario.x + 16 > self.__pow.x and self.__mario.x < self.__pow.x + 15):
                if self.__mario.dy > 0:  # Here we are just checking the position of Mario
                    return "above"  # and seeing if Mario collides with the pow form above or below.
                elif self.__mario.dy < 0:
                    return "below"

    def position_mario_collision_pow(self):
        """This method keep handling collision between enemies and pow"""
        if self.__pow.count_hits >= 3:  # First of all we will check if MArio has collide with
            self.__pow.dissapear = True  # the pow three times or less, and if it is the third time
            for enemy in self.__enemies:  # it will disappear and the enemies will stop.
                enemy.direc = 0
        elif self.mario_collision_pow() == "above":  # In the next conditions it is checked wether the MArio has collide from above or below,
            self.__mario.y = self.__pow.y - 24  # If the first thing happens it remains above the block, if the second thing happens
            self.__mario.dy = 0  # the sprite changes
            self.__mario.air = False
            self.__mario.jumpable = True
        elif self.mario_collision_pow() == "below":
            if self.__pow.count_hits == 0:
                self.__mario.y = self.__pow.y + 24
            if self.__pow.count_hits == 1:
                self.__mario.y = self.__pow.y + 24 - 3
            if self.__pow.count_hits == 2:
                self.__mario.y = self.__pow.y + 24 - 7
            self.__pow.count_hits += 1
            self.__mario.dy = 0

    def draw(self):
        """This method draws the game elements using Pixels graphics functions"""
        pyxel.cls(0)
        pyxel.text(60, 10, str(pyxel.frame_count), 14)  # This lines draws text on the screen.
        pyxel.text(250, 5, "Score  " + str(self.score), 7)  # This lines draws an image on the screen
        pyxel.text(100, 5, "Lifes " + str(self.__mario.lifes), 7)
        pyxel.blt(self.__mario.x, self.__mario.y, *self.__mario.sprite)

        for enemy in self.__enemies:  # with all this for loops we go through the different lists
            pyxel.blt(enemy.x, enemy.y,
                      *enemy.sprite)  # created at the begining and we set different sprites for each object.
        for cube in self.__floor:
            pyxel.blt(cube.x, cube.y, *cube.sprite)
        for tuberia in self.__tuberias:
            if self.__tuberias[2] == tuberia:
                pyxel.blt(tuberia.x, tuberia.y, *tuberia.sprite_arriba)
            elif self.__tuberias[3] == tuberia:
                pyxel.blt(tuberia.x, tuberia.y, *tuberia.sprite_arriba2)
            else:
                pyxel.blt(tuberia.x, tuberia.y, *tuberia.sprite)

        for platform in self.__plataformas:
            pyxel.blt(platform.x, platform.y, *platform.sprite)

        if not self.__pow.dissapear:
            if self.__pow.count_hits == 0:  # Here the image of the pow changes
                pyxel.blt(self.__pow.x, self.__pow.y,
                          *self.__pow.sprite)  # depending on the number of collisions that Mario has
            if self.__pow.count_hits == 1:  # done with the pow block
                pyxel.blt(self.__pow.x, self.__pow.y, *self.__pow.hit1_sprite)
            if self.__pow.count_hits == 2:
                pyxel.blt(self.__pow.x, self.__pow.y, *self.__pow.hit2_sprite)

        for coin in self.__coins:
            pyxel.blt(coin.x, coin.y, *coin.sprite)