# these are the term counts calculated in the lab
# keys are words in Trump's tweets;
# values are number of tweets with that word in it

lab_dict = {'trump': 13924, 'russia': 412, 'obama': 2712, 'fake news': 333, 'mexico': 199}

terms = list(lab_dict.keys())
counts = list(lab_dict.values())

# the order of the keys is "nondeterministic" which basically means random
# For CS40: Anytime you use the .keys()/.values()
#convert to list
#the order we would like; the order that is "reasonable for the purposes of the project is alphabetical"
#this is the wrong way to do it "terms.sort()"

terms.sort()
accumulator = []
for term in terms:
    accumulator.append(lab_dict[term])
counts = accumulator

# this code generates a plot
# rely on documentation on website, look at inspect element for code of other graphs
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.bar(terms, counts)
plt.show()