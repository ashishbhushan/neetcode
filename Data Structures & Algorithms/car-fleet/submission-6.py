class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        dictpos = {}
        n = len(position)
        for pos in range(n):
            dictpos[position[pos]] = speed[pos]
        
        stack = []
        sortedpos = sorted(position)
        i = n-2
        initime = (target - sortedpos[-1])/dictpos[sortedpos[-1]]
        stack.append(initime)

        print(stack)

        while i>=0:
            print(i)
            currspeed = dictpos[sortedpos[i]]
            currtime  = (target-sortedpos[i])/currspeed
            
            if currtime>stack[-1]:
                stack.append(currtime)
            
            i-=1

        return len(stack)