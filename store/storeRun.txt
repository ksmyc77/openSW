from gameRunMethod import *
from gameDisplayMethod import *

#game run Method
def gameRun() :
  #variable
  time1 = time.time()
  velocidade = 100
  game_speed = 1.2
  pontos = 0
  green = (0, 255, 0)
  blue = (0, 0, 255)
  white = (255, 255, 255)
  gravity = 5
  game_over = False

  jump = False
  jumping = False

  #run
  while True:
    #event handler
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.KEYDOWN:
        #jump
        if event.key == pygame.K_SPACE:
          if rex.y >= 240:
            sound_jump.play()
            time1 = time.time()
            velocidade = -35
            rex.y = 240
            gravity = 5
    #print(velocidade)

    #jump
    t = time.time() - time1
    if velocidade < 100 and rex.y <= 240:
      if velocidade > 0: 
        gravity = 2
      rex.y += (int(velocidade*t))
      velocidade += gravity*t

    rex_rect = pygame.Rect(rex.x+8, rex.y, 26, 60)

    if check_collision_with_list(rex_rect, cactus_obj, white, obs_dx=10, obs_dy=15):
      sound_hit.play()
      game_over = True
    #if check_collision_with_list(rex_rect, cloud_obj, blue):
    #    game_over = True

    if game_over:
      gameOver(pontos)

    if not game_over:
      pontos += 0.5
      
    move_element(terrain_obj, game_speed, 3, -500, 960, terrain_obj.coord_list[0][1])
    move_element(cloud_obj, game_speed, 1, 0, random.randint(800, 1200),random.randint(20, 200))
    move_element(cactus_obj, game_speed, 4, 100, random.randint(800, 1500),cactus_obj.coord_list[0][1])
    
    display_all_Running(rex_rect, white, pontos)
    pygame.display.update()
    clock.tick(60)