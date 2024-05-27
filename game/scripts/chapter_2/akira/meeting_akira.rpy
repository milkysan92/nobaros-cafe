label meeting_akira:
    emi talk "Let's go clean up some empty dishes."
    narrator base "I grab a few of the neatly folded rags and head back out to the floor."
    scene blank with bgwipe
    scene cafe with bgwipe
    narrator base "A peaceful hum lingers, customers engrossed in conversation throughout the space."
    narrator "The soft murmur of voices creates a soothing backdrop, inviting all who enter to relax and unwind in the welcoming embrace of the cafe."
    narrator "Starting at the table closest to me, I gingerly gather the dirty dishes."
    narrator "The ceramic dishes clink softly as I stack them, their surfaces adorned with remnants of delicious meals enjoyed by the customers."
    narrator "Once the dishes are cleared, I swiftly wipe down the surface with a rag. As I progress, the pure white look of the rag turns discoloured from all the spills and crumbs."
    narrator "Soon, the smooth tabletop gleams, revealing the intricate wood grain underneath."
    narrator "I move onto the next table, scanning for any signs of leftover dishes."
    emi talk "Hm? Isn't that. . ."
    narrator base "My eyes fall on the corner of the cafe, where a familiar figure lounges around."
    narrator "He savours his espresso with small, deliberate sips, the steam dissipating in a lazy manner. Sunlight filters through the window, enveloping him in a warm aura."
    narrator "Drawing slightly closer, I squint in an attempt to discern his features."
    show akira with dissolve
    emi "(It's Akira! I ran into him back at Yuugen House the other night.)"
    narrator "His sun-kissed hair is styled in a clean fashion, with a few golden strands tucked behind his ear."
    narrator "The rose-brown hue of his eyes are framed by a sophisticated pair of glasses. A green blazer casually drapes over the shoulders of his well-fitted black dress shirt, tying the look together with a sense of refinement."
    narrator "He sets down his espresso, his gaze fixed on the scenery outside. Despite his relaxed posture, there's a subtle intensity in his eyes, as if he's analyzing the world around him."
    narrator "There's an undeniable charm about him, an aura of nonchalance that makes it seem like he could fall asleep anytime. Yet his presence is striking, leaving a lasting impression on anyone who crosses his path."
    emi "(. . .!!)"
    emi "(What am I doing? {w=0.2}Snap out of it Emi! You're in the middle of working. Stop ogling at him before he catches you!)"
    narrator "Just then, our eyes meet. Akira recognizes me immediately and waves hello, gesturing for me to come over."
    emi "(He didn't catch me staring just now, did he?)"
    narrator "I swallow my pride and make my way over to him, pretending that I just noticed him."
    narrator "Akira greets me with a kind smile, adjusting his posture as I approach the table."
    akira "Hello, we meet again."
    akira "You're Emi, right? I believe we met back at Yuugen House the other night."
    emi talk "Y-yes, I remember you. I think you said your name is Akira?"
    emi base "(Why am I stammering!? I need to calm down.)"
    akira "Bingo, you've got the right guy."
    akira "Are you busy? It's a lovely day out, and it'd be nice to chat with someone to pass the time."
    narrator "A small voice at the back of my mind tempts me to join Akira."
    emi talk "Oh, sorry, I'm in the middle of doing something. I need to collect some empty dishes and clean tables."
    akira base "Ah, is that so? So Ingram has already assigned you a fair amount of chores to work on, huh?"
    narrator "Akira shifts his gaze, scanning the cafe as he observes the other tables. I peek at the espresso cup in front of him."
    emi "(Is he almost done with his drink? It looks like there's just a sip or two left.)"
    narrator "Noticing my gaze, Akira picks up the cup and holds it in his hands, meeting my eyes with another warm smile."
    akira "It seems everyone else is still engrossed in their conversations."
    akira "Since I'm nearly finished with my espresso, why don't you take a short break and join me? It'll give you a chance to rest and also clear some dishes."
    narrator "He gestures towards the other tables, where customers are still chatting away."
    akira "Plus, it'll help you kill two birds with one stone, as they say."
    narrator "Akira's offer is quite convincing, and the little voice in my head continues to tempt me."

    # Choose whether to chat with Akira or not
    menu:
        emi talk "I think I'll. . ."
        "Focus on cafe chores":
            call cafe_duties from _call_cafe_duties

        "Sit down and chat":
            call afternoon_chat from _call_afternoon_chat

    $ collected_dishes = True
    $ chores_left -= 1
    scene blank with bgwipe
    scene storage_room with bgwipe
    return