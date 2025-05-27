class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        #keeps the highest altitude recorded
        highest = 0
        #keeps track of the current altitude, starts at 0 from problem
        current = 0
        #loops though all the values
        for i in range(len(gain)):
            #add the index its currenly from gain array to current
            current += gain[i]
            #if the current altiltude is greater then highest, record it
            if current > highest:
                highest = current
                
        return highest
