    #SynthReason - Synthetic dawn
    #Copyright (C) 2022 George Wagenknecht
    #This program is free software: you can redistribute it and/or modify
    #it under the terms of the GNU General Public License as published by
    #the Free Software Foundation, either version 3 of the License, or
    #(at your option) any later version.
    #This program is distributed in the hope that it will be useful,
    #but WITHOUT ANY WARRANTY; without even the implied warranty of
    #MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    #GNU General Public License for more details.
    #You should have received a copy of the GNU General Public License
    #along with this program.  If not, see <https://www.gnu.org/licenses/>.

#Count of object expression -> success/requirement expression -> action-object subset non/commonality expression = Generalisation.
from pattern.en import pluralize, singularize
from nltk.corpus import wordnet as wn
import random
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
                    if wn.synsets(proc4, pos=wn.NOUN):
                        proc5 = wn.synsets(proc4, pos=wn.NOUN)[0].name().split(".")[0]
                        if rand != proc5:
                            second = rand + " is a " + proc5
                            final = pluralize(rand) + " are " + pluralize(proc3[0].name().split(".")[0])
                            print(many)
                            print(second)
                            print(final)
                            print()
                            fa.write(many + "\n")
                            fa.write(second + "\n")
                            fa.write(final + "\n")
                            fa.write("\n")
                            fa.flush()
fa.close()
#prove statement with a syllogism






