import pygame

width = 800
height = 600


clientNumber = 0


class Player:
    def __init__(self, location: tuple, size: tuple, color: tuple):
        """Player Class Initialization

        Args:
            location (tuple): x,y of starting location
            size (tuple): height,width of rectangle
            color (tuple): RBG of color code
        """
        self.x = location[0]
        self.y = location[1]
        self.width = size[0]
        self.height = size[1]
        self.color = color
        self.rect = (self.x, self.y, self.width, self.height)

        self.vel = 3

    def draw(self, win: pygame.Surface) -> None:
        pygame.draw.rect(win, self.color, self.rect)

    def move(self) -> None:
        try:
            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT]:
                self.x -= self.vel

            if keys[pygame.K_RIGHT]:
                self.x += self.vel

            if keys[pygame.K_UP]:
                self.y -= self.vel

            if keys[pygame.K_DOWN]:
                self.y += self.vel

            self.rect = (self.x, self.y, self.width, self.height)
        except Exception as e:
            if (len(e.args) > 0) and (e.args[0] == "video system not initialized"):
                return
            exception_type = type(e).__name__
            print(f"An exception of type {exception_type} occurred.")


def redrawWindow(win: pygame.Surface, player: Player) -> None:
    try:
        win.fill((255, 255, 255))
        player.draw(win)
        pygame.display.update()
    except Exception as e:
        if (len(e.args) > 0) and (e.args[0] == "display Surface quit"):
            return
        exception_type = type(e).__name__
        print(f"An exception of type {exception_type} occurred.")


def main() -> None:
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption("T-T-T Client")
    run = True
    p = Player((50, 50), (100, 100), (0, 255, 0))
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p.move()
        redrawWindow(win, p)

    print("end run")
    return


def add(a: int, b: int) -> int:
    """Adds two integers together

    Args:
        a (int): first integer
        b (int): second integer

    Returns:
        int: sum of integers
    """
    return a + b


if __name__ == "__main__":
    main()
