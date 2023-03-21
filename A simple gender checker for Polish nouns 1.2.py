#!/usr/bin/env python
# coding: utf-8

# In[46]:


# This is a program that checks the grammatical gender of the input noun in Polish.
# As the development progresses, new updates will include more complicated functions
# allowing users to detect the gender of the word more effectively, including exception.

# Author: Krzysztof Borowski
# Website: http://KRZdot.wordpress.com
# Twitter: https://twitter.com/KRZdot
# LinkedIn: https://www.linkedin.com/in/KRZdot

# Version history
# v 1.0 - basic version of the program developed
# v 1.1 - masculine and neuter gender exceptions added
# v 1.2 - feminine exceptions added

# The input form
word = input("Please enter your Polish noun in its dictionary form: ").lower()

print("You entered:",word.upper())
print()

#masculine category: exceptions
if word.endswith("mężczyzna") or word.endswith("mezczyzna") or word.endswith("sędzia") or word.endswith("wojewoda") or word.endswith("hrabia") or word.endswith("satelita") or word.endswith("ysta") or word.endswith("ista") or word.endswith("nauta") or word.endswith("beksa") or word.endswith("niezdara") or word.endswith("łamaga") or word.endswith("oferma") or word.endswith("szko") or word.endswith("oźny") or word.endswith("ozny") or word.endswith("gość") or word.endswith("gosc"):
    print("This word is masculine.")

#feminine category: exceptions rules
elif word.endswith("ani") or word.endswith("ini") or word.endswith("ań") or word.endswith("aśń") or word.endswith("asn") or word.endswith("eśń") or word.endswith("esn") or word.endswith("aść") or word.endswith("asc") or word.endswith("iść") or word.endswith("isc") or word.endswith("ość") or word.endswith("osc") or word.endswith("dź"):
    print("This word is feminine.")

#feminine category: exceptions
elif word.endswith("miedź") or word.endswith("miedz") or word.endswith("głąb") or word.endswith("moc") or word.endswith("noc") or word.endswith("klacz") or word.endswith("ciecz") or word.endswith("rzecz") or word.endswith("dzicz") or word.endswith("smycz") or word.endswith("kokorycz") or word.endswith("Bydgoszcz") or word.endswith("goszcz") or word.endswith("brać") or word.endswith("brac") or word.endswith("chuć") or word.endswith("chuc") or word.endswith("jać") or word.endswith("jac") or word.endswith("mać") or word.endswith("mac") or word.endswith("płeć") or word.endswith("plec") or word.endswith("sieć") or word.endswith("siec") or word.endswith("czeladź") or word.endswith("czeladz") or word.endswith("gołoledź") or word.endswith("gololedz") or word.endswith("krawędź") or word.endswith("krawedz") or word.endswith("łódź") or word.endswith("lodz") or word.endswith("powódź") or word.endswith("powodz") or word.endswith("odpowiedź") or word.endswith("odpowiedz") or word.endswith("spowiedź") or word.endswith("spowiedz") or word.endswith("wypowiedź") or word.endswith("wypowiedz") or word.endswith("zapowiedź") or word.endswith("zapowiedz") or word.endswith("kolej") or word.endswith("kąpiel") or word.endswith("kapiel") or word.endswith("myśl") or word.endswith("mysl") or word.endswith("sól") or word.endswith("baśń") or word.endswith("basn") or word.endswith("czerń") or word.endswith("czern") or word.endswith("czerwień") or word.endswith("czerwien") or word.endswith("dłoń") or word.endswith("dlon") or word.endswith("goleń") or word.endswith("golen") or word.endswith("jaźń") or word.endswith("jazn") or word.endswith("jesień") or word.endswith("jesien") or word.endswith("kieszeń") or word.endswith("kieszen") or word.endswith("krtań") or word.endswith("krtan") or word.endswith("otchłań") or word.endswith("otchlan") or word.endswith("pieczeń") or word.endswith("pieczen") or word.endswith("pieśń") or word.endswith("piesn") or word.endswith("pleśń") or word.endswith("plesn") or word.endswith("przestrzeń") or word.endswith("przestrzen") or word.endswith("przyjaźń") or word.endswith("przyjazn") or word.endswith("przystań") or word.endswith("przystan") or word.endswith("skroń") or word.endswith("skron") or word.endswith("waśń") or word.endswith("wasn") or word.endswith("woń") or word.endswith("won") or word.endswith("zieleń") or word.endswith("zielen") or word.endswith("gołdap") or word.endswith("goldap") or word.endswith("macierz") or word.endswith("twarz") or word.endswith("mysz") or word.endswith("wesz") or word.endswith("białoruś") or word.endswith("bialorus") or word.endswith("ruś") or word.endswith("wieś") or word.endswith("wies") or word.endswith("gałąź") or word.endswith("galaz") or word.endswith("rzeź") or word.endswith("rzez") or word.endswith("grabież") or word.endswith("grabiez") or word.endswith("mlodzież") or word.endswith("mlodziez") or word.endswith("odzież") or word.endswith("odziez") or word.endswith("podaż") or word.endswith("podaz") or word.endswith("sprzedaż") or word.endswith("sprzedaz") or word.endswith("straż") or word.endswith("straz") or word.endswith("uprząż") or word.endswith("uprzaz") or word.endswith("brew") or word.endswith("brukiew") or word.endswith("marchew") or word.endswith("konew") or word.endswith("krew") or word.endswith("rukiew") or word.endswith("rzodkiew") or word.endswith("żagiew") or word.endswith("zagiew") or word.endswith("chorągiew") or word.endswith("choragiew"):
    print("This word is feminine.")
    
# feminine category
elif word.endswith("a"):
    print("This word is feminine.")

# neuter category
elif word.endswith("e") or (word.endswith("ę") or word.endswith("o") or word.endswith("u") or word.endswith("bby") or word.endswith("taxi") or word.endswith("kiwi") or word.endswith("ndi") or word.endswith("nei") or word.endswith("lawi")):
    print("This word is neuter.")

# masculine category
elif word.endswith("b") or (word.endswith("c") or word.endswith("ć") or word.endswith("d") or word.endswith("f") or word.endswith("g") or word.endswith("h") or word.endswith("j") or word.endswith("k") or word.endswith("l") or word.endswith("ł") or word.endswith("m") or word.endswith("n") or word.endswith("ń") or word.endswith("p") or word.endswith("r") or word.endswith("s") or word.endswith("ś") or word.endswith("t") or word.endswith("w") or word.endswith("x") or word.endswith("z") or word.endswith("ź") or word.endswith("ż")):
    print("This word is masculine.")

else:
    print("Looks like the word you entered may not be a noun in Polish. Check the word you entered to make sure it is a dictionary form.")


# In[ ]:




