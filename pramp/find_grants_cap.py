'''
The awards committee of your alma mater (i.e. your college/university) asked for your assistance with a budget allocation problem they’re facing. Originally, the committee planned to give N research grants this year. However, due to spending cutbacks, the budget was reduced to newBudget dollars and now they need to reallocate the grants. The committee made a decision that they’d like to impact as few grant recipients as possible by applying a maximum cap on all grants. Every grant initially planned to be higher than cap will now be exactly cap dollars. Grants less or equal to cap, obviously, won’t be impacted.

Given an array grantsArray of the original grants and the reduced budget newBudget, write a function findGrantsCap that finds in the most efficient manner a cap such that the least number of recipients is impacted and that the new budget constraint is met (i.e. sum of the N reallocated grants equals to newBudget).

Example:
input:  grantsArray = [2, 100, 50, 120, 1000], newBudget = 190
output: 47
'''
def find_grants_cap(grantsArray, newBudget):
  grantsArray.sort(reverse = True)
  currentBudget = sum(grantsArray)
  previousCap = 0
  N = len(grantsArray)
  for i in range (N):
    currentCap = grantsArray[i]
    currentBudget = currentBudget - previousCap*i + currentCap*i
    if currentBudget <= newBudget:
      cap = float(newBudget - (currentBudget - currentCap*i))/i
      return cap
    previousCap = currentCap
  return float(newBudget)/N

grantsArray = [2, 100, 50, 120, 1000]
newBudget = 190
print find_grants_cap(grantsArray, newBudget)