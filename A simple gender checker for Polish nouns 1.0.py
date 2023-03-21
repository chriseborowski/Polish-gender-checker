#!/usr/bin/env python
# coding: utf-8

# In[149]:


# This is a program that checks the grammatical gender of the input noun.

word = input("Please enter your Polish noun in its dictionary form: ").lower()

print("You entered:",word.upper())
print()

# feminine category
if word.endswith("a") or (word.endswith("ni") or word.endswith("ść") or word.endswith("dź")):
    print("This word is feminine.")
    print()
    print("NOTE: In Polish, biological gender takes precedence over grammatical gender. Therefore, nouns that end in '-a' and refer to males/male professions (e.g., 'artysta', 'mężczyzna') will be masculine.")

# neuter category
elif word.endswith("e") or (word.endswith("ę") or word.endswith("o") or word.endswith("u") or word.endswith("y") or word.endswith("xi")):
    print("This word is neuter.")

# masculine category
elif word.endswith("b") or (word.endswith("c") or word.endswith("ć") or word.endswith("d") or word.endswith("f") or word.endswith("g") or word.endswith("h") or word.endswith("j") or word.endswith("k") or word.endswith("l") or word.endswith("ł") or word.endswith("m") or word.endswith("n") or word.endswith("ń") or word.endswith("p") or word.endswith("r") or word.endswith("s") or word.endswith("ś") or word.endswith("t") or word.endswith("w") or word.endswith("x") or word.endswith("z") or word.endswith("ź") or word.endswith("ż")):
    print("This word is masculine.")

else:
    print("Looks like the word you entered may not be a noun in Polish. Check the word you entered to make sure it is a dictionary form.")

