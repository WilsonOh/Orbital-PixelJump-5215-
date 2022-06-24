import pygame


def pause_screen():
    window = pygame.display.get_surface()
    font = pygame.font.SysFont("arial", int(window.get_height() * 0.05))
    text = font.render(
        "GAME PAUSED, PRESS ESCAPE TO RETURN or q to QUIT", True, pygame.Color("black")
    )
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                if event.key == pygame.K_q:
                    quit()
        window.fill(pygame.Color("white"))
        window.blit(
            text,
            (
                int(window.get_width() // 2 - text.get_width() // 2),
                int(window.get_height() // 2 - text.get_height() // 2),
            ),
        )
        pygame.display.update()


def menu():
    window = pygame.display.get_surface()
    font = pygame.font.SysFont("arial", int(window.get_height() * 0.05))
    title = font.render("PIXELJUMP", True, pygame.Color("black"))

    options = ["Press ENTER to start the game", "Press ESCAPE to quit the game"]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit()
                if event.key == pygame.K_RETURN:
                    return
        window.fill(pygame.Color("white"))
        window.blit(
            title,
            (
                int(window.get_width() // 2 - title.get_width() // 2),
                int(window.get_height() // 2 - title.get_height() // 2),
            ),
        )
        pygame.display.update()
