

import csv

#This document only contains the classes


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
    def __init__(self,name="",alt_name="", description="",time=0):
        """"""
        self.name = name
        self.alt_name = alt_name #alternative names
        self.description = description #Some kind of description of the problem
        self.status = [True,False]
        self.time = time
    
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
            } 
            
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
