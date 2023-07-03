# chore flags
default swept_foyer = False
default dusted_books = False
default collected_dishes = False
default chores_left = 3
default TOTAL_CHORES = 3

label ch2:
    scene cafe with fade
    # (A bell chimes at the front of the store, signalling that another customer has left the store)
    show emi with dissolve
    e "Thank you for coming!"
    e "(Phew, that's the last one! I can finally catch my breath. . .)"
    show emi at right with move
    show ingram at left with dissolve
    i "Good job with the lunch rush. You held up pretty well."
    i "Here,{w=0.1} drink up and rehydrate yourself."
    narrator "Ingram showed up from behind the cafe counter, holding two glasses of what seems to be iced coffee."
    e "That was chaotic! I never knew a cafe could get that busy."
    i "Yeah, it's around this time that things start to really pick up the pace.\nIt gets pretty intense sometimes." 
    i "It looks like we've passed through the worst of it. Now we can focus on other stuff to do."
    e "Huh?! There's still more?"
    narrator "Ingram looked at me, donning a smug smile as always."
    i "Of course. We're only halfway through the day."
    e "*Sigh*"
    e "Alright then. What do we have to do?"
    e "(. . . is it just me? {w=0.3}Why does he look so happy about this?)"
    i "Well for starters, we could do a little housekeeping." 
    i "Let's see. . ."
    i "Maybe you can start with sweeping the foyer, {w=0.1}collecting some empty dishes from tables, {w=0.1}or dusting the books in the library."
    e "Wha-?!"
    e ". . ."
    e "We still have to do all that. . .?"
    i "Mmhm."
    i "I know it's a lot, but we have all day to get it done. {w=0.3}I'll let you choose what you want to start with."
    e "Urgh. . . {w=0.5}I guess it has to be done one way or another."
    e "Hold on a minute. . ."
    e "What about you? {w=0.5}What are you gonna be doing?"
    i "Well, someone has to be there to handle the customers right? {w=0.3}I'll be doing my barista duties and manning the cash register."
    i "You're still learning the ropes, so I don't think it's a good idea to leave you to those tasks just yet."
    i "At least, not until you're more comfortable with where everything is."
    e "(Hmm. . . that's fair, I guess that makes sense.)"
    i "Alright, let's get down to business then. {w=0.5}You can find anything you need at the back room."
    e "Yes boss!"
    narrator "I pulled up my sleeves in an attempt to pump myself up, as a chuckle escaped Ingram's mouth."
    narrator "He was clearly amused."
    e "(. . . Sometimes I wonder if he's secretly enjoying this.)"
    i "Oh by the way, you might meet some of the others who also live at the dorms."
    i "They tend to lounge around the cafe at this time."
    i "It might be a good chance for you to introduce yourself to them and get to know some people."
    e "(Hmm, that's true. {w=0.3}It would be nice to get to know who I'll be living with.)"
    e "What are their names?"
    i "There's [kai_name!t], [annelise_name!t], and [akira_name!t]. {w=0.3}I've told them about you before, so they should be aware of who you are."
    i "If you haven't met any of them already, today might be your chance. I'm sure they'll be happy to meet you."
    e "[kai_name!t], [annelise_name!t] and [akira_name!t]...{w=0.5} alright, {w=0.1}I'll remember that."
    e "Well then, {w=0.1}I'll be back soon!"
    i "Sounds good. {w=0.3}I'll be right here if you need anything."
    hide ingram with dissolve
    show emi at center with move
    e "Alright! Let's get started."
    call chores

    # Show sunset cafe scene to indicate that it's later in the day
    e "Yes! Finally finished."
    e "Now to report back to Ingram."
    return

# prompts for chores, will only return when all done
label chores:
    while not (swept_foyer and dusted_books and collected_dishes):
        if chores_left == 1:
            $ text = "Almost done! I just need to..."
        elif chores_left == TOTAL_CHORES:
            $ text = "Hmm... What to do first..."
        else:
            $ text = "Ok that's done... Now I'll..."
        
        menu:
            e "[text]"
            "Sweep the foyer" if not swept_foyer:
                call sweep_foyer

            "Dust the library books" if not dusted_books:
                call dust_books

            "Collect empty dishes" if not collected_dishes:
                call collect_dishes
    return

label sweep_foyer:
    "(Sweeping the foyer)"
    $ swept_foyer = True
    $ chores_left -= 1
    return

label dust_books:
    "(Dusting the library books)"
    $ dusted_books = True
    $ chores_left -= 1
    return

label collect_dishes:
    "(Collecting empty dishes)"
    $ collected_dishes = True
    $ chores_left -= 1
    return
