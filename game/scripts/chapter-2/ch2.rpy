# chore flags
default swept_foyer = False
default dusted_books = False
default collected_dishes = False

label ch2:
    # (A bell chimes at the front of the store, signalling that another customer has left the store)

    e "Thank you for coming!"
    e "(Phew, that's finally the last one! I can finally catch my breath...)"
    i "Good job with the lunch rush. Here, drink up and rehydrate yourself."
    narrator "Ingram showed up from behind the cafe counter, holding two glasses filled with what seems to be iced coffee."
    e "That was chaotic! I never knew a cafe could get that busy."
    i "Yeah, it's around this time that things start to really pick up the pace. It gets pretty intense sometimes." 
    i "It looks like we've passed through the worst of it. Now we can focus on other stuff to do."
    e "Huh?! There's still more?"
    narrator "Ingram looked at me, donning a smug smile as always."
    i "Of course. We're only halfway through the day."
    e "(Sigh)... alright then. What do we have to do?"
    e "(...is it just me? Why does he look so happy about this?)"
    i "Well for starters, we could do a little housekeeping." 
    i "Let's see..."
    i "Maybe you can start with sweeping the foyer, collecting some empty dishes from tables or dusting the books in the library."
    e "Wha-?!"
    i "I know it's a lot, but we have all day to get it done. I'll let you choose what you want to start with."
    e "Urgh... fine. Guess it has to get done one way or another."
    e "But wait.. 'we'? What about you? What are you gonna be doing?"
    i "Well someone has to be there to handle the customers right? I'll be doing my barista duties and manning the cash register."
    e "(Hmm... I can't argue against that logic. He does have a point.)"
    i "Alright, let's get down to business then. You can find anything you need at the back room."
    e "Yes boss!"
    narrator "I pulled up my sleeves in an attempt to pump myself up, as a chuckle escaped Ingram's mouth."
    narrator "Sometimes I wonder if he's secretly enjoying this."
    i "Oh by the way, you might meet some of the others who are living at the dorms."
    i "They tend to lounge around the cafe at this time."
    i "It might be a good chance for you to introduce yourself to them and get to know some people."
    e "(Hmm, that sounds like a good idea. It would be nice to get to know who I'll be living with.)"
    e "What are their names?"
    i "There's [kai_name!t], [annelise_name!t] and [akira_name!t]. They'll probably recognize you, since they all had a good look at you the first day you arrived here."
    e "[kai_name!t], [annelise_name!t] and [akira_name!t]... alright I'll remember that."
    e "Well then, I'll be back soon!"
    i "Sounds good. I'll be right here if you need anything."

    call chores

    e "All done"
    return

# prompts for chores, will only return when all done
label chores:
    while not (swept_foyer and dusted_books and collected_dishes):
        menu:
            e "Hmm... What to do..."

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
    return

label dust_books:
    "(Dusting the library books)"
    $ dusted_books = True
    return

label collect_dishes:
    "(Collecting empty dishes)"
    $ collected_dishes = True
    return
