# Prologue master script; the main situation logic belongs here; there should be no dialogue lines
label prologue_master:
    # TODO: Delete these disclaimers further into development
    "Welcome to the Nobaros Cafe prototype!"
    "This is the very base of the game that will be continually refined/added to as we go through the development stages."
    "The goal is to provide a base idea of the story and implement the route/choice logic."
    "All images/bgm are to get a vague idea of what kind of scene is set up, but Renpy logic involving sprites or transitions will need to be edited."
    "The images have been either sourced from the internet (ex: Google images) or created by the creator's friend(s)."
    "{color=#8489ff}Developer notes are highlighted in blue (like this), and will be removed at a later part of the development stage.{/color}"
    "With that being said, please enjoy the prototype as it is and please send your feedback to @milkysan92 on Discord!"
    "PROLOGUE BEGIN"
    call ingram_intro
    call emi_intro
    call nobaros_intro
    call around_town_intro
    call nobaros_cafe_intro
    call sweven_mirror_intro
    call yuugen_house_intro
    return