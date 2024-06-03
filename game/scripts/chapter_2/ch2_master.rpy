# Chapter 2 master script; the main situation logic belongs here; there should be no dialogue lines
default drinks = False
default twilight = False

label ch2_master:
    # call cafe_intro from _call_cafe_intro
    # call report_to_ingram from _call_report_to_ingram
    # # TODO: Put this choice menu in report_to_Ingram
    # menu:
    #     emi base "(What should I tell him. . .?)"
    #     "Ask about Ingram":
    #         call about_ingram from _call_about_ingram
    #     "Mention the others":
    #         narrator "A gut feeling tells me to leave the thought alone, so I decide to tell him about Kai, Akira and Annelise instead."
    # call meeting_others from _call_meeting_others
    # call new_customer_2
    # call sweven_mirror_2
    # # TODO: Put this choice menu in sweven_mirror_2
    # menu:
    #     ch2_emi "(Hmm, where should we go?)"
    #     "Waterfall":
    #         call waterfall
    #     "Maple tree grove":
    #         call maple_grove
    call welcome_dinner
    call bath_time
    menu:
        emi "What should I do?"
        "Grab a drink":
            $ drinks = True 
        "Chill upstairs in bedroom":
            $ twilight = True
    if drinks:
        call something_to_drink
        menu:
            emi "Hmm, I think I'll choose. . ."
            "Water":
                call midnight_snack
            "Milk":
                call milk_and_honey
            "Tea":
                call lull_of_lavender
    else:
        call twilight_stroll
    return