'''
creature templates
'''

import assets
import entity
import item
import weapon


# corpses


# creatures

def small_corpse(x, y):
    corpse = item.Item(name='small corpse', x=x, y=y,
                         sprite=assets.goblin_corpse, shadow_sprite=assets.goblin_corpse_shade,
                         quantity=1, action_set=['eat', 'throw'],
                         weapon_com=weapon.small_corpse)
    return corpse

def bone_corpse(x, y):
    corpse = item.Item(name='bone corpse', x=x, y=y,
                         sprite=assets.skeleton_corpse, shadow_sprite=assets.skeleton_corpse_shade,
                         quantity=1, action_set=['eat', 'throw'],
                         weapon_com=weapon.mace)
    return corpse

def goblin(x, y):
    creature = entity.Entity(name='goblin', race='Goblin', x=x, y=y,
                       vitality=3, strength=2, dexterity=4, intelligence=4, hitdie=4, ai='aggro',
                       sprite=assets.goblin_tile, shadow_sprite=assets.goblin_tile_shade,
                       corpse=small_corpse(x, y), mainhand=weapon.small_weapon(x=x, y=y), offhand=weapon.small_shield(x=x, y=y))
    return creature

def skeleton(x, y):
    creature = entity.Entity(name='skeleton', race='Skeleton', x=x, y=y, exp=15,
                       vitality=3, strength=4, dexterity=6, intelligence=3, hitdie=4, ai='aggro',
                       sprite=assets.skeleton, shadow_sprite=assets.skeleton_shade,
                       corpse=bone_corpse(x, y), mainhand=weapon.good_weapon(x=x, y=y), immunities=['bleeding'])
    return creature