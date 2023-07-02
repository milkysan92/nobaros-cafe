image swevenMirror = "sweven-mirror.jpg"
image blank = "#000000"
image light = "#FFFFFF"
define unknown_e = Character("?????", color="#ffbcca")
define unknown_i = Character("?????", color="#9fe7ff")

label intro:
    scene swevenMirror with fade
    narrator "Memories."
    narrator "They're joyful little things, aren't they?"
    narrator "String them together, and they'll spin all sorts of interesting stories."
    narrator "Stories that come from those who have journeyed this same path before you."
    narrator "Imagine those you love and cherish.{w=0.5} Why are they so special to you?"
    narrator "It's because of the memories you share with them, {w=0.3} no?"
    narrator "Wouldn't you even say that your memories shape who you are?"
    show blank with dissolve
    narrator ". . ."
    narrator "You are a gentle soul. {w=0.5}I can see you've been bruised by the trauma you've faced in the past."
    narrator "Your memories bring you only pain and suffering."
    narrator "You can't bring yourself to endure it any more."
    narrator "And that's why you've come to me for help,{w=0.5} yes? {w=0.5}"
    narrator ". . .{w=0.5} I see. {w=0.5} Very well then."
    narrator "If this is your final decision, {w=0.3}then I will lend you my power."
    narrator "I hope that one day, {w=0.3}you will be able to face yourself and move on from these memories."
    narrator "Now then, {w=0.3}close your eyes and breathe."
    narrator "Sweet dreams.{w=0.5} Until we meet again."

    # (Longer transition between monologue and Emi's pov intro)
    scene light with fade
    narrator ""
    unknown_e "Warm..."
    unknown_i "..."
    unknown_i "Someone..."
    unknown_e "Who...?"

    return