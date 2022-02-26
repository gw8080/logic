#Count of object expression -> success/requirement expression -> action-object subset non/commonality expression = Generalisation.
from pattern.en import pluralize, singularize
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import wordnet as wn
import random
from operator import itemgetter
f = open('objects.txt',"r")
fa = open("logic_output.txt", "w")
for Object in f:
    proc = wn.synsets(Object.strip("\n"))

    if proc:
        for item in proc:
            proc2 = item.name().split(".")[0]
            for x in range(0, 3):
                proc3 = item.hyponyms()
                if proc3:
                    for itemB in proc3:
                        proc4 = item.name().split(".")[0]
                        if pluralize(item.name().split(".")[0]) != pluralize(itemB.name().split(".")[0]):
                            many = pluralize(item.name().split(".")[0]) + " are " + pluralize(itemB.name().split(".")[0])
                            rand = random.choice(proc).name().split(".")[0]
                            if wn.synsets(singularize(itemB.name().split(".")[0]), pos=wn.VERB):
                                if wn.synsets(singularize(itemB.name().split(".")[0]), pos=wn.VERB)[0].name().split(".")[0] != singularize(itemB.name().split(".")[0]):
                                    if wn.synsets(proc4, pos=wn.NOUN):
                                        proc5 = wn.synsets(proc4, pos=wn.NOUN)[0].name().split(".")[0]
                                        if rand != proc5:
                                            second = rand + " is a " + proc5
                                            final = pluralize(rand) + " are " + pluralize(itemB.name().split(".")[0])
                                            print(many)
                                            print(second)
                                            print(final)
                                            print()
                                            fa.write(many + "\n")
                                            fa.write(second + "\n")
                                            fa.write(final + "\n")
                                            fa.flush()
    proc2 = pluralize(rand)
fa.close()
#prove statement with a syllogism






