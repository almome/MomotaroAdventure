label ch1:

    define n1 = Character('Niño')
    define n2 = Character('Niña')
    define yuUnKnow = Character('???')

    "Pasaron 8 años desde que [momo] entró en las vidas de los ancianos para llenarlos de felicidad."
    "La niña creció sana y fuerte. [momo] también era conocida en el pueblo, casi siempre estaba corriendo por las calles jugando con otros niños."
    "Rebosaba energía."

    play sound "sound/ninios.ogg"

    n1 "¡Juguemos al escondite!"
    n1 "¡[momo]! ¡Tú la llevas!"
    momo "¡Eh! Siempre la llevo yo..."
    momo "¡Es injusto!"
    n1 "Es que eres la más rápida y fuerte, siempre ganas tú cuando no la llevas."
    n2 "Si no fueras tan fuerte..."
    momo "Bueno, si no queda más remedio..."
    momo "¡Venga que empiezo! 1..."
    momo "2..."
    momo "3..."
    momo "4..."
    momo "5..."
    momo "6..."
    momo "7..."
    momo "8..."
    momo "9..."
    momo "10..."
    momo "¡Allá voy!"

    "[momo] comenzó a recorrer las calles del pequeño pueblo,"
    "pero entonces al entrar en un estrecho callejón..."
    play sound "sound/tropiezo.ogg"
    with Shake((0, 0, 0, 0), 0.3, dist=10)

    momo "¡Auch!"
    momo "¡Ay! Perdona, estaba corriendo y no te vi."

    "[momo] se tropezó con un niño de su misma edad."
    "El niño tenía el pelo castaño y unos ojos verdes intensos. Nunca antes habá visto unos ojos igual."

    yuUnKnow "No pasa nada..."
    momo "Oye... Nunca te he visto por estos lugares, no eres de por aquí ¿verdad?"
    yuUnKnow "No, he llegado aquí de casualidad."
    yuUnKnow "Llevo vagando solo desde hace tiempo..."
    momo "¿¡Estas solo!? ¿Y tu padres?"
    yuUnKnow "No están..."
    momo "¿Cómo que no están?"
    yuUnKnow "..."
    yuUnKnow "Me abandonaron hace tiempo."
    momo "¡Oh! Vaya, lo siento mucho."
    yuUnKnow "No pasa nada, me las arreglo bien por ahora."
    yuUnKnow "Estoy durmiendo entre estos tablones de madera y como de la sobras que hay en el restaurante."
    momo "..."
    yuUnKnow "Pero no te pongas triste por mi, soy fuerte y me las apaño muy bien."
    #*gruñido de tripa*
    yuUnKnow "..."
    yuUnKnow "Uy, jeje..."
    yuUnKnow "Es que aún no he encontrado nada para desayunar."
    momo "Ten, esto es para ti."

    "[momo] se sacó un pequeño saquito que contenía kibi dangos."
    "Extrajo uno y se lo dió al hambriento niño."
    "Este rápidamente lo devoró y un par de lágrimas de emoción recorrieron sus mejillas."

    yuUnKnow "Muchísimas gracias, eres muy generosa."
    momo "No hay de qué. Por cierto, ¿cuál es tu nombre?"
    yuUnKnow "Yû, me llamo Yû. ¿Y tu?"
    momo " Mi nombre es [momo], mucho gusto en conocerte."
    yu "Lo mismo digo. A partir de ahora seremos amigos y te protegeré de todos los males."

    "El niño tomó un trozo de madera y lo blandió como si se tratara de una katana"

    momo "Eres muy valiente. Pero solo te he dado un kibi dango, es muy poco."
    yu "Es el mejor kibi dango que he comido en mi vida."

    menu:
        "Dejarlo tranquilo y seguir jugando.":
            call ch1_1
        "Invitar a jugar.":
            call ch1_2

    "Hola esto sigue :D"

return
