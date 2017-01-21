#Second Scientist Jeneva Cleary
define jeneva_intro_complete = False

label jeneva_intro:
    scene black with Fade(1.0, 0.5, 1.0)
    
    "..."
    
    "Unknown" "Patient should be waking soon, Captain. You'll get a full report later."
    
    "Captain" "Good work, Cleary. If you need me I'll be on the Bridge."
    
    "Cleary" "Yes, Captain."
    
    "..."
    
    "Cleary" "... {w=1.0}Are you awake... {w=0.4}now?!"
    
    scene bg science
    show jeneva
    with Dissolve(1)
     
    m "Yeah. I...{w=0.5} made it onto the station. {w=0.5}Huh."
    
    j "Yup! Welcome aboard. Glad to have you here. I'm Jeneva Cleary."
    
    m "Glad to be here, {w=0.3}I think."
    
    j "So, how are you feeling?"
    menu:
        "Like I lost a fight with a Ungardian Tiger":
            j "Oh, have you met one before? I've always wanted to visit."
            j "We don't get much time off doing these jobs though, do we?"
        "Like someone's injected me with a lot of painkillers, but not quite enough":
            j "I'm sorry. I have stronger painkillers, but the Captain has said she wants to be able to talk to you."
        "Fine.":
            j "Well, at least we know you're a terrible liar."
    j "Do you think you're up to walking?"
    menu:
        "Sure. I'm tough.":
            j "I'm sure you are. Well, I might not {i}technically{/i} be a doctor, but you're clear from my perspective."
        "Aren't you the doctor? You tell me.":
            j "Well, I'm not {i}technically{/i} a doctor. But yes, you're clear from my perspective."
        "I think I need to lie here for another year until it all stops hurting.":
            j "Unfortunately, we don't have time for that. I might not {i}technically{/i} be a doctor, but you're clear to move from my perspective."
    menu:
        "Wait, not {i}technically{/i} a doctor!?":
            j "I'm actually a xenobiologist. Which technically means I'm more qualified to deal with aliens, but humans are sort of just more common aliens. So I know what I'm doing. Mostly."
        "Was I just operated on by a vet?":
            j "No!"
            j "...A vet would technically be more qualified. I'm a xenobiologist, so I'm trained to work with non-terrestrial biology. Though when you get down to it, it's all just biology."
    j "At any rate, I'm the closest this ship has to a doctor. And in my eyes, you should be ship shape! More or less."
    j "Try to take it easy on the heavy lifting for a few days."
    j "I believe the Captain wanted to speak to you. But I can answer some of your questions first, if you'd like?"
    call jeneva_menu_intro
    jump chap1_postwakeup
    
label jeneva_revisit_intro:
    scene bg science
    show jeneva
    
    j "Hi there. Are you feeling okay?"
    
    jump jeneva_menu_intro
    
label jeneva_menu_intro:
    menu:
        "How did I get here?":
            jump jeneva_intro_howdidigethere
        "What can you tell me about this station?":
            jump jeneva_station
        "What do you do for fun around here?":
            jump jeneva_fun
        "What can you tell me about the rest of the crew?":
            jump jeneva_askaboutcrew
        "That's all for now" if jeneva_intro_complete:
            j "Okay! Look after yourself."
            return

label jeneva_intro_howdidigethere:
    j "Your pod was attacked by Locus Locusts. And yes, that's their technical term."
    j "The person who discovered them had a rather bad grasp of Latin. Auto-translators are always 5 years off perfection, if you believe the experts."
    j "Have you ever studied latin?"
    menu:
        "No. I'm a logistics officer. Not a lot of room for latin.":
            j "Oh, of course. I'm sorry, I tend to ramble a lot."
        "Do you always get distracted this easily?":
            j "Yes! Sorry. Right, your rescue."
    j "As soon as we saw your pod incoming, the captain throw on a spacesuit, grabbed her rifle and jumped out the airlock."
    j "Completely insane, of course. But she took out the bugs on your ship, attached her own tether to it and had us tow it back while she held on with her knees and blasted more bugs."
    j "In case you've forgotten, that's the tether that you should absolutely never disconnect from yourself whilst you're on a spacewalk. No exceptions."
    menu:
        "The captain did that for me?":
            j "In part, yes. I suspect she mostly did it for 'the kick', as she would say."
            j "I'm not sure anyone understands why they put an ex-fighter pilot in charge of a station with no engines."
        "That seems highly irresponsible":
            j "Oh, absolutely. Risking one of our two spacesuits, and our only weapon, for a kick?"
            j "And to save you, of course. Though I have no idea how she knew that would work."
    j "Once she'd pulled your pod in, we managed to get the doors open for long enough to pull you out."
    j "The pod was too badly damaged to get your posessions out though. I'm sorry."
    menu:
        "All of my stuff is gone? I had an original Playstation 8 in there!":
            j "Sorry. You wouldn't believe how many alarms Kari had to disable just so that we could get you out."
        "Well, I'll take being alive over what I brought with me.":
            j "That's the spirit."
    
    $ jeneva_intro_complete = True
    
    j "Did you have any other questions?"
    jump jeneva_menu_intro

label jeneva_station:
    j "Probably not much more than you saw in your orientation video."
    j "We're stationed here to observe the civilisation on the planet below."
    j "Technologically, they're at a similar stage to humanity around year 2000."
    menu:
        "What was humanity even like that long ago?":
            j "Quite primitive. Still stuck on one planet, degrading that planet, and at war with each other."
        "Technologically? You're implying they're different in some other way?":
            j "Well, phyically they're quite different. Six limbed and seemingly telepathic, for a start."
            j "What I would give to see one up close..."
    j "We report our findings back to the United First-contact Orginisation every six months."
    j "If we needed to intervene for some sort of humanitarian, or any any other reason, they'd make the call."
    j "Did you have any other questions?"
    jump jeneva_menu_intro

label jeneva_fun:
    j "Fun?"
    j "Well, I guess I study the planet below us?"
    j "That's probably not what you meant, but we really are doing important work here."
    j "There's so many people out there willing to look at places like this as a threat, which I just don't think of them as."
    j "They are, however, incredibly interesting."
    menu:
        "Have you ever been accused of being work obsessed?":
            j "Oh, all the time. But I really am fascinated with it."
        "Anything less work related?":
            j "To be honest, I hadn't really considered it. I guess you could look out the windows? There's some nice views."
    j "I hope the captain lets us take one of the aliens to study one day. I'm fairly sure I know what sedatives to use so that they don't remember the trip. It would be fascinating, don't you think?"
    menu:
        "Sure! I'd love to see one up close.":
            j "I'm glad you think so! I'll have to let the captain know once this is all resolved."
        "Is that even remotely legal?":
            j "Technically? No. It would technically be illegal."
            j "That said, I've been reading the laws around it a little, and I think there's some loopholes. We just need to make sure we don't influence their society at all."
    
    j "Did you have any other questions?"
    jump jeneva_menu_intro
    
label jeneva_askaboutcrew:
    j "Not much! We haven't written their profiles yet!"
    
    j "Did you have any other questions?"
    jump jeneva_menu_intro
    