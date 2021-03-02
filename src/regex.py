import re
import copy
class regex(object):
    def __init__(self,name_file):
        with open(name_file, errors='ignore') as f:
            lines=f.read()
            line=lines.split("\n")
            self.realText=[]
            self.text=[]
            texts=""
            for row in line:
                for sentence in row.split(". "):
                    self.realText.append(sentence)
            line=lines.lower()
            line=line.split("\n")
            for row in line:
                texts+=row
                for sentence in row.split(". "):
                    self.text.append(sentence)
            k=0
            while(k<len(self.text)):
                if(self.text[k]==''):
                    del self.text[k]
                else:
                    k+=1
            k=0
            while(k<len(self.realText)):
                if(self.realText[k]==''):
                    del self.realText[k]
                else:
                    k+=1
            print(self.text)
            print(self.realText)
            self.base_of_date="Tidak ditemukan"
            self.getDate()
            self.getDigit()
            self.getBaseOfDate()
            self.getIndexOfDate()
            self.getIndexOfDigit()
            # Hapus bila ada jumlah yang ada pada tanggal misal "11" ada pada 11 januari 2020 maka 11 hapus dari list
            for i,row in enumerate(self.list_of_date):
                if(row!=[]):
                    for rows in row:
                        k=0
                        while(k<len(self.list_of_digit[i])):
                            if(self.list_of_digit[i][k] in rows):
                                del self.list_of_digit[i][k]
                                del self.index_of_digit[i][k]
                            else:
                                k+=1
            # Hapus digit yang ada "-" didepannya
            for i,row in enumerate(self.list_of_digit):
                if(row!=[]):
                    k=0
                    while(k<len(self.list_of_digit[i])):
                        if("-"+self.list_of_digit[i][k] in self.text[i]):
                            del self.list_of_digit[i][k]
                            del self.index_of_digit[i][k]
                        else:
                            k+=1
            print(self.list_of_date)
            print(self.list_of_digit)
    def getBaseOfDate(self):
        for date in self.list_of_date:
            if(date!=[]):
                self.base_of_date=date[0][0]
                return;
    def getDate(self):
        re_1=r'(?:senin|selasa|rabu|kamis|jumat|sabtu|minggu)[\s,]{1,2}.\d{1,2}/\d{1,2}/\d{1,4}.\spukul\s\d{1,2}.\d{1,2}\s[a-z]{3,4}'
        re_2='(?:senin|selasa|rabu|kamis|jumat|sabtu|minggu)[\s,]{1,2}\d{1,2}\s[a-z]{3}\s\d{1,4}\s\d{1,2}.\d{1,2}\s[a-z]{3,4}'
        re_3='[(]{0,1}\d{1,2}/\d{1,2}/\d{1,4}[,)]{0,1}\s\d{1,2}.\d{1,2}\s[a-z]{3,4}'
        re_4='(?:senin|selasa|rabu|kamis|jumat|sabtu|minggu)\s[(]{1}\d{1,2}/\d{1,2}/\d{1,4}[)]{1}'
        re_5='[a-z]{3}[.\s]{1,2}[a-z]{3}\s\d{1,2}\s\d{5,6}.\d{2}\s[a-z]{2}'
        re_6='\d{1,2}.\d{2}\s(AM|PM)'
        re_7='[(]{0,1}\d{1,2}/\d{1,2}/\d{1,4}[)]{0,1}'
        re_8='[\d]{1,2} [adfjmnos]\w* [\d]{4}}'

        '''format re_i
        re_1:Sabtu (11/4/2020) pukul 18.43 WIB
        re_2:Sabtu, 11 Apr 2020 20:07 WIB
        re_3:20/04/2020, 10:00 WIB
        re_4:Sabtu (19/4/2020)
        re_5:Sat, Apr 11 20209:06 PM
        re_6:6:20 PM
        re_7:(19/4/2020)
        re_8: 20 April 2020
        '''
        self.list_of_date=[]
        for text in self.text:
            self.list_of_date.append(re.compile("(%s|%s|%s|%s|%s|%s|%s|%s)" % (re_1,re_2,re_3,re_4,re_5,re_6,re_7,re_8)).findall(text))
    
    def getDigit(self):
        self.list_of_digit=[]
        for row in self.text:
            #digit=re.findall(r'\s\d{1,}\s',row)
            #for digits in digit:    
            self.list_of_digit.append(re.findall(r'\d{1,}',row))
    
    def getIndexOfDate(self):
        re_1=r'(?:senin|selasa|rabu|kamis|jumat|sabtu|minggu)[\s,]{1,2}.\d{1,2}/\d{1,2}/\d{1,4}.\spukul\s\d{1,2}.\d{1,2}\s[a-z]{3,4}'
        re_2='(?:senin|selasa|rabu|kamis|jumat|sabtu|minggu)[\s,]{1,2}\d{1,2}\s[a-z]{3}\s\d{1,4}\s\d{1,2}.\d{1,2}\s[a-z]{3,4}'
        re_3='[(]{0,1}\d{1,2}/\d{1,2}/\d{1,4}[,)]{0,1}\s\d{1,2}.\d{1,2}\s[a-z]{3,4}'
        re_4='(?:senin|selasa|rabu|kamis|jumat|sabtu|minggu)\s[(]{1}\d{1,2}/\d{1,2}/\d{1,4}[)]{1}'
        re_5='[a-z]{3}[.\s]{1,2}[a-z]{3}\s\d{1,2}\s\d{5,6}.\d{2}\s[a-z]{2}'
        re_6='\d{1,2}.\d{2}\s(AM|PM)'
        re_7='[(]{0,1}\d{1,2}/\d{1,2}/\d{1,4}[)]{0,1}'
        re_8='[\d]{1,2} [adfjmnos]\w* [\d]{4}}'

        '''format re_i
        re_1:Sabtu (11/4/2020) pukul 18.43 WIB
        re_2:Sabtu, 11 Apr 2020 20:07 WIB
        re_3:20/04/2020, 10:00 WIB
        re_4:Sabtu (19/4/2020)
        re_5:Sat, Apr 11 20209:06 PM
        re_6:6:20 PM
        re_7:(19/4/2020)
        re_8: 20 April 2020
        '''
        self.index_of_date=[]
        p = re.compile("(%s|%s|%s|%s|%s|%s|%s|%s)" % (re_1,re_2,re_3,re_4,re_5,re_6,re_7,re_8))
        for row in self.text:
            index=[]
            for m in p.finditer(row):
                index.append(m.start())
            self.index_of_date.append(index)
            del index
    
    def getIndexOfDigit(self):
        self.index_of_digit=[]
        p = re.compile(r'\d{1,}')
        for row in self.text:
            index=[]
            for m in p.finditer(row):
                index.append(m.start())
            self.index_of_digit.append(index)
            del index        

    def getRealDigit(self,keyword_index,idx):
        index=keyword_index
        min=2**(32)
        minIndex=0
        for i,digit in enumerate(self.index_of_digit[idx]):
            if(abs(digit-index)<min):
                min=abs(digit-index)
                minIndex=i
        return self.list_of_digit[idx][minIndex]
    
    def getRealDate(self,keyword_index,idx):
        index=keyword_index
        min=2**(32)
        minIndex=0
        for i,digit in enumerate(self.index_of_date[idx]):
            if(abs(digit-index)<min):
                min=abs(digit-index)
                minIndex=i
        return self.list_of_date[idx][minIndex]

    def checkData(self,data):
        for datas in data:
            if(datas!=[]):
                return True

    def regexMatch(self,pattern):
        #Untuk menampung hasil findall dari pattern pada text
        keyword=[]
        for row in self.text:
            keyword.append(re.findall(pattern.lower(),row))
        #sebagai indeks dari keyword_index(bila dalam satu kalimat terdapat lebih dari 1 keyword)
        list_of_hasil=[]
        if(self.checkData(keyword)):
            for i in range(len(keyword)):
                if(keyword[i]!=[]):
                    keyword_index=[]
                    hasil=[]
                    p = re.compile(pattern.lower())
                    for m in p.finditer(self.text[i]):
                        keyword_index.append(m.start())
                    for keyword_idx in keyword_index:
                        #cari waktu
                        if(self.list_of_date[i]==[]):
                            hasil.append("Waktu: "+str(self.base_of_date))
                            print(self.base_of_date)
                        else:
                            hasil.append("Waktu: "+str(self.getRealDate(keyword_idx,i)[0]))
                            print(self.getRealDate(keyword_idx,i))
                        #cari banyak korban
                        if(self.list_of_digit[i]==[]):  
                            hasil.append("Jumlah: 0")
                        else:
                            hasil.append("Jumlah: "+str(self.getRealDigit(keyword_idx,i)))
                        hasil.append("Kalimat: "+ self.realText[i])
                        list_of_hasil.append(hasil)
        else:
            list_of_hasil=[["Waktu: -","Jumlah: -","Tidak ditemukan kalimat yang mengandung "+pattern+"."]]
        return list_of_hasil