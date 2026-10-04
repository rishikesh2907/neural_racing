import pygame

pygame.init()

WIDTH = 1000
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("Neural Racing")

clock = pygame.time.Clock()

running = True

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  screen.fill((30,30,30))
  
  pygame.draw.rect(
      screen,
      (255, 255, 255),
      (100, 100, 800, 500)
   )
  pygame.draw.rect(
      screen,
      (30, 30, 30),
      (250, 250, 500, 200)
     )
  
  
  pygame.display.flip()
  clock.tick(60)

pygame.quit()

