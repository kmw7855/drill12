import random
from pico2d import *
import time
frame_time = 0.0

PIXEL_PER_METER = (10.0 / 0.3) # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0 # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)



class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class bird:
    def __init__(self):
        self.x, self.y = random.randint(100, 400), random.randint(100, 300)
        self.turn = -1
        self.frame = 0
        self.image = load_image('bird100x100x14.png')

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y) #새의 크기를 100픽셀 즉 300cm으로 지정

    def update(self):
        
        self.frame = (self.frame + 1) % 8
        self.x += RUN_SPEED_PPS *frame_time * self.turn * -1 #위의 6~10번쨰 수식에 의해 새는 시속 20km의 속도를 가짐
        if self.x > 800:
            self.turn * -1
        if self.x < 0:
            self.turn * -1


open_canvas(800,600, sync = True)

team = [bird() for i in range(5)]

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

grass = Grass()

running = True

current_time = time.time()
while running:

    clear_canvas()
    grass.draw()

    handle_events()
    
    for bird in team:
        bird.update()

    for bird in team:
        bird.draw()

    frame_time = time.time() - current_time
    frame_rate = 1.0 / frame_time
    current_time += frame_time
    print("Frame Time: %f sec, Frame Rate: %f fps" %(frame_time,frame_rate))
    update_canvas()

    delay(0.01)

close_canvas()

#https://youtu.be/n7jAraJyacI