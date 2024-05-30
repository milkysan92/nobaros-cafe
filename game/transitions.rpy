# This is where any custom transitions will be defined

init:
# Transition for changing sprite expressions
    $ faceswap = Dissolve(0.2)

# Transitions for side image sprites
    $ config.side_image_same_transform = Dissolve(0.2)     # Switching between same character
    $ config.side_image_change_transform = Dissolve(0.2)   # Switching between diff characters

# Transform for being startled (entire scene or sprite)
    transform startle(rate=0.050):
        linear rate xoffset 2 yoffset -6
        linear rate xoffset -2.8 yoffset -2
        linear rate xoffset 2.8 yoffset -2
        linear rate xoffset -2 yoffset -6
        linear rate xoffset +0 yoffset +0

# Transform for being hit (stubbing toe, falling, etc. . .)
    transform impact(rate=0.090):
        linear rate xoffset 4 yoffset -15
        # linear rate xoffset -5.6 yoffset -4
        linear rate xoffset 5.6 yoffset -4
        # linear rate xoffset -4 yoffset -12
        linear rate xoffset +0 yoffset +0

# Transform for dialogue impact (Tripping over something, being startled, etc. . .)
    $ talkpunch = Move((0, 15), (0, -15), .10, bounce=True, repeat=True, delay=.075)

# Modified ease transition for moving sprites
    # transform ease(start, end, time):
    #     # start and end must be in ATL language (right, left, etc...)
    #     subpixel True
    #     start
    #     easein time end

# BG Transition that wipes towards right
    $ bgwipe = ImageDissolve("Transitions/blank.png", 1.0, 32)

# Various transitions from online
    $ circlewipe = ImageDissolve("Transitions/circlewipe-cw.jpg", 1.0, 8)
    $ ccirclewipe = ImageDissolve("Transitions/circlewipe-ccw.jpg", 1.0, 8)
    $ bites = ImageDissolve("Transitions/bites.jpg", 1.0, 8)
    $ bowtie = ImageDissolve("Transitions/bowtie.png", 1.0, 8)
    $ cmet = ImageDissolve("Transitions/cmet.jpg", 1.0, 8)
    $ cwside = ImageDissolve("Transitions/cw-side.jpg", 1.0, 8)
    $ cwtop = ImageDissolve("Transitions/cw-top.jpg", 1.0, 8)
    $ dots = ImageDissolve("Transitions/dots.png", 1.0, 8)
    $ edges = ImageDissolve("Transitions/edges.png", 1.0, 8)
    $ flips = ImageDissolve("Transitions/flips.png", 1.0, 8)
    $ fur = ImageDissolve("Transitions/fur.jpg", 1.0, 8)
    $ goslow = ImageDissolve("Transitions/goslow.png", 5.0, 8)
    $ letter = ImageDissolve("Transitions/letter.png", 1.0, 8)
    $ maze = ImageDissolve("Transitions/maze.png", 1.0, 8)
    $ radio = ImageDissolve("Transitions/radio.jpg", 1.0, 8)
    $ snake = ImageDissolve("Transitions/snake.png", 1.0, 8)
    $ snake2 = ImageDissolve("Transitions/snake2.png", 1.0, 8)
    $ snakes = ImageDissolve("Transitions/snakes.png", 1.0, 8)
    $ sunshine = ImageDissolve("Transitions/sunshine.jpg", 1.0, 8)
    $ glasswool = ImageDissolve("Transitions/glasswool.jpg", 1.0, 8)
    $ wet = ImageDissolve("Transitions/wet.jpg", 1.0, 8)

    $ w1 = ImageDissolve("Transitions/1.jpg", 1.0, 8)
    $ w2 = ImageDissolve("Transitions/2.png", 1.0, 8)
    $ w3 = ImageDissolve("Transitions/3.jpg", 1.0, 8)
    $ w4 = ImageDissolve("Transitions/4.jpg", 1.0, 8)
    $ w5 = ImageDissolve("Transitions/5.jpg", 1.0, 8)
    $ w6 = ImageDissolve("Transitions/6.jpg", 1.0, 8)
    $ w7 = ImageDissolve("Transitions/7.png", 1.0, 8)
    $ w8 = ImageDissolve("Transitions/8.jpg", 1.0, 8)
    $ w9 = ImageDissolve("Transitions/9.jpg", 1.0, 8)
    $ w10 = ImageDissolve("Transitions/10.jpg", 1.0, 8)
    $ w11 = ImageDissolve("Transitions/11.jpg", 1.0, 8)
    $ w12 = ImageDissolve("Transitions/12.jpg", 1.0, 8)
    $ w13 = ImageDissolve("Transitions/13.jpg", 1.0, 8)
    $ w14 = ImageDissolve("Transitions/14.png", 1.0, 8)
    $ w15 = ImageDissolve("Transitions/15.png", 1.0, 8)
    $ w16 = ImageDissolve("Transitions/16.png", 1.0, 8)
    $ w17 = ImageDissolve("Transitions/17.png", 1.0, 8)
    $ w18 = ImageDissolve("Transitions/18.png", 1.0, 8)
    $ w19 = ImageDissolve("Transitions/19.jpg", 1.0, 8)

    # Mirror transition; cw for entering and ccw for exiting
    $ swevenwipe_cw = ImageDissolve("Transitions/20.jpg", 1.5, 16)
    $ swevenwipe_ccw = ImageDissolve("Transitions/20.jpg", 1.5, 16, reverse=True)

    $ w21 = ImageDissolve("Transitions/21.jpg", 1.0, 8)
    $ w22 = ImageDissolve("Transitions/22.png", 1.0, 8)
    $ w23 = ImageDissolve("Transitions/23.png", 1.0, 8)
    $ w24 = ImageDissolve("Transitions/24.png", 1.0, 8)
    $ w25 = ImageDissolve("Transitions/25.png", 1.0, 8)
    $ w26 = ImageDissolve("Transitions/26.png", 1.0, 8)
    $ w27 = ImageDissolve("Transitions/27.png", 1.0, 8)
    $ w28 = ImageDissolve("Transitions/28.png", 1.0, 8)
    $ w29 = ImageDissolve("Transitions/29.png", 1.0, 8)
    $ w30 = ImageDissolve("Transitions/30.png", 1.0, 8)
    $ w31 = ImageDissolve("Transitions/31.png", 1.0, 8)
    $ w32 = ImageDissolve("Transitions/32.png", 1.0, 8)
    $ w33 = ImageDissolve("Transitions/33.png", 1.0, 8)