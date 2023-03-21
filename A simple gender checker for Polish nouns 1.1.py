#!/usr/bin/env python
# coding: utf-8

# In[49]:


# This is a program that checks the grammatical gender of the input noun in Polish.
# As the development progresses, new updates will include more complicated functions
# allowing users to detect the gender of the word more effectively, including exception.

# Author: Krzysztof Borowski
# Website: http://KRZdot.wordpress.com
# Twitter: https://twitter.com/KRZdot
# LinkedIn: https://www.linkedin.com/in/KRZdot

# The input form
word = input("Please enter your Polish noun in its dictionary form: ").lower()

print("You entered:",word.upper())
print()

#masculine category: exceptions
if word.endswith("mężczyzna") or word.endswith("mezczyzna") or word.endswith("sędzia") or word.endswith("wojewoda") or word.endswith("hrabia") or word.endswith("satelita") or word.endswith("ysta") or word.endswith("ista") or word.endswith("nauta") or word.endswith("beksa") or word.endswith("niezdara") or word.endswith("łamaga") or word.endswith("oferma") or word.endswith("szko") or word.endswith("oźny") or word.endswith("ozny"):
    print("This word is masculine.")

# feminine category
elif (word.endswith("a") or word.endswith("ni") or word.endswith("ść") or word.endswith("dź")):
    print("This word is feminine.")

# neuter category
elif word.endswith("e") or (word.endswith("ę") or word.endswith("o") or word.endswith("u") or word.endswith("bby") or word.endswith("taxi") or word.endswith("kiwi") or word.endswith("ndi") or word.endswith("nei") or word.endswith("lawi")):
    print("This word is neuter.")

# masculine category
elif word.endswith("b") or (word.endswith("c") or word.endswith("ć") or word.endswith("d") or word.endswith("f") or word.endswith("g") or word.endswith("h") or word.endswith("j") or word.endswith("k") or word.endswith("l") or word.endswith("ł") or word.endswith("m") or word.endswith("n") or word.endswith("ń") or word.endswith("p") or word.endswith("r") or word.endswith("s") or word.endswith("ś") or word.endswith("t") or word.endswith("w") or word.endswith("x") or word.endswith("z") or word.endswith("ź") or word.endswith("ż")):
    print("This word is masculine.")

else:
    print("Looks like the word you entered may not be a noun in Polish. Check the word you entered to make sure it is a dictionary form.")

#add: plural (virile/non-virile: "y", "i", "owie")
#add: f category from Wiki
#add: m nouns that ends in -i, -y


# In[ ]:




