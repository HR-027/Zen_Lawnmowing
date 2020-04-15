import pygame
from Zen_Settings import *
from Zen_Sprites import *

# Game class for the main game
class Game:
    def __init__(self):
        pygame.init()
        # Sets the size of the window
        self.screen = pygame.display.set_mode([WIDTH, HEIGHT])
        # Sets the title of the window
        pygame.display.set_caption(TITLE)
        # Calculates how much time between each cycle
        self.clock = pygame.time.Clock()
        # If a key is held down for 500 milliseconds
        pygame.key.set_repeat(500, 100)

# Sets up for a new game
    def new(self):
        # A list that contains all the sprites in the game
        self.all_sprites = pygame.sprite.Group()
        # For the blocks
        self.blocks = pygame.sprite.Group()
        # For the path
        self.paths = pygame.sprite.Group()
        # For the path
        self.mobs = pygame.sprite.Group()

        # Player sprite is added to the game screen
        self.player = Player(self, 3, 8)

        # The path the player takes
        self.path = Path(self, self.player.pos[0][0], self.player.pos[0][1])

        self.mob = Mob(self, 4, 6)

        # Places a row of blocks at the top, bottom, left and right of the screen
        for x in range(0, WIDTH):
            Block(self, x, -1)
        for x in range(0, WIDTH):
            Block(self, x, 10)
        for y in range(0, HEIGHT):
            Block(self, -1, y)
        for y in range(0, HEIGHT):
            Block(self, 16, y)

# Checks to see if the game is running and then calls a series of functions if it is
    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.event_handler()
            self.update()
            self.draw()

    # Updates the game
    def update(self):
        self.all_sprites.update()

# Draws the grid the player will move on
    def draw_grid(self):
        # drawing the y axis lines
        for x in range(0, WIDTH, TILESIZE):
            pygame.draw.line(self.screen, GREY, (x, 0), (x, (HEIGHT-(TILESIZE * 2))))

        # drawing the x axis lines
        for y in range(0, (HEIGHT-TILESIZE), TILESIZE):
            pygame.draw.line(self.screen, GREY, (0, y), (WIDTH, y))

        # Draws the taskbar
        pygame.draw.rect(self.screen, ORANGE, (0, (HEIGHT - (TILESIZE * 2)), WIDTH, HEIGHT))

# Draws the stuff onto the screen
    def draw(self):
        # Fills the background to a green colour
        self.screen.fill(GREEN)
        # Calls the function which draws a grid
        self.draw_grid()
        # Draws all the sprites onto the screen
        self.all_sprites.draw(self.screen)
        # Flips the screen
        pygame.display.flip()

# The event handler to see what is pressed
    def event_handler(self):
        for event in pygame.event.get():
            # Allows the user to exit the program
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                # If left is pressed it calls move and rotates image
                if event.key == pygame.K_LEFT:
                    self.player.image = pygame.transform.rotate(self.player.img_copy, 90)
                    self.player.move(dx=-1)
                # If right is pressed it calls move and rotates image
                if event.key == pygame.K_RIGHT:
                    self.player.image = pygame.transform.rotate(self.player.img_copy, -90)
                    self.player.move(dx=+1)
                # If down is pressed it calls move and rotates image
                if event.key == pygame.K_DOWN:
                    self.player.image = pygame.transform.rotate(self.player.img_copy, 180)
                    self.player.move(dy=+1)
                # If up is pressed it calls move and rotates image
                if event.key == pygame.K_UP:
                    self.player.image = pygame.transform.rotate(self.player.img_copy, 0)
                    self.player.move(dy=-1)

# Handles the menu
    def menu(self):
        pass


g = Game()
while True:
    g.new()
    g.run()
