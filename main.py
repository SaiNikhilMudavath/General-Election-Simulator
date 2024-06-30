import pygame
pygame.init()

class Light:
    def __init__(self,x,y,radius):
        self.color=(0,0,0)
        self.x=x
        self.y=y
        self.state=False
        self.radius=radius
        self.glow=False # for glowing only after 5 seconds (on evm)
        
    def draw(self,screen):
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.radius)
    
    def toggle_state(self):
        self.state =not self.state
        self.color= (0,255,0) if self.state else (255,0,0)

def generate_lights(lights):
    for i in range(13):
        lights.append(Light(1040,310+(30*i),9))

class player:
    def __init__(self,name,width,height,image):
        self.name=name
        self.width=width
        self.height=height
        self.x=1600;self.y=680
        self.latest_t=0
        self.image=image
        self.vote_count=0  #used so that he can press button on evm only once
        self.inked=False
        self.verified_police=False
        self.voted=False
        self.voted_option=0
        self.coord=[1]
        self.dir='v' #can be v/h. v for vertical
        self.pos=0
        self.message=True
    
    def automove(self):
        if self.pos<len(self.coord)-1:
            
            if(self.dir=='v'):
                a=1;b=0
            else:
                a=0;b=1
            i=self.pos
            
            if self.pos%2==0: 
                y2=self.coord[i+1][a]-self.coord[i][a]
                if y2>0: 
                    if self.dir=='v':
                        if(self.y<=self.coord[i+1][a]):
                            self.y+=5
                            self.image="player2"
                    else:
                        if(self.x<=self.coord[i+1][a]):
                            self.x+=5
                            self.image="player2r"
                elif y2<0: 
                    if self.dir=='v':
                        if(self.y>=self.coord[i+1][a]):
                            self.y-=5
                            self.image="player2b"
                    else:
                        if(self.x>=self.coord[i+1][a]):
                            self.x-=5
                            if self.inked:
                                self.image="player2li"
                            else:
                                self.image="player2l"
            else:   
                x2=self.coord[i+1][b]-self.coord[i][b]
                if x2>0: 
                    if self.dir=='v':
                        if(self.x<=self.coord[i+1][b]):
                            self.x+=5
                            self.image="player2r"
                    else:
                        if(self.y<=self.coord[i+1][b]):
                            self.y+=5
                            self.image="player2"
                elif x2<0: 
                    if self.dir=='v':
                        if(self.x>=self.coord[i+1][b]):
                            self.x-=5
                            if self.inked:
                                self.image="player2li"
                            else:
                                self.image="player2l"
                    else:
                        if(self.y>=self.coord[i+1][b]):
                            self.y-=5
                            self.image="player2b"

            if self.dir=='v':
                if (i%2==0 and abs(self.coord[i+1][1]-self.y)<=10) or (i%2==1 and abs(self.coord[i+1][0]-self.x)<=10):
                    self.pos+=1
            elif self.dir=='h':
                if (i%2==0 and abs(self.coord[i+1][0]-self.x)<=10) or (i%2==1 and abs(self.coord[i+1][1]-self.y)<=10):
                    self.pos+=1
            return True
        else:
            return False
        
    def draw(self,window):
        player_image=pygame.image.load("templates/"+self.image+".png")
        window.blit(player_image,(self.x,self.y))

    def move(self,keys):
        if keys[pygame.K_LEFT]:
            self.x-=5
            if self.inked:
                self.image="playerinkedl"
            else:
                self.image="playerl"
            self.message=False
        if keys[pygame.K_RIGHT]:
            self.x+=5
            if self.inked:
                self.image="playerinkedr"
            else:
                self.image="playerr"
            self.message=False
        if keys[pygame.K_UP]:
            self.y-=5
            if self.inked:
                self.image="playerb"
            else:
                self.image="playerb"
            self.message=False
        if keys[pygame.K_DOWN]:
            self.y+=5
            if self.inked:
                self.image="playerinked"
            else:
                self.image="player"
            self.message=False

class paper:
    def __init__(self,x,y,w,h):
        self.x=x;self.y=y;self.w=w;self.h=h
    
    def move_paper(self):
        if self.y>210:
            self.y+=1
            self.h-=1
        else:
            self.y+=1

class message:
    def __init__(self,messages_list):
        self.image=pygame.image.load("templates/messagebox.png")
        self.index=0
        self.messages_list=messages_list
        self.show_message=[]

    def show(self, window, x, y):

        surface = pygame.Surface(self.image.get_size())
        surface.blit(self.image, (0, 0))

        lines = self.wrap_text(self.messages_list[self.index], 48)  
        font_size = 20  
        font = pygame.font.Font(None, font_size)

        line_height = font.get_linesize()
        y_offset = (surface.get_height() - len(lines) * line_height) // 2  
        for line in lines:
            text = font.render(line, True, (255, 255, 255))
            text_rect = text.get_rect(center=(surface.get_width() // 2, y_offset))
            surface.blit(text, text_rect)
            y_offset += line_height
        window.blit(surface, (x, y))

    def wrap_text(self, text, max_width):
        words = text.split()
        lines = []
        current_line = ''
        for word in words:
            if len(current_line + ' ' + word) <= max_width:
                current_line += ' ' + word
            else:
                lines.append(current_line.strip())
                current_line = word
        lines.append(current_line.strip())
        return lines


def draw_button(window,color,x,y,width,height,text):
    font=pygame.font.SysFont(None,40)
    pygame.draw.rect(window,color,(x,y,width,height))
    text_surface=font.render(text,True,(0,0,0))
    text_rect=text_surface.get_rect(center=(x+width/2,y+height/2))
    window.blit(text_surface,text_rect)

def handle_events(state,playeri,lights):

    px,py=playeri.x,playeri.y
    print(px,py)

    for event in pygame.event.get():

        if event.type==pygame.QUIT:
            return False
        
        elif event.type==pygame.MOUSEBUTTONDOWN and (state=="start_screen"):
            mouse_x,mouse_y=pygame.mouse.get_pos()
            if state=="start_screen" and 1600<mouse_x<1700 and 800<mouse_y<900:
                return "game_screen"
            
        elif state=="game_screen" and px<200 and py<200 and playeri.verified_police:
                return "voting_screen"
    
        elif state=="game_screen" and px<200 and py<200:
            playeri.verified_police=True
            playeri.latest_t=pygame.time.get_ticks()
      
        elif state=="voting_screen" and px>1420 and px<1600:
            return "voting_screen1"
        
        elif state=="voting_screen1" and px>800 and px<1200 and py<400 and py>180:
            playeri.inked=True
        
        elif state=="voting_screen1" and px<200 and py>200:
            playeri.latest_t=pygame.time.get_ticks()
            return "voting_screen2"

        elif state=="voting_screen2" and px<140 and py<255 and py>180:
            return "ballot_unit"
        
        elif state=="ballot_unit" and event.type==pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y=pygame.mouse.get_pos()
            
            for i in range(13):
                if (mouse_x-lights[i].x>27 and mouse_x-lights[i].x < 77 ) and (abs(mouse_y-lights[i].y) < lights[i].radius) and (playeri.vote_count==0) and (lights[i].glow):
                    lights[i].color=(255,0,0)
                    player1.voted_option=i
                    player1.voted=True
    
    return state

def messageshow(playeri,window,m,state,number):

    print(playeri.x,playeri.y,state,number)
    
    if state=="game_screen" and playeri.x>1500 and playeri.y>600 and m.show_message[0]==True:
        m.show(window,1600,600)
    elif state=="game_screen" and 1400<playeri.x<1500 and m.show_message[0]:
        m.show_message[0]=False
        m.index+=1
    
    elif state=="game_screen" and playeri.x<400 and playeri.y<400 and m.show_message[1]:
        m.show(window,300,500)

    elif state=="voting_screen" and 1570<playeri.x<1620 and 80<playeri.y<200 and m.show_message[2]:
        m.index=3
        m.show(window,1500,200)
    
    elif state=="voting_screen" and 1500<playeri.x<1620 and m.show_message[3] and number==0:
        m.index=4
        m.show(window,1500,700)
    
    elif state=="voting_screen" and number==1:
        m.index=2
        m.show(window,100,500)
    
    elif state=="voting_screen1" and 900<playeri.x<1500 and m.show_message[4]:
        m.index=5
        m.show(window,1100,700)
    
    elif state=="voting_screen1" and 100<playeri.x<300 and m.show_message[5]:
        m.index=6
        m.show(window,200,800)
    
    elif state=="voting_screen2" and number==1:
        m.index=6
        m.show(window,200,800)

    elif state=="ballot_unit":
        if(number==0):
            m.index=7
            m.show(window,800,100)
        elif number==1:
            m.index=8
            m.show(window,800,10)
    
    elif state=="voting_screen1" and 450<playeri.x<780:
        m.index=9
        m.show(window,600,800)
            
            
def main(window):
    #parameters used:
    start_background=pygame.image.load("templates/bginitial.png").convert()
    game_background=pygame.image.load("templates/2nd.png")
    voting_background=pygame.image.load("templates/voting_background.png")
    ballot_unit=pygame.image.load("templates/ballotunitnames.png")
    map=pygame.image.load("templates/map.png")
    player1=player("main",50,50,"player")
    police=pygame.image.load("templates/policel.png")
    vvpatback=pygame.image.load("templates/vvpattable.png")
    voting_background_1=pygame.image.load("templates/voting_background1.png")
    voting_background_2=pygame.image.load("templates/voting_background2.png")
    #lights which are required on evm
    lights=[]
    generate_lights(lights)
    player2=player("side",50,50,"player")
    player2.x=1340;player2.y=-50
    player2.coord=[(1340, -50), (1340, 10), (980, 10), (980, 205), (465, 205), (465, 50), (135, 50)]
    coord2=[(1000,260),(50,260)]
    player2.dir="v"
    my_msg_list=["Utilize the keyboard controls for movement. This is a simulation game for voting. Navigate to the designated voting location where a police officer is present.","Approach the police officer closely and await verification of your voter card.","Verify the voter ID to confirm affiliation with this polling station. Please remain stationary during this process.","The individuals seated here are local residents, representatives of political parties who can identify voters from local area.Move towards officer in the yellow dress.","The officer will verify your voter card details and announce your name loudly for verification by local political party members.","The official will apply ink to the voter's finger to prevent electoral fraud and uphold the integrity of the voting process.","The official will activate the vote in the control unit to enable casting and counting of the vote in the ballot unit.Move towards the blue compartment","This is ballot unit, press the blue button next to your chosen candidate's name to cast your vote. An illuminated light confirms your vote.","This is known as VVPAT. It displays the chosen option on paper without providing a physical copy to the voter, storing the record internally.","The officer will collect your signature.",]
    m=message(my_msg_list)
    m.show_message=[True,True,True,True,True,True,True,True,True,True,True]

    trans_start=0
    trans_delay=5000

    running=True
    state="start_screen"

    clock = pygame.time.Clock()
    FPS = 60

    pygame.mixer.music.load("templates/welcome_1.mp3")
    pygame.mixer.music.play()

    evm_ready_light=Light(924,270,8);lc=0
    vvpatlight=Light(959,388,7)
    vvpat_counter=0

    sound_counter=0

    p=paper(933,200,60,80)

    #game loop
    while running:

        clock.tick(FPS)
        
        new_state=handle_events(state,player1,lights)
        if new_state!=state:
            state=new_state
            continue

        keys=pygame.key.get_pressed()

        if state == "start_screen":
            window.blit(start_background, (0,0))
            draw_button(window, (255,165,0),1600,800,100,100,"Start")
            player1.move(keys)

        elif state == "game_screen":
            window.blit(game_background, (0,0))
            player1.draw(window)
            window.blit(police,(0,50))
            if player2.automove():
                player2.draw(window)
            
            messageshow(player1,window,m,state,0)
            player1.move(keys)

        elif state=="voting_screen":
            if (pygame.time.get_ticks()-player1.latest_t>5000):
                window.blit(voting_background,(0,0))
                if lc==0:
                    player1.x=1600
                    player1.y=100
                    lc+=1
            
                player1.draw(window)
                player1.move(keys)
                messageshow(player1,window,m,state,0)
                player2.coord=coord2
                player2.dir="h"

                if player2.automove():
                    player2.draw(window)
                
            else:
                #blit game_screen only.should wait for 5 sec
                window.blit(game_background, (0,0))
                player1.draw(window)
                window.blit(police,(0,50))
                player1.move(keys)
                player2.x=1000;player2.y=260;player2.pos=0
                player2.inked=True
                messageshow(player1,window,m,state,1)

        elif state=="voting_screen1":
            b=pygame.time.get_ticks()
            a=player1.latest_t
            if(b-a>2000):
                window.blit(voting_background_1,(0,0))
                player1.draw(window)
                player1.move(keys)
                messageshow(player1,window,m,state,0)
            else:
                window.blit(voting_background,(0,0))
                player1.draw(window)

        elif state=="voting_screen2":
            b=pygame.time.get_ticks()
            a=player1.latest_t
            if(b-a>2000):
                window.blit(voting_background_2,(0,0))
                player1.draw(window)
                player1.move(keys)
                messageshow(player1,window,m,state,1)
            else:
                window.blit(voting_background_1,(0,0))
                player1.draw(window)
                player1.move(keys)
                messageshow(player1,window,m,state,1)
        
        elif state=="ballot_unit":
            b=pygame.time.get_ticks()
            a=player1.latest_t
            if(b-a>3000):
                player1.move(keys)
                window.blit(map,(0,0))
                window.blit(ballot_unit,(806,250))
                messageshow(player1,window,m,state,0)

                if lc<50: #count corresponds to 2 seconds so that then after vote is released
                    evm_ready_light.color=(0,0,0)
                else:
                    evm_ready_light.color=(0,255,0)
                    for i in range(13):
                        lights[i].glow=True

                if (not player1.voted):
                    evm_ready_light.draw(window)
                lc+=1

                for i in range(13):
                    lights[i].draw(window)

                if player1.voted:
                    vvpat_counter+=1
                    
                if vvpat_counter>=120:
                    window.blit(vvpatback,(0,0))
                    messageshow(player1,window,m,"ballot_unit",1)
                    vvpatlight.draw(window)
                    symbols=["α","β","γ","ε","φ","χ","ξ","δ","ω","π","σ","μ","NOTA"]
                    if player1.voted_option==12:
                        font = pygame.font.Font(None, 30)
                        option=font.render(symbols[player1.voted_option],True,(23,23,23))
                    else:
                        font = pygame.font.Font(None, 90)
                        option=font.render(symbols[player1.voted_option],True,(23,23,23))
                    
                    pygame.draw.rect(window,(255,255,255),(p.x,p.y,p.w,p.h))
                    option_rect=option.get_rect(center=(965,240))

                    window.blit(option,option_rect)

                    p.move_paper()

                    pygame.mixer.music.load("templates/beep.mp3")
                    if(sound_counter%10==0):
                        pygame.mixer.music.play()
                    sound_counter+=1

                    if(pygame.time.get_ticks()-player1.latest_t>20000):
                        running=False
            else:
                window.blit(voting_background_2,(0,0))
                player1.draw(window)
                if keys[pygame.K_LEFT] or keys[pygame.K_DOWN] or keys[pygame.K_UP]:
                    player1.move(keys)
                
        elif state == False:
            running=False

        pygame.display.update()
