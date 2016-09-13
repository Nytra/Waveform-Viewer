import pygame, os, sys, math, time
from pygame.locals import *

pygame.init()

COLOUR = pygame.Color(255, 255, 0, 0)
BG = pygame.Color(0, 0, 0, 0)
screen_info = pygame.display.Info()
canvas_width = 800
canvas_height = 600
frequency = 4
amplitude = 50 # px
speed = 1
pygame.display.set_caption("Waveform Viewer")
basic_font = pygame.font.SysFont("monospace", 16)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


screen = pygame.display.set_mode((canvas_width, canvas_height))
screen.fill(BG)
surface = pygame.Surface((canvas_width, canvas_height))
surface.fill(BG)

running = True
up = False
down = False
right = False
left = False
shift = 0 # px
s_left = False
s_right = False
zero_line = True
while running:
    if frequency > 0:
        period = 1 / frequency
    else:
        period = 0
    msg_freq = "Frequency: %d Hz" % frequency
    msg_ampl = "Amplitude: %d Nm" % amplitude
    msg_period = "Period: %f S" % period
    msg_shift = "Shift: %d" % shift
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                up = True
            if event.key == pygame.K_DOWN:
                down = True
            if event.key == pygame.K_RIGHT:
                right = True
            if event.key == pygame.K_LEFT:
                left = True
            if event.key == pygame.K_r:
                frequency = 0
                amplitude = 0
                shift = 0
            if event.key == pygame.K_a:
                s_left = True
            if event.key == pygame.K_d:
                s_right = True
            if event.key == pygame.K_z:
                if zero_line:
                    zero_line = False
                else:
                    zero_line = True
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                up = False
            if event.key == pygame.K_DOWN:
                down = False
            if event.key == pygame.K_RIGHT:
                right = False
            if event.key == pygame.K_LEFT:
                left = False
            if event.key == pygame.K_a:
                s_left = False
            if event.key == pygame.K_d:
                s_right = False
    if up:
        amplitude += 1
    if down:
        amplitude -= 1
    if left:
        frequency -= 1
    if right:
        frequency += 1
    if s_right:
    	shift += 1
    if s_left:
    	shift -= 1
    if shift < 0:
    	shift = 0
    if frequency < 0:
        frequency = 0
    if amplitude < 0:
        amplitude = 0
    surface.fill(BG)
    for x in range(0, canvas_width):
        y_sin = int((canvas_height/2) + amplitude*math.sin(frequency*((float(x)/canvas_width)*(2*math.pi) + (speed*time.time()))))
        y_cos = int((canvas_height/2) + amplitude*math.cos(frequency*((float(x+shift)/canvas_width)*(2*math.pi) + (speed*time.time()))))
        y_tan = int((canvas_height/2) + amplitude*math.tan(frequency*((float(x)/canvas_width)*(2*math.pi) + (speed*time.time()))))
        y_total = y_sin - y_cos + (canvas_height // 2)
        surface.set_at((x, y_sin), COLOUR)
        surface.set_at((x, y_cos), RED)
        surface.set_at((x, y_tan), BLUE)
        surface.set_at((x, y_total), WHITE)
        if zero_line:
            surface.set_at((x, canvas_height // 2), WHITE)
    freq_text = basic_font.render(msg_freq, False, WHITE, BLACK)
    ampl_text = basic_font.render(msg_ampl, False, WHITE, BLACK)
    period_text = basic_font.render(msg_period, False, WHITE, BLACK)
    shift_text = basic_font.render(msg_shift, False, WHITE, BLACK)
    surface.blit(freq_text, (5, 10))
    surface.blit(ampl_text, (5, 30))
    surface.blit(period_text, (5, 50))
    surface.blit(shift_text, (5, 70))
    screen.blit(surface, (0,0))
    pygame.display.flip()
    pygame.time.delay(5)
pygame.quit()
sys.exit()
