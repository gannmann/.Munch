"""
Issac Gann (gannmann) 2020

assets module imports sprites from image files and spritesheets.
"""

import pygame
pygame.init()

# CONFIG
window_width = 800
window_height = 600
#fullscreen = False
framerate = 60

# INTIALIZE
master_window = pygame.display.set_mode((window_width, window_height), flags=pygame.HWSURFACE | pygame.ASYNCBLIT)

icon = pygame.image.load('tiles/logo.png')

# ASSET STUFF
tile_width = 64
tile_height = 64

# offset items/player/monsters 16 tiles west and 32 tiles down
item_width = 32
item_height = 32

shade = (0, 0, 50)
hidec = (255, 255, 255, 100)

def from_file(location, hide=False):
    tile = pygame.image.load(location)
    tile.convert_alpha()
    shadow_tile = tile.copy()
    shadow_tile.fill(shade, special_flags= pygame.BLEND_RGBA_MIN)
    if not hide:
        return (tile, shadow_tile)
    else:
        hide_tile = tile.copy()
        hide_tile.fill(hidec, special_flags= pygame.BLEND_RGBA_MULT)
        shadow_hide_tile = shadow_tile.copy()
        shadow_hide_tile.fill(hidec, special_flags= pygame.BLEND_RGBA_MULT)
        return (tile, shadow_tile, hide_tile, shadow_hide_tile)

def from_sheet(spritesheet, x, y, hide=False):
    tile = spritesheet.subsurface((x*tile_width, y*tile_height, tile_width, tile_height))
    tile.convert_alpha()
    shadow_tile = tile.copy()
    shadow_tile.fill(shade, special_flags= pygame.BLEND_RGBA_MIN)
    if not hide:
        return (tile, shadow_tile)
    else:
        hide_tile = tile.copy()
        hide_tile.fill(hidec, special_flags= pygame.BLEND_RGBA_MULT)
        shadow_hide_tile = shadow_tile.copy()
        shadow_hide_tile.fill(hidec, special_flags= pygame.BLEND_RGBA_MULT)
        return (tile, shadow_tile, hide_tile, shadow_hide_tile)

# corpse sprites
corpse, corpse_shade = from_file('tiles/Dungeon Crawl Stone Soup Full/misc/blood/blood_puddle_red.png')

def get_corpse(sprite, shadow_sprite):
    new_corpse = corpse.copy()
    pygame.Surface.blit(new_corpse, sprite, (0, 0))
    new_corpse = pygame.transform.rotate(new_corpse, 90)

    new_corpse_shade = corpse_shade.copy()
    pygame.Surface.blit(new_corpse_shade, shadow_sprite, (0, 0))
    new_corpse_shade = pygame.transform.rotate(new_corpse_shade, 90)

    return new_corpse, new_corpse_shade

#sheet = pygame.image.load('tiles/nethack_tiles_32x32px_by_nevanda.png')
sheet = pygame.image.load('tiles/rltiles-pack/64x64.png')
sheet = sheet.convert_alpha()


# CREATURES or features lol

up_staircase, up_staircase_shade = from_sheet(sheet, 5, 5)

down_staircase, down_staircase_shade = from_sheet(sheet, 4, 5)

game_background = (16, 16, 16)

# stone brick tiles
sheet_stone = pygame.image.load('tiles/rltiles-pack/catacomb.png')
sheet_stone = sheet_stone.convert_alpha()

w0_stone, w0_stone_shade, w0_stone_hide, w0_stone_shade_hide = from_sheet(sheet_stone, 0, 0, True)
w1_stone, w1_stone_shade, w1_stone_hide, w1_stone_shade_hide = from_sheet(sheet_stone, 1, 0, True)
w2_stone, w2_stone_shade, w2_stone_hide, w2_stone_shade_hide = from_sheet(sheet_stone, 2, 0, True)
w3_stone, w3_stone_shade, w3_stone_hide, w3_stone_shade_hide = from_sheet(sheet_stone, 3, 0, True)
w4_stone, w4_stone_shade, w4_stone_hide, w4_stone_shade_hide = from_sheet(sheet_stone, 4, 0, True)
w5_stone, w5_stone_shade, w5_stone_hide, w5_stone_shade_hide = from_sheet(sheet_stone, 5, 0, True)
w6_stone, w6_stone_shade, w6_stone_hide, w6_stone_shade_hide = from_sheet(sheet_stone, 6, 0, True)
w7_stone, w7_stone_shade, w7_stone_hide, w7_stone_shade_hide = from_sheet(sheet_stone, 7, 0, True)
w8_stone, w8_stone_shade, w8_stone_hide, w8_stone_shade_hide = from_sheet(sheet_stone, 0, 1, True)
w9_stone, w9_stone_shade, w9_stone_hide, w9_stone_shade_hide = from_sheet(sheet_stone, 1, 1, True)
wA_stone, wA_stone_shade, wA_stone_hide, wA_stone_shade_hide = from_sheet(sheet_stone, 2, 1, True)
wB_stone, wB_stone_shade, wB_stone_hide, wB_stone_shade_hide = from_sheet(sheet_stone, 3, 1, True)
wC_stone, wC_stone_shade, wC_stone_hide, wC_stone_shade_hide = from_sheet(sheet_stone, 4, 1, True)
wD_stone, wD_stone_shade, wD_stone_hide, wD_stone_shade_hide = from_sheet(sheet_stone, 5, 1, True)
wE_stone, wE_stone_shade, wE_stone_hide, wE_stone_shade_hide = from_sheet(sheet_stone, 6, 1, True)
wF_stone, wF_stone_shade, wF_stone_hide, wF_stone_shade_hide = from_sheet(sheet_stone, 7, 1, True) 

closed_door_1_stone, closed_door_1_stone_shade, closed_door_1_stone_hide, closed_door_1_stone_shade_hide = from_sheet(sheet_stone, 0, 2, True) 
closed_door_2_stone, closed_door_2_stone_shade, closed_door_2_stone_hide, closed_door_2_stone_shade_hide = from_sheet(sheet_stone, 1, 2, True)
open_door_1_stone, open_door_1_stone_shade, open_door_1_stone_hide, open_door_1_stone_shade_hide = from_sheet(sheet_stone, 2, 2, True)
open_door_2_stone, open_door_2_stone_shade, open_door_2_stone_hide, open_door_2_stone_shade_hide = from_sheet(sheet_stone, 3, 2, True)

floor_stone, floor_stone_shade = from_sheet(sheet_stone, 4, 2)

# item sprites
banana_tile, banana_tile_shade = from_file('tiles/Dungeon Crawl Stone Soup Full/item/food/banana_new.png')

# monster sprites
goblin_tile, goblin_tile_shade = from_file('tiles/Dungeon Crawl Stone Soup Full/monster/goblin_new.png')
goblin_corpse, goblin_corpse_shade = get_corpse(goblin_tile, goblin_tile_shade)

skeleton, skeleton_shade = from_file('tiles/Dungeon Crawl Stone Soup Full/monster/undead/skeletal_warrior_new.png')
skeleton_corpse, skeleton_corpse_shade = get_corpse(skeleton, skeleton_shade)

# player sprites
player_tile, player_tile_shade = from_file('tiles/Dungeon Crawl Stone Soup Full/monster/unique/chuck.png')

'''
FONTS
'''
body_font = pygame.font.Font('fonts/Gorilla.ttf', 12)
tiny_font = pygame.font.Font('fonts/Gorilla.ttf', 8)

# colors

floor_color = (96, 96, 96)
floor_color_dark = (64, 64, 64)

wall_color = (160, 160, 160)
wall_color_dark = (128, 128, 128)

open_door_color = (0, 204, 0)
open_door_color_dark = (0, 153, 0)

closed_door_color = (0, 0, 204)
closed_door_color_dark = (0, 0, 153)

feature_color = (255, 0, 255)
feature_color_dark = (204, 0, 204)

item_color = (255, 255, 0)
item_color_dark = (204, 204, 0)

entity_color = (255, 0, 0)
entity_color_dark = (204, 0, 0)

target, target_shade = from_sheet(sheet, 6, 10)
