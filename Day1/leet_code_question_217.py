# Return true when there is a duplicate and return false when there is not 

class Solution(object):
    def containsDuplicate(self, nums):
        hashset = set() # EMPTY HASHSET

        # COMPARING THE CURRENT NUMBER WITH HASHSET VALUES, AND RETURN ACCORDING TO THAT
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False