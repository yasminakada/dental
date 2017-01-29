
from Dental import *


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
	dp_dict[i] = ProblemTooth(i)

#Create DP's and put them in the dictionary
for i in dp_names_gums:
	dp_dict[i] = ProblemGums(i)

for i in dp_names_other:
	dp_dict[i] = ProblemOther(i)
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

"""
-------------------------
	Treatment - T's
-------------------------
"""
treatment_dict = {} # Treatment dictionary

t_names = ["drain", "further examination", "nasal drops or anibiotics", \
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

if dp_dict_other["sinusitus"].status == True:
	pain.be
