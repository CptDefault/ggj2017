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
        "I think it was a fluke":
            c "We make our own luck, soldier!"
    
    c "It's good that we have you. We seem to have ourselves a bit of a situation here."
    c "These damn scientists can't add two and two together. I've been reviewing the shipping manifests, and we're missing quite a few ingredients that haven't been accounted for."
    c "I need you to get out there and figure out what they've been doing with these parts. There's practically enough missing to build a small bomb!"
    c "Of course, I probably shouldn't expect any better of someone without our rigid military training. Get in there and teach them how to fill out their requisitions sheets the way a real soldier would!"
    
    menu:
        "Yes, ma'am!":
            pass
        "You realise I graduated a civilian course about filing shipping manifests?":
            c "Don't sell yourself short, soldier! I've seen your track record. Three weeks at Norpoint Military Academy would have taught you more than those lousy scientists have learnt in their entire lives!"
    
    c "Any questions, soldier?"
    jump myron_menu_intro
    
label myron_revisit_intro:
    scene bg bridge
    show myron
    
    c "Soldier! Report!"
    
    jump myron_menu_intro
    
label myron_menu_intro:
    menu:
        "I hear you did some fairly incredible things to save me earlier.":
            jump myron_intro_howdidigethere
        "What do you do for fun around here?":
            jump myron_fun
        "Can I ask some questions about the rest of the crew?":
            jump myron_askaboutcrew
        "That's all for now" if myron_intro_complete:
            c "Then hop to it! Those scientists aren't about to solve any problems themselves!"
            c "And check in on our engineer, too. She's usually good with the parts, but I'm still waiting on her to fix the radio."
            c "Dismissed, soldier!"
            return
            
label myron_intro_howdidigethere:
    c "No more than I'd do for any fellow soldier, soldier!"
    c "It's always good to go flying and shoot things."
    c "And when you're a fighter pilot at heart who's been stuck on a ship without engines for almost a year, well..."
    c "Every jetpack starts looking a little bit like a fighter."
    
    $ myron_intro_complete = True
    
    c "Any other questions, soldier?"
    jump myron_menu_intro


label myron_fun:
    c "To be honest, there's not a lot of 'fun' on this assignment, soldier."
    c "That flying I got to do resuing you was the most fun I've had all month."
    
    c "Any other questions, soldier?"
    jump myron_menu_intro
    
label myron_askaboutcrew:
    c "Absolutely, soldier!"
label myron_askaboutcrew_loop:
    menu:
        "First Scientist Quincy":
            c "Civillian Specialist Quincy doesn't know the first thing about proper military procedures!"
            c "Whilst I'm sure the work she's doing is important to someone in a stuffy office, it's hardly exciting, is it?"
        "Second Scientist Jeneva":
            c "Cleary? I think of her as a bit of a duckling."
            c "No teeth, and not a clue about proper military procedures, but she's a sweet girl."
        "Engineer Kari":
            c "She keeps a functional ship, though I'll admit I can't keep up with all the technical terms she's using."
            c "That's why I'm the captain and she's the engineer, I guess!"
            c "Of course, I still don't understand why a girl from such a well off family is hiding out here."
            menu:
                "Makes sense. Can I ask about someone else?":
                    jump myron_askaboutcrew
                "Well off family, you say?":
                    c "Well."
                    c "Forget I said anything, soldier!"
                    c "Not sure the girl would forgive me if I let that one slip."
                    c "And I absolutely cannot afford another court martial!"
        "That's it about the crew":
            c "Any other questions, soldier?"
            jump myron_menu_intro
    c "Any other question about your fellow crew, soldier?"
    jump myron_askaboutcrew_loop
    