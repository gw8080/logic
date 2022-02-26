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
            proc3 = item.hypernyms()
            if proc3:
                proc4 = proc[0].name().split(".")[0]
                if pluralize(proc[0].name().split(".")[0]) != pluralize(proc3[0].name().split(".")[0]):
                    many = pluralize(proc[0].name().split(".")[0]) + " are " + pluralize(proc3[0].name().split(".")[0])
                    rand = random.choice(proc).name().split(".")[0]
                    if wn.synsets(singularize(proc3[0].name().split(".")[0]), pos=wn.VERB):
                        if wn.synsets(singularize(proc3[0].name().split(".")[0]), pos=wn.VERB)[0].name().split(".")[0] != singularize(proc3[0].name().split(".")[0]):
                            must = "you should " + wn.synsets(singularize(proc3[0].name().split(".")[0]), pos=wn.VERB)[0].name().split(".")[0] + " " +  singularize(proc[0].name().split(".")[0])+ " " + singularize(proc3[0].name().split(".")[0])  + " for " + rand
                            if wn.synsets(proc4, pos=wn.NOUN):
                                proc5 = wn.synsets(proc4, pos=wn.NOUN)[0].name().split(".")[0]
                                if rand != proc5:
                                    second = rand + " is a " + proc5
                                    final = pluralize(rand) + " are " + pluralize(proc3[0].name().split(".")[0])
                                    print(many)
                                    print(second)
                                    print(final)
                                    print(must)
                                    print()
                                    fa.write(many + "\n")
                                    fa.write(second + "\n")
                                    fa.write(final + "\n")
                                    fa.write(must + "\n\n")
                                    fa.flush()
fa.close()
#prove statement with a syllogism






