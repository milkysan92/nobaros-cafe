# Prologue master script; the main situation logic belongs here; there should be no dialogue lines
label prologue_master:
    call ingram_intro
    call emi_intro
    call nobaros_intro
    call around_town_intro
    call nobaros_cafe_intro
    call sweven_mirror_intro
    call yuugen_house_intro
    call cafe_training_intro
    call new_customer_1
    call sweven_mirror_1
    call staircase_encounter_intro
    return