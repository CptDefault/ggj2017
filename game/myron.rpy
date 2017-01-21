#Myron Padilla, captain of the research station

define myron_intro_complete = False

label myron_intro:
    scene bg bridge
    show myron
    
    c "Good to see you back on your feet, Officer"
    c "It's not everyone who can bounce back from a bit of a hull breach in such a small pod."
    
    menu:
        "That's what they train us for, right?":
            c "Absolutely, soldier! Best training in the galaxy."
        "I think it was a fluke"
            c "We make our own luck, soldier!"
    
    c "It's good that we have you. We seem to have ourselves a bit of a situation here."
    c "These damn scientists can't add two and two together. I've been reviewing the shipping manifests, and we're missing quite a few ingredients that haven't been accounted for."
    c "I need you to get out there and figure out what they've been doing with these parts. There's practically enough missing to build a small bomb!"
    c "Of course, I probably shouldn't expect any better of someone without our rigid military training. Get in there and teach them how to fill out their requisitions sheets the way a real soldier would!"
    
    menu:
        "Yes, ma'am!":
            pass
        "You realise I graduated a civilian course about filing shipping manifests?":
            c "Don't be modest, soldier! I've seen your track record. Three weeks at Norpoint Military Academy would have taught you more than those lousy scientists have learnt in their entire lives!"
    
    c "Any questions, soldier?"
    jump myron_menu_intro
    
    
label myron_menu_intro:
    menu:
        "I hear you did some fairly incredible things to save me earlier.":
            jump myron_intro_howdidigethere
        "What do you do for fun around here?":
            jump myron_fun
        "What can you tell me about the rest of the crew?":
            jump myron_askaboutcrew
        "That's all for now" if myron_intro_complete:
            c "Dismissed, soldier!"
            return
            
label myron_intro_howdidigethere:
    c "No more than I'd do for any fellow soldier, soldier!"
    c "It's always good to go flying and shoot things."
    c "And when you're a fighter pilot at heart who's been stuck on a ship without engines for almost a year, well..."
    c "Every jetpack starts looking a little bit like a fighter."
    
    c "Any other questions, soldier?"
    jump myron_menu_intro


label myron_fun:
    c "To be honest, there's not a lot of 'fun' on this assignment, soldier."
    c "That flying I got to do resuing you was the most fun I've had all month."
    
    c "Any other questions, soldier?"
    jump myron_menu_intro
    
label myron_askaboutcrew:
    c "Not much! We haven't written their profiles yet!"
    
    c "Any other questions, soldier?"
    jump myron_menu_intro
    