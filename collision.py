from player import *
from fireball import *

def is_touch(player : Player, fireball : Fireball) -> bool:
    if ((fireball.y + fireball.size[1] - 40) < player.y):
        return False
    if ((fireball.x + fireball.size[0] - 40) < player.x):
        return False
    if ((fireball.x) > (player.x + player.size[0] - 30)):
        return False
    if (fireball.y > player.y):
        return False
    return True

def collision(player : Player, fireball):
    for i in range(len(fireball) - 1):
        if (is_touch(player, fireball[i]) == True):
            player.life -= 1
            fireball.pop(i)
            i -= 1
