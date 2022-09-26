basic.clearScreen()
let conto = 0
let valore_caratteristico = 0



code_skeletons = {
    "1" : 
        """
        /**
        * CESTINO SORRIDENTE
        */
        basic.forever(function () {
            if (input.buttonIsPressed(Button.A)) {
                basic.showIcon(IconNames.Happy)
            }
        })
        """, 
    "1" : 
        """
        /**
        * ALBERO ANIMATO
        */
        basic.forever(function () {
            if (input.buttonIsPressed(Button.A)) {
                basic.showIcon(IconNames.Heart)
                basic.showIcon(IconNames.SmallHeart)
            }
        })
        """, 
    "1" : 
        """
        /**
        * OROLOGIO SEGNAFREDDO
        */
        basic.forever(function () {
            if (input.buttonIsPressed(Button.A) && input.temperature() < 10) {
                basic.showIcon(IconNames.Sad)
            }
        })
        """, 
    "1" : 
        """
                /**
        * TAVOLO GIOCO X 2, FACCINA E MUSICA
        */
        basic.forever(function () {
            if (input.buttonIsPressed(Button.A)) {
                basic.showIcon(IconNames.Happy)
            }
            if (input.buttonIsPressed(Button.B)) {
                music.startMelody(music.builtInMelody(Melodies.Dadadadum), MelodyOptions.Once)
            }
        })
        """, 
    "1" : 
        """
                /**
        * CAVALLO SFIDA X 2, O  FACCINA O MUSICA
        */
        basic.forever(function () {
            if (input.buttonIsPressed(Button.A)) {
                basic.showIcon(IconNames.Happy)
            } else if (input.buttonIsPressed(Button.B)) {
                music.startMelody(music.builtInMelody(Melodies.Dadadadum), MelodyOptions.Once)
            }
        })
        """, 
    "1" : 
        """
        /**
        * PANCHINA x DUE., CON FACCINA E POI MUSICALE
        */
        basic.forever(function () {
            if (input.buttonIsPressed(Button.A)) {
                basic.showIcon(IconNames.Happy)
                if (input.buttonIsPressed(Button.B)) {
                    music.startMelody(music.builtInMelody(Melodies.Dadadadum), MelodyOptions.Once)
                }
            }
        })
        """, 
    "1" : 
        """
                /**
        * IL CANESTRO MOSTRA-PUNTEGGIO
        */
        basic.forever(function () {
            if (input.buttonIsPressed(Button.A)) {
                conto += 1
                basic.showString("" + (conto))
            }
        })
        """, 
    "1" : 
        """
        
        /**
        * IL DADO MUSICALE
        */
        basic.forever(function () {
            basic.pause(2000)
            valore_caratteristico += randint(1, 6)
            basic.showNumber(valore_caratteristico)
            if (valore_caratteristico % 2 == 0) {
                music.startMelody(music.builtInMelody(Melodies.Dadadadum), MelodyOptions.Once)
            }
        })
        """, 
    "1" : 
        """
        /**
        * ALBERO ANIMATO, ALTRIMENTI SPENTO
        */
        basic.forever(function () {
            if (input.buttonIsPressed(Button.A)) {
                basic.showIcon(IconNames.Heart)
                basic.showIcon(IconNames.SmallHeart)
            } else {
                basic.clearScreen()
            }
        })
        """, 
    "1" : 
        """
        /**
        * CESTINO SORRIDENTE, ALTRIMENTI SPENTO
        */
        basic.forever(function () {
            if (input.buttonIsPressed(Button.A)) {
                basic.showIcon(IconNames.Happy)
            } else {
                basic.clearScreen()
            }
        }) 
        """, 
    "1" : 
        """
                /**
        * OROLOGIO SEGNAFREDDO, ALTRIMENTI SPENTO
        */
        basic.forever(function () {
            if (input.buttonIsPressed(Button.A) && input.temperature() < 10) {
                basic.showIcon(IconNames.Sad)
            } else {
                basic.clearScreen()
            }
        })
        """, 
    "1" : 
        """
        /**
        * TAVOLO GIOCO X 2, FACCINA E MUSICA, ALTRIMENTI SPENTO
        */
        basic.forever(function () {
            if (input.buttonIsPressed(Button.A)) {
                basic.showIcon(IconNames.Happy)
            } else {
                basic.clearScreen()
            }
            if (input.buttonIsPressed(Button.B)) {
                music.startMelody(music.builtInMelody(Melodies.Dadadadum), MelodyOptions.Once)
            } else {
                music.stopAllSounds()
            }
        })
        """, 
    "1" : 
        """
        /**
        * CAVALLO SFIDA X 2, O  FACCINA O MUSICA, ALTRIMENTI SPENTO
        */
        basic.forever(function () {
            if (input.buttonIsPressed(Button.A)) {
                basic.showIcon(IconNames.Happy)
            } else if (input.buttonIsPressed(Button.B)) {
                music.startMelody(music.builtInMelody(Melodies.Dadadadum), MelodyOptions.Once)
            } else {
                basic.clearScreen()
                music.stopAllSounds()
            }
        })
        """, 
    "1" : 
        """
        /**
        * PANCHINA x DUE., CON FACCINA E POI MUSICALE, ALTRIMENTI SPENTA
        */
        basic.forever(function () {
            if (input.buttonIsPressed(Button.A)) {
                basic.showIcon(IconNames.Happy)
                if (input.buttonIsPressed(Button.B)) {
                    music.startMelody(music.builtInMelody(Melodies.Dadadadum), MelodyOptions.Once)
                } else {
                    music.stopAllSounds()
                }
            } else {
                basic.clearScreen()
            }
        })
        """, 
    "1" : 
        """
        /**
        * IL CANESTRO MOSTRA-PUNTEGGIO, ALTRIMENTI SPENTO
        */
        basic.forever(function () {
            if (input.buttonIsPressed(Button.A)) {
                conto += 1
                basic.showString("" + (conto))
            } else {
                basic.clearScreen()
            }
        })
        """, 
    "1" : 
        """   
        /**
        * IL DADO MUSICALE, ALTRIMENTI SPENTO
        */
        basic.forever(function () {
            basic.pause(2000)
            valore_caratteristico += randint(1, 6)
            basic.showNumber(valore_caratteristico)
            if (valore_caratteristico % 2 == 0) {
                music.startMelody(music.builtInMelody(Melodies.Dadadadum), MelodyOptions.Once)
            } else {
                music.stopAllSounds()
            }
        })
        """, 
     
}











