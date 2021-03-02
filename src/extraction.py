import kmp
import boyce
import regex
class extraction(object):
    def __init__(self,uploaded_files, text, option):
        if(option=="pilihan1"):
            kmp_0=kmp.kmp()
            kmp_0.convertText(uploaded_files)
            if(kmp_0.kmpMatch(text.lower())==-1):
                self.hasil=[['',"Tidak ditemukan "+ text + " pada file." ,'']]
            else:
                self.hasil=[['',"indeks pada file: "+str(kmp_0.kmpMatch(text.lower())),'']]
        elif(option=="pilihan2"):
            boyer=boyce.boyce()
            boyer.convertText(uploaded_files)
            if(boyer.bmMatch(text.lower())==-1):
                self.hasil=[['',"Tidak ditemukan "+ text + " pada file." ,'']]
            else:
                self.hasil=[['',"indeks pada file: "+str(boyer.bmMatch(text.lower())),'']]
        else:
            reg=regex.regex(uploaded_files)
            self.hasil=reg.regexMatch(text)
    def getHasil(self):
        return self.hasil