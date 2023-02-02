import os
import sys
import pygame
import requests

map_request = "https://static-maps.yandex.ru/1.x/?ll=137.554721,-27.358666&z=2&l=sat"

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
screen.blit(pygame.image.load(map_file), (0, 0))
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
os.remove(map_file)
