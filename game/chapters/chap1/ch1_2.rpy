label ch1_2:

    $Afecto_Yu += 1   #Incrementa afecto yu
    define m = Character('Mujer')
    define h = Character('Hombre')
    define n1 = Character('Niño')
    define uM = Character('???')

    momo "Oye, ¿quieres jugar al escondite conmigo y los otros?"
    yu "¡Sí, claro!"
    momo "¡Estupendo! Pero no te confíes, soy muy rápida."
    yu "Seguro que con el kibi dango que me has dado corro más que tú."
    momo "Eso habrá que verlo."
    momo "Bueno, ayudame a buscar al resto de mis amigos y comenzamos el juego de nuevo."
    yu "¡Venga, vamos!"

    "Los dos niños comenzaron a correr por las angostas calles del pueblo, mirando en cada rincón y tras cada arbusto."
    "Ya eran pocos los niños los que faltaban por encontrar cuando, de repente..."

    m "¡¡ONIIIIIIIS!!"
    h "¡Escondanse en sus casas! ¡Rápido!"
    h "¡¡VIENEN A DEVORARNOS A TODOS!!"
    m "¡CORRAAAAN!"

    momo "¿O-Onis? Pero, ¡¿qué es eso?!"
    momo "¿¡Porque la gente está tan aterrada!? ¿Yû?"
    yu "Demonios saqueadores..."
    yu "No es la primera vez que los veo. Traen consigo el horror y la destrucción."

    "Un fuerte sonido retumbó en todo el lugar."
    "Una nube de polvo se elevaba cerca en la entrada principal del pueblo."

    momo "¡AH! ¡¿Qué hacemos?!"
    yu "Ve a refugiarte con tu familia. ¡Corre!"
    yu "Yo vigilaré que no te siga ningún oni. Luego iré al restaurante a ver como están."
    momo "¡Ni hablar!"
    momo "No te dejaré solo, yo tambien quiero ayudar a la gente del pueblo."
    yu "¿Estas segura?"
    momo "Sí."
    yu "Pues vamos, pero no te separes de mi. Yo te protegeré, [momo]."

    "Ambos fueron corriendo al restaurante, cuidando de no encontrarse a ningún oni, aunque [momo] no sabía como eran."
    "Según la descripción de Yû, debían ser seres horribles."
    yu "¡Hola! ¿Hay alguien aquí?"

    "Un silencio sepulcral reinaba en el restaurante, aquello les daba muy mala espina."
    "Yû tomó a [momo] de la mano e intentó salir corriendo pero ya era demasiado tarde."

    #*sonido de choque*

    uM "Vaya, vaya… ¿Que tenemos aqui? ¡Un par de renacuajos!"

    "Al fin [momo] pudo ver qué era un oni. Una criatura de forma humanoide pero de piel azulada, con cuernos en la cabeza y vestida con pieles de tigre."
    "Era un poco más alta y grande que un humano medio, y lucían unos amedrentadores colmillos en su boca. Pese a aquello, lucía una belleza salvaje que nunca había visto."

    uM "¿No os han dicho nunca vuestros papis que cuando vienen los onis hay que esconderse?"
    uM "Sinó nos comemos vivos a los niños. Pero ya es demasiado tarde, ustedes seréis mi tentempié."
    uM "¡Buajajajaja!"

    momo "¡Ah!"
    yu "¡No nos cogerás!"

    "Yû agarró fuerte de la mano a [momo] y salieron corriendo hacia la cocina. Mientras la oni se carcajeaba de ellos."

    uM "¡Jajaja! ¿Vais directos a la cocina para ahorrarme el trabajo de llevaros?"
    uM "Nunca he tenido una comida tan educada jajajaja."
    uM "Pero no es necesario cocinaros renacuajos... ¡Vivos estáis más sabrosos!"

    "Como si lo oliera, la oni fue directa al sitio donde el dueño del restaurante guardaba las ganancias. Tomó el dinero y todo lo que había de valor."

    uM "Estupidos niños, van y se lo creen."
    uM "Los onis tenemos mejores cosas que comer que crías de humano… ¡Oh!"
    uM "¡Que hermoso y reluciente colgante! Si me lo pongo seguro que impresiono a mi querido Takashi, ¡kya!"

    yu "¡Eh tú! ¡Monstruo!"
    uM "¡Te atreves a llamar monstruo a la bella Midori!"
    midori "¡Estúpido mocoso! ¡Te vas a enterar!"

    #sonido de golpe con cazo
    "La oni fue hacia la cocina y Yû la golpeó con un cucharón. Midori ni se inmutó."

    midori "Hace falta mucho más para poder herir a un oni, ¡niño!"

    "Midori le da una patada a Yû y lo manda a la otra punta de la cocina. El niño grita del dolor. [momo] sale de su escondite."

    momo "¡Yû!"

    midori "¡Anda, pero si estabas ahí escondida! Mira lo que le va a pasar a tu amiguito por enfadarme…"

    "Midori va a acercar a Yû…"

    #(Mini-opciones que no cambian el argumento mucho)
    #----------------------------------------------------------------------------------------------------------------------

    # menu:
    #     "Atacar a la oni.":     #Insertar cambio
    #         momo ¡No le harás daño a Yû!
    #
    #     	#name salta sobre la oni y le tira del pelo fuertemente.
    #
    #     	Midori: ¡AAAAGH! ¡Maldita niña!
    #
    #     	La oni empieza a moverse frenéticamente para deshacerse de #name, pero esta se aferra a la cabellera de Midori como si la vida le fuera en ello.
    #
    #     	yu ¡#name! ¡Ten cuidado! ¡Voy a ayudarte!
    #
    #     Yû se levantó del suelo, dolorido, y cogió unos huevos y empezó a lanzarlos.
    #
    #     	yu ¡Ahí tienes monstruo!
    #     	Midori: ¡Malditos!
    #
    #     	#name agarró por suerte un pequeño saco de harina de trigo y se lo lanzó a Yû. Entonces el niño le tiró la harina a la oni en la cara.
    #
    #     	Midori: ¡Agh! ¡No veo nada! No puede ser… ¡No quiero que Takashi me vea así! ¡Toda sucia!
    #     	yu ¡Ahora #name! ¡Cojamos las riquezas y huyamos!
    #     	Midori: ¡Noooo! ¡Las joyas que he robado!
    #
    #     	Yû y #name salieron corriendo del restaurante salvando el dinero, las joyas y riquezas de la familia que llevaba el restaurante. A Yû le daban las sobras, pero él se sentía agradecido con ellos.
    #     	Al salir del restaurante vieron que el pueblo estaba destrozado, la gente estaba huyendo al bosque, donde se encontraba el templo.
    #
    #     	yu No creo que quede mucha gente en el pueblo, todos está yendo hacia el bosque.
    #     	momo Mi casa está cerca del bosque, al lado del río. ¡Vamos!
    #     "Interponerse entre la oni y Yû.":
    #
    # Atacar a la oni… (Yû acaba de cocinero en el restaurante)
    # 	momo ¡No le harás daño a Yû!
    #
    # 	#name salta sobre la oni y le tira del pelo fuertemente.
    #
    # 	Midori: ¡AAAAGH! ¡Maldita niña!
    #
    # 	La oni empieza a moverse frenéticamente para deshacerse de #name, pero esta se aferra a la cabellera de Midori como si la vida le fuera en ello.
    #
    # 	yu ¡#name! ¡Ten cuidado! ¡Voy a ayudarte!
    #
    # Yû se levantó del suelo, dolorido, y cogió unos huevos y empezó a lanzarlos.
    #
    # 	yu ¡Ahí tienes monstruo!
    # 	Midori: ¡Malditos!
    #
    # 	#name agarró por suerte un pequeño saco de harina de trigo y se lo lanzó a Yû. Entonces el niño le tiró la harina a la oni en la cara.
    #
    # 	Midori: ¡Agh! ¡No veo nada! No puede ser… ¡No quiero que Takashi me vea así! ¡Toda sucia!
    # 	yu ¡Ahora #name! ¡Cojamos las riquezas y huyamos!
    # 	Midori: ¡Noooo! ¡Las joyas que he robado!
    #
    # 	Yû y #name salieron corriendo del restaurante salvando el dinero, las joyas y riquezas de la familia que llevaba el restaurante. A Yû le daban las sobras, pero él se sentía agradecido con ellos.
    # 	Al salir del restaurante vieron que el pueblo estaba destrozado, la gente estaba huyendo al bosque, donde se encontraba el templo.
    #
    # 	yu No creo que quede mucha gente en el pueblo, todos está yendo hacia el bosque.
    # 	momo Mi casa está cerca del bosque, al lado del río. ¡Vamos!
    #
    # Interponerte entre la oni y Yû. (Yû se pone a trabajar en el restaurante y entrena en un dojo)
    # 	momo ¡No le harás daño! ¡Vete de aquí!
    #
    # 	#name se puso entre la oni y Yû, con los brazos abiertos. La mirada de #name era intensa, demasiado para una niña.
    #
    # 	Midori: Eres muy valiente renacuaja… Pero eso no servi-.
    # 	momo ¡He dicho que te vayas! Ya tienes el oro y los objetos de valor ¿no? ¡Pues déjalo en paz!
    #
    # 	Midori se quedó parada por la fuerza que tenía la niña, la observó con recelo. Nunca antes había permitido que la hablaran así, todo aquel que lo hiciera acababa muerto. Pero esta niña era poderosa, su voz era totalmente autoritaria, sentía la fuerza de sus palabra. La oni pensó en aquella profecía… Entonces se volvió y se dirigió a la salida de la cocina.
    #
    # 	Midori: Estúpida renacuaja.
    # 	momo ¡No me llamo renacuaja! ¡Me llamo #name, y algún día me encargaré de ti!
    # 	Midori: Jujuju.
    #
    # 	Yû y #name oyeron como los pasos de la oni se alejaban, por fin se relajaron. Respiraban entrecortadamente por el miedo, nunca se había enfrentado directamente a una criatura así.
    #
    # 	yu #name… Gracias.
    # 	momo No me las des, me salió solo. En verdad estaba muy asustada.
    # 	yu Lo se, te temblaban las piernas.
    #
    # 	#name ayudó a Yû a levantarse y juntos salieron del restaurante.
    #
    # 	yu Prometí que te protegería, pero al final has sido tú la que me ha protegido… Lo siento.
    # 	momo No tienes porqué disculparte.
    # 	yu Sí, te he fallado. A partir de ahora quiero ser mas fuerte.
    #
    # momo Pero si has sido muy valiente enfrentandote a esa oni.
    # 		yu ¿De verdad te he parecido valiente?
    # 		momo Claro. Eres un gran protector.
    # 		Ambos se sonríen.
    # momo Ambos nos haremos más fuerte.
    # 		yu De acuerdo.
    #
    # 	Entonces ambos huyeron hacia el bosque donde estaba el templo, todo el pueblo corría hacia allí.

    #------------------------------------------------------------------------------------------------------------------------

    "Mientras corrían hacia el bosque, [momo] alcanzó a ver a un grupo de onis. Eran enormes, todos con piel azulada con más o menos intensidad."
    "Entre ellos destacaba un oni que parecía el líder del grupo. Sus miradas se cruzaron y un escalofrío recorrió a [momo]."
    #Cambio de escenario (bosque o templo)
    "Por fin llegaron al templo del bosque, donde todo el pueblo se había refugiado."

    anciana "¡[momo]! ¡Estás bien! ¡Estaba muy preocupada por tí, hija mia!"
    anciano "¡Gracias a los cielos que no te ha ocurrido nada!"
    momo "Mamá, papá, es horrible lo que está ocurriendo."

    "Los tres se abrazaron. Yû que los observaba se sintió fuera de lugar y se dio la vuelta para marcharse"
    ", pero entonces alguien le tomó de la mano."

    momo "¡Papá, mamá! Este es Yû, me ha protegido todo el tiempo. Ha sido muy valiente plantándole cara a una malvada oni."
    anciano "Eres un joven con agallas. Muchas gracias por cuidar de mi hija, nunca te estaremos lo suficientemente agradecidos."
    anciana "Muchas gracias."
    yu "No hay de qué, en realidad [momo] ha sido mucho más valiente."
    anciano "Nunca te he visto por este pueblo, ¿de donde vienes?"
    yu "Vengo del norte, donde atacaron con anterioridad los onis, mis padres..."
    anciana "¡No te preocupes muchacho! Que en este pueblo no te va a faltar de nada"
    anciana ", hablaré con el dueño del restaurante a ver si tiene algun puesto de trabajo para ti y así te da un lugar donde vivir."
    yu "Oh, eso sería genial, pero no quiero ser una molestia."
    anciana "El protector de mi querida hija merece ser uno más de este pueblo."
    anciana "Yo me encargo hijo, no te preocupes."

    "La pareja de ancianos se alejaron para hablar con el dueño del restaurante. [momo] se quedaron solos entre tanta multitud y de repente ambos se miraron."

    momo "Este templo… tiene algo extraño. Nunca he estado dentro."

    "[momo] comenzó a andar con la mirada fija hacia la entrada al jardín central del templo."

    yu "Eh [momo], ¿a dónde vas?"
    momo "Sígueme. Vamos a explorar un poco el sitio."
return
