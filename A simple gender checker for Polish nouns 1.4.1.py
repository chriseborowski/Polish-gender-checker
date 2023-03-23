#!/usr/bin/env python
# coding: utf-8

# This is a program that checks the grammatical gender of the input noun in Polish.
# As the development progresses, new updates will include more complicated functions
# allowing users to detect the gender of the word more effectively, including exception.

# This version of the program works for nouns in the following categories:
# (a) masculine singular,
# (b) feminine singular,
# (c) neuter singular,
# (d) masculine (virile) singular,
# (e) nonmasculine (virile) singular,

# Version history
# v. 1.0 - basic version of the program developed
# v. 1.1 - masculine and neuter gender exceptions added
# v. 1.2 - feminine exceptions added
# v. 1.3 - masculine plural nouns added (virile and non-virile)

# Regular categories
# masculine category

masc = ("b", "c", "ć", "d", "f", "g", "h", "j", "k", "l", "ł", "m", "n", "ń", "p"
        , "r", "s", "ś", "t", "w", "x", "z", "ź", "ż")

# neuter category

neut = ("e", "ę", "o", "u", "bby", "taxi", "kiwi", "ndi", "nei", "lawi")

# virile category

virile = ("i", "isci", "iści", "cy", "dzi", "dzy", "rzy", "si", "zi", "owie", "czanie"
          , "ganie", "kanie", "polanie", "łmanie", "lmanie", "rmanie", "rzanie", "szanie"
          , "żanie", "żuje", "zuje", "oscie", "oście", "dzie", "ęża", "arze")

# non-virile category

nonvirile = ("osci", "ości", "by", "dy", "fy", "gi", "hy", "ki", "ly", "ły", "my", "ny"
             , "py", "ry", "sy", "szy", "ty", "wy", "zy", "że", "onie", "sie", "zie"
             , "le", "je", "pie", "bie", "mie", "awie", "oce", "acze", "ecze", "ocze"
             , "ucze", "ycze", "dze", "edzie", "ędzie", "dże", "sze", "erze", "urze")

# Exceptions categories
# masculine exceptions category

masc_exceptions = ("mężczyzna", "mezczyzna", "sedzia", "wojewoda", "hrabia", "satelita"
                   , "ysta", "ista", "nauta", "beksa", "niezdara", "łamaga", "oferma"
                   , "szko", "oźny", "gość", "gosc")

# feminine exceptions category

fem_exceptions = ("ani", "ini", "ań", "aśń", "asn", "eśń", "esn", "aść", "asc", "iść"
                  , "isc", "ość", "osc", "dź", "miedź", "miedz", "moc", "noc", "klacz"
                  , "ciecz", "rzecz", "dzicz", "smycz", "kokorycz", "Bydgoszcz"
                  , "goszcz", "brać", "brac", "chuć", "chuc", "jać", "jac", "mać", "mac"
                  , "płeć", "plec", "sieć", "siec", "czeladź", "czeladz", "gołoledź"
                  , "gololedz", "krawędź", "łódź", "lodz", "powódź", "powodz", "odpowiedź"
                  , "odpowiedz", "spowiedź", "spowiedz", "wypowiedź", "wypowiedz"
                  , "zapowiedź", "zapowiedz", "kolej", "kąpiel", "kapiel", "myśl", "mysl"
                  , "baśń", "basn", "czerń", "czern", "czerwień", "czerwien", "dłoń", "dlon"
                  , "goleń", "golen", "jaźń", "jazn", "jesień", "jesien", "kieszeń", "kieszen"
                  , "krtań", "krtan", "otchłań", "otchlan", "pieczeń", "pieczen", "pieśń"
                  , "piesn", "pleśń", "plesn", "przestrzeń", "przestrzen", "przyjaźń", "przyjazn"
                  , "przystań", "przystan", "skroń", "skron", "waśń", "wasn", "woń", "won"
                  , "zieleń", "zielen", "gołdap", "goldap", "macierz", "twarz", "mysz", "wesz"
                  , "białoruś", "bialorus", "ruś", "wieś", "wies", "gałąź", "galaz", "rzeź"
                  , "rzez", "grabież", "grabiez", "mlodzież", "mlodziez", "odzież", "odziez"
                  , "podaż", "podaz", "sprzedaż", "sprzedaz", "straż", "straz", "uprząż"
                  , "uprzaz", "brew", "brukiew", "marchew", "konew", "krew", "rukiew", "rzodkiew"
                  , "żagiew", "zagiew", "chorągiew", "choragiew")

# The input form
word = input("Please enter your Polish noun in its dictionary (nominative) form: ").lower()

print("You entered:",word.upper())
print()

# execute masculine exceptions category

if word.endswith(masc_exceptions) or any(word.endswith(suffix) for suffix in masc_exceptions):
    print("This word is masculine, singular.")

# execute feminine exceptions category

elif word.endswith(fem_exceptions) or any(word.endswith(suffix) for suffix in fem_exceptions):
    print("This word is feminine, singular.")

# feminine category
elif word.endswith("a"):
    print("This word is feminine, singular.")

# masculine category

elif word.endswith(masc) or any(word.endswith(suffix) for suffix in masc):
    print("This word is masculine, singular.")

#non-virile category

elif word.endswith(nonvirile) or any(word.endswith(suffix) for suffix in nonvirile):
    print("This word is non-virile, plural.")
    
elif word.endswith(virile) or any(word.endswith(suffix) for suffix in virile):
    print("This word is virile, plural.")

# neuter category

elif word.endswith(neut) or any(word.endswith(suffix) for suffix in neut):
    print("This word is neuter, singular.")

else:
    print("Looks like the word you entered may not be a noun in Polish. Check the word you entered to make sure it is in a dictionary form.")