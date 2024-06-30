import pygame
import math 
import time 

global state
state=0
global score 
score=0
def to_radians(angles):
    return math.radians(angles)
class wheel:
    def __init__(self) :
        self.radius=0
        self.angle=0
        self.c_x=0
        self.c_y=0
        self.spin_x=0
        self.spin_y=0
        self.spin_width=0
        self.wh_color=(150,150,150)
        self.sp_color=(50,50,50)
    
    def update(self,main_x,main_y,rad,wide):
        self.c_x= main_x 
        self.c_y= main_y 
        self.radius=rad
        self.spin_width=wide 
    def spin(self,a,angle_radians):
        self.spin_x=self.c_x + self.radius * 1* pygame.math.Vector2(math.cos(angle_radians),math.sin(angle_radians)).rotate(a).x 
        self.spin_y=self.c_y + self.radius * 1* pygame.math.Vector2(math.cos(angle_radians),math.sin(angle_radians)).rotate(a).y 
        
    def show(self,screen,a):
        pygame.draw.circle(screen,self.wh_color,(self.c_x,self.c_y),self.radius) 
        self.spin(a,to_radians(0))
        pygame.draw.line(screen,self.sp_color,(self.c_x,self.c_y),(self.spin_x,self.spin_y),self.spin_width)        
        self.spin(a,to_radians(60))
        pygame.draw.line(screen,self.sp_color,(self.c_x,self.c_y),(self.spin_x,self.spin_y),self.spin_width) 
        self.spin(a,to_radians(120))
        pygame.draw.line(screen,self.sp_color,(self.c_x,self.c_y),(self.spin_x,self.spin_y),self.spin_width)
        self.spin(a,to_radians(180))
        pygame.draw.line(screen,self.sp_color,(self.c_x,self.c_y),(self.spin_x,self.spin_y),self.spin_width)
        self.spin(a,to_radians(240))
        pygame.draw.line(screen,self.sp_color,(self.c_x,self.c_y),(self.spin_x,self.spin_y),self.spin_width)
        self.spin(a,to_radians(300))
        pygame.draw.line(screen,self.sp_color,(self.c_x,self.c_y),(self.spin_x,self.spin_y),self.spin_width)

class belt:
    
    def __init__(self):
        self.belt_x=0
        self.belt_y=0
        self.width=0
        self.height=0
        self.color=(100,100,100)
        self.radius=0
        self.semi_color=(100, 100, 100)
    
    def update(self,x,y,w,d,r):
        self.belt_x=x
        self.belt_y=y
        self.width=w 
        self.height=d 
        self.radius=r 
        
    def semicircle(self,screen, center_x, center_y, radius, start_angle, end_angle, width, color):
        num_points = 100
        points = []
        for i in range(num_points):
            angle_rad = math.radians(start_angle + (end_angle - start_angle) * i / num_points)
            points.append((center_x + radius * math.cos(angle_rad), center_y + radius * math.sin(angle_rad)))
        pygame.draw.lines(screen, color, False, points, width)
    
    def belt_show(self):
        pygame.draw.rect(screen, self.color, (self.belt_x, self.belt_y-2, self.width, self.height))
        pygame.draw.rect(screen, self.color, (self.belt_x-5, self.belt_y-(2*self.radius)-2, self.width+10, self.height))
        self.semicircle(screen, w1.c_x, w1.c_y, w1.radius, 90, 270, 5, self.semi_color)
        self.semicircle(screen, w2.c_x, w2.c_y, w2.radius, 90, -90, 5, self.semi_color)

class dustbin:
    
    def __init__(self,x,y,w,d):
        self.bin_x=x
        self.bin_y=y 
        self.bin_width=w
        self.bin_height=d 
        self.bin_areas={
            'organic': pygame.Rect(x-300, y+400, w, d),      
            'recyclable': pygame.Rect(x-150, y+400, w, d),   
            'non_biodegradable': pygame.Rect(x, y+400, w, d), 
            'hazardous': pygame.Rect(x+150, y+400, w, d)   
        }
    
    def line_show(self,screen,mouse_pos):
        global state
        global score
        for c,a in self.bin_areas.items():
            if a.collidepoint(mouse_pos):
                if c=='organic':
                    # print("st:",state)
                    state=1
                    pygame.draw.line(screen, (0, 0, 255), (w2.c_x+65, w2.c_y-w2.radius+20), (a.centerx,a.top), 5)
                elif c=='recyclable':
                    state=2
                    pygame.draw.line(screen, (0, 255, 0), (w2.c_x+50, w2.c_y-w2.radius+10), (a.centerx,a.top), 5)
                elif c=='non_biodegradable':
                    state=3
                    pygame.draw.line(screen, (255, 255, 0), (w2.c_x+45, w2.c_y-w2.radius+7), (a.centerx,a.top), 5)
                elif c=='hazardous':
                    state=4
                    pygame.draw.line(screen, (255, 0, 0), (w2.c_x+35, w2.c_y-w2.radius+2.5), (a.centerx,a.top), 5)
            
    def show(self,screen):
        # pygame.draw.line(screen, (0, 255, 0), (w2.c_x+40, w2.c_y-w2.radius+5), (w2.c_x+250, w2.c_y), 5)
        for c,a in self.bin_areas.items():
            if c=='organic':
                pygame.draw.rect(screen, (0, 0, 255), a, 2)
            elif c=='recyclable':
                pygame.draw.rect(screen, (0, 255, 0), a, 2)
            elif c=='non_biodegradable':
                pygame.draw.rect(screen, (255, 255, 0), a, 2)
            elif c=='hazardous':
                pygame.draw.rect(screen, (255, 0, 0), a, 2)

class panda:
    def __init__(self,x,y,d):
        # self.image_x=x
        # self.image_y=y 
        self.identity=d 
        self.state=0
        self.count=0
        self.angle=-90
        self.rotate_angle=0
        self.x=x
        self.y=y
        self.image=pygame.image.load("materials/bone1.png")
        self.rect=self.image.get_rect()
    
    def show(self,screen):
        global state
        global score 
        if self.x==200 and self.y<370:
            self.y+=6
            self.rect.topleft=(self.x,self.y)
            screen.blit(self.image,self.rect)
        elif self.y>369 and self.y<374 and self.x<1100:
            self.x+=8
            self.rect.topleft=(self.x,self.y)
            screen.blit(self.image,self.rect)
        elif self.count==0 and self.state==0:
            self.count+=1
            self.state=state
            if self.identity==self.state:
                score+=10
            else:
                score-=10
        elif self.state==1 and self.x<1350:
            # if self.x<1400:
            #     self.x = w2.c_x + w2.radius * math.cos((self.angle))
            #     self.y = w2.c_y + w2.radius * math.sin(self.angle)
            #     r_image=pygame.transform.rotate(self.image, -math.degrees(angle))
            #     r_rect=r_image.get_rect()
            #     screen.blit(r_image,r_rect)
            #     self.angle+=1
            # else:
            slope=(800-self.y)/(1350-self.x)
            self.x+=6
            self.y+=(6*slope)
            self.rect.topleft=(self.x,self.y)
            screen.blit(self.image,self.rect)
            pygame.draw.line(screen, (0, 0, 255), (w2.c_x+65, w2.c_y-w2.radius+20), (1350,800), 5)
        elif self.state==2 and self.x<1500:
            slope=(800-self.y)/(1500-self.x)
            self.x+=9
            self.y+=(9*slope)
            self.rect.topleft=(self.x,self.y)
            screen.blit(self.image,self.rect)
            pygame.draw.line(screen, (0, 255, 0), (w2.c_x+50, w2.c_y-w2.radius+10), (1500,800), 5)
        elif self.state==3 and self.x<1650:
            slope=(800-self.y)/(1650-self.x)
            self.x+=12
            self.y+=(12*slope)
            self.rect.topleft=(self.x,self.y)
            screen.blit(self.image,self.rect)
            pygame.draw.line(screen, (255, 255, 0), (w2.c_x+45, w2.c_y-w2.radius+7), (1650,800), 5)
        elif self.state==4 and self.x<1800:
            slope=(800-self.y)/(1800-self.x)
            self.x+=15
            self.y+=(15*slope)
            self.rect.topleft=(self.x,self.y)
            screen.blit(self.image,self.rect)
            pygame.draw.line(screen, (255, 0, 0), (w2.c_x+35, w2.c_y-w2.radius+2.5), (1800,800), 5)
        elif self.state==0:
            # self.y+=4
            if self.y<600:
                # self.rotate_angle = math.degrees(math.atan2(w2.c_y - self.y, w2.c_x - self.x)) - 90
                self.x = w2.c_x + (w2.radius) * math.cos(to_radians(self.angle))
                self.y = w2.c_y + (w2.radius+25) * math.sin(to_radians(self.angle))
                # rotated_image = pygame.transform.rotate(self.image, self.rotate_angle)
                # rotated_rect = rotated_image.get_rect(center=self.rect.center)
                # screen.blit(rotated_image, rotated_rect.topleft)
            else:
                self.x-=4
            self.rect.topleft=(self.x,self.y)
            screen.blit(self.image,self.rect)
            self.angle+=5
        else:
            # once verify the final condition
            self.x=1850
        
pygame.init()

width=1920
height=1080
screen = pygame.display.set_mode((width,height))
clock=pygame.time.Clock()
# for running pandas
timer=0
interval=1.5

# for controlling the state
state_timer=0

angle=0
run=True

# wheels initialisation
w1=wheel()
w1.update((200),(500),100,5)
w2=wheel()
w2.update((1100),(500),100,5)
b1=belt()
# belt 
b1.update(w1.c_x,w1.c_y+100,900,5,100)
d=dustbin(w2.c_x+500, 400, 100, 100)

# pandas intializing
# p=panda(200,0,2)
pandas = []
pandas.append(panda(200, 0,3)) 
# pandas.append(panda(200, 100)) 
while run:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False 
        elif event.type==pygame.MOUSEBUTTONDOWN:
            pos=pygame.mouse.get_pos()
            d.line_show(screen,pos)
   
    w1.show(screen,angle)
    w2.show(screen,angle)
    b1.belt_show()
    d.show(screen) # Add first panda
    # p.show(screen)
    for p in pandas:  
        p.show(screen)
        if p.x>=1850:
            pandas.remove(p)
        elif p.x<=1130 and p.y>=600:
            pandas.remove(p)
    # print(len(pandas))
    font = pygame.font.SysFont(None, 36)  # Choose a font and size
    score_text = font.render("Score: " + str(score), True, (0, 0, 0))  # Render the score text
    screen.blit(score_text, (10, 10))  # Display the score text on the screen
    pand_count=font.render('panda_no: '+str(len(pandas)),True,(0,0,0))
    screen.blit(pand_count,(300,10))
    timer += clock.get_time() / 1000 
    if timer>=interval:
        pandas.append(panda(200,0,3))
        timer=0
    # state_timer+
    # if state_timer>=(in)    
    if state_timer>=70:
        state_timer=0
        state=0
    state_timer+=1
    pygame.display.update()
    angle+=5
    clock.tick(60) 