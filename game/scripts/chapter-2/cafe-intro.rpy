# chore flags
default swept_foyer = False
default dusted_books = False
default collected_dishes = False
default chores_left = 3
default TOTAL_CHORES = 3

label cafe_intro:
    scene cafe with fade
    show emi with dissolve
    emi "Thank you for coming!"
    emi "(Phew, that's the last customer! I can finally catch my breath. . .)"
    narrator "A bell chimes at the front of the store, signaling the end of the chaotic lunch hour."
    narrator "The cafe had been busier than usual. The morning hours were peaceful, with a few regulars popping in for their usual coffee or bagel."
    narrator "As the sun rose higher in the sky, more and more customers trickled in, looking for a refreshment to enjoy."
    narrator "Before I knew it, the store had filled up in the blink of an eye. I was scrambling in every direction, taking orders and relaying them to Ingram. Somehow, I managed to survive. Barely."
    narrator "I plop myself down at an empty table, stretching my arms up in the air to relieve the tension in my muscles." 
    narrator "Suddenly, a small poke taps at my shoulder, prompting me to look back. Ingram had come from behind the counter, with two icy drinks in hand and a pleased smile on his face."
    show emi at right with move
    show ingram at left with dissolve
    ingram "Good job with the lunch rush. You held up pretty well out there."
    ingram "Here,{w=0.1} I made some iced coffee for us. Think of it as a little treat for working so hard. Drink up and rehydrate yourself."
    narrator "Ingram takes the seat in front of me, passing one of the drinks over to me. Taking the glass in hand, I start taking modest sips to avoid spilling coffee on myself."
    emi "(Oh? This coffee. . .)"
    narrator "My tastebuds are greeted by a pleasant, sweet taste. Ingram had mixed some vanilla syrup into the coffee. In an instant, my sweet tooth kicks in, tempting me to devour the whole thing."
    narrator "I indulge in the icy goodness and small sips quickly turn into bigger gulps. Next thing I know, there are only a few ice cubes remaining at the bottom of my glass. I let out a satisfied sigh."
    emi "Thanks for the drink, I really needed that!"
    narrator "I look at Ingram, who is still finishing his drink. The ice cubes in his drink make a distinct clink as he downs the rest of it."
    narrator "He's awfully calm and collected, far from what I'd imagine from someone who also went through the same chaos I experienced earlier."
    emi "You know Ingram, you're really impressive"
    emi "You handled yourself so well behind the counter. I never even knew a cafe could get that busy!"
    narrator "Ingram chuckles as he sets his glass down with a solid thud."
    ingram "It's around this time that things start to really pick up the pace. It gets pretty intense sometimes."
    ingram "But one way or another, I've gotten used to it. It's nothing much really."
    ingram "But don't worry. With time, you'll be able to breeze right through the rush hours too."
    narrator "I gulp as Ingram smiles at me. Maybe he just means well, but the smile feels kind of. . . intimidating."
    narrator "The idea of being able to deal with so many orders at once still seems like a faraway dream for me."
    emi "(Maybe in a million years, sure. . .)"
    narrator "Ingram gets up from the table, collecting the two glasses as he heads back to the counter. I quickly follow suite, rejuvenated from the little coffee break."
    ingram "Well then, now that we've gotten a chance to catch our breath, we can focus on other things."
    narrator "I nearly choke at ingram's words."
    emi "Huh?! Say that again? There's still more?"
    ingram "Hm? Of course, we're only halfway through the day. There's still lots to do."
    narrator "I feel my heart sink. The happy, nonchalant mood from earlier disappears as I'm reminded that the day isn't over yet."
    narrator "I sneak a peek over at Ingram, who's already starting to wipe down the counter tops and fill the coffee grinders."
    emi "(. . .is it just me? {w=0.3}Why does he look so happy about this?)"
    emi ". . .*Sigh*"
    emi "Alright then. What do we have to do?"
    narrator "Ingram looks straight at me, his smug smile not budging a single bit. He's dead serious. Maybe even a bit sadistic."
    ingram "Well for starters, there's a little housekeeping that needs to be done." 
    ingram "Let's see. . ."
    ingram "Well, the foyer needs some sweeping. . .{w=0.1}and there's empty dishes that need to be collected from the tables. {w=0.1}Oh, and the library corner could use some dusting."
    emi ". . ."
    emi "We still have to do all that. . .?"
    ingram "Mmhm. You'll never run out of things to do around here."
    ingram "I know it's a lot, but we have all day to get it done. {w=0.3}I'll let you choose what you want to start with."
    emi "Urgh. . . {w=0.5}well, I guess it has to be done one way or another."
    emi "What about you then? {w=0.5}What are you gonna be doing?"
    ingram "Well, someone has to be there to handle the customers right? {w=0.3}I'll be doing my barista duties and manning the cash register."
    ingram "You're still learning the ropes, so I don't think it's a good idea to leave you to those tasks just yet."
    ingram "At least, not until you're more comfortable with where everything is."
    emi "Oh. . .I guess that makes sense."
    ingram "Alright, let's get down to business then. {w=0.5} I'm going to go refill some of the pastries in the display case. You can find anything you need at the back room."
    emi "Ah, yes boss!"
    hide ingram with dissolve
    show emi at center with move
    narrator "As Ingram heads over to the other side of the counter, I turn around to look for supplies in the back."
    emi "(Okay, let's do this! I should just focus on one thing at a time. This will all be over in the blink of an eye!)"
    narrator "I smack my face twice in an attempt to pump myself up."
    ingram ". . .pfft."
    show ingram at left with dissolve 
    show emi at right with move
    narrator "A snicker creeps up from behind. I spin around, finding myself face to face with Ingram once again."
    narrator "He covers his mouth in a futile attempt to stifle his laugh. I could see his entire body shaking to keep it in as I feel my cheeks burning with embarrassment."
    ingram "S-sorry, I didn't mean to interrupt your. . ."
    emi "I though you went to go fill up the display case!"
    ingram "I was going to, but I forgot to tell you something."
    ingram "Though I didn't expect you to slap yourself as soon as I turned my back. . ."
    narrator "Ingram nearly slips at the end of his sentence, but manages to keep himself together."
    emi "(. . .isn't he enjoying this a little too much?)"
    narrator "I feel the burning sensation from my cheeks spread up to my ears. I just wanna jump in a hole and bury myself six feet under. I better change the subject before he says anything else."
    emi "A-anyway! What was it that you wanted to tell me?"
    ingram "Right, I wanted to let you know that you might meet some of the others who also live around Yuugen house."
    ingram "They tend to lounge around the cafe at this time."
    ingram "It might be a good chance for you to introduce yourself and get to know them a bit."
    emi "That's fair. What are their names?"
    ingram "There's [kai_name!t], [annelise_name!t], and [akira_name!t]. {w=0.3}I've mentioned you before, so they should be aware of who you are."
    ingram "If you haven't met any of them already, today might be your chance. I'm sure they'll be happy to meet you."
    emi "[kai_name!t], [annelise_name!t] and [akira_name!t]...{w=0.5} alright, {w=0.1}I'll remember that."
    emi "Well then, {w=0.1}I'll be back soon!"
    ingram "Sounds good. {w=0.3}I'll be right here if you need anything. Just don't go beating yourself up umprompted again."
    emi "Ahhh!! Stop bringing it up!"
    narrator "Ingram smiles as I try and shoo him away."
    hide ingram with dissolve
    show emi at center with move
    narrator "Once he's out of sight, I then make my way over to the back storage room."
    # Transition to a closet BG scene
    emi "Whoa! This place is surprisingly clean."
    narrator "I'm pleasantly surprised by the level of organization inside the storage room."
    narrator "There are a whole bunch of cleaning supplies that looked untouched. Running a finger along one of the shelves, I find that there's not a speck of dust to be found. The place was absolutely spotless."
    emi "(Did Ingram do all of this too? He really is on a different level!)"
    narrator "I look around for things I would need to finish my chores, finding a broom in the corner, feather duster hanging on the wall and some neatly folded rags on a shelf."
    emi "(Hmm. . . what to do first?)"
    call chores

    # Show sunset cafe scene to indicate that it's later in the day
    emi "Yes! Finally finished."
    emi "Now to report back to Ingram."
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
            emi "[text]"
            "Sweep the foyer" if not swept_foyer:
                call meeting_kai

            "Dust the library books" if not dusted_books:
                call meeting_annelise

            "Collect empty dishes" if not collected_dishes:
                call meeting_akira
    return
