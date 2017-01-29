
# TODO: Decide on a way to represent DS's, DP's etc. Most likely as an object.
# TODO: Store all types of DP's in some form (dict or list)
# TODO: Research method: How do we connect them? Some kind of semantics? 
#		Will we do this rule-based 
#		And write out all rules, or have some structure (graph or something) and
#		And have the code automatically find his way?
# TODO: interface python
# TODO: add hash to classes.

# Using a graph:
# http://stackoverflow.com/questions/4901815/object-of-custom-type-as-dictionary-key


import csv


"""
---------------------------------
---------------------------------
		MAINCLASSES
---------------------------------
---------------------------------
"""

class DentalState(object):
    """
    """
    def __init__(self):
        """"""
        self.status = ["healthy", "unhealthy"]

	def changeStatus(self, s):
		self.status = s


class DentalProblem(object):
    """
    """
    def __init__(self,name="",alt_name="", description=""):
        """"""
        self.status = [True,False]
        self.name = name
        self.alt_name = alt_name #alternative names
        self.description = description #Some kind of description of the problem

    def __str__(self):
        return "<<DP:"+ self.name +">>"

    def __repr__(self):
        return "<<DP:"+ self.name +">>"


class DentalObservable(object):
    """
    """
    def __init__(self):
        """"""


class Treatment(object):
    """
    """
    def __init__(self, name = ""):
        """"""
        self.name = name
        self.status = [True,False]
        self.time = range(5,95,5)
    
    def __str__(self):
        return "<<TREATMENT:"+ self.name +">>"

        
class DentalModel(object):
	"""
	"""
	def __init__(self):
		pass

"""
---------------------------------
---------------------------------
		SUBCLASSES
---------------------------------
---------------------------------
"""



"""
---------------------------------
Dental State
---------------------------------
"""

class StateGum(DentalState):
	"""
	"""
	def __init__(self):
		""""""
		self.state = ["normal", "slight inflammation", "severe inflammation"]
		self.recession = [True,False]


class StateEnamel(DentalState):
	"""
	"""
	def __init__(self):
		""""""
		self.state = ["normal", "cracked", "broken", "cavity"]


class StatePulp(DentalState):
	"""
	"""
	def __init__(self):
		""""""
		self.state = ["normal", "inflamation"]

class StateDentine(DentalState):
	"""
	"""
	def __init__(self):
		""""""
		self.state = ["normal", "sensitive", "hypersensitive"]

class StateApex(DentalState):
	"""
	"""
	def __init__(self):
		""""""
		self.state = ["normal", "inflamation"]


"""
---------------------------------
Dental Problems
---------------------------------
"""

class ProblemTooth(DentalProblem):
    def __str__(self):
        return "<<DP-TOOTH:"+ self.name +">>"
    pass


class ProblemGums(DentalProblem):
    def __str__(self):
        return "<<DP-GUMS:"+ self.name +">>"


class ProblemOther(DentalProblem):
    def __str__(self):
        return "<<DP-OTHER:"+ self.name +">>"



"""
---------------------------------
Dental Observables
---------------------------------
"""
class ObservablePain(DentalObservable):
    """
    """
    def __init__(self):
    	""""""
        # Dictlist consist of 2 element lists with [attribute, value]
        self.name ="pain"
        self.statusdict = {}
            
        self.paintype = [["throbbing", "sharp"], "Would you describe the pain as nagging/throbbing or sharp/stinging?"]
        self.jaw = [["upper", "lower"], "Is the pain in the upper or lower jaw?"]
        self.onset = [["recent","chronic"], "When did you start experiencing this pain?"]
        self.reaction_to_cold = [["increase","decrease","same"], "Does the pain decrease when consuming something cold?"]
        self.reaction_to_heat = [["increase","decrease","same"], "Does the pain decrease when consuming something cold?"]
        self.reaction_to_pressure = [["increase","decrease", "same"], "Does the pain decrease when there is pressure on it?"]
        self.location = [["known","unknown"], "Do you know which tooth or molar causes the pain?"]
        self.source = [["particular_tooth","multiple_teeth","outside_teeth"], "Do you feel like the pain comes from multiple teeth?"]
        self.course = [["worsened_or_same", "reduced"],"Has the pain changed from when you first experienced it?"]
        self.pain_bending_stairs = [[True,False], "Does the pain increase when bending or taking the stairs?"]
        self.duration = [["short","medium", "long"],] # This might need some translation into measurable times

    def addAttributes(self, attrlist):
        # attrlist is a list of lists that consist of 2 element. example : [ [attribute, value] ]
        self.statusdict = {}
        for i in attrlist:
            if i[i] != "":
                self.statusdict[i[0]] = i[1]
            else:
                self.statusdict[i[0]] = None


    def __str__(self):
        return "<<DO-PAIN>>"

    def __repr__(self):
        return "<<DO-PAIN>>"

    # def set_paintype(self, val):
    #     self.paintype = val

    # def set_onset(self, val):
    #     self.onset = val

    # def set_reaction_to_cold(self, val):
    #     self.reaction_to_cold = val

    # def set_reaction_to_heat(self, val):
    #     self.reaction_to_heat = val

    # def set_location(self, val):
    #     self.location = val

    # def set_source(self, val):
    #     self.source = val

    # def set_course(self, val):
    #     self.course = val

    # def set_pain_bending_stairs(self, val):
    #     self.pain_bending_stairs = val

    # def set_duration(self, val):
    #     self.duration = val

    


class ObservableSwelling(DentalObservable):
    """
    """
    def __init__(self):
    	""""""
        self.name ="swelling"
    	self.status = [[True,False],"Is there swelling also?"]

    def set_status(self, val):
        self.status = val

    def __str__(self):
        return "<<DO-SWELLING>>"

    def __repr__(self):
        return "<<DO-SWELLING>>"


class ObservableTooth(DentalObservable):
    """
    """
    def __init__(self):
    	""""""
        self.name ="tooth"
        self.number = range(1,32) # number? What does this number refer to?
        self.recent_treatment_bump = [[True,False], "Recently, did you receive any dental treatments recently or perhaps bump it?" ]



    def __str__(self):
        return "<<DO-TOOTH>>"

    def __repr__(self):
        return "<<DO-TOOTH>>"


class ObservableGums(DentalObservable):
    """
    """
    def __init__(self):
    	""""""
        self.name ="gums"
    	self.bleeding = [[True,False], "When brushing or flossing your teeth, do your gums bleed?"]
    	# self.colour = self.color = ["bright_red", "normal"]

    def __str__(self):
        return "<<DO-GUMS>>"

    def __repr__(self):
        return "<<DO-GUMS>>"


class ObservableCommonCold(DentalObservable):
    """
    """
    def __init__(self):
    	""""""
        self.name ="commoncold"
    	self.status = [[True,False], "Do you have a cold or clogged sinuses, on the side of the pain? "]

    def set_status(self, val):
        self.status = val

    def __str__(self):
        return "<<DO-COMMONCOLD>>" 

    def __repr__(self):
        return "<<DO-COMMONCOLD>>" 



"""
=========================
-------------------------
    INSTANCES
-------------------------
=========================
"""

"""
-------------------------
    States - DS's
-------------------------
"""

ds_gums =  StateGum()
ds_enamel = StateEnamel()
ds_pulp = StatePulp()
ds_dentine = StateDentine()
ds_apex = StateApex()

"""
-------------------------
    Problems | DP's
-------------------------
"""
# Add name variable to the classes, initially set to None, later changed in official naming
# Add description as a variable as well

dp_dict = {} # Dental problem dictionary
do_dict = {} # Dental Observable

dp_names_tooth = ["reversible pulpitis", "irreversible pulpitis",\
    "cavity", "periapical periodontitis", "treatment pain", \
    "sensitive tooth neck", "periodontitis"]

dp_names_gums = ["gingival recession", "gingivitis", "pocket"]

dp_names_other = ["sinusitis", "need examination",\
    "abces", "other than teeth", "no emergency", \
    "uncertain"]

# Create DP's and put them in the dictionary
for i in dp_names_tooth:
    dp_dict[i] = [ProblemTooth(i)]

#Create DP's and put them in the dictionary
for i in dp_names_gums:
    dp_dict[i] = [ProblemGums(i)]

for i in dp_names_other:
    dp_dict[i] = [ProblemOther(i)]
    print dp_dict[i]

"""
-------------------------
    Observables- DO's
-------------------------
"""

do_pain = ObservablePain()
do_swelling = ObservableSwelling()
do_tooth = ObservableTooth()
do_gums = ObservableGums()
do_commoncold = ObservableCommonCold()

do_dict = {"pain":do_pain, "swelling":do_swelling, "tooth":do_tooth, "gums":do_gums, "commoncold":do_commoncold}

"""
-------------------------
    Treatment - T's
-------------------------
"""
treatment_dict = {} # Treatment dictionary

t_names = ["drain", "further examination", "nasal drops or antibiotics", \
    "extraction", "denture syringing and rinse advice" \
    "extraction","reasure", "painkillers sensodyne", "root canal treatment"]

# Create treatments and put them in the dictionary
for i in t_names:
    treatment_dict[i] = Treatment(i)
    print treatment_dict[i]


"""
=========================
-------------------------
    MODEL / RULES
-------------------------
=========================
"""

"""
-------------------------
    Manifestation rules
-------------------------
"""

manifestation_rules = []

with open('manifestation_rules.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    manifestation_titles = readCSV.next()
    observable_att_list = []

    for row in readCSV:
        dp = DentalProblem(row[0],row[1],row[2])
        base = [dp, "manifestation"]
        for i in range(4,len(row)):
            if len(row[i]) == 0: 
                continue # If there is no value, meaning no effect on this observable
            observable_type, observable_attribute = manifestation_titles[i].split(".")
            observable_att_list.append(observable_attribute)
            new_rule = []
            new_rule.extend(base)
            new_rule.extend([observable_type, observable_attribute, row[i]])
            manifestation_rules.append(new_rule) # example [dp, "manifests", "pain", "onset", "recent"]


print manifestation_rules

# response = raw_input("Enter observable type, seperated by a comma. Example-> pain.onset,recent" )

print "========================== \n"
print "========================== \n"


def findDiagnoses(manrules, painlist,diagnose_list = []):
    #manrules = manifestation_rules
    #painlist = ["do name like swelling", "attribute","value"]
    l = []
    if len(diagnose_list) == 0:
        for rule in manrules:
            # print rule, "-----", painlist
            if rule[2] == painlist[0] and rule[3] == painlist[1] and rule[4] == painlist[2] :
                l.append(rule[0])
    else:
        for rule in manrules:
            # print rule, "-----", painlist
            if rule[0] in diagnose_list:
                if rule[2] == painlist[0] and rule[3] == painlist[1] and rule[4] == painlist[2] :
                    l.append(rule[0])
    return l

dia = findDiagnoses(manifestation_rules,["pain", "location", "known"])
print dia


keepgoing = True
response = raw_input(" Vul in observable,attribute,value: \n")
plist = response.split(",")
dia = findDiagnoses(manifestation_rules,plist)
print dia
if len(dia)<=1:
    keepgoing = False

while keepgoing:
    if len(dia)>=1:
        response = raw_input(" Vul in observable,attribute,value: \n")
        plist = response.split(",")
        dia = findDiagnoses(manifestation_rules,plist,dia)
        print dia
        if len(dia)<=1:
            keepgoing = False

print "Diagnose: ", dia










# if dp_dict["sinusitis"].status == True:
#     do_pain.pain_bending_stairs = True
#     do_commoncold.status = True
#     do_pain.source = "multiple_teeth"
#     do_pain.location = "unkown"
#     do_swelling.status = False

# if dp_dict["pocket"].status == True:
#     do_pain.pain_bending_stairs = False

# print do_pain.set_duration
# print do_pain.set_duration == do_pain.set_duration