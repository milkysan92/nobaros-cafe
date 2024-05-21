label new_customer_2:
    scene cafe
    show ingram at left
    show emi at right
    uk_generic "Um, excuse me. . ."
    narrator "A hesitant voice breaks my train of thought, and I turn my head to find a man who appears quite disoriented."
#TODO: Figure out how to simultaneously ease the duo while dissolving izumi
#TODO: Figure out how to write this ease transition as its own transform
    show ingram:
        left
        easein 1.0 xpos 1600

    show emi:
        right
        easein 1.0 xpos 4100
    # show ingram at Position(xpos=1600, xanchor='left')
    # show emi at Position(xpos=4100, xanchor='right')
    pause(0.5)
    show izumi at left with dissolve
    emi "Hi, how can I help you?"
    uk_generic "Do you know where I am? I think I'm a bit lost."
    emi "(He doesn't know where he is? Could he be a customer?)"
    narrator "I glance at Ingram, who seems to have realized what I was thinking. He nods at me, confirming my suspicions, and steps forward to greet the man."
    show ingram:
        xpos 1600
        easein 1.0 xpos 1500
    ingram "Welcome to Nobaros, the realm situated between life and death."
    ingram "My name is Ingram, I work as a barista here at Nobaros Cafe."
    ingram "It's a pleasure to meet you. May I know how I should refer to you?"
    uk_generic "Oh uh, just Izumi is fine."
    ingram "Well then Izumi, do you remember anything? Either about yourself or what you were doing just before this?"
    izumi "Yes, I was in my room not that long ago. I still remember it clearly."
    izumi "I was just about to head to bed, but then I suddenly felt a sharp pain in my chest and had trouble breathing. Within minutes, I lost my strength and passed out."
    izumi "For a brief moment, everything felt cold and still. All the thoughts in my head completely disappeared, and I just felt absolute nothingness."
    narrator "Izumi clutches his chest, the memory of his heart attack still vivid."
    izumi "When I regained consciousness, I found myself here."
    emi "(Hmm, so he does remember what happened to him. That rules out the possiblity of him being a vagabond.)"
    emi "(So that means he's actually. . .)"
    emi "(What a surprise, he's so young too. Is he in his twenties maybe? There's no way he's older than thirty at most.)"
    izumi "So you said this is the realm between life and death. . .? I'm not in the afterlife just yet?"
    ingram "No, you're here because there are unresolved matters from your life."
    ingram "As a spirit guide, I'll be helping you through the process of fulfilling one last joy before you move on."
    ingram "But first, would you like something to drink? It may help to calm your mind and sort your feelings out as we chat."
    narrator "Ingram presents the special drink menu to him, offering a selection of beverages to choose from."
    ingram "You can select any of the drinks on this menu here."
    izumi ". . .I see. Thank you, I'll take some sencha tea please."
    ingram "Coming right up."
    hide ingram with dissolve
    show emi at right
    with ease
    narrator "Ingram leaves to go prepare the tea, leaving the two of us alone at the counter."
    narrator "As soon as Ingram is out of sight, Izumi turns to me with an uncertain look."
    izumi "So your name is. . .?"
    emi "Ah hello, my name is Emi! I help Ingram out with the spirit guiding stuff."
    izumi "Ah okay, nice to meet you. . ."
    narrator "Izumi's voice grows quiet, and awkward silence fills the air."
    emi ". . ."
    izumi ". . ."
    emi "S-so, what do you think of Nobaros?"
    izumi "Eh? I guess it's nice and peaceful. . ."
    emi "Right? I like it too!"
    izumi "I see. . ."
    emi ". . ."
    izumi ". . ."
    emi "(Ingram, I'm begging you, please come back soon. . .)"
    narrator "I carefully watch Izumi out of the corner of my eye, trying to be as discreet as possible."
    narrator "He appears to be studying the cafe interior, soaking in all the little details. His gaze becomes fixated on the array of coffee beans stacked against the wall, staring while deep in thought."
    narrator "As he looks over the coffee selection, the ambient light accentuates his photogenic features, almost as if he came straight out of a book. Despite his towering height, he has a gentle demeanor that's far from intimidating."
    narrator "Interestingly, he doesn't seem very shocked or angry, despite his circumstances."
    emi "(Hmm, I thought he'd be more distressed in this situation.)"
    emi "(Obviously, nobody would be very happy after a heart attack, but he's strangely calm.)"
    emi "(If it were me in his position. . .)"
    narrator "A chill runs down my spine. Shaking my head, I decide not to explore that thought."
    emi "(Let's not accidentally jinx myself.)"
    emi "(I haven't recovered my memories yet. Until then, who knows what could've happened to me?)"
    show ingram at Position(xpos=1600, xanchor='left') behind emi with dissolve
    show emi:
        right
        easein 1.0 xpos 4100
    narrator "Just then, Ingram returns with a pot of freshly brewed sencha."
    ingram "Sorry for the wait, here's your tea."
    narrator "As Ingram pours a cup for Izumi, hot steam emanates from the spout, dissipating into the air with each passing moment."
    izumi "Thank you, sorry for the trouble."
    narrator "As Izumi sips his drink, the tension in his shoulders disappears and his body deflates with a satisfied look."
    narrator "After a moment of relaxation, Ingram starts explaining the spirit guiding process. Izumi listens attentively, nodding with an acknowledging look every so often."
    emi "(. . .He hasn't questioned anything Ingram said so far. This guy really is handling himself well.)"
    narrator "Just as Ingram finishes his explanation, Izumi notices my gaze and turns to me."
    izumi "Um sorry, is there something on my face?"
    izumi "It's just that you're staring at me so intently. . ."
    emi "Oh no, sorry! I didn't mean to make you uncomfortable."
    izumi "It's alright, I was just a little anxious whether my glasses were misaligned or something."
    emi "Don't worry, it's nothing like that. I was just impressed by how well you're taking Ingram's explanation."
    emi "It's quite a lot of new information to take in, especially after you just learned about your. . .erm. . ."
    izumi "It's okay, I'm alright. There's no need to beat around the bush, you can speak comfortably."
    ingram "Emi does have a point though. All sorts of people come through these parts."
    ingram "It usually takes time for reality to set in, although it does vary from person to person."
    ingram "Some need extra time to sort out their feelings, while others transition quite smoothly."
    ingram "But from what I can see, it almost seems like you've accepted what happened already, is that right?"
    izumi "Ah, well. . ."
    narrator "Izumi averts his gaze, his eyes settling on the trail of steam rising lazily from his cup. Unspoken words and unresolved emotions flicker across his expression, but his lips remain still."
    narrator "He hesitates for a moment, searching for the right words. Finally, he speaks, his voice soft and tinged with a hint of vulnerability."
    izumi "Would you care to listen to my story?"
    ingram "Of course, go ahead. Whatever you're comfortable telling us."
    ingram "It would help us understand you and your life better."
    izumi ". . ."
    izumi ". . .I have what's called cardiomyopathy. It's a condition that makes it harder for my heart to pump blood."
    izumi "Because of my condition, I've dealt with heart complications all my life."
    izumi "Although I used to live in the city as a kid, my parents decided to move to the countryside when I entered middle school."
    izumi "They thought a more peaceful lifestyle might've been better for me."
    show izumi smile at left with faceswap
    izumi "But as a kid, there was nothing more boring than being surrounded by nothing to do."
    narrator "Izumi chuckles, his laughter carrying a hint of nostalgia as he reminisces his youth."
    izumi "I started picking up photography to pass the time. At first, it was just borrowing my dad's camera to take pictures of the cicadas during the summer."
    izumi "But over time, the hobby grew on me. That's how I became a photographer."
    emi "Oh wow, that's amazing! Did you ever publish your photos at an exhibition of some sorts?"
    show izumi at left with faceswap
    izumi "Yes, my photos were often posted on a blog that was managed by my older sister."
    izumi "I was hesitant at first, but after some encouragement from my sister, I decided to let her post my photos."
    izumi "The blog ended up attracting a lot of attention, and people left really nice comments about how much they liked my photos. So after that, I continued to snap photos for her to post."
    show izumi smile at left with faceswap
    izumi "In fact, some of my favourite memories are from photography trips my sister organized. She'd find out about a scenic location from social media, then drag me there to sightsee and take photos."
    izumi "When I told her I wanted to go professional, she bought me a brand new camera for my birthday. It was the super expensive kind too."
    izumi "She was always supportive of me. Even after she moved out and got married, she kept the photography blog going."
    narrator "A warm smile carves itself on Izumi's lips at the mention of his sister. He looks out the window with a tender look."
    izumi "It was her way of trying to create memories with me."
    izumi "With my heart condition, I couldn't help but get anxious about what would happen if I passed away at any given moment."
    izumi "She was the one who showed me how to live in the present."
    emi "(. . .His sister must've been proud of him to support him so wholeheartedly. He talks about her so kindly.)"
    show izumi at left with faceswap
    izumi "Now that I'm here, it's sort of a funny feeling. On one hand, I really miss her."
    izumi "But on the other hand, I'm really glad that I was able to leave behind all of my photos at least."
    show izumi smile at left with faceswap
    izumi "That way, a part of me will always remain by her side as she carries on with life."
    show izumi at left with faceswap
    izumi "So. . .I guess that's why in your eyes, I'm dealing with this relatively well. A part of me has always expected this to happen someday."
    emi "I see. You're really mature for thinking that way, it's admirable."
    show izumi smile at left with faceswap
    izumi "Thanks for the compliment."
    show izumi at left with faceswap
    izumi ". . .There's just one thing I haven't been able to achieve as a photographer."
    izumi "To create my magnum opus. My one true masterpiece."
    izumi "There were definitely lots of photos that turned out beautifully, but there was always something missing from them."
    emi "What was missing? Was there a certain feeling or subject you were aiming for?"
    narrator "Izumi shakes his head, staring down at his lap without an answer. Judging from the melancholy in his expression, the topic must've weighed heavily on him."
    izumi "Unfortunately, I'm not actually sure what that 'something' is."
    izumi "I'm just not satisfied with the photos I've taken to date."
    narrator "Izumi meets our gaze, his eyes carrying a determined glint of hope."
    narrator "In that moment, I realize that despite his gentle impression, there's a resilience in him; a quiet, stubborn strength to fulfill his desire."
    izumi "So this spirit guiding thing. . ."
    izumi "I'll use it as another chance to create the photo I've been striving for."
    ingram ". . .I see, I applaud your resolve."
    ingram "I'm sure once you find that missing puzzle piece, that desire of yours won't burden you anymore."
    ingram "And I'd wager your sister would want you to move on freely."
    show izumi smile at left with faceswap
    izumi "Yeah, I can just imagine her scolding me if I didn't."
    show izumi at left with faceswap
    ingram "Thank you for sharing about your life with us. We'll definitely do our best to help you."
    narrator "Ingram rises from his chair and walks over to Izumi, extending his hand."
    show izumi smile at left with faceswap
    narrator "Izumi smiles, accepting the gesture with a slight bow. A quiet understanding seems to form between the two, almost like an unspoken promise."
    show izumi at left with faceswap
    ingram "Emi, can you start stacking the chairs on the tables? I don't think we'll receive any more customers, so we'll be closing up shop a bit earlier than usual."
    ingram "We'll bring Izumi to the mirror afterwards."
    emi "Okay, just leave it to me! I'll get it done in no time."
    izumi ". . ."
    scene blank with bgwipe
    scene sweven_mirror with bgwipe
    pause(0.3)
    show ingram at Position(xpos=1600, xanchor='left') behind emi
    show emi at Position(xpos=4100, xanchor='right')
    show izumi at left
    with dissolve
    ingram "Here we are. This is the Sweven Mirror, where the spirit guiding will take place."
    ingram "Once you enter, you'll go through a dream sequence before finally being sent off to the afterlife."
    izumi "So this is where it's all going to happen. . ."
    narrator "Izumi approaches the mirror, stopping just shy of it. For a moment, he appears to be pondering something. But before long, he takes a deep breath and turns around to face me and Ingram."
    izumi "Thank you for this. I really do appreciate it."
    show izumi smile at left with faceswap
    narrator "Izumi's face lights up, his eyes shining with resolve. His expression is unwavering; a reflection of the courage he's mustered to face his past."
    narrator "As he steps towards the mirror, its surface begins to shimmer with an ethereal light, enveloping him in a gentle embrace."
    narrator "I watch as the light swirls around him, drawing him into its depths with a soft, almost melodic hum."
    hide izumi smile with dissolve
    show ingram:
        xpos 1600
        easein 1.0 left
    show emi:
        xpos 4100
        easein 1.0 right
    narrator "As Izumi disappears into the mirror, its light slowly fades, leaving behind a lingering sense of peace."
    narrator "With a simple gesture, Ingram indicates that it's now my turn to enter."
    ingram "Emi, remember that you can always consult me if you get stuck while going through his memories."
    ingram "Just step aside and call for me inside your mind, then I'll respond."
    emi "Thanks Ingram, I'll do that if I need your help."
    narrator "Ingram smiles at my response and closes his eyes. Raising both arms, he opens his palms and mutters under his breath."
    narrator "Within seconds, a blue luminescent aura forms itself around the both of us. A tender feeling courses through my body, bringing a sense of weightlessness."
    emi "(The aura feels gentler this time. Did he adjust his powers slightly to make me more comfortable?)"
    narrator "With Ingram concentrating on maintaining the aura around us, I turn to face the mirror."
    emi "(Let's go. I'll do everything I can to help Izumi!)"
    scene swevenlight with swevenwipe_cw
    pause(0.5)
    scene blank with fade
    return
