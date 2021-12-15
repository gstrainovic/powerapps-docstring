[x] Script erstellen das den Quellcode abändern kann: 
    Alle Werte mit UpdateIf([Tabelle],Lookup(...),{xxx}) durch Patch([Tabelle],ThisItem,{xxx}) ersetzten.
    In der Spalte des Lookup können verschiedene Werte stehen. Der Tabellenname [Tabelle] und {xxx} sollen identisch bleiben.   
    Der Lookup entfällt und wird durch ThisItem ersetzt.

    From:
    UpdateIf(colQuestionRow,ID218=ThisItem.ID218,{Edit:"Edit"}),

    To:
    Patch(colQuestionRow,ThisItem,{Edit:"Edit"}),

[x] 
Ich würde gerne auf den Screens sehen welcher Flow dort jeweils getriggert wird. [Flowname].Run ist das eindeutige Merkmal.
Umgekehrt hätte ich auch gerne eine Übersicht aller Flows und dann wo diese verwendet werden.

[ ] Migratie to Azure DevOps