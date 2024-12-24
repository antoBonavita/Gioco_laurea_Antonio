import pygame
import sys
import random

# Allora io ci tenevo a fare questa cosa
pygame.init()
#con l'aiuto di chatgpt 
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60

# ho realizzato questa cosa 
pygame.display.set_caption("Tanti auguri!!!!")

# non giudicare il mio codice
spotify_img= pygame.image.load("immagini/spotify.jpg")
spotify_img = pygame.transform.scale(spotify_img, (150, 150))
background_img = pygame.image.load("immagini/first_back1.jpeg")
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))
character1_img = pygame.image.load("immagini/antonio.png")
character1_img = pygame.transform.scale(character1_img, (200, 200))
character1_down_img = pygame.image.load("immagini/antonio_down.png")
character1_down_img = pygame.transform.scale(character1_down_img, (50, 100))
character2_img = pygame.image.load("immagini/lella.png")
character2_img = pygame.transform.scale(character2_img, (180, 180))
character2_down_img = pygame.image.load("immagini/lella_down.png")
character2_down_img = pygame.transform.scale(character2_down_img, (50, 100))
platform_img = pygame.image.load("immagini/blocco.png")
platform_img = pygame.transform.scale(platform_img, (50, 50))


# ne tanto meno la grafica
clock = pygame.time.Clock()

# non sono una brava programmatrice come te purtroppo
class Player:
    def __init__(self, image_standing, image_crouching, start_pos):
        self.image_standing = image_standing
        self.image_crouching = image_crouching
        self.image = image_standing
        self.rect = self.image.get_rect(midbottom=start_pos)
        
        self.velocity_y = 0
        self.is_jumping = False
        self.is_crouching = False
        self.collision_rect = pygame.Rect(
            self.rect.x,  # Riduce il margine a sinistra
            self.rect.y ,  # Riduce il margine sopra
            self.rect.width - 100,  # Riduce il margine a destra
            self.rect.height - 20  # Riduce il margine sotto
        )
    def move(self, keys, speed, jump_strength, gravity):
        if keys[pygame.K_LEFT]:
            self.rect.x -= speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += speed
        if keys[pygame.K_SPACE] and not self.is_jumping:
            self.velocity_y = jump_strength
            self.is_jumping = True
        if keys[pygame.K_DOWN]:
            self.crouch()
        else:
            self.stand()


        # ma io volevo fare qualcosa di unico
        self.velocity_y += gravity
        self.rect.y += self.velocity_y

    def crouch(self):
        if not self.is_crouching:
            self.image = self.image_crouching
            self.rect = self.image.get_rect(midbottom=self.rect.midbottom)
            self.is_crouching = True
        self.collision_rect.x = self.rect.x 
        self.collision_rect.y = self.rect.y 
    def stand(self):
        if self.is_crouching:
            self.image = self.image_standing
            self.rect = self.image.get_rect(midbottom=self.rect.midbottom)
            self.is_crouching = False
        self.collision_rect.x = self.rect.x +40
        self.collision_rect.y = self.rect.y +20

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)
        #pygame.draw.rect(screen, (255, 0, 0), self.collision_rect, 2)

# spero di esserci riuscita
class Platform:
    def __init__(self, x, y, image, scroll_speed):
        self.image = image
        self.rect = pygame.Rect(x, y, image.get_width(), image.get_height())  
        self.scroll_speed = scroll_speed
    
    def update(self):
        self.rect.x -= self.scroll_speed  
        if self.rect.right < 0:
            self.reset_position(WIDTH, HEIGHT)
    

    def draw(self, screen):
       
        screen.blit(self.image, (self.rect.x , self.rect.y ))
        #pygame.draw.rect(screen, (255, 0, 0), self.rect, 2)

    def reset_position(self, width, height):
        self.rect.x = random.randint(100, width - 150)
        self.rect.y = random.randint(200, height -100)
        



def finale():
    font = pygame.font.Font("font/font1.ttf", 36)
    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        SCREEN.blit(background_img, (0, 0))
        SCREEN.blit(spotify_img, (300, 350))
        text = font.render("La nostra storia che non finisce mai di finire", True, "black") 
        text1 = font.render("che non finisce mai di finire", True, "black") 
        SCREEN.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - 50))
        SCREEN.blit(text1, (WIDTH // 2 - text1.get_width() // 2, HEIGHT // 2 ))
       
        pygame.display.flip()
        clock.tick(FPS)

# puoi modificarlo se vuoi, ma non giudicarmi troppo mentre le foi 
def homepage():
    selected_character = None
    start_button = pygame.Rect(330, 300, 150, 50)
    character1_button = pygame.Rect(110, 310, 210, 250)
    character2_button = pygame.Rect(495, 330, 210, 230)
    
    font = pygame.font.Font("font/SuperMario256.ttf", 36)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if character1_button.collidepoint(mouse_pos):
                    selected_character = (character1_img, character1_down_img)
                elif character2_button.collidepoint(mouse_pos):
                    selected_character = (character2_img, character2_down_img)
                elif start_button.collidepoint(mouse_pos) and selected_character:
                    return selected_character

        SCREEN.blit(background_img, (0, 0))
        SCREEN.blit(character1_img, (character1_button.x + 10, character1_button.y + 10))
        SCREEN.blit(character2_img, (character2_button.x + 10, character2_button.y + 10))

        pygame.draw.rect(SCREEN, "steelblue", start_button, 2)
        start_text = font.render("START", True, "red")
        SCREEN.blit(start_text, (start_button.x + 9, start_button.y + 10))

        if selected_character == (character1_img, character1_down_img):
            pygame.draw.rect(SCREEN, "red", character1_button, 3)
        elif selected_character == (character2_img, character2_down_img):
            pygame.draw.rect(SCREEN, "red", character2_button, 3)

        pygame.display.flip()
        clock.tick(FPS)


def gameplay(selected_character):
    scroll_speed = 2
    
    player = Player(*selected_character, (100, HEIGHT - 50))
    platforms = [Platform(random.randint(100, WIDTH - 150), random.randint(200, HEIGHT - 100), platform_img, scroll_speed) for _ in range(3)]
    
    background = pygame.image.load("immagini/new_sfondo.jpg").convert()
    background = pygame.transform.scale(background, (WIDTH+10, HEIGHT))
    background_x = 0
    

    gravity = 0.5
    player_speed = 4
    jump_strength = -15
    font = pygame.font.Font("font/SuperMario256.ttf", 15)
   
    phrases = [
        "Ci possediamo solo il tempo che passiamo insieme",
        "Secondo te sapevao già come finiva dalla prima sera",
        "Sei il mio rimedio ai problemi", 
        "Che si amano strano", 
        "Era bello sentirti e tenerti vicino"
    ]
    message_timer = 0
    phrase_index = 0 
    message = None
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        player_on_platform = False
        platform_to_remove = None

        player.move(keys, player_speed, jump_strength, gravity)

        # Gestione delle collisioni con le piattaforme
        if len(platforms)<=0:
                platforms = [Platform(random.randint(100, WIDTH - 150), random.randint(200, HEIGHT - 100), platform_img, scroll_speed) for _ in range(3)] 
        for platform in platforms:
            
            if player.collision_rect.colliderect(platform.rect):
                # Collisione dall'alto
                if player.velocity_y > 0 and player.collision_rect.bottom <= platform.rect.top + 10:
                    player.rect.bottom = platform.rect.top
                    player.collision_rect.bottom = platform.rect.top
                    player.velocity_y = 0
                    player.is_jumping = False
                    player_on_platform = True

                # Collisione dal basso
                elif player.velocity_y < 0 and player.collision_rect.top >= platform.rect.bottom - 40:
                    
                    player.rect.top = platform.rect.bottom
                    player.collision_rect.top = platform.rect.bottom
                    player.velocity_y = 0
                    platform_to_remove = platform
                      # Mostra il prossimo messaggio
                    if phrase_index < len(phrases):
                        message = phrases[phrase_index]
                        phrase_index += 1 
                        message_timer = pygame.time.get_ticks() 
                    else:
                        finale()

                # Collisione laterale sinistra
                elif player.collision_rect.right > platform.rect.left and player.rect.centerx < platform.rect.centerx:
                    player.rect.right = platform.rect.left  + 50
                    player.collision_rect.right = platform.rect.left +50

                # Collisione laterale destra
                elif player.collision_rect.left < platform.rect.right and player.rect.centerx > platform.rect.centerx:
                    player.rect.left = platform.rect.right
                    player.collision_rect.left = platform.rect.right

                   
        if platform_to_remove:
            platforms.remove(platform_to_remove)

        if not player_on_platform and player.rect.bottom < HEIGHT:
            player.is_jumping = True
        elif player.rect.bottom >= HEIGHT: 
            player.rect.bottom = HEIGHT
            player.velocity_y = 0
            player.is_jumping = False

        background_x -= scroll_speed
        if background_x <= -WIDTH:
            background_x = 0

        for platform in platforms:
           
            platform.update()
    
            if platform.rect.top > HEIGHT:
                platform.reset_position(WIDTH, HEIGHT)
                


        SCREEN.blit(background, (background_x, 0))
        SCREEN.blit(background, (background_x + WIDTH -scroll_speed , 0))
        for platform in platforms:
            platform.draw(SCREEN)
        player.draw(SCREEN)

        if message:
            elapsed_time = pygame.time.get_ticks() - message_timer
            if elapsed_time < 4000:  # 5 secondi in millisecondi
                text_surface = font.render(message, True, "red")
                SCREEN.blit(text_surface, (WIDTH // 2 - text_surface.get_width() // 2, HEIGHT // 2))
            else:
                message = None  

        pygame.display.flip()
        clock.tick(FPS)


selected_character = homepage()
gameplay(selected_character)
