

label jeneva_intro:
    scene bg science 
    show jeneva
    j "So, how are you feeling?"
    menu:
        "Like I lost a fight with a Ungardian Tiger":
            j "Oh, have you met one before? I've always wanted to visit."
            j "We don't get much time off doing these jobs though, do we?"
        "Like someone's injected me with a lot of painkillers, but not quite enough":
            j "I'm sorry. I have stronger painkillers, but the capain has said she wants to be able to talk to you."
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
    j "At any rate, I believe the captain wanted to speak to you. But I can answer some of your questions first, if you'd like?"
    
    
label jeneva_menu_intro:
    menu:
        "How did I get here?":
            jump jeneva_intro_howdidigethere

label jeneva_intro_howdidigethere:
    j "Your pod was attacked by Locus Locusts. And yes, that's their technical terms."
    j "The person who discovered them had a rather bad grasp of Latin. Auto-translators are always 5 years off perfection, if you believe the experts."
    j "Have you ever studied latin."
    menu:
        "No. I'm a logistics officer. Not a lot of room for latin.":
            j "Oh, of course. I'm sorry, I tend to ramble a lot."
        "Do you always get distracted this easily.":
            j "Yes! Sorry. Right, your rescue."
    j "As soon as we saw your pod incoming, the captain throw on a spacesuit, grabbed her rifle and jumped out the airlock."
    j "Completely insane, of course. But she managed to take out the bugs on your ship, and pulled it back in by attatching her tether to it."
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
    
    
    
    