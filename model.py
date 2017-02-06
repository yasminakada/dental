# Run this file in command line for a demo
from Dental import *


# Get all diagnoses from the manifestation rules.
def getAllDiagnoses(manrules):
    l=[]
    for rule in manrules:
        if rule[0] not in l:
            l.append(rule[0])
    return l

# Find diagnoses that fit the observable description given
# Order on exact matches then possible matches
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

# Look voor an observable attribute that is a manifestation of the DP (dental problem)
def getQuestion(dp, askedlist,manrules):
    for rule in manifestation_rules:
        if rule[0] == dp:
            p = rule[2]
            a = rule[3]
            v = rule[4]
            if [p,a,v] not in askedlist and v!="":
                return [[p,a,v], do_dict[p].getQuestion(a)]
    return False,False

# Ask about this observable attribute
def askQuestion(question):
    constrained_input = question[0]
    q = question[1]

    print q
    for i, item in enumerate(constrained_input):
        print "[ ", i," ]  ", item
    return 

# Retrieve the answer
def getAnswer(question):
	accepted = False
		while not accepted:
			try :
				response = input(">>>")
				if response < 1 or response > 0:
					accepted = True
			except :
				print "ONLY SINGLE DIGITS THAT ARE PRESENTED ARE ALLOWED "
	return question[0][response]

# Check the diagnoses left and ask next question
# When there are no conclusive questions to be asked, you get an exact match
# Meaning the probability of this problem is high
# Ask if you want to check other diagnoses when the list has more than 1 diagnosis still
def checkDiagnosis(diagnoses, askedlist, manifestation_rules):
    keepgoing = True
    print "++++ Specify ++++"
    counter = 0 # Count how many times no questions could be generated.
    if len(dia)>=1:
        for diagnose in diagnoses:
            print "++++ Check: ", diagnose, " ++++"
            dp = diagnose
            plist,question = getQuestion(dp, askedlist, manifestation_rules)
            if not plist or not question: #When no questions are left for this dp
                counter+=1
                print "The diagnose fits the description: ", dp
                if len(diagnoses) == 1:
                    print "There are no other diagnoses to cover"
                    keepgoing = False
                    break
                response = input("Do you want to check the remaining diagnoses? 0 or 1:  ")
                if not response:
                    print "Diagnoses are: ", diagnoses
                    print "Diagnoses to base appointment on: ", dp
                    keepgoing = False
                    break
                else: 
                    continue
            break
    if len(diagnoses) == counter: # All questions have been asked.
        print "There are no questions left. End of program."
        print "Diagnoses are: ", diagnoses 
        keepgoing = False
    
    return keepgoing,plist,question    

if __name__ == "__main__":

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


	"""
	-------------------------
	    Observables- DO's
	-------------------------
	"""
	do_dict = {} # Dental Observable
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
	with open('manifestation_rules.csv') as csvfile:
		readCSV = csv.reader(csvfile, delimiter=',')
		manifestation_titles = readCSV.next()
		observable_att_list = []

		for row in readCSV:
			dp = DentalProblem(row[0],row[1],row[2])
			dp_dict[row[0]] = dp
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



	"""
	=========================
	-------------------------
	INFERENCE DIAGNOSIS
	-------------------------
	=========================
	"""
	askedlist = [] # list of attributes that have been obtained and verified
	keepgoing = True
	"""
	-------------------------
	COVER
	-------------------------
	"""
	dia = getAllDiagnoses(manifestation_rules) # Use manifestation model to get the pain diagnoses

	print "========================== \n"
	print "========================== \n"
	print "ALL Diagnoses: ", dia


	"""
	-------------------------
	SELECT , 
	SPECIFY , 
	OBTAIN, 
	VERIFY
	loop
	-------------------------
	"""
	while keepgoing:
		print "========================== \n"
		print "========================== \n"
		if len(dia)>=1:
			keepgoing, plist,question = checkDiagnosis(dia,askedlist,manifestation_rules)

			if keepgoing:
				askQuestion(question)
				plist[2] = getAnswer(question)
				askedlist.append(plist)
				print askedlist

				dia = findDiagnoses(manifestation_rules,plist,dia)
				print ""
				print dia
				if len(dia) == 0:
					keepgoing = False
		else:
			print "There are no diagnoses found. Has to be determined by dentist."
			keepgoing = False

	"""
	=========================
	-------------------------
	INFERENCE PROCEDURE
	-------------------------
	=========================
	"""

	procedure_rules = []
	 # with open('manifestation_rules.csv') as csvfile:
	with open('treatment_rules.csv') as csvfile:
		readCSV = csv.reader(csvfile, delimiter=',')
		treatment_titles = readCSV.next()
 
		for row in readCSV:
			treatment = Treatment(row[0],row[1],row[2],row[3])
			dp = dp_dict[row[4]]
			treatment_dict[row[0]] = treatment
			rule = [treatment, "treats", dp]

			procedure_rules.append(rule)

	print ""
	print "---------------"
	print " TREATMENT AND TIME"
	print "---------------"
	for diagnosis in dia:
		print "Diagnosis: ", diagnosis.name, ":"
		for rule in procedure_rules:
			if diagnosis == rule[2]:
				t = rule[0]
				print "     ", t.name, "-->" , t.time

