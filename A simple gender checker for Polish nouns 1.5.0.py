#!/usr/bin/env python
# coding: utf-8

# Regular categories
# masculine category
masculine = ("b", "c", "ć", "d", "f", "g", "h", "j", "k", "l", "ł", "m", "n", "ń",
        "p", "r", "s", "ś", "t", "w", "x", "z", "ź", "ż")

# neuter category
neuter = ("e", "ę", "o", "u", "um", "bby", "taxi", "kiwi", "ndi", "nei", "lawi")

# virile category
virile = ("i", "isci", "iści", "cy", "dzi", "dzy", "rzy", "si", "zi", "owie",
          "czanie", "ganie", "kanie", "polanie", "łmanie", "lmanie", "rmanie",
          "rzanie", "szanie", "żanie", "żuje", "zuje", "oscie", "oście", "dzie",
          "ęża", "arze", "panicze")

# non-virile category
nonvirile = ("osci", "ości", "by", "dy", "fy", "gi", "hy", "ki", "ly", "ły",
             "my", "ny", "py", "ry", "sy", "szy", "ty", "wy", "azy", "ezy",
             "izy", "ozy", "uzy", "yzy", "że", "onie", "sie", "zie", "le",
             "je", "pie", "bie", "mie", "nie", "awie", "oce", "acze", "ecze",
             "ocze", "ucze", "ycze", "zcze", "dze", "edzie", "ędzie", "dże",
             "sze", "erze", "urze", "dzieci", "a", "ęta", "eta", "postaci")

# Exceptions categories
# masculine exceptions category
masculine_exceptions = ("mężczyzna", "mezczyzna", "sędzia", "sedzia", "wojewoda",
                   "hrabia", "satelita", "ysta", "ista", "nauta", "beksa",
                   "niezdara", "łamaga", "oferma", "szko", "oźny", "gość",
                   "gosc")

# feminine exceptions category
feminine_exceptions = ("ani", "ini", "ań", "aśń", "asn", "eśń", "esn", "aść", "asc",
                  "iść", "isc", "ość", "osc", "dź")

# feminine word exceptions category
feminine_word_exceptions = (
  "miedź", "miedz", "moc", "noc", "klacz", "ciecz", "rzecz", "dzicz", "smycz",
  "kokorycz", "Bydgoszcz", "goszcz", "brać", "brac", "chuć", "chuc", "jać",
  "jac", "mać", "mac", "płeć", "plec", "sieć", "siec", "czeladź", "czeladz",
  "gołoledź", "gololedz", "krawędź", "łódź", "lodz", "powódź", "powodz",
  "odpowiedź", "odpowiedz", "spowiedź", "spowiedz", "wypowiedź", "wypowiedz",
  "zapowiedź", "zapowiedz", "kolej", "kąpiel", "kapiel", "myśl", "mysl",
  "baśń", "basn", "czerń", "czern", "czerwień", "czerwien", "dłoń", "dlon",
  "goleń", "golen", "jaźń", "jazn", "jesień", "jesien", "kieszeń", "kieszen",
  "krtań", "krtan", "otchłań", "otchlan", "pieczeń", "pieczen", "pieśń",
  "piesn", "pleśń", "plesn", "przestrzeń", "przestrzen", "przyjaźń",
  "przyjazn", "przystań", "przystan", "skroń", "skron", "waśń", "wasn", "woń",
  "won", "zieleń", "zielen", "gołdap", "goldap", "macierz", "twarz", "mysz",
  "wesz", "białoruś", "bialorus", "ruś", "wieś", "wies", "gałąź", "galaz",
  "rzeź", "rzez", "grabież", "grabiez", "mlodzież", "mlodziez", "odzież",
  "odziez", "podaż", "podaz", "sprzedaż", "sprzedaz", "straż", "straz",
  "uprząż", "uprzaz", "brew", "brukiew", "marchew", "konew", "krew", "rukiew",
  "rzodkiew", "żagiew", "zagiew", "chorągiew", "choragiew", "mięta", "mieta,"
  "pięta", "pieta", "renta", "zachęta", "zacheta")

# input form
word = input("Enter a word: \n")
print("You entered:", word.upper())
choice = input("Is this a singular [S] or plural [P] word?\n")

# This code checks for grammatical gender based on the user's input
if choice.lower() == "s":
  if word in feminine_word_exceptions or any(
      word.endswith(suffix) for suffix in feminine_word_exceptions):
    print("This is a feminine word.")
  elif word.endswith(feminine_exceptions) or any(
      word.endswith(suffix) for suffix in feminine_exceptions):
    print("This is a feminine word.")
  elif word in masculine_exceptions:
    print("This is a masculine word.")
  elif word.endswith(neuter) or any(word.endswith(suffix) for suffix in neuter):
    print("This is a neuter word.")
  elif word.endswith(masculine):
    print("This is a masculine word.")
  elif word.endswith("a"):
    print("This is a feminine word.")
  else:
    print("Please check your number selection or spelling and try again.")
elif choice.lower() == "p":
  if word.endswith(nonvirile) or any(
      word.endswith(suffix) for suffix in nonvirile):
    print("This is a non-virile word.")
  elif word.endswith(virile) or any(
      word.endswith(suffix) for suffix in virile):
    print("This is a virile word.")
  else:
    print("Please check your number selection or spelling and try again.")
else:
  print("Please check your number selection or spelling and try again.")