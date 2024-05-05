define unknown_an = Character("?????", color="#fff0b1")

label meeting_annelise:
    emi "Let's go give the library a good dusting!"
    narrator "I promptly grab the duster hanging on the wall and make a beeline for the library."
    
    scene library with fade
    show emi with dissolve
    narrator "A sea of novels stacked on ebony bookshelves comes into view, bathed in a blanket of soft, inviting sunlight."
    narrator "The bookshelves line one wall, while big windows adorns the others, offering a glimpse of the outside world."
    narrator "Several comfy-looking armchairs are scattered around, each accompanied by a quaint table with a potted plant, breathing life into the room."
    narrator "A serene silence occupies the space, the rich scent of old books mixed with the faint aroma of coffee from the cafe."
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
    unknown_an "O-oh, um, yes! I'm fine. I was just. . . lost in my books, so I didn't realize someone else entered the room. . ."
    narrator "The girl answers in a meek voice that is barely audible. It nearly takes all of my concentration to make out what she's saying."
    narrator "I begin to collect the books scattered across the floor, stacking them neatly beside her."
    narrator "Speaking in a gentle tone, I try my best to make her comfortable."
    emi "Don't worry about it, it's my fault for not looking where I was going!"
    emi "Are you sure you're really alright? I didn't hurt you or anything?"
    unknown_an "That's okay, I was just a bit startled that's all."
    unknown_an "Thank you for helping with the books. I didn't realize anyone else would be here today. . ."
    emi "Oh, I'm here to help dust the library as per Ingram's orders!"
    emi "My name's Emi by the way. I recently started helping out around the cafe, so I'm relatively new around here."
    unknown_an "Ah, Ingram? {w=0.2}Really? You're a friend of his?"
    narrator "Mentioning Ingram's name seems to have sparked something in the girl. Her eyes brighten with a newfound clarity."
    emi "Yeah, you could say that! He thought I could help pitch in with things around the cafe, so that's how I ended up here. {w=0.2}Oh, and with spirit guiding too!"
    unknown_an "Could you be the new girl that Ingram was mentioning? You'll be staying at Yuugen House too then?"
    emi "That's me! Sorry, but I don't think I caught your name?"
    unknown_an "Oh s-sorry! I forgot to introduce myself. My name is Annelise. It's nice to have another girl around."    
    narrator "Annelise smiles timidly, feeling a tad more relaxed after realizing that I was a friend of Ingram's."
    emi "Alright, I won't disturb you from your reading too much then! I'll get right to cleaning, and you can go back to enjoying your book."
    annelise "Okay, good luck with the cleaning. Let me know if you need any help."
    hide annelise with dissolve
    show emi at center with move
    narrator "Annelise dives right back into her reading as I begin dusting on the other side of the library."
    narrator "I take the opportunity to tidy up the remaining books on the tables."
    narrator "Fortunately, there isn't much dust to clean and I swiftly make my way through the bookshelves, ensuring to get into each nook and cranny."
    show emi at right with move
    show annelise at left with dissolve
    narrator "As I approach Annelise, I notice the pile of books beside her has grown."
    emi "(Is she planning to read those books? Or has she already finished them?)"

    # Choose whether to put the books away or leave Annelise alone
    menu:
        "Offer to put the books away":
            call shelve_books
        
        "Continue dusting the library":
            call continue_dusting
    
    $ dusted_books = True
    $ chores_left -= 1
    return

label shelve_books:
    emi "Hey Annelise, do you need some help putting those books away? You can toss them my way if you want!"
    narrator "Annelise looks up from her novel, her eyes sparkling as if I just read her mind. She eagerly nods in agreement."
    annelise "Yes, actually! I'm glad you asked, I got these books as a recommendation from Ingram, but I'm not tall enough to reach the shelf they came from."
    annelise "I didn't want to bother him because he looked so busy. There have been customers all day, so I haven't found a good time to ask him about it. . ."
    emi "That shouldn't be a problem! I'm here to tidy up the area anyways. Where do these books go?"
    narrator "Annelise looks away with a bit of a guilty look. She points to a spot near the very top of one of the bookshelves in the wall."
    emi "(Oh. . . that spot might be just out of my reach.)"
    narrator "I pause for a moment, pondering how to reach the shelf Annelise pointed to."
    emi "(I could ask Ingram, but then nobody would be around to deal with customers. And the chairs around here might not be tall enough.)"
    emi "(I wonder if there's a ladder around that we could use. . .)"
    emi "(Oh! There might be one in the back room. There are all sorts of things back there, so surely that includes a ladder.)"
    emi "Just wait here Annelise! I'm going to check the back. There might be a ladder there that we can use."
    annelise "That's a good idea! I'll be waiting then."
    hide emi with dissolve
    scene storage_room with fade
    show emi with dissolve
    narrator "I quickly rush out of the library and check the back room, shuffling through the cleaning supplies in search of anything that looks remotely like a step ladder."
    emi "(Hmm. . . I could've sworn there was one around here.)"
    emi "(. . . Ah! {w=0.2}There it is!)"
    narrator "My eyes spot a folded step ladder hidden behind one of the shelves. I make my way over and quickly grab it, brushing off any dust stuck to it."
    narrator "With the ladder in hand, I head back to the library where Annelise is waiting."
    hide emi with dissolve
    scene library with fade
    show annelise at left with dissolve
    show emi at right with dissolve
    emi "I'm back! And look what I found!"
    narrator "As I show the ladder to Annelise, she looks at me in amazement and claps happily."
    annelise "Oh, there really was a ladder!"
    annelise "You're amazing Emi! Now we can put the books away, and I don't have to keep hoarding them by my side."
    narrator "Annelise smiles gently as she rises to her feet, carrying the stack of books over to me."
    narrator "I set up the ladder and carefully take a step, making sure that I have solid footing before climbing up to the top."
    narrator "Once I have a good view of the top shelf, I gesture for Annelise to pass me the books. She obliges, and we work through the stack slowly and methodically."
    scene library with fade
    show annelise at left
    show emi at right
    with dissolve
    emi "And that's the last one! Good work, thanks for helping me out!"
    annelise "Oh no, it's my pleasure! If anything, I'm indebted to you."
    annelise "I didn't have the heart to burden you while you were dusting the shelves, so I really appreciate that you were willing to help. . ."
    narrator "Annelise twiddles with her fingers, a little flustered by my compliment."
    emi "(Is she not used to compliments? She's pretty shy huh. . .)"
    emi "Are you a big reader? I couldn't help but notice that we put away quite a few books."
    emi "Did you read them all today?"
    annelise "Eh? {w=0.2}Ah yes, I really enjoy reading. I usually get so immersed in the story that I often tune out of reality."
    emi "That sounds fun! It's almost as if you're travelling to an entirely different dimension."
    annelise "Yes, {w=0.2}that's exactly how it feels!"
    annelise "Imagining what could happen if I did certain things differently than the main character feels wonderous."
    emi "Do you have a favourite book?"
    annelise "I do! Let me go grab it and show you!"
    narrator "Annelise's face brightens at the mention of discussing her favourite book. Her eyes shine with joy, and a radiant smile spreads across her face."
    hide annelise with dissolve
    narrator "Filled with cheerful spirit, she skips over to a nearby bookshelf in a capricious, graceful manner, like she's floating on air."
    narrator "She picks out a small novel, handling it with a gentle touch as she returns."
    show annelise at left with dissolve
    narrator "She presents the book to me, holding it out like a precious treasure. There's an air of pride and joy about her, reminiscent of an adorable child showing off their favourite toy."
    narrator "It's like the timid girl I encountered earlier has disappeared completely." 
    annelise "This is it! It's called Hiraeth, and I highly recommend it."
    annelise "It's about a young artist named Elara." 
    annelise "She experiences these extraordinary dreams where she visits a mystical land called Hiraeth, filled with enchanting mysteries and sights as far as the eye can see."
    emi "That sounds fascinating! What do you like about it?"
    annelise "I really admire Elara's strength!"
    annelise "Despite being a struggling artist with lots of challenges to overcome, she manages to find inspiration in her journeys to Hiraeth."
    annelise "Each new discovery she comes across fuels her creativity, leading to her next big artistic breakthrough!"
    annelise "I aspire to be as courageous as her one day. Her adventures sound so exhilarating!"
    narrator "I can't help but smile at Annelise's enthusiasm as she gushes about the novel."
    narrator "She notices my smile, and realizes she's been chatting non-stop for a while. She suddenly stops, cutting herself off."
    annelise "Ah, sorry! I'm probably boring you with all of this. . ."
    emi "No, not at all! I enjoyed listening to you talk! If anything, it makes me want to read the book too."
    narrator "Just then, a small piece of paper slips out from the book, floating gently to the ground between us."
    narrator "As I bend down to pick it up, Annelise quickly snatches it before I can. I look up at her, noticing a faint blush on her cheeks."
    emi "Oh, is everything okay?"
    annelise "Huh? Oh, yes, it's nothing. . ."
    annelise "I just. . . I sometimes like to sketch too. It's embarrassing, so I'd prefer if you don't tell anybody else about it."
    emi "Oh, I understand! Your secret is safe with me."
    narrator "Annelise visibly relaxes, breathing a sigh of relief. It seems she's a bit shy about sharing her art with others."
    emi "Alright! I'll have to get back to doing chores soon, or else Ingram will come looking for me."
    emi "Would you like anything to drink? You've been talking for a while, so maybe a refresher might help?"
    narrator "Annelise shakes her head, holding Hiraeth close to her chest."
    annelise "No thank you, I think I'm okay! Thank you for asking though."
    emi "Alright, sounds good. If you need anything, just let me know!"
    emi "I really have to go now, but it was nice meeting you."
    emi "Let's talk more about books when we're back at Yuugen House!"
    annelise "Yes, of course! I'd be more than happy to."
    narrator "Annelise bows slightly, a smile lighting up her face."
    narrator "I return the smile and wave as I exit the library, leaving her to her reading."
    hide emi with dissolve
    scene storage_room with fade
    show emi with dissolve
    emi "(That was pleasant! I didn't expect Annelise to be such a passionate book lover. Now I'm really curious about Hiraeth.)"
    emi "(I'll have to ask her for more recommendations later.)"
    return

label continue_dusting:
    narrator "I decide to leave Annelise alone, figuring that she probably just found more books to read."
    scene library with fade
    show emi with dissolve
    narrator "Eventually, I manage to finish dusting all the shelves in no time."
    emi "(Hmm, somehow that felt a lot quicker than I expected. . .)"
    show emi at right with move
    show annelise at left with dissolve
    narrator "I glance over at Annelise, who hasn't moved an inch since we conversed earlier."
    narrator "She has yet to notice that I finished dusting the shelves."
    emi "(That book pile is really growing by the minute. . .)"
    narrator "I decide to approach Annelise, curious about the books sitting beside her."
    emi "Annelise, are you a big reader? I couldn't help but notice that you have quite a few books in your pile."
    emi "That's a lot to read in one day, isn't it?"
    narrator "Annelise snaps back to reality as she looks up from her book, surprised by my question. It seems she wasn't expecting me to make conversation with her."
    annelise "Eh? {w=0.2}Ah yes, I really enjoy reading. I usually get so immersed in the story that I often tune out of reality."
    annelise "When that happens, time just flies right by."
    emi "That sounds fun! It's almost as if you're time travelling."
    annelise ". . .!"
    annelise "Yes, {w=0.2}that's exactly how it feels!"
    annelise "Imagining what could happen if I did certain things differently than the main character feels wonderous."
    narrator "Annelise perks up, suddenly more engaged in the conversation. She must be excited to talk about what she's reading."
    emi "So what are you currently reading? You seem so focused on it. Is it a good story?"
    annelise "Oh, this is my favourite book! Let me show you."
    narrator "Annelise's face brightens at the mention of the book she's reading. Her eyes shine with joy, and a radiant smile spreads across her face."
    narrator "Filled with cheerful spirit, she rises to her feet and skips over in a capricious, graceful manner, like she's floating on air."
    narrator "She presents the book to me, holding it out like a precious treasure. There's an air of pride and joy about her, reminiscent of an adorable child showing off their favourite toy."
    narrator "It's like the timid girl I encountered earlier has disappeared completely."
    annelise "Here, it's called Hiraeth. It may not look very interesting at first glance, but I highly recommend it!"
    annelise "It's about a young artist named Elara." 
    annelise "She experiences these extraordinary dreams where she visits a mystical land called Hiraeth, filled with enchanting mysteries and sights as far as the eye can see."
    emi "That sounds fascinating! What do you like about it?"
    annelise "I really admire Elara's strength!"
    annelise "Despite being a struggling artist with lots of challenges to overcome, she manages to find inspiration in her journeys to Hiraeth."
    annelise "Each new discovery she comes across fuels her creativity, leading to her next big artistic breakthrough!"
    annelise "I aspire to be as courageous as her one day. Her adventures sound so exhilarating!"
    narrator "I can't help but smile at Annelise's enthusiasm as she gushes about the novel."
    narrator "She notices my smile, and realizes she's been chatting non-stop for a while. She suddenly stops, cutting herself off."
    annelise "Ah, sorry! I'm probably boring you with all of this. . ."
    emi "No, not at all! I enjoyed listening to you talk! If anything, it makes me want to read the book too."
    narrator "Just then, a small piece of paper slips out from the book, floating gently to the ground between us."
    narrator "As I bend down to pick it up, Annelise quickly snatches it before I can. I look up at her, noticing a faint blush on her cheeks."
    emi "Oh, is everything okay?"
    annelise "Huh? Oh, yes, it's nothing. . ."
    annelise "I just. . . I sometimes like to sketch too. It's embarrassing, so I'd prefer if you don't tell anybody else about it."
    emi "Oh, I understand! Your secret is safe with me."
    narrator "Annelise visibly relaxes, breathing a sigh of relief. It seems she's a bit shy about sharing her art with others."
    emi "Alright! I'll have to get back to doing chores soon, or else Ingram will come looking for me."
    emi "Would you like anything to drink? You've been talking for a while, so maybe a refresher might help?"
    narrator "Annelise shakes her head, holding Hiraeth close to her chest."
    annelise "No thank you, I think I'm okay! Thank you for asking though."
    emi "Alright, sounds good. If you need anything, just let me know!"
    emi "I really have to go now, but it was nice meeting you."
    emi "Let's talk more about books when we're back at Yuugen House!"
    annelise "Yes, of course! I'd be more than happy to."
    narrator "Annelise bows slightly, a smile lighting up her face."
    narrator "I return the smile and wave as I exit the library, leaving her to her reading."
    hide emi with dissolve
    scene storage_room with fade
    show emi with dissolve
    emi "(That was pleasant! I didn't expect Annelise to be such a passionate book lover. Now I'm really curious about Hiraeth.)"
    emi "(I'll have to ask her for more recommendations later.)"
    return