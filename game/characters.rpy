
# CHARACTER NAME VARIABLES----------------------------------------------------------------------------------------------
# Main characters
# TODO: Allow Emi's name to be customizable based on player input;
# Code files will use "emi", but player name will be displayed in-game
define emi_name = _("Emi")
define ingram_name = _("Ingram")
define kai_name = _("Kai")
define annelise_name = _("Annelise")
define akira_name = _("Akira")

# Customers for spirit guiding missions
define ch1_name = _("Brio")
define ch2_name = _("Izumi")
define ch6_name = _("Akina")

# Other NPCs
define friend_name = _("Yua")
define crush_name = _("Shohei")
define emi_ch2 = _("Himari")
define grandson_name = _("Haruto")

# CHARACTER DEFINITIONS----------------------------------------------------------------------------------------------
# Redefine narrator to control emi's side image during narration
define narrator = Character("", image="emi")

# Main characters
# Define Emi and her many personas from spirit guiding missions
define emi = Character(emi_name, color="#ffbcca", image="emi")
define sgm_emi = Character(f"{emi_name}?", color="#ffbcca")
define config.side_image_tag = "emi"    # This line is for persistent side image

# Emi CH2 SGM
define ch2_emi = Character(f"{emi_name} (as {emi_ch2})", color="#ffbcca", image="himari")
image himari = "Sprites/Customers/Himari/himari_base.avif"
image himari concern = "images/Sprites/Customers/Himari/himari_concern.avif"

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
image izumi = "Sprites/Customers/Izumi/izumi_base.avif"
image izumi smile = "Sprites/Customers/Izumi/izumi_smile.avif"
define haruto = Character(grandson_name, color="#ffffff")
define grandma = Character(f"{grandson_name}'s grandma", color="#ffffff")
define grandpa = Character(f"{grandson_name}'s grandpa", color="#ffffff")

# Chapter 6
define akina = Character(ch6_name, color="#d9d9d9")

# Other NPCs
define yua = Character(friend_name, color="#d9d9d9")
define shohei = Character(crush_name, color="#d9d9d9")

# Unknown characters for pre-introduction interactions
define uk_nar = Character("", what_slow_cps=30)
define uk_generic = Character("?????", color="#ffffff")
define uk_emi = Character("?????", color="#ffbcca")
define uk_ingram = Character("?????", color="#9fe7ff")
define uk_kai = Character("?????", color="#fad5af")
define uk_akira = Character("?????", color="#c7f5c5")
define uk_annelise = Character("?????", color="#fff0b1")
