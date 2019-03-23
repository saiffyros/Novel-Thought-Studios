
define a = Character("Alyssa", image="alyssa")

image alyssa concerned = "alyssa_concerned.png"

image alyssa neutral = "alyssa_neutral.png"
image alyssa original = "alyssa_original.png"

image side alyssa concerned = "side_alyssa_concerned.png"
image side alyssa = "side_alyssa.png"



label start:

    show praetorium

    a "You've created a new Ren'Py game."

    menu:
        "test 1":
            "test 1 checking"
        "test 2":
            "test 2 checking"

    a "Once you add a story, pictures, and music, you can release it to the world!"

    show alyssa neutral

    a "I've made a delicious tart. Come I'll show you."

    a concerned "Where's my tart???"

    show screen button1

    a "I bet Janice ate it!"

    hide alyssa neutral
    hide alyssa concerned

    show alyssa original
    a "This is my original design..."
    a "It's looking good."


    return

#screen button1:
    #textbutton "Mostrar/Esconder" action If(renpy.get_screen("button2"), true=Hide("button2"), false=Show("button2"))

#screen button2:
    #text "123456789"
