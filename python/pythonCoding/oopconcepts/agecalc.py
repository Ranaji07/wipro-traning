from oopconcepts.myexception import AgeMyException


class AgeCalcuation():
   def voting_age_check(self, age):
      if age < 18:
         raise AgeMyException('Not Eligible to vote...')
      else:
           return True
