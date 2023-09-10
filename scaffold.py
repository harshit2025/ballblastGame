import pygame
import random
import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)

cap = cv2.VideoCapture(0)
cap.set(3, 1200)
cap.set(4, 600)


pygame.init()
screenWidth = 1200
screenHeight = 600
count = 0
pygame.display.set_caption("Ball Blast")
win = pygame.display.set_mode((screenWidth, screenHeight))

#Load an cannon image and create a pygame object
cannon_obj = pygame.image.load('cannon.png')
cannon_obj = pygame.transform.scale(cannon_obj, (70, 100))

#Set Backgroung image
bg = pygame.image.load('background.png')
bg = pygame.transform.scale(bg, (1200 , 600))

#Load a ball image and create a pygame object
enemy = pygame.image.load('ball.png')


score = 0
clock = pygame.time.Clock()
font = pygame.font.SysFont("comicsans", 30, True)
GRAVITY = .2
flag = False



class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.isJump = False
        self.jumpCount = 10
        self.vel = 15
        self.hitbox = pygame.Rect(self.x + 5 , self.y +15, width, height)

    def draw(self, window):
        window.blit(cannon_obj, (self.x, self.y))
        self.hitbox.x = self.x
        self.hitbox.y = self.y

    def hit(self):
        self.x = 50
        self.y = screenHeight - self.height
        font1 = pygame.font.SysFont('comicsans', 100)
        text = font1.render('Game Over', 1, (255, 0, 0))
        win.blit(text, (600 - (text.get_width() / 2), 200))
        pygame.display.update()
        i = 0
        while i < 200:
            pygame.time.delay(10)
            i += 1







class Ball(object):
    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.health = random.randint(60 , 120)
        self.enemy = pygame.transform.scale(enemy, (self.health,self.health))
        self.width = self.health
        self.height = self.health
        self.hit_box = pygame.Rect(self.x, self.y, self.width, self.height)
        self.visible = True
        self.dx = dx
        self.dy = dy

    def draw(self, window):
        if self.visible:

            window.blit(self.enemy, (self.x, self.y))
            self.move()
            self.hit_box.x = self.x
            self.hit_box.y = self.y

        if not self.visible:
            self.hit_box = (1000, 1900, 5, 5)

    def move(self):
        if self.hit_box[1] < 0:
            self.y = self.y + 20
            self.dy *= -1
        if self.hit_box[1] + 120 > screenHeight:
            self.y = self.y - 20
            self.dy *= -1    
        if self.hit_box[0] < 15 or self.hit_box[0] + self.hit_box[3] +15 > screenWidth:
            self.dx *= -1

        self.x += self.dx
        self.y += self.dy
        self.dy += GRAVITY

    def hit(self):
        if self.health > 50:
            self.health -= 1
            self.width = self.health
            self.height = self.health
            self.x -= 0.5
            self.y -= 0.5
            self.hit_box = pygame.Rect(self.x , self.y, self.width, self.height)
            self.enemy = pygame.transform.scale(enemy, (self.health,self.health))
        else:
            self.visible = False

    def hit_player(self):
        self.x = random.randint(0, screenWidth - 140)
        self.y = random.randint(0, (screenHeight//2)-100)




class Projectile(object):
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.vel = -10

    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)

    def move(self):
        self.y += self.vel






def redraw_game_window(projectiles, balls):
    win.blit(bg, (0, 0))
    #draw cannon
    #draw projectiles
    #draw balls
    text = font.render("Score: " + str(score), 1, (0, 0, 0))
    win.blit(text, (screenWidth // 2 - 55, 10))
    pygame.display.update()









# Main Loop
cannon = #create a player (cannon) object at bottom center
prev = curr = screenWidth//2
bullets = []
targets = list(#create a Ball object at random point in the window)
    
run = True
new_ball_timer = 1.0
while run:
    time_delta = clock.tick(30)/1000.0
    if new_ball_timer > 0.0:
        new_ball_timer -= time_delta
    else:
        new_ball_timer = 1.0
        targets.append(#create a Ball object at random point in the window)

    for target in targets:
        if cannon.hitbox.colliderect(target.hit_box):
            cannon.hit()
            target.hit_player()
            score = 0
            cannon = Player(screenWidth//2, screenHeight - cannon_obj.get_height(), cannon_obj.get_width(), cannon_obj.get_height())
            bullets = []
            targets = [Ball(random.randint(0, screenWidth - 140),
            random.randint(0, (screenHeight//2)-100),
            random.randint(1, 2), 1)]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    bullets.append(Projectile(round(cannon.x + cannon.width // 2), round(cannon.y), 6, (0, 0, 0)))
    bullets.append(Projectile(round((cannon.x + cannon.width // 2) +10), round(cannon.y), 6, (0, 0, 0)))
    bullets.append(Projectile(round((cannon.x + cannon.width // 2) -10), round(cannon.y), 6, (0, 0, 0)))


   #write code for moving bullets 

    for bullet in bullets:
        for target in targets:
            if #write condition for colliding in y direction:
                if #write condition for colliding in x direction:
                    target.hit()
                    score = score+1
                    if(not target.visible):
                        #pop the target from targets
                    #pop the bullet from bullets
                    flag = True
                    break

        if(not flag):
            if 0 < bullet.y < 600:
                bullet.move()
            else:
                bullets.pop(bullets.index(bullet))
        flag = False        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and cannon.x > cannon.vel:
        cannon.x -= cannon.vel
    if keys[pygame.K_RIGHT] and cannon.x < screenWidth - cannon.width:
        cannon.x += cannon.vel

    success, img = cap.read()
    imageHeight, imageWidth, _ = img.shape
    img.flags.writeable = False
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(cv2.flip(img, 1))
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                img,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style())

            handlist = hand_landmarks

        for point in mp_hands.HandLandmark:
            if point.value == 8:
                normalizedLandmark = hand_landmarks.landmark[point]
                cur = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)[0]
                break
        print(cur)  
        dis = cur-prev
        prev = cur
        #write your code snippet to move cannon according to the prev and cur position of your index finger
    cv2.imshow('MediaPipe Hands', cv2.cvtColor(cv2.flip(img, 1), cv2.COLOR_RGB2BGR))
    #redraw the game window

pygame.quit()