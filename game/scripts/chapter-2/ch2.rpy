label ch2:
    i "Thank you for coming!"
    e "That was chaotic! I never know a cafe could get that busy."
    i "Yeah, it's around this time that things start to really pick up the pace. YOu'll get used to it over time."
    i "It looks like we've passed through the worst of it. Now we can focus on other stuff we gotta do."
    e "Huh?! There's still more?"
    i "Of course. We've only halfway through the day."
    e "(sigh...)"
    e "Awww, alright then. What do I have to do?"
    i "Well for starters, we could do a little housekeeping."
    i "Here, I'll tell you what needs to be done. You can choose what you wanna start with."
    i "You could go sweep the foyer and greet customers as they come, collect some empty dishes from tables or dust the books in the library."
    e "What about you? What are you doing?"
    i "I'll be doing my barista duties and manning the cash register."
    e "(Hmm... alright then. I'll go...)"
    
    $ k_name = _("Kai")
    $ an_name = _("Annelise")
    $ ak_name = _("Akira")

    i "Okay then. You can find the equipment at the back storage."
    e "Yes boss!"
    i "Oh by the way, you might meet some of the others who are living at the dorms."
    i "They tend to lounge around the cafe at this time. "
    i "It might be a good chance for you to introduce yourself to them and get to know some people."
    e "You're right. That sounds like a good idea."
    e "What are their names?"
    i "There's [k_name!t], [an_name!t] and [ak_name!t]. They'll probably recognize you, since they all had a good look at you the first day you arrived here."
    e "[k_name!t], [an_name!t] and [ak_name!t]... alright I'll remember that."
    e "I'll be back soon!"
    i "Sounds good. I'll be right here if you need anything."

    menu:
        e "Hmm... What to do..."

        "Sweep the foyer":
            call sweep_foyer

        "Dust the library books":
            call dust_books

        "Collect empty dishes":
            call collect_dishes

    e "All done"
    return

label sweep_foyer:
    "(Sweeping the foyer)"
    return

label dust_books:
    "(Dusting the library books)"
    return

label collect_dishes:
    "(Collecting empty dishes)"
    return