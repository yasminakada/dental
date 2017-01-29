
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
        self.questdict = { \
            "paintype": [["throbbing", "sharp"], "Would you describe the pain as nagging/throbbing or sharp/stinging?"],\
            "jaw" : [["upper", "lower"], "Is the pain in the upper or lower jaw?"],\
            "onset": [["recent","chronic"], "When did you start experiencing this pain?"],\
            "reaction_to_cold" :[["increase","decrease","same"], "Does the pain decrease when consuming something cold?"],\
            "reaction_to_heat":[["increase","decrease","same"], "Does the pain decrease when consuming something cold?"],\
            "reaction_to_pressure": [["increase","decrease", "same"], "Does the pain decrease when there is pressure on it?"],\
            "location": [["known","unknown"], "Do you know which tooth or molar causes the pain?"],\
            "source": [["particular_tooth","multiple_teeth","outside_teeth"], "Do you feel like the pain comes from multiple teeth?"],\
            "course": [["worsened_or_same", "reduced"],"Has the pain changed from when you first experienced it?"],\
            "pain_bending_stairs":  [["TRUE","FALSE"], "Does the pain increase when bending or taking the stairs?"],\
            "duration": [["short","medium", "long"],"After the cold/hot/pressur stimulus, how long do you feel the pain?"] \
            } # This might need some translation into measurable times
            
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
        self.duration = [["short","medium", "long"], "After the cold/hot/pressur stimulus, how long do you feel the pain?"] # This might need some translation into measurable times
        

    def addAttributes(self, attrlist):
        # attrlist is a list of lists that consist of 2 element. example : [ [attribute, value] ]
        self.statusdict = {}
        for i in attrlist:
            if i[i] != "":
                self.statusdict[i[0]] = i[1]
            else:
                self.statusdict[i[0]] = None

    def getQuestion(self, attrstring):
        return self.questdict[attrstring]

    def __str__(self):
        return "<<DO-PAIN>>"

    def __repr__(self):
        return "<<DO-PAIN>>"

class ObservableSwelling(DentalObservable):
    """
    """
    def __init__(self):
    	""""""
        self.name ="swelling"
    	self.status = [[True,False],"Is there swelling also?"]

        self.questdict = { \
        "status": [["TRUE","FALSE"],"Is there swelling also?"]
        }

    def getQuestion(self, attrstring):
        return self.questdict[attrstring]

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
        self.recent_treatment_bump = [[True,False], "Recently, did you receive any dental treatments or perhaps bump it?" ]

        self.questdict = { \
        "recent_treatment_bump": [["TRUE","FALSE"], "Recently, did you receive any dental treatments or perhaps bump it?"]
        }

    def getQuestion(self, attrstring):
        return self.questdict[attrstring]

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
        
        self.questdict = { \
        "bleeding": [["TRUE","FALSE"], "When brushing or flossing your teeth, do your gums bleed?"]
        }

    def getQuestion(self, attrstring):
        return self.questdict[attrstring]

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

        self.questdict = { \
        "status": [["TRUE","FALSE"], "Do you have a cold or clogged sinuses, on the side of the pain? "]
        }
    def getQuestion(self, attrstring):
        return self.questdict[attrstring]

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

# with open('manifestation_rules.csv') as csvfile:
with open('mr2.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    manifestation_titles = readCSV.next()
    observable_att_list = []

    for row in readCSV:
        dp = DentalProblem(row[0],row[1],row[2])
        base = [dp, "manifestation"]
        for i in range(4,len(row)):
            # if len(row[i]) == 0: 
            #     continue # If there is no value, meaning no effect on this observable
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


def getAllDiagnoses(manrules):
    l=[]
    for rule in manrules:
        if rule[0] not in l:
            l.append(rule[0])
    return l

def findDiagnoses(manrules, painlist=[],diagnose_list = []):
    #manrules = manifestation_rules
    #painlist = ["do name like swelling", "attribute","value"]
    l = []
    possible = []

    print "Trying to shorten list...."
    for rule in manrules:
        dp = rule[0]
        if dp in diagnose_list: #Use list of diagnoses that were already found earlier
            if rule[2] == painlist[0] and rule[3] == painlist[1]:
                if rule[4] == painlist[2]:
                    print "--Exact match: ", dp
                    l.append(dp)
                elif rule[4]=="":
                    print "--Possible match: ", dp
                    possible.append(dp)
                else:
                    print "--Remove - not a match: ", dp
    if len(l) == 0:
        print " ****** NO EXACT MATCHES FOUND ******"
    l.extend(possible) # When a dp does not have a value, this problem is added to the end of the list as s possibility
    
    return l


def getQuestion(dp, askedlist,manrules):
    for rule in manifestation_rules:
        if rule[0] == dp:
            p = rule[2]
            a = rule[3]
            v = rule[4]
            if [p,a] not in askedlist and v!="":
                return [[p,a,v], do_dict[p].getQuestion(a)]
    return False,False

# askedlist =[]
# keepgoing = True
# response = raw_input(" Vul in observable,attribute,value: \n")
# plist = response.split(",")
# dia = findDiagnoses(manifestation_rules,plist)
# print dia
# if len(dia)<=1:
#     keepgoing = False

# while keepgoing:
#     if len(dia)>=1:
#         prompt = getQuestion()
#         response = raw_input(" Vul in observable,attribute,value: \n")
#         plist = response.split(",")
#         dia = findDiagnoses(manifestation_rules,plist,dia)
#         print dia
#         if len(dia)<=1:
#             keepgoing = False

# print "Diagnose: ", dia



askedlist =[]
keepgoing = True

dia = getAllDiagnoses(manifestation_rules)
print ""
print dia

while keepgoing:
    if len(dia)>=1:
        plist,prompt = getQuestion(dia[0], askedlist, manifestation_rules)
        if not plist or not prompt:
            print "Diagnose has been found, only one exact match?"
            keepgoing = False
            break

        possible_input = prompt[0] #Possible input is stored here
        q = prompt[1]

        print q
        for i in range(len(possible_input)):
            print i, " -> ", possible_input[i]
        response = input(">>> ")
        plist[2] = possible_input[response] # Change the p,a,v such that it fits the description given by patient
        askedlist.append(plist[0:2]) # Add pain, attribute to askedlist to not ask again
        print "Asked: ", askedlist
        dia = findDiagnoses(manifestation_rules,plist,dia)
        print ""
        print dia
        if len(dia)==0:
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