#Lead Scientist Quincy Sylvester

define quincy_intro_complete = False
define quincy_intro_complete_planet = False
define quincy_intro_complete_supplies = False

label quincy_intro:
    scene bg science
    show quincy
    
    s "What? Can't you see I'm busy"
    menu:
        "The captain asked me to talk to you about some missing supplies":
            s "Wonderful. Did you miss the part where I'm busy?"
        "What are you working on":
            s "Busy things that would go over your head."
    s "Below us, we're witnessing the fall of an alien civilisation to a pathetically small swarm of Locus Locusts."
    s "I need to document this. As that's my job."
    s "It's almost disappointing, how after all their years of fighting themselves they still can't mount an effective defense against a few billion bugs."
    menu:
        "You're not bothered by all the people dying down there?":
            s "They're not people. Not legally. We're here to observe if they're actually worthy of that status."
        "I'm sure we'd have done much better in year 2000":
            s "Yes, why don't you mock me? I'm sure neither of us have anything better to do than stand here and chatter."
    
    s "What do you actually want?"
    jump quincy_menu_intro
    
    
label quincy_menu_intro:
    menu:
        "What can you tell me about the civilisation below us?":
            jump quincy_intro_planetbelow
        "Do you know anything about the missing supplies?":
            jump quincy_intro_missingsupplies
        "What do you do for fun around here?":
            jump quincy_fun
        "What can you tell me about the rest of the crew?":
            jump quincy_askaboutcrew
        "That's all for now" if quincy_intro_complete_planet && quincy_intro_complete_supplies:
            $ quincy_intro_complete = True
            s "Then leave."
            return
            
label quincy_intro_planetbelow:
    s "They're savage primitives that are almost capable of spaceflight, and the United First-contact Orginisation needs to decide if they're actually stable enough to be allowed into the galaxy."
    menu:
        "Allowed into the galaxy? Are you saying someone would kill them off?":
            s "Nothing so dramatic. Usually their spacefaring vessels are destroyed, along with a few key centers of production. They have an abundance of rules about everything, including clipping the wings of an unstable civilisation."
        "Are you suggesting they should decide that they shouldn't?":
            s "This is one of the less stable races I've observed. No effective worldwide government. Warring."
            s "All together, dangerously unstable. Though I'm just a documenter. It's not my call."
    s "Of course, that might not matter if they don't survive the Locusts. Which, in my professional oppinion, they won't."
    menu:
        "Couldn't someone help them?":
            s "Sure, a few small military vessels could easily take care of these bugs. But there's no one but us here, and I'm told we're having trouble with our radio."
        "You don't seem very sad about this.":
            s "No, I haven't been secretive that I don't like these aliens."
    s "That's not to say that I think what's happening is a good thing. These Locusts shouldn't be here, and not reporting them is a clear breach of procedure."
    s "The radio needs to be fixed, so that we can report back to the United First-contact Orginisation. They'll decide on a correct way to deal with the situation."
    s "And letting these aliens, however much I dislike them, be destroyed by a Locust swarm is not the correct outcome."
    $ quincy_intro_complete_planet = True
    jump quincy_menu_intro

label quincy_intro_missingsupplies:
    s "I can't tell you anything about them. I always file the correct paperwork, I can assure you."
    s "You'll be after Cleany, the second scientist, or Kari, the engineer."
    s "They're both scatterbrained, and I would not put failing to file paperwork past them."
    menu:
        "The captain wants you to look over the list, at least":
            s "Fine."
        "The captain seemed to think there was enough on this missing parts list to make an explosive.":
            s "She's paranoid. And hoping for a fight at every opportunity. Never the less, do you have the list on you?"
    "She scans the list quickly."
    s "This certainly is enough to make a small bomb. Half a kilo of explosives. Enough to take out some ship subsystems and rupture the hull."
    s "Still, I can't imagine anyone on the ship actually building a bomb. No one's that vicious."
    $ quincy_intro_complete_supplies = True
    s "Are we done?"
    jump quincy_menu_intro
label quincy_fun:
    s "Fun? Did you miss that I'm busy?"
    s "Did you miss the genocide happening below us? You want to talk about fun?"
    
    s "Stop wasting my time."
    jump quincy_menu_intro
    
label quincy_askaboutcrew:
    s "Not much! We haven't written their profiles yet!"
    
    s "Do you have anything to ask that isn't a waste of both of our time?"
    jump quincy_menu_intro
    