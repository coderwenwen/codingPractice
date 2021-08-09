class ValidAnagram(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        keyValueSDict = {}
        indexS = 0
        lstS = list(s)
        while indexS < len(lstS):
            if lstS[indexS] not in keyValueSDict:
                keyValueSDict[lstS[indexS]] = 1
            else:
                keyValueSDict[lstS[indexS]] = keyValueSDict[lstS[indexS]] + 1
            indexS = indexS + 1

        indexT = 0
        lstT = list(t)
        keyValueTDict = {}
        while indexT < len(lstT):
            if lstT[indexT] not in keyValueTDict:
                keyValueTDict[lstT[indexT]] = 1
            else:
                keyValueTDict[lstT[indexT]] = keyValueTDict[lstT[indexT]] + 1
            indexT = indexT + 1

        if keyValueTDict == keyValueSDict:
            return True
        else:
            return False
