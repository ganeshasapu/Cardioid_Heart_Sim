import pygame
import math
from Classes import Button, Text

pygame.init()

w = 800
h = 800
win = pygame.display.set_mode((w, h))
pygame.display.set_caption("Game of Life")

clock = pygame.time.Clock()
run = True

r = round(w // 3)
main_scene = True
main_scene_objs = []
main_call = []

Buttons = []
# Simulation Variables
points = 200
factor = 0
run_sim = False


def next_frame():
    global factor
    factor += 0.05


def stop_sim():
    global run_sim
    run_sim = False


def continue_sim():
    global run_sim
    run_sim = True


def restart():
    global run_sim
    global factor
    run_sim = False
    factor = 0


def check_events():
    global run
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Stops Program
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Checks event to object and Changes object state
            for obj in Buttons:
                if obj.is_hovering:
                    obj.is_pressed_down = True
        elif event.type == pygame.MOUSEBUTTONUP:
            # Checks event to object and Changes object state
            for obj in Buttons:
                if obj.is_hovering:
                    obj.is_pressed_down = False
                    obj.is_pressed_up = True
    for obj in Buttons:
        obj.state_check()


def update_game_events():
    main_call.clear()
    main_call.append(main_scene)


def get_position(index):
    index = index % points
    angle = ((math.pi * 2) / points) * index
    x = round(r * math.cos(angle + math.pi) + w // 2)
    y = round(r * math.sin(angle + math.pi) + (h // 2) - 25)
    return x, y


def make_points():
    pygame.draw.circle(win, (255, 255, 255), (w // 2, (h // 2) - 25), r, 1)
    for i in range(points):
        pos = get_position(i)
        pygame.draw.circle(win, (255, 255, 255), pos, 5)


def make_lines():
    for i in range(points):
        a = get_position(i)
        b = get_position(i * factor)
        pygame.draw.line(win, (255, 255, 255), a, b, 1)


def draw():
    global factor
    win.fill((0, 0, 0))
    if run_sim:
        factor += 0.05
    make_points()
    make_lines()
    for obj in main_scene_objs:
        win.blit(obj.image_to_display, obj.get_center_cor())
    pygame.display.update()


def main():
    update_game_events()
    while run:
        clock.tick(25)
        check_events()
        draw()
    pygame.quit()


next_B = Button.Button('Images/next_b.png', (w // 8, h // 1.06), next_frame, (w, h), (6, 22), main_call,
                       scene=main_scene_objs, list_to_append=Buttons)
stop_B = Button.Button('Images/stop_b.png', (w // 2.6, h // 1.06), stop_sim, (w, h), (6, 22), main_call,
                       scene=main_scene_objs, list_to_append=Buttons)
run_B = Button.Button('Images/run_b.png', (w // 1.6, h // 1.06), continue_sim, (w, h), (6, 22), main_call,
                      scene=main_scene_objs, list_to_append=Buttons)
restart_B = Button.Button('Images/restart_b.png', (w // 1.15, h // 1.06), restart, (w, h), (6, 22), main_call,
                          scene=main_scene_objs, list_to_append=Buttons)
title = Text.Text("Cardioid Simulation", (255, 255, 255), "Fonts/Varela.otf", (w // 2, h // 16), (w, h), 16, scene=main_scene_objs)

main()
