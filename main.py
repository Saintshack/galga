spacePlane = sprites.create(img("""
    ..ccc..........ffffff...
    ..f44c.......ffcc22ff...
    ..f244c...fffccccfff....
    ..f2244ccc22224442cc....
    ..cf22cc222222222b99c...
    .c222222222222b111999c..
    f222ccccccc22299111bb2c.
    fffffccc222c22222222222c
    ...ccc22224422222222222f
    ...c222244422222222222f.
    ...c22244cffc2222222ff..
    ....ccccffffcfffffff....
    .......ffff2c2f.........
    .......ffff2ccf.........
    ........ffffff..........
    ........................
"""), SpriteKind.player)
spacePlane.set_stay_in_screen(True)
info.set_life(3)
controller.move_sprite(spacePlane, 200, 200)

def on_a_pressed():
    dart = sprites.create_projectile_from_sprite(img("""
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . 2 2 2 . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
    """), spacePlane, 200, 0)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_update_interval():
    bogey = sprites.create(img("""
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . 2 . . . . . . . . .
        . . . . . . 7 7 . . . . . . . .
        . . . 7 2 7 2 . 7 . . . . . . .
        . . 2 7 7 7 7 . . 7 . . . . . .
        . . . 7 2 7 2 . 7 . . . . . . .
        . . . . . . 7 7 . . . . . . . .
        . . . . . . 2 . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
    """), SpriteKind.enemy)
    bogey.set_velocity(-100, randint(-100, 0))
    bogey.left = scene.screen_width()
    bogey.y = randint(0, scene.screen_height())
    bogey.set_flag(SpriteFlag.AUTO_DESTROY, True)
game.on_update_interval(500, on_update_interval)

def on_on_overlap(sprite, otherSprite):
    otherSprite.destroy()
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap)

def on_on_overlap2(sprite, otherSprite):
    otherSprite.destroy()
    sprite.destroy(effects.fire, 100)
    info.change_score_by(1)
    music.string_playable("", 120)
    music.play(music.melody_playable(music.ba_ding), music.PlaybackMode.UNTIL_DONE)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap2)

