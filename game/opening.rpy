label opening:
    
    #background probs gonna be some external view of the ship observing the planet
    
    scene bg_opening_pod
    
    "You wake up to the persistent sound of the ship's alarm as you near your destination, your body still lethargic from the aftereffects of cryosleep."
    
    "After a three month trip, you now only need to wait twenty minutes as the single passenger transport pod approaches and docks with the station that will be your new assignment."
    
    "The control panel detects your eyes opening. The screen lights up with information, along with an offer to open the viewport."
    
    "There are far more red flashing status symbols around the transport's minimal sensors than there should be. {w=1.0}A loud thump and a tremor across the ship confirms that something is wrong."
 
label first_action_menu: 
    menu:
        "Open a comms channel with the research station":
            "The line trills as it attempts to connect. There is no response."
            jump first_action_menu
        "Check your GalaxyNet update feed":
            "Your feed is blank. You've failed to connect to the nearest Net Relay."
            jump first_action_menu
        "Open the viewport":
            jump space_scenery

label space_scenery:
    scene bg_opening_stars
    
    "The transport doesn't have ranged scanners, since interstellar trips rarely encounter anything. So, at a wave of your fingers, the viewport is activated, revealing your surroundings."
    
    "The first thing you see is the planet, followed by the research station as it hovers at the furthest possible gravitational orbit. Then you see the wave of bugs swarming across space."
    
    "You've heard of these aliens; they're invasive parasites, and shouldn't be in this sector of space. Your ship wasn't equipped to deal with them."
    
    "There's nothing you can do about that now, however. You can see the station fighting them off with its basic defence weaponry, but it struggles not to be overwhelmed. There's a good chance the station won't have seen your approach."
    
    "The bugs are fast and big in numbers, launching themselves at the station and your transport pod from somewhere beyond your vision. One bug is already clinging to your ship."
     
    "You can see its large mandibles scraping at the surface of your pod, looking for weaknesses. Another thump and tremor alerts you to a second alien landing on your pod."
    
    "A third one hits you with enough force to dent the outer layer. The pod's alarms increase in volume while the momentum tips your trajectory off-course."
    
    "The station swings out of your view, and you find yourself face-to-face with the planet. If the bugs don't tear you open first, the landing will kill you. The pods alarms continue to blare at you helpfully."
    
    menu:
        "Panic!":
            "The ship senses your adrenalin spiking, and you feel a pinprick as the cryopod injects you with a depressant in an attempt to help."
            
            "Before you can get the benefits of that, there's another loud thump as the pod is shaken by an impact. The suspension on your cryosleep bed snaps, throwing you out of the bed."
            
            jump headtrauma
            
        "Close the viewport":
            
            "You close the viewport, then hear a loud thump as the pod is shaken by another impact. The suspension on your cryosleep bed snaps, throwing you out of the bed."
            
            jump headtrauma
            
        "Readjust your trajectory":
            "Your fingers fly across the controls, activating the thrusters."
            
            "You're not changing course fast enough. A readout alerts you to one of the thrusters being blocked by something large, probably an alien bug."
            
            "After a few seconds the thruster begins to overheat."
            
            "It eases up suddenly, finally blockage-free, but before you can move far you hear a loud thump as the pod is shaken by another impact. The suspension on your cryosleep bed snaps, throwing you out of the bed."
            jump headtrauma
            
label headtrauma:
    "You feel pain as your head hits the dense metal wall of the pod. {w=1.0}Then you feel nothing."
    
    jump jeneva_intro