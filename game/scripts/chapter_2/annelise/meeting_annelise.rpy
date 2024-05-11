label meeting_annelise:
    emi "Let's go give the library a good dusting!"
    narrator "I promptly grab the duster hanging on the wall and make a beeline for the library."
    
    scene library with fade
    show emi with dissolve
    narrator "A sea of novels encased in ebony bookshelves comes into view. Tall glass windows frame the room, cascading the space in a blanket of soft, inviting sunlight."
    narrator "Clusters of cozy armchairs beckon from various corners, each accompanied by a quaint table with a potted plant. The room is steeped in a serene hush, as the rich scent of aged paper mingles with the faint aroma of coffee from the cafe."
    narrator "I carefully step onto the hardwood floor. To my surprise, there isn't a single creak as I slowly shifted my weight to enter the room."
    emi "(It's so quiet! I can almost hear the sound of my own breath.)"
    narrator "As I wander around, I delicately run my fingers along the neatly organized rows of books, feeling the slightly rough texture of their spines."
    narrator "The selection is vast, ranging from scientific encyclopedias to enchanting novels, each book whispering stories of worlds unknown."
    narrator "The cozy atmosphere envelops me, tempting me to indulge in a tale or two. I could easily see myself taking a nap in this room if I wasn't careful."
    emi "(Now then, where would be a good place to start dusting?)"
    emi ". . . Ah!"
    narrator "Suddenly, my legs are blocked by something solid, and I nearly fall before regaining my footing in the nick of time."
    narrator "I look behind me, finding a pile of books scattered all over the floor, their pages fluttering in the air."
    narrator "On the floor, there's a girl who looks as if she was in the middle of reading."
    narrator "She looks right at me, her eyes wide with surprise. It seems like I startled her by accidentally tripping over her pile of books."
    show emi at right with move
    show annelise at left with dissolve
    emi "I'm so sorry! I didn't see you there. Are you okay?"
    uk_annelise "O-oh, um, yes! I'm fine. I was just. . . lost in my books, so I didn't realize someone else entered the room. . ."
    narrator "The girl answers in a meek voice that is barely audible. It nearly takes all of my concentration to make out what she's saying."
    narrator "I begin to collect the books scattered across the floor, stacking them neatly beside her."
    narrator "Speaking in a gentle tone, I try my best to make her comfortable."
    emi "Don't worry about it, it's my fault for not looking where I was going!"
    emi "Are you sure you're really alright? I didn't hurt you or anything?"
    uk_annelise "That's okay, I was just a bit startled that's all."
    uk_annelise "Thank you for helping with the books. I didn't realize anyone else would be here today. . ."
    emi "Oh, I'm here to help dust the library as per Ingram's orders!"
    emi "My name's Emi by the way. I recently started helping out around the cafe, so I'm relatively new around here."
    uk_annelise "Ah, Ingram? {w=0.2}Really? You're a friend of his?"
    narrator "Mentioning Ingram's name seems to have sparked something in the girl. Her eyes brighten with a newfound clarity."
    emi "Yeah, you could say that! He thought I could help pitch in with things around the cafe, so that's how I ended up here. {w=0.2}Oh, and with spirit guiding too!"
    uk_annelise "Could you be the new girl that Ingram was mentioning? You'll be staying at Yuugen House too then?"
    emi "That's me! Sorry, but I don't think I caught your name?"
    uk_annelise "Oh s-sorry! I forgot to introduce myself. My name is Annelise. It's nice to have another girl around."
    narrator "Annelise smiles timidly, feeling a tad more relaxed after realizing that I was a friend of Ingram's."
    emi "Alright, I won't disturb you from your reading too much then! I'll get right to cleaning, and you can go back to enjoying your book."
    annelise "Okay, good luck with the cleaning. Let me know if you need any help."
    hide annelise with dissolve
    show emi at center with move
    narrator "Annelise dives right back into her reading as I begin dusting on the other side of the library, taking the opportunity to tidy up the remaining books on the tables."
    narrator "Fortunately, there isn't much dust to clean and I swiftly make my way through the bookshelves, ensuring to get into each nook and cranny."
    show emi at right with move
    show annelise at left with dissolve
    narrator "As I approach Annelise, I notice the pile of books beside her has grown."
        emi "(Is she planning to read those books? Or has she already finished them?)"

    # Choose whether to put the books away or leave Annelise alone
    menu:
        "Offer to put the books away":
            call shelve_books from _call_shelve_books
        
        "Continue dusting the library":
            call continue_dusting from _call_continue_dusting
    
    $ dusted_books = True
    $ chores_left -= 1
    return