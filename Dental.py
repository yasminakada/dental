
# TODO: Decide on a way to represent DS's, DP's etc. Most likely as an object.
# TODO: Store all types of DP's in some form (dict or list)
# TODO: Research method: How do we connect them? Some kind of semantics? 
#		Will we do this rule-based 
#		And write out all rules, or have some structure (graph or something) and
#		And have the code automatically find his way?
# TODO: interface python

# http://stackoverflow.com/questions/4901815/object-of-custom-type-as-dictionary-key


class DentalState(object):
    """
    """
    def __init__(self,name,status=false):
        """"""
        self.name = name
        self.status = status

    def changeStatus(self, s):
		self.status = s

class DentalProblem(object):
    """
    """
    def __init__(self, name, status=false):
        """"""
        self.name = name
        self.status = status

    def changeStatus(self, s):
		self.status = s

class DentalObservable(object):
    """
    """
    def __init__(self):
        """"""
        pass

class Treatment(object):
    """
    """
    def __init__(self):
        """"""
        pass
        
class DentalModel(object):
	"""
	"""
	def __init__(self):
		pass
