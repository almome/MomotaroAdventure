label ch1_1:

    define m = Character('Mujer')
    define h = Character('Hombre')
    define n1 = Character('Niño')

    momo "¡Claro! Si necesitas cualquier cosa, vivo en la casita cercana al río."
    momo "Cuidate."
    yu "Muchas gracias [momo]. Si tienes algún problema: silba fuerte."
    momo "¡Procuraré hacerlo!"

    "[momo] se fue alejando de Yû, continuando con el juego que había comenzado con los otros niños."
    "De repente el cielo se nubló y un grito desgarrador rompió la paz del pueblo."
    with Shake((0, 0, 0, 0), 0.5, dist=20)
    #Gritos de gente
    m "¡¡ONIIIIIIIS!!"
    h "¡Escondanse en sus casas! ¡Rápido!"
    h "¡¡VIENEN A DEVORARNOS A TODOS!!"
    m "¡CORRAAAAN!"

    momo "¿O-Onis? Pero, ¡¿qué es eso?!"
    momo "¿¡Porque la gente está tan aterrada!?"

    #Sonido fuerte
    "Un fuerte sonido retumbó en todo el lugar."
    with Shake((0, 0, 0, 0), 1.5, dist=20)
    "Una nube de polvo se elevaba cerca, en la entrada principal del pueblo."

    momo "¡AH! ¿¡Que ha ocurrido!? Sentí como si fuera un terremoto."
    #Insertar pausa
    n1 "¡Mamá! ¡Mi mamá estaba en esa zona comprando! ¡Mi mamá!"

    menu:
        "Quedarte con el niño y cuidarlo.":
            call ch1_1_1
        "Ir a buscar a la madre del niño.":
            call ch1_1_2
    return
