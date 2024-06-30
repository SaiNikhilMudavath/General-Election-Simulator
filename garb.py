import pygame
import math 
import random
import time 

global state
state=0
global score 
score=0

main_array=["materials/green/","materials/blue/","materials/red/","materials/yellow/"]
green_array=["flower.jpg","foodwaste.jpg","meat.jpg","peels.jpg"]
blue_array=["cardboard.jpg","foodtins.jpg","glassbottles.jpg","newspaper.jpg","tetrapack.jpg"]
red_array=["bodyfluid.jpg","cotton.jpg","sanitarytissues.jpg","surgknife.jpg","syringe.jpg"]
yellow_array=["battery1.png","cleaning.png","deodrant.jpg","paint.jpg","pestisides.jpg"]

show_dict={
    "materials/green/flower.jpg":"cut flowers", "materials/green/foodwaste.jpg":"plate scrapings", 
    "materials/green/meat.jpg":"meat and bones" , "materials/green/peels.jpg":"vegetable peelings",
    "materials/blue/cardboard.jpg":"cardboard", "materials/blue/foodtins.jpg":"food tins",
    "materials/blue/glassbottles.jpg":"glass bottles","materials/blue/newspaper.jpg":"newspaper","materials/blue/tetrapack.jpg":"tetra pack packaging",
    "materials/red/bodyfluid.jpg":"body fluid","materials/red/cotton.jpg":"cotton dressings",
    "materials/red/sanitarytissues.jpg":"sanitary napkins","materials/red/surgknife.jpg":"surgical knives","materials/red/syringe.jpg":"syringes",
    "materials/yellow/battery1.png":"battery","materials/yellow/cleaning.png":"cleaning liquids",
    "materials/yellow/deodrant.jpg":"deodrant bottle","materials/yellow/paint.jpg":"paint","materials/yellow/pestisides.jpg":"pestisides"
}

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
    
    def belt_show(self,screen,w1,w2):
        pygame.draw.rect(screen, self.color, (self.belt_x, self.belt_y-2, self.width, self.height))
        pygame.draw.rect(screen, self.color, (self.belt_x-5, self.belt_y-(2*self.radius)-2, self.width+10, self.height))
        self.semicircle(screen, w1.c_x, w1.c_y, w1.radius, 90, 270, 5, self.semi_color)
        self.semicircle(screen, w2.c_x, w2.c_y, w2.radius, 90, -90, 5, self.semi_color)

class dustbin:
    
    def __init__(self,x,y,w,d,w2):
        self.bin_x=w2.c_x+x
        self.bin_y=w2.c_y+y 
        self.bin_width=w
        self.bin_height=d 
        self.bin_areas={
            'organic': pygame.Rect(self.bin_x, self.bin_y, w, d),      
            'recyclable': pygame.Rect(self.bin_x+200, self.bin_y, w, d),   
            'non_biodegradable': pygame.Rect(self.bin_x+400, self.bin_y, w, d), 
            'hazardous': pygame.Rect(self.bin_x+600, self.bin_y, w, d)   
        }
    
    def line_show(self,screen,mouse_pos,w2):
        global state
        global score
        for c,a in self.bin_areas.items():
            if a.collidepoint(mouse_pos):
                if c=='organic':
                    # print("st:",state)
                    state=1
                    pygame.draw.line(screen, (0, 255, 0), (w2.c_x+65, w2.c_y-w2.radius+20), (a.centerx,a.top), 5)
                elif c=='recyclable':
                    state=2
                    pygame.draw.line(screen, (0, 0, 255), (w2.c_x+50, w2.c_y-w2.radius+10), (a.centerx,a.top), 5)
                elif c=='non_biodegradable':
                    state=3
                    pygame.draw.line(screen, (255, 255, 0), (w2.c_x+45, w2.c_y-w2.radius+7), (a.centerx,a.top), 5)
                elif c=='hazardous':
                    state=4
                    pygame.draw.line(screen, (255, 0, 0), (w2.c_x+35, w2.c_y-w2.radius+2.5), (a.centerx,a.top), 5)
            
    def show(self,screen):
        # pygame.draw.line(screen, (0, 255, 0), (w2.c_x+40, w2.c_y-w2.radius+5), (w2.c_x+250, w2.c_y), 5)
        blue_bin=pygame.image.load("bins/bluedustbin.jpg")
        green_bin=pygame.image.load("bins/greenbin.jpg")
        yellow_bin=pygame.image.load("bins/yellowbin.jpg")
        red_bin=pygame.image.load("bins/redbin.jpg")
        for c,a in self.bin_areas.items():
            if c=='organic':
                # pygame.draw.rect(screen, (0, 255, 0), a, 2)
                screen.blit(green_bin,a)
            elif c=='recyclable':
                # pygame.draw.rect(screen, (0, 0, 255), a, 2)
                screen.blit(blue_bin,a)
            elif c=='non_biodegradable':
                # pygame.draw.rect(screen, (255, 255, 0), a, 2)
                screen.blit(yellow_bin,a)
            elif c=='hazardous':
                # pygame.draw.rect(screen, (255, 0, 0), a, 2)
                screen.blit(red_bin,a)

class panda:
    def __init__(self,x,y,d,p):
        # self.image_x=x
        # self.image_y=y 
        self.rotate_radius=0
        self.identity=d 
        self.state=0
        self.count=0
        self.image_address=p
        self.angle=-90
        self.rotate_angle=0
        self.x=x
        self.y=y
        self.image=pygame.image.load(p)
        self.rect=self.image.get_rect()
    
    def show(self,screen,w2,d):
        global state
        global score 
        if self.x==200 and self.y<350:
            self.y+=6
            self.rect.center=(self.x,self.y)
            screen.blit(self.image,self.rect)
        elif self.y>=350 and self.y<374 and self.x<w2.c_x:
            self.x+=8
            self.rotate_radius=w2.c_y-self.y
            self.rect.center=(self.x,self.y)
            font = pygame.font.SysFont(None, 36)
            namedisplay = font.render(str("GARBAGE ITEM: "+show_dict[self.image_address]), True, (0, 0, 0))  # Render the score text
            screen.blit(namedisplay, (800, 150))  # Display the score text on the screen
            screen.blit(self.image,self.rect)
            if self.count==0 and self.state==0 and self.x>w2.c_x-100:
                self.count+=1
                self.state=state
                if self.identity==self.state:
                    score+=1
                # else:
                #     score-=10
        elif self.state==1 and self.x<d.bin_x+75:
            # if self.x<1400:
            #     self.x = w2.c_x + w2.radius * math.cos((self.angle))
            #     self.y = w2.c_y + w2.radius * math.sin(self.angle)
            #     r_image=pygame.transform.rotate(self.image, -math.degrees(angle))
            #     r_rect=r_image.get_rect()
            #     screen.blit(r_image,r_rect)
            #     self.angle+=1
            # else:
            slope=(d.bin_y-self.y)/(d.bin_x+75-self.x)
            self.x+=6
            self.y+=(6*slope)
            self.rect.center=(self.x,self.y)
            screen.blit(self.image,self.rect)
            pygame.draw.line(screen, (0, 255, 0), (w2.c_x+65, w2.c_y-w2.radius+20), (d.bin_x+75,d.bin_y), 5)
        elif self.state==2 and self.x<d.bin_x+275:
            slope=(d.bin_y-self.y)/(d.bin_x+275-self.x)
            self.x+=9
            self.y+=(9*slope)
            self.rect.center=(self.x,self.y)
            screen.blit(self.image,self.rect)
            pygame.draw.line(screen, (0, 0, 255), (w2.c_x+50, w2.c_y-w2.radius+10), (d.bin_x+275,d.bin_y), 5)
        elif self.state==3 and self.x<d.bin_x+475:
            slope=(d.bin_y-self.y)/(d.bin_x+475-self.x)
            self.x+=12
            self.y+=(12*slope)
            self.rect.topleft=(self.x,self.y)
            screen.blit(self.image,self.rect)
            pygame.draw.line(screen, (255, 255, 0), (w2.c_x+45, w2.c_y-w2.radius+7), (d.bin_x+475,d.bin_y), 5)
        elif self.state==4 and self.x<d.bin_x+675:
            slope=(d.bin_y-self.y)/(d.bin_x+675-self.x)
            self.x+=15
            self.y+=(15*slope)
            self.rect.topleft=(self.x,self.y)
            screen.blit(self.image,self.rect)
            pygame.draw.line(screen, (255, 0, 0), (w2.c_x+35, w2.c_y-w2.radius+2.5), (d.bin_x+675,d.bin_y), 5)
        elif self.state==0:
            # self.y+=4
            if self.y<610:
                # self.rotate_angle = math.degrees(math.atan2(w2.c_y - self.y, w2.c_x - self.x)) - 90
                self.x = w2.c_x + (self.rotate_radius) * math.cos(to_radians(self.angle))
                self.y = w2.c_y + (self.rotate_radius) * math.sin(to_radians(self.angle))
                # rotated_image = pygame.transform.rotate(self.image, self.rotate_angle)
                # rotated_rect = rotated_image.get_rect(center=self.rect.center)
                # screen.blit(rotated_image, rotated_rect.topleft)
            else:
                self.x-=4
            self.rect.center=(self.x,self.y)
            screen.blit(self.image,self.rect)
            self.angle+=5
        else:
            # once verify the final condition
            self.x=1850

    
def create_panda():
    selected_bin= random.choice(main_array)
    if selected_bin=="materials/green/":
        selected_garbage=random.choice(green_array)
        return panda(200,0,1,(selected_bin+selected_garbage))
    elif selected_bin=="materials/blue/":
        selected_garbage=random.choice(blue_array)
        return panda(200,0,2,(selected_bin+selected_garbage))
    elif selected_bin=="materials/red/":
        selected_garbage=random.choice(red_array)
        return panda(200,0,4,(selected_bin+selected_garbage))
    elif selected_bin=="materials/yellow/":
        selected_garbage=random.choice(yellow_array)
        return panda(200,0,3,(selected_bin+selected_garbage))
    
pygame.init()

# width=1920
# height=1080
# screen = pygame.display.set_mode((width,height))

# pandas.append(panda(200, 100)) 
def main(screen,inter):
    global score
    global state
    clock=pygame.time.Clock()
    # for running pandas
    timer=0
    interval=inter

    # for controlling the state
    state_timer=0

    angle=0
    run=True

    # wheels initialisation
    w1=wheel()
    w1.update((200),(500),100,5)
    w2=wheel()
    w2.update((900),(500),100,5)
    b1=belt()
    # belt 
    b1.update(w1.c_x,w1.c_y+100,700,5,100)
    d=dustbin(250, 300, 150, 150,w2)

    # pandas intializing
    # p=panda(200,0,2)
    pandas = []
    pandas.append(create_panda()) 
    while run:
        screen.fill((255,255,255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False 
            elif event.type==pygame.MOUSEBUTTONDOWN:
                pos=pygame.mouse.get_pos()
                d.line_show(screen,pos,w2)
    
        w1.show(screen,angle)
        w2.show(screen,angle)
        b1.belt_show(screen,w1,w2)
        d.show(screen) # Add first panda
        # p.show(screen)
        for p in pandas:  
            p.show(screen,w2,d)
            if p.x>=1850:
                pandas.remove(p)
            elif p.x<=900 and p.y>=600:
                pandas.remove(p)
        # print(len(pandas))
        font = pygame.font.SysFont(None, 36)  # Choose a font and size
        score_text = font.render("SCORE: " + str(score), True, (0, 0, 0))  # Render the score text
        screen.blit(score_text, (900, 50))  # Display the score text on the screen
        # pand_count=font.render('panda_no: '+str(len(pandas)),True,(0,0,0))
        # screen.blit(pand_count,(300,10))
        timer += clock.get_time() / 1000 
        if timer>=interval:
            pandas.append(create_panda())
            timer=0
        # state_timer+
        # if state_timer>=(in)    
        if state_timer>=90:
            state_timer=0
            state=0
        state_timer+=1
        pygame.display.update()
        angle+=5
        clock.tick(60) 
        
