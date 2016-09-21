
define anciana = Character('Anciana')
define anciano = Character('Anciano')


label prologo:

    scene bg aldea_feliz
    play music "music/prologo_aldea.ogg"

    "Érase una vez, hace mucho tiempo, una pareja de ancianos que vivían en un tranquilo
    pueblo en las montañas."
    #Imagen cabaña del matromio
    "El viejo matrimonio nunca tuvo hijos, por lo que vivían solos en su acogedora cabaña a la orilla del río."
    "Cada uno se dedicaba a sus tareas diarias, siguiendo siempre la misma rutina. Parecía que el tiempo no avanzaba, la tranquilidad reinaba en aquel lugar, hasta que un día…"

    anciana "Querido, hoy hace un día precioso. Ya se acerca la primavera."
    anciano "Tienes razón, pero por la noche aún hace frío. Iré a por leña."
    anciana "Yo lavaré la ropa en el río."
    anciano "Ten cuidado, el río tiene mucha corriente estos días. No quiero que te pase nada."
    anciana "Descuida, tu mujer es vieja pero aún está llena de energía."
    anciano "Nunca cambiarás."

    #Anciana lavando en el rio
    play sound "sound/river.ogg" loop fadeout 1.0 fadein 1.0
    "La anciana fue hacia el río y comenzó a lavar su ropa. La corriente era fuerte, tal y como había dicho el anciano."
    "Y aunque aquello pareciera un señal de mal augurio, no siempre las sorpresas son malas."

    anciana "¡Anda! ¿Qué es aquello rosa que baja por el río?"
    anciana "Parece…"
    #Imagen de melocotón en el agua
    anciana "¡Oh! ¡Pero si es un melocotón gigantesco!"

    "La curiosidad hizo que la valiente y enérgica anciana se introdujera en el río y con todas sus fuerzas sacó el melocotón hasta la orilla del río."

    #Ancina con el melocotón gigante
    anciana "¡Como pesa!"
    anciana "Este melocotón no es normal. Lo llevaré a casa y que mi marido lo abra."
    stop sound

    "Y con la velocidad que le permitía la edad y el peso de aquel fruto, la anciana llegó a su hogar y esperó inquieta a que llegase su marido."

    #Imagen del melocotón encima de la mesa
    anciano "Ya estoy en casa cariño."
    anciana "¡Amor mio! ¡Mira, ven!"
    anciano "Eso es… ¡¿Un melocotón gigante?!"
    anciana "Así es, vi como flotaba río abajo y lo rescaté. Ábrelo, quiero ver su interior."

    "El anciano tomó un machete y con sumo cuidado partió el melocotón. Ambos quedaron maravillados. "

    #Imagen del melocotón abierto y con el bebé dentro
    play sound "sound/babylaught.ogg"
    "Un bebé se encontraba en su interior y los miraba con unos enormes ojos."

    anciano "¡Oh! ¡Pero si es un bebé! ¡¿Como puede ser esto posible?!"
    anciana "¡Es una niña!. Una hermosa y rosada niña. ¡Es un milagro!"
    anciano "Creo que finalmente los dioses nos han otorgado una hija, cariño."
    anciana "Llevamos tantos años solos… ¡Va a ser la alegría de la casa!"
    anciano "Debemos elegir un nombre… "

    ## MEJORA: Poner en una ventana emergente
    define momo = Character("[momo]")

    $momo = renpy.input("¿Como se llamará esta preciosa niña?")
    $momo = momo.strip()

    anciana "Se llamará [momo]."

    #Opcional imagen de los dos ancianos con el bebé
    "Bienvenida a la familia [momo]."



    return
