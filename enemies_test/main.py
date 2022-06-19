import pygame


window = pygame.display.set_mode((1720, 1200), pygame.RESIZABLE)
clock = pygame.time.Clock()


sprites = pygame.sprite.Group()


class Entity(pygame.sprite.Sprite):
    def __init__(
        self,
        pos: tuple[int, int],
        size: tuple[int, int],
        color: str,
        *groups: pygame.sprite.AbstractGroup,
    ) -> None:
        super().__init__(*groups)
        self.velocity = pygame.Vector2((0, 0))
        self.image = pygame.Surface(size)
        self.rect = self.image.get_rect(topleft=pos)
        self.image.fill(pygame.Color(color))

    def draw(self) -> None:
        window.blit(self.image, self.rect)


class Enemy(Entity):
    def __init__(
        self,
        pos: tuple[int, int],
        size: tuple[int, int],
        color: str,
        *groups: pygame.sprite.AbstractGroup,
    ) -> None:
        super().__init__(pos, size, color, *groups)

    def check_collision(self) -> None:
        for sprite in sprites:
            if sprite != self:
                if self.rect.colliderect(sprite.rect):
                    self.rect.bottom = sprite.rect.top
                    self.velocity.y = 0
                    if self.velocity.x == 0:
                        self.velocity.x = 10

    def move(self) -> None:
        for sprite in sprites:
            if sprite != self:
                if self.rect.left < sprite.rect.left:
                    self.rect.left = sprite.rect.left
                    self.velocity.x *= -1
                elif self.rect.right > sprite.rect.right:
                    self.rect.right = sprite.rect.right
                    self.velocity.x *= -1

    def update(self) -> None:
        if self.velocity.y < 10:
            self.velocity.y += 0.8
        self.rect.move_ip(self.velocity)
        self.move()
        self.check_collision()
        print(self.velocity)


class Plank(Entity):
    def __init__(
        self,
        pos: tuple[int, int],
        size: tuple[int, int],
        color: str,
        *groups: pygame.sprite.AbstractGroup,
    ) -> None:
        super().__init__(pos, size, color, *groups)
        self.rect.centerx = window.get_rect().centerx
        self.rect.y = int(window.get_height() * 0.8)


enemy = Enemy((window.get_width() // 2, 400), (70, 150), "red", sprites)
plank = Plank((0, 0), (int(window.get_width() * 0.7), 50), "black", sprites)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    window.fill(pygame.Color("white"))
    enemy.draw()
    plank.draw()
    enemy.update()
    pygame.display.update()
    clock.tick(60)
