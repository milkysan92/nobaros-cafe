label meeting_akira:
    emi "Let's go clean up some empty dishes."
    narrator "I grab a few of the neatly folded rags and head back out to the floor."
    scene cafe with fade
    show emi with dissolve
    narrator "A peaceful hum lingers, customers engrossed in conversation throughout the space."
    narrator "The soft murmur of voices creates a soothing backdrop, inviting all who enter to relax and unwind in the welcoming embrace of the cafe."
    narrator "Starting at the table closest to me, I gingerly gather the dirty dishes."
    narrator "The ceramic dishes clink softly as I stack them, their surfaces adorned with remnants of delicious meals enjoyed by the customers."
    narrator "Once the dishes are cleared, I swiftly wipe down the surface with a rag. As I progress, the pure white look of the rag turns discoloured from all the spills and crumbs."
    narrator "Soon, the smooth tabletop gleams, revealing the intricate wood grain underneath."
    narrator "I move onto the next table, scanning for any signs of leftover dishes."
    emi "Hm? Isn't that. . ."
    narrator "My eyes fall on the corner of the cafe, where a familiar figure lounges around."
    narrator "He savours his espresso with small, deliberate sips, the steam dissipating in a lazy manner. Sunlight filters through the window, enveloping him in a warm aura."
    narrator "Drawing slightly closer, I squint in an attempt to discern his features."
    show emi at right with move
    show akira at left with dissolve
    emi "(It's Akira! I ran into him back at Yuugen House the other night.)"
    narrator "His sun-kissed hair is styled in a clean fashion, with a few golden strands tucked behind his ear."
    narrator "The rose-brown hue of his eyes are framed by a sophisticated pair of glasses. A green blazer casually drapes over the shoulders of his well-fitted black dress shirt, tying the look together with a sense of refinement."
    narrator "He sets down his espresso, his gaze fixed on the scenery outside. Despite his relaxed posture, there's a subtle intensity in his eyes, as if he's analyzing the world around him."
    narrator "There's an undeniable charm about him, an aura of nonchalance that makes it seem like he could fall asleep anytime. Yet his presence is striking, leaving a lasting impression on anyone who crosses his path."
    emi "(. . .!!)"
    emi "(What am I doing? {w=0.2}Snap out of it Emi, you're in the middle of working. Stop ogling at him before he catches you!)"
    narrator "Just then, our eyes meet. Akira recognizes me immediately and waves hello, gesturing for me to come over."
    emi "(He didn't catch me staring just now, did he?)"
    narrator "I swallow my pride and make my way over to him, pretending that I just noticed him."
    narrator "Akira greets me with a kind smile, adjusting his posture as I approach the table."
    akira "Hello, we meet again." 
    akira "You're Emi, right? I believe we met back at Yuugen House the other night." 
    emi "Y-yes, I remember you. I think you said your name is Akira?"
    emi "(Why am I stammering!? I need to calm down.)"
    akira "Bingo, you've got the right guy."
    akira "Are you busy? It's a lovely day out, and it'd be nice to chat with someone to pass the time."
    narrator "A small voice at the back of my mind tempts me to join Akira."
    emi "Oh, sorry, I'm in the middle of doing something. I need to collect some empty dishes and clean tables."
    akira "Ah, is that so? So Ingram has already assigned you a fair amount of chores to work on, huh?"
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
        emi "I think I'll. . ."
        "Focus on cafe chores":
            call cafe_duties from _call_cafe_duties

        "Sit down and chat":
            call afternoon_chat from _call_afternoon_chat

    $ collected_dishes = True
    $ chores_left -= 1
    hide emi with dissolve
    scene storage_room with fade
    show emi with dissolve
    return

label cafe_duties:
    narrator "With a resigned sigh, I shake my head, acknowledging that my chores should take priority."
    narrator "If I slack off now, there's a chance that I wouldn't be able to finish them all in time."
    emi "Sorry, I would love to, but I'll have to take a rain check. There's a lot of work I need to focus on before the day ends."
    akira "I see. I understand, no need to apologize. I admire your work ethic."
    narrator "Akira gracefully lifts the cup to his lips, savouring the last sip of his espresso."
    narrator "With a fluid motion, he finishes the drink and extends the empty cup to me. He stretches leisurely, a long sigh escaping his lips."
    akira "Well then, I've stuck around for long enough now. The sun has made me drowsy, so I think I'll take a stroll to wake myself up."
    narrator "I watch as Akira stands up, a sense of regret creeping in."
    narrator "Despite running into each other twice now, I still don't know very much about him. I wish I had more time to chat with him, to learn about his experiences in Nobaros."
    narrator "As Akira makes his way to the door, he turns back and smiles at me."
    akira "It's been a pleasure, good luck with your shift."
    akira "Perhaps we can continue our conversation next time."
    emi ". . . !"
    emi "Yes, definitely! Have a good day."
    hide akira with dissolve
    show emi at center with move
    narrator "His departure leaves me with a sense of missed opportunity, a feeling that maybe I should have taken him up on his offer and savoured the moment."
    narrator "I sigh softly, knowing that duty calls and I ultimately made the responsible choice."
    emi "(Next time, I'll definitely take the chance to converse with him properly!)"
    emi "(Let's quickly finish up here and return the rags.)"
    return

label afternoon_chat:
    emi "You know what, you have a point! It can't hurt to take a little break."
    narrator "I plop down on the seat across from Akira, sinking into the comfortable cushion on the chair. He smiles, pleased that I've accepted his invitation."
    akira "I'm glad to hear that. It's always nice to have some company on a day like today."
    akira "It's also important to take breaks from time to time, don't you think?"
    narrator "His easygoing demeanor puts me at ease, and I find myself relaxing in no time. I return his smile, feeling a sense of warmth at his words."
    akira "So how's everything going around the cafe? You're fairly new, yet you're already working so diligently."
    emi "Oh, I'm learning a lot from Ingram! But I've still got a long way to go before I get to whip up some fancy desserts though."
    akira "Is that so? You seem so excited to get baking, is there a particular reason?"
    emi "Have you seen those cakes in the display case? They look absolutely stunning!"
    emi "Wouldn't it be really cool if I could do that myself? I'd love to create something so pretty-looking."
    emi "There's also something special about seeing people enjoy what I've made with my own two hands."
    narrator "Akira chuckles softly, his laughter like a melody that fills the air. As I speak, I notice a spark of recognition in his eyes, as if he understands the satisfaction of pursuing one's passions."
    narrator "Leaning forward, he rests his chin on his hand, his gaze full of intrigue and curiosity."
    akira "That's admirable. Both precision and skill are essential to creating such complicated desserts, so it's good to hone them through practice."
    akira "As a regular, I'd be honoured to taste your creations someday."
    narrator "I feel a surge of pride at his compliment, grateful for his recognition."
    emi "Thank you, I'm touched that you think so highly of me."
    akira "Of course. Only through diligence and perseverance can you expect to reap meaningful results."
    narrator "I stare as Akira takes another sip of his espresso."
    narrator "His calm demeanor exudes a sense of confidence that is both comforting and inspiring. He seems so at ease, blending seamlessly into his surroundings."
    emi "(I wonder if he's been here for a while. . .)"
    akira "How are you finding Nobaros? Adjusting well?"
    narrator "His question catches me off guard, as if he's read my mind."
    emi "Eh? Ah, I mean, it's. . . different. I'm still trying to get my bearings to be honest. But I do appreciate how tranquil this place is. I think I'll slowly be able to adjust."
    akira "I understand. When I first arrived, it was quite overwhelming."
    akira "Nobaros was unlike anything I've experienced before. But I've found it to be quite nice, a place of introspection and growth if you will."
    emi "It's reassuring to hear that. What was your first impression of Nobaros, if you don't mind me asking?"
    akira "Frankly speaking, I was in disbelief. The concept of being in a place like this, where people who have passed on or are close to it coexist, was unfathomable to me."
    akira "Walking around here with that in mind was a strange feeling. And even more so when I realized that included me."
    akira "But over time, I've come to appreciate the peace it offers. It provided an opportunity to slow down and reflect on a lot of things."
    akira "Things that I would've never stopped to think about in reality."
    emi "(No wonder he seems so well-adjusted. . .)"
    narrator "As Akira gracefully savours another sip of his espresso, I couldn't help but wonder about his life before Nobaros. What kind of life did he lead in the real world?"
    narrator "With a fluid motion, he finishes the drink and extends the empty cup to me."
    narrator "Rising from his seat, he stretches languidly, a sigh of satisfaction escaping his lips. He looks content, as if our conversation has left him refreshed."
    akira "Well then, I've kept you from your duties long enough. The sun has made me drowsy, so I think I'll take a stroll to wake myself up."
    akira "Thanks for entertaining me, it's been a pleasure."
    akira "Good luck with your shift."
    emi "Thank you! Enjoy your walk."
    hide akira with dissolve
    show emi at center with move
    narrator "I watch as Akira leaves, a sense of contentment washing over me."
    narrator "As I hold his empty cup, I feel a tinge in my chest, part of me wishing that there was more time to chat with him."
    narrator "I sigh softly, knowing that duty calls. {w=0.2}But I'm also content, happy with the choice I made."
    emi "(Let's quickly finish up here and return the rags.)"
    return