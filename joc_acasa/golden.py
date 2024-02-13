import pygame
import random

pygame.init()


WIDTH, HEIGHT = 1920, 1080


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Golden Dash")


background_image = pygame.image.load(r"C:\Users\Asus Tuf Gaming\Desktop\Tips\python\joc_acasa\gleb-ppgorelov-5.jpg")


player_size = 70
player_speed = 10
enemy_size = 80
enemy_speed = 12

player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - player_size - 10

enemy_x = random.randint(0, WIDTH - enemy_size)
enemy_y = 0

score = 0

font = pygame.font.Font(None, 36)

def main():
    global player_x, player_y, enemy_x, enemy_y, score

    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        player_x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * player_speed
        
        player_x = max(0, min(WIDTH - player_size, player_x))
        
        enemy_y += enemy_speed
        
        if (
            player_x < enemy_x + enemy_size
            and player_x + player_size > enemy_x
            and player_y < enemy_y + enemy_size
            and player_y + player_size > enemy_y
        ):
            
            running = False
        
        if enemy_y > HEIGHT:
            
            enemy_x = random.randint(0, WIDTH - enemy_size)
            enemy_y = 0
            score += 1
        
        screen.blit(background_image, (0, 0))
        
        pygame.draw.rect(screen, (255, 215, 0), (player_x, player_y, player_size, player_size))
        
        pygame.draw.rect(screen, (255, 0, 0), (enemy_x, enemy_y, enemy_size, enemy_size))
        
        score_text = font.render(f"Scor: {score}", True, (0, 0, 0))
        screen.blit(score_text, (10, 10))

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
