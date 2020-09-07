import json
nums = [4,5,6,7,3,14,15]
filename = 'nums.json'
with open (filename, 'w') as FFF:
    json.dump(nums, FFF)

file = 'nums.json'
with open (file) as F1:
    numbers_new = json.load(F1)
print(numbers_new)