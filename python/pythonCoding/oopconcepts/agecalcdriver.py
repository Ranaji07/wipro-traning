from oopconcepts.agecalc import AgeCalcuation
from oopconcepts.myexception import AgeMyException

age = int(input('Age: '))

aobj = AgeCalcuation()
try:
    if aobj.voting_age_check(age):
        print('Eligible. Contact next step...')
except AgeMyException as ae:
    print(ae)