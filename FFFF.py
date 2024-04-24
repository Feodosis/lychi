from random import randint

from pygame import *
mixer.init()
mixer.music.load("mp3rington_club_id_16140.mp3")
mixer.music.play()
# fire_sound = mixer.Sound()
img_back = "65e9f93db0799.jpg"
img_hero = "65e9f9072ba18.png"
img_bullet = "kisspng-bowling-ball-ten-pin-bowling-real-bowling-5aa257a9ddaa75.318842411520588713908 (1).jpg "
img_enemy = "65e9f8f545f4e.png"
img_enemy2 = "png-clipart-baseball-cap-hat-swim-caps-baseball-cap-hat-black-thumbnail-removebg-preview (1).png"
img_hill = "1979145_ca622.png"
img_hill2 = "banan.png"
score = 0
lost = 0
max_lost = 3


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_wigth - 80:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet(img_bullet, self.rect.centerx, self.rect.top, 15, 20, -15)
        bullets.add(bullet)
class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_wigth - 80)
            self.rect.y = -10
            lost += 1
win_wigth = 700
win_height = 500
display.set_caption("Shooter")
window = display.set_mode((win_wigth, win_height))
background = transform.scale(image.load(img_back), (win_wigth, win_height))

ship = Player(img_hero, 5, win_height - 100, 80, 100, 10)
bullets = sprite.Group()
monsters = sprite.Group()
for i in range(1, 6):
    monster = Enemy(img_enemy, randint(80, win_wigth-80), -60, 80, 50, randint(1,5))
    monsters.add(monster)
for i in range(1, 6):
    monster = Enemy(img_enemy2, randint(80, win_wigth-80), -60, 80, 90, randint(1,5))
    monsters.add(monster)
for i in range(1, 6):
    monster = Enemy(img_hill, randint(80, win_wigth-80), -60, 80, 90, randint(1,5))
    monsters.add(monster)
for i in range(1, 6):
    monster = Enemy(img_hill2, randint(80, win_wigth-80), -60, 80, 50, randint(1,5))
    monsters.add(monster)
font.init()
font1 = font.SysFont('Arial', 70)
font1 = font.Font(None, 80)
font2 = font.Font(None, 36)
win = font1.render("You win!", True, (255, 255, 255))
lose = font1.render("You lose!", True, (180, 0, 0))
goal = 15
life = 3
max_fire = 5
real_time = False
num_fire = 0
from time import time as timer




finish = False
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key  == K_SPACE:
                # if num_fire < max_fire and real_time == False:
                #     num_fire += 1
                    ship.fire()
                    #fire_sound.play()
                # if num_fire >= max_fire and real_time == False:
                #     real_time = True
                #     last_time = timer()


    if not finish:
        window.blit(background, (0, 0))
        ship.update()
        bullets.update()
        monsters.update()
        text = font2.render("Рахунок:"+str(score), True, (255, 255, 255))
        window.blit(text, (10, 20))
        text_lose = font2.render("Пропущено:"+str(lost), True, (255, 255, 255))
        window.blit(text_lose, (10,50))

        ship.reset()
        bullets.draw(window)
        monsters.draw(window)
        collides = sprite.groupcollide(monsters, bullets, True, True)
        for c in collides:
            score += 1
            monster = Enemy(img_enemy, randint(80, win_wigth-80), -40, 80, 50, randint(1, 5))
        monsters.add(monster)
        if real_time == True:
            now_time = timer()
            # if now_time - last_time < 3:
            #     reload = font2.render("Wait, reload....", True, (150, 0, 0))
            #     window.blit(reload, (260, 460))
        if sprite.spritecollide(ship, monsters, False):
            sprite.spritecollide(ship, monsters, True)
            life -= 1
        if life == 0 or lost >= max_lost:
            finish = True
            window.blit(lose, (200, 200))
        if score >= goal:
            finish = True
            window.blit(win, (200, 200))
        if life == 3:
            life_color = (0, 150, 0)
        if life == 2:
            life_color = (150, 150, 0)
        if life == 1:
            life_color = (150, 0, 0)
        text_life = font1.render(str(life), True, life_color)
    else:
        time.delay(3000)
        score = 0
        lost = 0
        life = 3
        num_fire = 0
        finish = False
        real_time = False
        for b in bullets:
            b.kill()
        for m in monsters:
            m.kill()
        for i in range(1,6):
            monster = Enemy(img_enemy, randint(50, win_wigth - 80,), -60, 80, 50, randint(1,5))
        monsters.add(monster)
        for i in range(1,6):
            monster = Enemy(img_enemy2, randint(50, win_wigth - 80,), -60, 80, 90, randint(1,5))
        monsters.add(monster)
        for i in range(1,6):
            monster = Enemy(img_hill, randint(50, win_wigth - 80,), -60, 80, 90, randint(1,5))
        monsters.add(monster)
        for i in range(1,6):
            monster = Enemy(img_hill2, randint(50, win_wigth - 80,), -60, 80, 50, randint(1,5))
        monsters.add(monster)
        # else:
        #         num_fire = 0



    display.update()
    time.delay(50)