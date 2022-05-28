import pygame, sys

# initialise pygame
pygame.init()

# dimension of window
WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)

# title of window
pygame.display.set_caption("My First Pygame")

# setting clock/fps
clock = pygame.time.Clock()

# creating game window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# dirt and grass image (16 x 16)
grass_image = pygame.image.load('assets/grass.png')
dirt_image = pygame.image.load('assets/dirt.png')
TILE_SIZE = grass_image.get_width()

# scrolling movement (list) allow decimals
true_scroll = [0, 0]

print('adding animations')

def load_map(path):
    f = open(path + '.txt', 'r')
    data = f.read()
    f.close()
    data = data.split('\n')
    game_map = []
    for row in data:
        game_map.append(list(row))
    return game_map


game_map = load_map('assets/map')

display_width = 480
display_height = 270
display_size = (display_width, display_height)
# scaling the dirt and grass to window (4x)
display = pygame.Surface(display_size)

# player image
player_image = pygame.image.load('assets/KNIGHT.png')
#player_image = pygame.image.load('assets/SECONDMODEL.png')
player_image = pygame.transform.scale(player_image, (16, 16))
bg_image = pygame.image.load('assets/01073865290819.5d61d475f0072.jpg')
bg_image = pygame.transform.scale(bg_image, display_size)

# cloud background
close_cloud1 = pygame.image.load('assets/Cirrus_cloud_2.png')
close_cloud1 = pygame.transform.scale(close_cloud1, (91, 37))
close_cloud2 = pygame.image.load('assets/Cumulonimbus_cloud_2.png')
close_cloud2 = pygame.transform.scale(close_cloud2, (186, 66))
far_cloud1 = pygame.image.load('assets/Cirrocumulus_cloud_3.png')
far_cloud1 = pygame.transform.scale(far_cloud1, (135, 71))
far_cloud2 = pygame.image.load('assets/Regular_cloud_2.png')
far_cloud2 = pygame.transform.scale(far_cloud2, (96, 32))

background_objects = [[0.25, [100, 50, far_cloud1.get_width(), far_cloud1.get_height()]],
                      [0.25, [300, 20, far_cloud2.get_width(), far_cloud2.get_height()]],
                      [0.50, [50, 20, close_cloud1.get_width(), close_cloud1.get_height()]],
                      [0.50, [250, 50, close_cloud2.get_width(), close_cloud2.get_height()]]]

my_background_objects = [[0.25, [100, 50, far_cloud1]],
                         [0.25, [300, 20, far_cloud2]],
                         [0.50, [50, 20, close_cloud1]],
                         [0.50, [250, 50, close_cloud2]]]

moving_right = False
moving_left = False

# momentum is for gravity
player_y_momentum = 0

# airtime updates per frame, adds buffer to jumping a few frames after collision
air_timer = 0

# rect for player, for collisions
player_rect = pygame.Rect(240, 85, player_image.get_width(), player_image.get_height())
test_rect = pygame.Rect(WINDOW_WIDTH / 2 - 75, WINDOW_HEIGHT / 2 - 75, 100, 50)


# rect : player rect, tiles : list of rects
def collision_test(rect, tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list


# movement, x first, check collisions, then y, check collision. NOT DIAGONAL
# move rect with movement(list), tiles to generate hitlist with
def move(rect, movement, tiles):
    collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}
    # move x first, then check for collisions and adjust
    rect.x += movement[0]
    hit_listx = collision_test(rect, tiles)
    for tile in hit_listx:
        # if moving right
        if movement[0] > 0:
            rect.right = tile.left
            collision_types['right'] = True
        elif movement[0] < 0: # moving left
            rect.left = tile.right
            collision_types['left'] = True
    # moving y later, with a new updated hit_list
    rect.y += movement[1]
    hit_listy = collision_test(rect, tiles)
    for tile in hit_listy:
        # if falling down
        if movement[1] > 0:
            rect.bottom = tile.top
            collision_types['bottom'] = True
        elif movement[1] < 0:
            rect.top = tile.bottom
            collision_types['top'] = True
    return rect, collision_types


# game loop
while True:
    display.blit(bg_image, (0, 0))

    # divide by 20 to add abit of delay for camera (looks better)
    true_scroll[0] += (player_rect.x - true_scroll[0] - 248)/20
    true_scroll[1] += (player_rect.y - true_scroll[1] - 143)/20

    # scroll has no decimals to make less screen tearing
    scroll = true_scroll.copy()
    scroll[0] = int(true_scroll[0])
    scroll[1] = int(true_scroll[1])

    # adding the background objects with parallax scrolling, List(amount to * into scroll, List(rect parameter))
    '''
    for obj in background_objects:
        obj_rect = pygame.Rect(obj[1][0] - scroll[0] * obj[0], obj[1][1] - scroll[1] * obj[0],
                               obj[1][2], obj[1][3])
        if obj[0] == 0.5:
            pygame.draw.rect(display, (14, 222, 150), obj_rect)
        else:
            pygame.draw.rect(display, (9, 91, 85), obj_rect)
    '''

    for obj in my_background_objects:
        display.blit(obj[1][2], (obj[1][0] - scroll[0] * obj[0], obj[1][1] - scroll[1] * obj[0]))

    # list to keep track of not "air" for collision later
    tile_rects = []

    y = 0
    for row in game_map:
        x = 0
        for tile in row:
            if tile == '1':
                # x and y are * by the image size to get correct coordinates
                display.blit(dirt_image, (x * TILE_SIZE - scroll[0], y * TILE_SIZE - scroll[1]))
            if tile == '2':
                display.blit(grass_image, (x * TILE_SIZE - scroll[0], y * TILE_SIZE - scroll[1]))
            # if tile is not "air", we need to keep track of rect so we can add collision
            if tile != '0':
                tile_rects.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            x += 1
        y += 1

    # for tiles in tile_rects:
    #     pygame.draw.rect(display, (255,0,0), tiles)

    # default no movement
    player_movement = [0, 0]
    if moving_right:
        player_movement[0] += 2
    if moving_left:
        player_movement[0] -= 2
    player_movement[1] += player_y_momentum
    player_y_momentum += 0.2
    # capping the falling acceleration
    if player_y_momentum > 6:
        player_y_momentum = 6

    player_rect, collisions = move(player_rect, player_movement, tile_rects)

    if collisions['bottom']:
        player_y_momentum = 0
        air_timer = 0
    else:
        air_timer += 1

    if collisions['top']:
        player_y_momentum = 0

    display.blit(player_image, (player_rect.x - scroll[0], player_rect.y - scroll[1]))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                moving_right = True
            if event.key == pygame.K_a:
                moving_left = True
            if event.key == pygame.K_SPACE:
                # about 3 frames for 0.2 momentum to clear 1 pixel, 3 frames for buffer
                if air_timer < 8:
                    player_y_momentum = -4
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                moving_right = False
            if event.key == pygame.K_a:
                moving_left = False

    screen.blit(pygame.transform.scale(display, WINDOW_SIZE), (0, 0))
    pygame.display.update()
    clock.tick(60)
