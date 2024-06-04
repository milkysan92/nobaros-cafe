# TODO: Incorporate this label at the end of cafe_intro.rpy when editing process is finished
# prompts for chores, will only return when all done
label chores:
    while not (swept_foyer and dusted_books and collected_dishes):
        if chores_left == 1:
            $ text = "(I'm making good progress! Now I just need to. . .)"
        elif chores_left == TOTAL_CHORES:
            $ text = "(Hmm. . . what should I start with?)"
        else:
            $ text = "(Now I should. . .)"
        
        menu:
            emi base "[text]"
            "Sweep the foyer" if not swept_foyer:
                call meeting_kai from _call_meeting_kai

            "Dust the library books" if not dusted_books:
                call meeting_annelise from _call_meeting_annelise

            "Collect empty dishes" if not collected_dishes:
                call meeting_akira from _call_meeting_akira
    return