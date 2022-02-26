#Count of object expression -> success/requirement expression -> action-object subset non/commonality expression = Generalisation.
from pattern.en import pluralize, singularize
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import wordnet as wn
import random
f = open('noun.txt',"r")
for Object in f:
    proc = wn.synsets(Object.strip("\n"))
    if proc:
        for item in proc:
            proc2 = item.name().split(".")[0]
            proc3 = item.hypernyms()
            if proc3:
                proc4 = proc[0].name().split(".")[0]
                if pluralize(proc[0].name().split(".")[0]) != pluralize(proc3[0].name().split(".")[0]):
                    many = pluralize(proc[0].name().split(".")[0]) + " are " + pluralize(proc3[0].name().split(".")[0])
                    rand = random.choice(proc).name().split(".")[0]
                    proc5 = wn.synsets(proc4, pos=wn.NOUN)[0].name().split(".")[0]
                    if rand != proc5:
                        second = rand + " is a " + proc5
                        final = pluralize(rand) + " are " + pluralize(proc3[0].name().split(".")[0])
                        print(many)
                        print(second)
                        print(final)
                        print()
#prove statement with a syllogism