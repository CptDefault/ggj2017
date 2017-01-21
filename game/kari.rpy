
label kari_intro:
    scene bg engineering 
    
    show kari working
    "The woman before you is completely engrossed in a tangle of wires hanging from the wall."
    e "So, this doohickey goes with that one. {w=1.0}Yeah. {w=1.0}Or, no?"
    show kari smiling
    e "Oh, hi! You're back on your feet!"
    show kari concerned
    e "Are you feeling better? Seems you got quite the welcoming party."
    menu:
        "It wasn't the smoothest arrival I've had":
            jump kari_intro_notsmooth
        "That was nothing. You should see what visiting my aunt is like!":
            jump kari_intro_visitaunt

label kari_intro_notsmooth:
    e "Too right! Those bugs are just making a mess of everything here"
    jump kari_intro_wallBlowsUpe
label kari_intro_visitaunt:
    "Oh, sure! I mean, this must all seem pretty tame to you, right?"
    $ kari_aunt_mentioned = True
    jump kari_intro_wallBlowsUp
    
label kari_intro_wallBlowsUp:
    "Sparks burst from the wall."
    show kari working
    e "Oh, blast. Hey, pass me the combombulator?"
    menu:
        "Pass her a faintly glowing wrench":
            "Kari frowns, but hits something in the wall with the not-combombulator until the sparks stop."
        "Pass her a long stick with several pairs of what look like scissors hanging from it":
            "Kari frowns, but hits something in the wall with the not-combombulator until the sparks stop."
        "Pass her a drink bottle with several wires poking out of it":
            "Kari throws you a grin and gets to work. Moments later, the sparks stop."
    show kari smiling
    e "Well, that should keep going until the bugs blow it up again."
    e "What can I do for you?"
    jump kari_menu_intro

label kari_menu_intro:
    menu:
        "What was your name, again? I never caught more than \"Kari\"?":
            jump kari_name
        "What can you tell me about the radio transmitter?":
            jump kari_radio
        "What do you do for fun around here?":
            jump kari_fun
        "What can you tell me about the rest of the crew?":
            jump kari_askaboutcrew
        "That's all for now.":
            jump kari_bye

label kari_name:
    show kari frown
    e "Look, it's just Kari. Okay?"
    menu:
        "Sure. Forget I asked.":
            show kari smile
            "Thanks. Anything else I can do for you?"
            jump kari_menu_intro
        "Ah. Family issues?":
            if kari_aunt_mentioned:
                "Yeah. My family make visiting your aunt look like cuddling a bunny."
                "And it's got nothing to do with your case, so drop it. Okay?"
            else:
                "Yeah. And it's got nothing to do with your case, so drop it. Okay?"
            jump kari_menu_intro

label kari_radio:
    e "Someone stuffed it with half a kilo of explosives and lit the fuse?"
    e "Now the hull's breached, so that whole part of the ship's sealed off."
    e "No easy way I can get in there unless I go outside and patch it up first."
    menu:
        "Spacewalks are pretty routine, right":
            "Sure, if the ship's not under attack by space bugs every couple of hours."
        "I'm guessing there's a problem with that":
             "You may have noticed the space bugs attacking things like small shuttles. And, I suspect, people on spacewalks."
    "And besides, I've got enough work here keeping the whole station from blowing up."
    menu:
        "Any way of fixing the radio from here?":
            "Nope. That section's sealed off, and even if I suited up, I can't get in there without venting half the rest of the ship."
            "And the backup radio's in the same room. No hatch patch means no radio, period."
        "The captain said something about a backup?":
            "Right, the backup. It's in the same room as the radio, but again, can't get in there."
        "Come to think of it, I was supposed to work on the backup right before the bugs attacked. Someone spilt coffee into it and fried one of the modules."
        "And before you ask, no, I don't know who."
        "I did make a list of what I needed to fix it, though. I'll grab the parts, just in case we figure out a way in there."
                                                                                                   
    
label kari_fun:
    
    
label kari_askaboutcrew:
    
    
label kari_bye:
    "Okay! Catch you round!"