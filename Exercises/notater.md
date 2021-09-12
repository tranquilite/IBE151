# Noter til øvingsarbeidet

## Generelt
For tilfeller hvor oppgaven oppgir et inntrykk(/input) og et forventet resultat,
så er programflyten helt avhengig av som assert-setninger, slik at hele kodeblokker
vil hoppes over hvis python kjøres med optimiseringer (python -O).

En liten bisetning; Oppgavene er fine for å prøve seg i retninga av testdrevet
utvikling, siden øvingsoppgavene gjerne gir et sett inntrykk og et forventet
resultat, og i flere tilfeller også hvordan grensesnittet *burde* være.

## Filspesifikke anmerkninger

### u35.py
Ingen spesielle kommentarer. Oppgaver fra Week 35.pdf.  
u35 er ganske rå og dårlig formatert, så ikke se på denne som god praksis.
..eller tålbar praksis. Generelt unngå alt som ble gjort i u35.py.

*Vedr opg 4*  
Ikke til å legge skjul på at jeg blingsa litt her. Først merka jeg bare 
( *8 = people* ) men en uke etterpå når jeg var innom for å sjekke noe annet
dritt, så så jeg at også ( *4 += 7 / 2* ) burde være merket som SyntaxError. 
For første tilfellet er det underliggende problemet at du ikke kan tildele
en verdi på en fundamental type (for gøy; fordi det ikke finnes en STORE_CONST-bytecode).
Samme gjelder for siste, siden += er INPLACE_ADD som 
egentlig bare er STORE_FAST mot en (her) LOAD_CONST (7/2 optimaliseres ved runtime) 


### u36.py
*test_opg(crib: dict) -> None*  
Utnytter assert statements for å styre programflyten, og hele deler av
funksjonen vil passeres hvis python kjøres med optimisering (python -O -m u36)  
Gir en F hvis funksjonsproduktet ikke stemmer med det oppgaven forventer.


### hjelpere.py
*fprint*  
fprint er egentlig bare en wrapper som printer return-verdi fra funksjonen
til stdout (pluss litt pynt for oversiktens del)  
såeh.. ja. bruk @fprint