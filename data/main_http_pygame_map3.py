import os
import sys
import pygame
import requests

x, y = 37.974517, 23.733215
size = 1
map_request = f"https://static-maps.yandex.ru/1.x/?ll={x},{y}&z={size}&l=sat"

response = requests.get(map_request)

if not response:
    print("Ошибка выполнения запроса", map_request)
    print("http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)

map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(response.content)

pygame.init()
screen = pygame.display.set_mode((600, 450))
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_PAGEUP:
                if size < 18:
                    size += 1

            if event.key == pygame.K_PAGEDOWN:
                if size > 1:
                    size -= 1

            if event.key == pygame.K_DOWN:
                print(y)
                if y - 5 >= -80:
                    y -= 5

            if event.key == pygame.K_UP:
                print(y)
                if y + 5 <= 80:
                    y += 5

            if event.key == pygame.K_LEFT:
                if x - 5 >= -180:
                    x -= 5

            if event.key == pygame.K_RIGHT:
                if x + 5 <= 180:
                    x += 5

    map_request = f"https://static-maps.yandex.ru/1.x/?ll={x},{y}&z={size}&l=sat"
    map_file = "map.png"
    response = requests.get(map_request)
    with open(map_file, "wb") as file:
        file.write(response.content)
    screen.blit(pygame.image.load(map_file), (0, 0))
    pygame.display.flip()

pygame.quit()
os.remove(map_file)
