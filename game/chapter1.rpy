# After the prologue through to something dramatic.
# Not including individual character interactions


label chap1_postwakeup:
    scene bg bridge
    menu:
        "You've been asked to speak to the captain"
        "Find the Captain":
            call myron_intro
        "Go back to Jeneva, the Second Scientist":
            call jeneva_revisit_intro
    if myron_intro_complete:
        jump chap1_hub
    jump chap1_postwakeup

label chap1_hub:
    scene bg bridge
    menu:
        "Find the Captain":
            call myron_revisit_intro
        "Go back to Jeneva, the Second Scientist":
            call jeneva_revisit_intro
        "Visit Quincy, the Lead Scientist":
            if quincy_intro_complete:
                call quincy_revisit_intro
            else:
                call quincy_intro
        "Go to Engineering":
            if kari_intro_complete:
                call kari_revisit_intro
            else:
                call kari_intro
                
    if quincy_intro_complete and kari_intro_complete:
        jump chap1_somethingdramatic
    jump chap1_hub
    
label chap1_somethingdramatic:
    scene bg bridge
    
    e "Oh fiddles damn it!"
    show kari concerned at right
    e "Oi! Captain!"
    
    show myron at center
    c "Engineer! Report!"
    e "I got a drone bot into the radio room. You're not going to like this."
    show quincy at left
    s "Kari, I've spoken to you about inside voices before."
    e "The radio. It wasn't taken out by the bugs."
    e "It was taken out from inside. By..."
    c "A bomb! I knew it!"
    
    scene black with Dissolve (2)
    
    "Will our hero find out where the bomb came from?"
    "Is one of their four crewmates A TRAITOR?"
    "Find out next time in Episode 2 of SABOTAGE! A SCIENCE MISSION"