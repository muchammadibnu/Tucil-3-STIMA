class kmp(object):
    def kmpMatch(self, pattern):
        #algoritma didapatkan dari slide pa munir
        n=0
        m=0
        n = len(self.text)
        m = len(pattern)
        fail = []
        fail = self.computeFail(pattern);
        i=0
        j=0
        while (i < n):
            if (pattern[j] == self.text[i]):
                if (j == m - 1):
                    return i - m + 1
                i+=1
                j+=1
            elif(j > 0):
                j = fail[j-1]
            else:
                i+=1
        return -1 
    def computeFail(self,pattern):
        fail = [0 for i in range(len(pattern))]
        fail[0] = 0
        m = len(pattern)
        j = 0
        i = 1
        while (i < m):
            if (pattern[j] == pattern[i]):  
                fail[i] = j + 1;
                i+=1
                j+=1
            elif (j > 0):
                j = fail[j-1]
            else:
                fail[i] = 0;
                i+=1
        return fail
    def convertText(self,name_file):
        with open(name_file) as f:
            lines=f.read().lower()
            line=lines.split("\n")
            self.text=""
            for row in line:
                self.text+=row