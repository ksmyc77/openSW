from gameSetting import *
from gameDisplayMethod import display_all_gameover

#move obstacle
def move_element(scenario_obj, game_speed, game_speed_multiplicator,
                 x_limit, x_start, y_start):
    for i, coord in enumerate(scenario_obj.coord_list):
        #screen.blit(scenario_obj.surface, coord)
        # coord x
        scenario_obj.coord_list[i][0] -= game_speed_multiplicator*game_speed
        if coord[0] < x_limit:
            scenario_obj.coord_list[i][0] = x_start
            scenario_obj.coord_list[i][1] = y_start

#check collision with rex-obstacle
def check_collision_with_list(player_rect, obstacle_obj, color, obs_dx=0, obs_dy=0):
    for coord in obstacle_obj.coord_list:
        obstacle_rect = pygame.Rect(coord[0]+obs_dx,
                                    coord[1]+obs_dy, 50, 40)
        pygame.draw.rect(screen, color, obstacle_rect)
        if player_rect.colliderect(obstacle_rect):
            return True

#gameover
def gameOver(pontos):
    while True :
        display_all_gameover(pontos)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()