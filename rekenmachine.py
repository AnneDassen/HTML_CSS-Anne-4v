def lijsten_loop(lijst_namen):
  for x in range(len(lijst_namen)):
    print(lijst_namen[x])
  print("")
  print("Kies uit 1 van de bovenstaande lijsten. (Volledige naam):")

def woorden_loop(lijsten , gekozen_lijst):
  print("De lijst:")
  for key, value in lijsten[gekozen_lijst].items():
    print(key , "=" , value)

def keuzemenu():
  print("")
  print(" - - - - - - - - Keuzemenu - - - - - - - - ")
  print("|                                         |")
  print("| 1: Nieuwe woordenlijst maken.           |")
  print("| 2: Lijsten bekijken.                    |")
  print("| 3: Woorden toevoegen of veranderen.     |")
  print("| 4: Overhoren.                           |")
  print("| 5: Programma stoppen.                   |")
  print("|                                         |")
  print(" - - - - - - - - Keuzemenu - - - - - - - - ")
  print("Keuze:")

def nieuwe_lijst(lijsten, lijsten_loop, lijst_namen):
  print("")
  print("Nieuwe lijst")
  print("Hoe wil je de lijst noemen? (Mag het woord 'lijst' niet bevatten)")
  lijst_naam = input("")
  if lijst_naam in lijst_namen:
    print("Er bestaat al een lijst met deze naam.")
  else:
    lijsten[lijst_naam] = {}
    lijst_namen.append(lijst_naam)

def lijst_bekijken(lijsten, lijsten_loop, lijst_namen):
  print("")
  print("Lijsten bekijken")
  lijsten_loop(lijst_namen)
  gekozen_lijst = input("")
  if gekozen_lijst not in lijst_namen:
    print("Dit is geen bestaande lijst.")
  else:
    if len(lijsten[gekozen_lijst]) == 0:
      print("Deze lijst is leeg.")
    else:
      woorden_loop(lijsten, gekozen_lijst)

def woorden_toevoegen(lijsten, lijsten_loop, lijst_namen):
  if len(lijst_namen) == 0:
    print("Er zijn nog geen lijsten")
  else:
    print("")
    print("Lijst aanpassen")
    lijsten_loop(lijst_namen)
    gekozen_lijst = input("")
    if gekozen_lijst not in lijst_namen:
      print("Dit is geen bestaande lijst.")
    else:
      if len(lijsten[gekozen_lijst]) == 0:
        print("Deze lijst is leeg.")
      else:
        woorden_loop(lijsten, gekozen_lijst)
      print("Welk woord wil je toevoegen? (Typ een bestaand woord als je die wilt veranderen.)")
      nieuw = input("")
      print("Wat is de betekenis van dat woord?")
      betekenis = input("")
      lijsten[gekozen_lijst][nieuw] = betekenis

def overhoren(lijsten, lijsten_loop, lijst_namen):
  print("")
  print("Overhoren")
  lijsten_loop(lijst_namen)
  gekozen_lijst = input("")
  if gekozen_lijst not in lijst_namen:
    print("Deze lijst bestaat niet.")
  else:
    import random
    print("Typ stop om te stoppen met overhoren.")
    for key, value in lijsten[gekozen_lijst].items():
      woord = random.choice(list(lijsten[gekozen_lijst].keys()))
      print(woord)
      print("Geef de betekenis van het woord.")
      betekenis = input("")
      if betekenis == lijsten[gekozen_lijst][woord]:
        print("Correct!")
      elif betekenis == "stop":
        break
      else:
        print("Fout!")
    print("Klaar met overhoren.")

def stop():
  print("")
  print("Dankjewel voor het gebruiken van dit overhoorprogramma.")

def main():
  print("Welkom bij het overhoorprogramma")
  lijst_namen = []
  lijsten = {}
  keuze = 1
  while(keuze != 5):
    keuzemenu()
    keuze = int(input(""))
    if keuze == 1:
      nieuwe_lijst(lijsten, lijsten_loop, lijst_namen)
    elif keuze == 2:
      lijst_bekijken(lijsten, lijsten_loop, lijst_namen)
    elif keuze == 3:
      woorden_toevoegen(lijsten, lijsten_loop, lijst_namen)
    elif keuze == 4:
      overhoren(lijsten, lijsten_loop, lijst_namen)
    elif keuze == 5:
      stop()
    else:
      print("Onmogelijk antwoord. ")

main()
