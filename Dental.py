
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
    def __init__(self, name, status=False):
        """"""
        self.status = [True,False]

    def changeStatus(self, s):
		self.status = s


class DentalObservable(object):
    """
    """
    def __init__(self):
        """"""


class Treatment(object):
    """
    """
    def __init__(self):
        """"""
        self.status = [True,False]
        self.time = range(5,95,5)

        
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
	"""
	"""
	pass


class ProblemGums(DentalProblem):
	"""
	"""
	pass


class ProblemOther(DentalProblem):
	"""
	"""
	pass



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
        # TODO: check pain symptom/sign diagram probably can remove symptom and sign and 
        # leave it at subjective and objective observables
        self.paintype = ["throbbing", "sharp"]
        self.onset = ["recent","chronic"]
        self.reaction_to_cold = ["increase","decrease","same"]
        self.reaction_to_heat = ["increase","decrease","same"]
        self.location = ["known","unknown"]
        self.source = ["particular_tooth","multiple_teeth","outside_teeth"]
        self.course = ["worsened_or_same", "reduced"]
        self.pain_bending_stairs = [True,False]
        self.duration = ["short","medium", "long"] # This might need some translation into measurable times


class ObservableSwelling(DentalObservable):
    """
    """
    def __init__(self):
    	""""""
    	self.status = [True,False]


class ObservableTooth(DentalObservable):
    """
    """
    def __init__(self):
    	""""""
        self.number = range(1,32)# number? What does this number refer to?
        self.recent_treatment_bump = [True,False]


class ObservableGums(DentalObservable):
    """
    """
    def __init__(self):
    	""""""
    	self.bleeding = [True,False]
    	self.colour = self.color = ["bright_red", "normal"]


class ObservableCommonCold(DentalObservable):
    """
    """
    def __init__(self):
    	""""""
    	self.status = [True,False]        