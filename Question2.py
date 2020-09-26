import pandas as pd
import sys
import mmap

def calculate_bp(s1, s2): 
    m = len(s1) 
    n = len(s2) 
    if abs(m - n) > 2: 
        return abs(m-n) 

    if s1 == s2: #check if barcodes are similar
        return 0

    if m==n: #if lenghts are same then split first 33 and last 17 and check on them

        if s1[-17:] != s2[-17:]: #check if last 17 characters are not similar
                                #if not then and if the difference is more than 2bp then return as unique    
            
            substr1 = s1[-17:]
            substr2 = s2[-17:]
            count = 0
            i = 0
            j = 0
            while i<17 and j<17 and count<3:
                if substr1[i] != substr2[j]:
                    i+=1
                    j+=1
                    count+=1
                else:
                    i+=1
                    j+=1
            if count > 2:
                return count #if last 17 are different by more than 2 then no need to check first 33 
                             #as they are unique

        else: #if last 17 are same then check first 33 characters
            count = 0
            i = 0
            j = 0
            while i < 33 and j < 33 and count < 3: 
                if s1[i] != s2[j]: 
                    i+=1
                    j+=1
                    count+=1
                else:    
                    i+=1
                    j+=1
            return count

    else : #if strings are not of same length then have to check for all characters as we don't know 
            # where the missing character is to be placed

        count = 0 # as one character is missing ot extra
        i = 0
        j = 0
        while i < m and j < n and count<3: 
            if s1[i] != s2[j]: 
                if m > n: 
                    i+=1
                elif m < n: 
                    j+=1
                else:
                    i+=1
                    j+=1
                count+=1
            else:    
                i+=1
                j+=1
        if i < m or j < n: 
            count+=1
  
    return count

checked = {}
unique = {}
file = open("./sample barcode data.txt")
barcodes = file.readlines()
for i in range(len(barcodes)):
    barcodes[i] = barcodes[i].strip('\n')
    checked[barcodes[i]] = 0
    
for i in range(len(barcodes)):
    if checked[barcodes[i]] == 0:
        count = 1
        for j in range(i+1, len(barcodes)):
            if checked[barcodes[j]] == 0:
                bp_count = calculate_bp(barcodes[i], barcodes[j])
                if bp_count < 3:
                    checked[barcodes[j]] = 1
                    count += 1
        unique[barcodes[i]] = count                 
print(unique)