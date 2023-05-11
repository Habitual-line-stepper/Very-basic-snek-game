import pygame
import time
import random

pygame.init()
display_info = pygame.display.Info()
width = display_info.current_w
height = display_info.current_h
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snek gaem")
game_font = pygame.font.SysFont(None, 30)
score_font = pygame.font.SysFont(None, 30)

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

snek = 30
timer = pygame.time.Clock()
snek_spood = 30
snek_speech = ("I still HUNGER!!", "FEED ME MOAR!!", "MY POWER IS GROWING!!")


def player_score(score):
    score_track = score_font.render("Score: " + str(score), True, green)
    display.blit(score_track, [width / 2, 0])


def speak(text):
    text_surface = game_font.render(text, True, white)
    text_rect = text_surface.get_rect(center=(width / 2, height / 2))
    display.blit(text_surface, text_rect)
    pygame.display.update()


def snek_size(snek, snek_list):
    for i in snek_list:
        pygame.draw.rect(display, black, [i[0], i[1], snek, snek])


def game_text(text, colour):
    text = game_font.render(text, True, colour)
    text_rect = text.get_rect(center=(width / 2, height / 2))
    display.blit(text, text_rect)


def game_on():
    try_again = False
    lost = False
    x1 = width / 2
    y1 = height / 2
    x1_change = 0
    y1_change = 0
    snek_list = []
    snek_length = 1

    prey_x = round(random.randrange(0, width - snek) / 10.0) * 10.0
    prey_y = round(random.randrange(0, height - snek) / 10.0) * 10.0

    while not try_again:
        while lost:
            display.fill(white)
            game_text("Game over! Press Esc to quit or Space to play again!",
                      red)
            player_score(snek_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        lost = False
                        try_again = True
                    if event.key == pygame.K_SPACE:
                        game_on()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                lost = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -10
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = 10
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -10
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = 10
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            lost = True

        x1 += x1_change
        y1 += y1_change
        display.fill(blue)
        pygame.draw.rect(display, green, [prey_x, prey_y, snek, snek])
        snek_head = [x1, y1]
        snek_list.append(snek_head)
        if len(snek_list) > snek_length:
            del snek_list[0]
        for i in snek_list[:-1]:
            if i == snek_head:
                lost = True

        snek_size(snek, snek_list)
        player_score(snek_length - 1)
        pygame.display.update()

        if prey_x <= x1 < prey_x + snek or prey_x < x1 + snek < prey_x + snek:
            if prey_y <= y1 < prey_y + snek:
                prey_x = round(random.randrange(0, width - snek) / 10.0) * 10.0
                prey_y = round(random.randrange(0, height - snek) / 10.0) * 10.0
                snek_length += 1
            elif prey_y < y1 + snek < prey_y + snek:
                prey_x = round(random.randrange(0, width - snek) / 10.0) * 10.0
                prey_y = round(random.randrange(0, height - snek) / 10.0) * 10.0
                snek_length += 1

        timer.tick(snek_spood)
    pygame.quit()
    quit()


game_on()
