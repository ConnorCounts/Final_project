WIDTH = 1450
HEIGHT = 900
PLAYER_ACC = 2
PLAYER_FRICTION = -0.3
PLAYER_JUMP = 15
PLAYER_GRAV = 0.8
MOB_ACC = 2
MOB_FRICTION = -0.3
BLACK = (0,0,0)
BLUE = (50,50,255)
RED = (255,50,50)
WHITE = (255,255,255)
FPS = 60
RUNNING = True
PAUSED = False
platform_vel = 5

# Starting platforms
PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 40, (200,200,200), "ground"),
                 
                 (50, 785, 75, 75, (200, 200,200), "normal"),

                 (250, 700, 75, 75, (200, 200,200), "normal"),

                 (450, 600, 75, 75, (200, 200,200), "normal"),

                 (750, 550, 75, 75, (200,200,200), "normal"),

                 (1050, 500, 75, 75, (200,200,200), "normal"),

                 #(1350, 450, 75, 75, (200,200,200), "normal"),

                 (1050, 300, 75, 75, (200,200,200), "normal"), 

                 (1300, 400, 75, 75, (200,200,200), "normal"),

                 (750, 250, 75, 75, (200,200,200), "normal"), 

                 (450, 200, 75, 75, (200,200,200), "normal"),

                 (250, 150, 75, 75, (200,200,200), "normal"), 

                 (50, 100, 75, 75, (200,200,200), "top_plat")
                 ]
#MOVING_PLATFORM_LIST = [()]      