from gameSetting import *

#print obstacle
def display_obstacle_all(scenario_obj):
    for i, coord in enumerate(scenario_obj.coord_list):
        screen.blit(scenario_obj.surface, coord)

#gameover
def display_all_gameover(pontos):
    surface.fill((255, 255, 255))
    screen.blit(surface, (0, 0))
    display_obstacle_all(terrain_obj)
    display_obstacle_all(cloud_obj)
    display_obstacle_all(cactus_obj)
    screen.blit(rex_over, (rex.x, 240))
    display_score(pontos)
    textsurface_over = myfont.render(f'Game Over', False, (0, 0, 0))
    screen.blit(textsurface_over, (300, 50))

#player's score
def display_score(pontos):
    textsurface = myfont.render(f'{pontos:.0f}', False, (0, 0, 0))
    screen.blit(textsurface, (350, 0))

#display All
def display_all_Running(rex_rect, color, pontos) :
  surface.fill((255, 255, 255))
  screen.blit(surface, (0, 0))
  #rex_rect = pygame.Rect(rex.x+8, rex.y, 26, 60)
  pygame.draw.rect(screen, color, rex_rect)
  display_obstacle_all(terrain_obj)
  display_obstacle_all(cloud_obj)
  display_obstacle_all(cactus_obj)
  display_score(pontos)
  screen.blit(rex.update_surface(), (rex.x, rex.y))
  rex.run("run")