import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_MIN_RADIUS, ASTEROID_KINDS, ASTEROID_SPAWN_RATE, ASTEROID_MAX_RADIUS
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main(): 
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    print(clock)
    dt = 0
    asteroid_group = pygame.sprite.Group() 
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable) 
    Asteroid.containers  = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable, )
    Shot.containers = (updatable, drawable, shots)

    player = Player(x = SCREEN_WIDTH/2, y =SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField(asteroid_group)
   #
   # all_sprites = pygame.sprite.Group()
# asteroids_group = pygame.sprite.Group()

# # Create an AsteroidField instance
# asteroid_field = AsteroidField(asteroids_group)
# all_sprites.add(asteroid_field)
 
    while(True): 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                return
        screen.fill((0,0,0))
        updatable.update(dt=dt)
        for asteroid in asteroids: 
            if player.check_collision(asteroid): 
                print("Game Over!")
                return
        for drawables in drawable: 
            drawables.draw(screen)
        for asteroid in asteroids: 
            for shot in shots: 
                if asteroid.check_collision(shot) == True: 
                    asteroid.split()
                    shot.kill()

        pygame.display.flip()
        dt = clock.tick(60)/1000
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__": 
    main()