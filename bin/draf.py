def minFlipsMonoIncr(s: str) -> int:
        
        oneFreq, zeroFreq = 0, 0
        oneSeen, zeroSeen = 0, 0

        for i in range(len(s)):
            if s[i] == '1':
                oneFreq += 1
            if s[i] == '0':
                zeroFreq += 1
                
        minCost = zeroFreq
        for i in range(len(s)):
            if s[i] == '1':
                oneSeen += 1
            if s[i] == '0':
                zeroSeen += 1
            cost = (zeroFreq - zeroSeen) + oneSeen
            if cost < minCost:
                minCost = cost

        return minCost

print(minFlipsMonoIncr('0101100011'))