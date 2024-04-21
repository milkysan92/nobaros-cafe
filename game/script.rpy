# Master script; this script should contain global vars & overall chapter logic
define emi_name = _("Emi")
define ingram_name = _("Ingram")
define kai_name = _("Kai")
define annelise_name = _("Annelise")
define akira_name = _("Akira")

define emi = Character(emi_name, color="#ffbcca")
define ingram = Character(ingram_name, color="#9fe7ff")
define kai = Character(kai_name, color="#fad5af")
define akira = Character(akira_name, color="#c7f5c5")
define annelise = Character(annelise_name, color="#fff0b1")

label start:
    # call intro_script
    # call ch1_script
    # call ch2_script
    # call ch3_script
    # call ch4_script

    # From here on out, the player is locked in character specific routes; the logic for route locking will be contained in chapter 4
    # Might want to double check if it's possible to change/update the value of a variable if something changes within one of the scripts?
    # Set global variable ("route"?) to determine which route chapters to play

    # if route == "Ingram":
        # call ch5_ingram
        # call ch6_ingram
        # call ch7_ingram
        # Inspect variables referring to choices made and call the right ending
        # If relationshipPoints >= 40:
            # call goodEnd_ingram
        # else:
            # call badEnd_ingram

    # if route == "Kai":
            # call ch5_kai
            # call ch6_kai
            # call ch7_kai
            # Inspect variables referring to choices made and call the right ending
            # If relationshipPoints >= 40:
                # call goodEnd_kai
            # else:
                # call badEnd_kai

    # if route == "Akira":
            # call ch5_akira
            # call ch6_akira
            # call ch7_akira
            # Inspect variables referring to choices made and call the right ending
            # If relationshipPoints >= 40:
                # call goodEnd_akira
            # else:
                # call badEnd_akira

    # if route == "Annelise":
            # call ch5_annelise
            # call ch6_annelise
            # call ch7_annelise
            # Inspect variables referring to choices made and call the right ending
            # If relationshipPoints >= 40:
                # call goodEnd_annelise
            # else:
                # call badEnd_annelise

    # call intro
    # call phantasia
    # call intro_cafe
    return
