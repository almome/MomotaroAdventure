## The script of the game goes in this file.

## Declare characters used by this game. The color argument colorizes the name
## of the character.

define momo = Character("[momo]")
define anciana = Character('Anciana')
define anciano = Character('Anciano')
define yu = Character('Yû')
define midori = Character('Midori')


## The game starts here.

label start:

    $global espada
    $espada = False
    $global Afecto_Yu
    $Afecto_Yu = 0
    $global Afecto_Ta
    $Afecto_Ta = 0
    $global Afecto_Hi
    $Afecto_Hi = 0
    $global Afecto_Fa
    $Afecto_Fa = 0


    call prologo from _call_prologo

    call ch1 from _call_ch1

    ## This ends the game.

    return
