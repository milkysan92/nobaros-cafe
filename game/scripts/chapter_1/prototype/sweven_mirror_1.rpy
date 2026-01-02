label sweven_mirror_1:
    "..."
    scene workshop with fade
    emi "(Huh... Where am I...?)"
    "You find yourself wrapped several folds of fabric. The warmth is comforting, but also a bit restricting."
    "Looks like you're wrapped in what looks like a blanket?"
    emi "(Whoa...!!)"
    scene workshop at startle
    "You try and rise to your feet, only to stumble onto a hard surface."
    emi "(What the...?)"
    show bird emi at Position(ypos=1100, yanchor="center") with dissolve
    "(This would ideally be a picture showing your reflection as a little bird in a small mirror)"
    show bird emi at startle
    emi "Chirp chirp!"
    emi "(Is this me?! What happened to my body?!)"
    hide bird emi with dissolve
    "You look around and realize you're in a cozy workshop."
    "Above, you find several guitars hanging from the ceiling."
    emi "(This must be [ch1_name]'s workshop... But where's [ch1_name]?)"
    "You look around, but there's no sign of him."
    "You start to feel a bit uneasy being alone in an unfamiliar place."
    "Just then, the door opens."
    show brio with dissolve
    brio "Hm?"
    "He notices you and walks over to take a closer look."
    brio "Hello there, little one."
    "He extends a finger, brushing it against your feathers."
    brio "Seems like you're doing a lot better now."
    brio "You were barely breathing before, but I'm glad you made it through the night."
    hide brio with dissolve
    "With a smile, he heads over to his workbench."
    "You watch as he grabs a chisel and whittles away at a piece of wood."
    emi "(He looks so focused... it's amazing to see how much work goes into making a guitar.)"
    show brio with dissolve
    brio "You know, you remind me of my grandfather's bird."
    brio "I used to feed it bits of bread every morning before school."
    brio "He'd always get mad at me for overfeeding it, so our mornings were always full of noisy bickering."
    "He sighs fondly at the memory."
    brio "...I loved that bird."
    brio "I wish I could see him one last time."
    brio "Maybe I'll also carve a little something after this guitar, as a tribute."
    "His eyes glimmer as he brushes away the woodchips from the table."
    "You had a feeling he was talking about more than just the bird."
    brio "... (He's smiling here.)"
    show brio at startle
    brio "...! (No longer smiling)"
    emi "Chirp?"
    show brio at startle
    brio "Hurgh! (He's cupping his mouth while clutching stomach)"
    hide brio with dissolve
    "Suddenly, [ch1_name] rushes out of the room."
    "You hear a faint hurl, followed by running water and violent coughs."
    emi "(Oh no...)"
    emi "(He sounds like he's in so much pain.)"
    emi "(I almost forgot about him having cancer...)"
    emi "(I wish I could help him somehow.)"
    emi "(Should I ask Ingram...?)"
    show blank with fade
    "You close your eyes and concentrate, trying to envision Ingram's voice."
    emi "Ingram, are you there?)"
    "..."
    show ingram with dissolve
    ingram "Hello?"
    ingram "[emi_name], are you okay? I heard you calling for me."
    emi "Yes, don't worry, I'm okay."
    emi "It's just... [ch1_name] seems to be in a lot of pain..."
    emi "I'm stuck in a bird's body right now, but is there anything we can do to help him?"
    ingram "Unfortunately, since these memories are already set in reality, what we can change is very limited."
    emi "No way... so I can only sit here and watch?"
    ingram "That's correct. Our role is to encourage him to finish his guitar, but nothing more."
    ingram "If he doesn't change his mind despite our best efforts, then there's nothing else we can say or do."
    emi "I see..."
    ingram "In any case, don't put yourself in harm's way."
    ingram "You shouldn't be prioritizing someone else's happiness over your own wellbeing."
    emi "Got it, I'll be careful."
    hide ingram with dissolve
    hide blank with fade
    show brio with dissolve
    "Just then, [ch1_name] returns, looking a bit pale."
    brio "Urgh..."
    emi "Chirp chirp..."
    emi "(Poor him, it's not easy having to deal with such pain.)"
    emi "(How long has he been enduring it?)"
    brio "Ah, little one... sorry about that."
    "He smiles weakly, though you can see the strain in his eyes."
    "He takes a deep breath and composes himself, once again picking up his chisel."
    brio "There's not much time left..."
    brio "I need to hurry up..."
    scene blank with bgwipe
    scene workshop with bgwipe
    "Day after day, you watch [ch1_name] pour his heart and soul into crafting the guitar."
    "Over time, his symptoms seem to worsen. Yet his work never falters."
    "Before long, the guitar starts to take shape."
    scene blank with bgwipe
    scene workshop with bgwipe
    show brio with dissolve
    brio "Is this the right choice...?"
    "You stare at [ch1_name], his face contorted into a frown."
    "A crumpled sheet of paper and steaming cup of tea sits in front of him."
    "There are several lacquer names written. Some are scratched out while others are adorned with question marks."
    "A scrap woodblock sits nearby, glistening in the sun."
    "There are several swatches of lacquer on it, each one a slightly different finish than the other."
    emi "(He brought this out a while ago, but hasn't touched the guitar this whole time...)"
    "You stare at the unfinished guitar hanging against the wall. Several parts of it have been taped off in preparation for the lacquer."
    brio "Should I test another one..."
    "You turn back to [ch1_name]. His pencil is at the last name on the list."
    brio "No, this one has a beautiful finish. I'm sure there's no better color than this..."
    brio "But is it really what my grandfather would have put on his guitar?"
    "He tosses his pencil in frustration, rubbing his eyes under his glasses."
    "You scuttle closer."
    emi "Chirp chirp..."
    emi "(His face has gotten so much darker recently... I need to do something.)"
    emi "(How should I comfort him...?)"
    menu:
        "Reach a wing out to him":
            call reaching_out
        "Nuzzle against his arm":
            "Still in development"
            # call nuzzle_arm
    return