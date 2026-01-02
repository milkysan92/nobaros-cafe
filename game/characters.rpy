# CHARACTER NAME VARIABLES----------------------------------------------------------------------------------------------
# Names are set as variables to make translation easier down the line
# Main characters
# Code files & variables will use "emi", but player name will be displayed in-game
default emi_name = "Emi"
define emi_surname = _("Auclaire")
define ingram_name = _("Ingram")
define kai_name = _("Kai")
define kai_surname = _("Ayuzawa")
define annelise_name = _("Annelise")
define annelise_surname = _("Watanabe")
define akira_name = _("Akira")
define akira_surname = _("Higashi")

# Customers for spirit guiding missions
define ch1_name = _("Brio")
define ch2_name = _("Izumi")
define ch6_name = _("Akina")

# Other NPCs
define friend_name = _("Yua")
define crush_name = _("Shohei")
define grandson_name = _("Haruto")
define manager_name = _("Manager")

# List of names to check against for invalid player names
define npc_names = [
    ingram_name,
    kai_name,
    kai_surname,
    annelise_name,
    annelise_surname,
    akira_name,
    akira_surname,
    ch1_name,
    ch2_name,
    ch6_name,
    friend_name,
    crush_name,
    grandson_name,
    manager_name,
    "",
    "Akane",
    "Jun",
]

# Function to pick player name at start of game
label pickName:
    window show
    $ renpy.dynamic('done', 'name', 'prompt')
    $ done = False
    while not done:
        call screen name_input
        $ name = emi_name.strip()
        if name.capitalize() in npc_names:
            '
            "[name]" is an invalid name.
            Please choose a different name for yourself.
            '
        else:
            $ done = True
    $ emi_name = name
    window auto # Restore window auto mode
    return

# CHARACTER DEFINITIONS----------------------------------------------------------------------------------------------
# Redefine narrator to control emi's side image during narration
define narrator = Character("", image="emi")

# Main characters
# Define Emi and her many personas for spirit guiding missions (SGMs)
define emi = Character("[emi_name]", color="#ffbcca", image="emi")
define sgm_emi = Character("[emi_name]?", color="#ffbcca")
define past_emi = Character("Past [emi_name]", color="#d9d9d9", image="emi")
define config.side_image_tag = "emi"    # Persistent side image when others are talking

# Emi SGM
define ch1_emi = Character("[emi_name]?", color="#ffbcca", image="bird")
image bird emi = "images/Sprites/SGMs/ch1/bird_emi.png"
define ch2_emi = Character("[emi_name]?", color="#ffbcca", image="himari")
image himari = "images/Sprites/SGMs/Himari/himari_base.avif"
image himari concern = "images/Sprites/SGMs/Himari/himari_concern.avif"

# Define other charas with the image tag emi to control emi's side image while they're talking
define ingram = Character(ingram_name, color="#9fe7ff", image="emi")
define kai = Character(kai_name, color="#fad5af", image="emi")
define akira = Character(akira_name, color="#c7f5c5", image="emi")
define annelise = Character(annelise_name, color="#fff0b1", image="emi")

# Spirit guiding mission characters
# Chapter 1
define brio = Character(ch1_name, color="#d9d9d9")

# Chapter 2
define izumi = Character(ch2_name, color="#d9d9d9")
image izumi = "Sprites/SGMs/Izumi/izumi_base.avif"
image izumi smile = "Sprites/SGMs/Izumi/izumi_smile.avif"
define haruto = Character(grandson_name, color="#ffffff")
define grandma = Character(f"{grandson_name}'s grandma", color="#ffffff")
define grandpa = Character(f"{grandson_name}'s grandpa", color="#ffffff")

# Chapter 6
define akina = Character(ch6_name, color="#d9d9d9", image="emi")

# Other NPCs
define yua = Character(friend_name, color="#d9d9d9", image="emi")
define shohei = Character(crush_name, color="#d9d9d9", image="emi")
define manager = Character(manager_name, color="#d9d9d9", image="emi")

# Unknown characters for pre-introduction interactions
define uk_nar = Character("", what_slow_cps=30)
define uk_generic = Character("?????", color="#ffffff", image="emi")
define uk_emi = Character("?????", color="#ffbcca", image="emi")
define uk_ingram = Character("?????", color="#9fe7ff", image="emi")
define uk_kai = Character("?????", color="#fad5af", image="emi")
define uk_akira = Character("?????", color="#c7f5c5", image="emi")
define uk_annelise = Character("?????", color="#fff0b1", image="emi")
