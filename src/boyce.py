class boyce(object):
    def bmMatch(self, pattern):
        #algoritma didapatkan dari slide pa munir
        last=[]
        last = self.buildLast(pattern)
        n = len(self.text)
        m = len(pattern)
        i = m-1
        if (i > n-1):
            return -1 #kalo ga ketemu file bersangkutan
        j = m-1;
        if (pattern[j] == self.text[i]):
                if (j == 0):
                    return i # match
                else: # looking-glass technique
                    i-=1
                    j-=1
        else: # character jump technique
            lo = last[ord(self.text[i])] 
            i = i + m - min(j, 1+lo)
            j = m - 1
        while (i <= n-1):
            if (pattern[j] == self.text[i]):
                if (j == 0):
                    return i # match
                else: # looking-glass technique
                    i-=1
                    j-=1
            else: # character jump technique
                lo = last[ord(self.text[i])]
                i = i + m - min(j, 1+lo)
                j = m - 1
        return -1 # no match
    def buildLast(self,pattern):
        last = [-1 for i in range(128)]
        for i in range(len(pattern)):
            last[ord(pattern[i])] = i
        return last
    def convertText(self,name_file):
        with open(name_file) as f:
            lines=f.read().lower()
            line=lines.split("\n")
            self.text=""
            for row in line:
                self.text+=row