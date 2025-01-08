import pygame
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)

dis_width = 1280
dis_height = 800

score = 0

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption("Snake")
game_font = "bahnschrift"

clock = pygame.time.Clock()

snake_block = 10

font_style = pygame.font.SysFont(game_font, 25)
apples_font = pygame.font.SysFont(game_font, 25)


def apples(apples):
    value = apples_font.render("Apples: " + str(apples), True, white)
    dis.blit(value, [0, 0])


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, white, [x[0], x[1], snake_block, snake_block])


def message(msg, color, x, y):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [x, y])


def game_loop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    snake_speed = 12
    score = 0

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(3 * snake_block, dis_width - 3 * snake_block) / 10.0) * 10.0
    foody = round(random.randrange(3 * snake_block, dis_height - 3 * snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            message("You Lost! Press R to Play Again or Q to Quit", white, dis_width / 6, dis_height / 2)
            apples(score)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit(0)
                if event.type == pygame.KEYDOWN:
                    if event.type == pygame.QUIT:
                        exit(0)
                    if event.key == pygame.K_q:
                        exit(0)
                    if event.key == pygame.K_r:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    if x1_change != snake_block:
                        x1_change = -snake_block
                        y1_change = 0
                        break
                elif event.key == pygame.K_d:
                    if x1_change != -snake_block:
                        x1_change = snake_block
                        y1_change = 0
                        break
                elif event.key == pygame.K_w:
                    if y1_change != snake_block:
                        y1_change = -snake_block
                        x1_change = 0
                        break
                elif event.key == pygame.K_s:
                    if y1_change != -snake_block:
                        y1_change = snake_block
                        x1_change = 0
                        break
                elif event.key == pygame.K_q:
                    game_over = True
                    game_close = False

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)

        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])

        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_block, snake_list)

        pygame.display.update()
        pygame.display.set_caption(f"Snake | Apples: {score}")
        i = 1

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(3 * snake_block, dis_width - 3 * snake_block) / 10.0) * 10.0
            foody = round(random.randrange(3 * snake_block, dis_height - 3 * snake_block) / 10.0) * 10.0
            length_of_snake += 1
            snake_speed += 1
            score = str(length_of_snake - 1)

        clock.tick(snake_speed)

    pygame.quit()
    quit()


game_loop()
