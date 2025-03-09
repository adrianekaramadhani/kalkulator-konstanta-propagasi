def convertResistor(res, satuan):
    if "G" in satuan:
        resist = res*10**9
        return resist
    elif "M" in satuan:
        resist = res*10**6
        return resist
    elif "k" in satuan:
        resist = res*10**3
        return resist 
    elif "m" in satuan:
        resist = res*10**-3
        return resist
    elif "u" in satuan:
        resist = res*10**-6
        return resist
    elif "n" in satuan:
        resist = res*10**-9
        return resist
    elif "p" in satuan:
        resist = res*10**-12
        return resist
    elif "" in satuan:
        resist = res
        return resist
    else:
        print("Masukkan satuan yang benar")    
    
def convertCapasitor(cap, satuan):
    if "G" in satuan:
        cap = cap*10**9
        return cap
    elif "M" in satuan:
        cap = cap*10**6
        return cap
    elif "k" in satuan:
        cap = cap*10**3
        return cap
    elif "m" in satuan: 
        cap = cap*10**-3
        return cap
    elif "u" in satuan:
        cap = cap*10**-6
        return cap
    elif "n" in satuan:
        cap = cap*10**-9
        return cap
    elif "p" in satuan:
        cap = cap*10**-12
        return cap
    elif "" in satuan:
        cap
        return cap
    else:
        print("Masukkan satuan yang benar")    

def convertInduktor(ind, satuan):
    if "G" in satuan:
        ind = ind*10**9
        return ind
    elif "M" in satuan:
        ind = ind*10**6
        return ind
    elif "k" in satuan:
        ind = ind*10**3
        return ind
    elif "m" in satuan:
        ind = ind*10**-3
        return ind
    elif "u" in satuan:
        ind = ind*10**-6
        return ind
    elif "n" in satuan:
        ind = ind*10**-9
        return ind
    elif "p" in satuan:
        ind = ind*10**-12
        return ind
    elif "" in satuan:
        ind
        return ind
    else:
        print("Masukkan satuan yang benar")    
        
def convertKonduktansi(kon, satuan):
    if "G" in satuan:
        kon = kon*10**9
        return kon
    elif "M" in satuan:
        kon = kon*10**6
        return kon
    elif "k" in satuan:
        kon = kon*10**3
        return kon
    elif "m" in satuan:
        kon = kon*10**-3
        return kon
    elif "u" in satuan:
        kon = kon*10**-6
        return kon
    elif "n" in satuan:
        kon = kon*10**-9
        return kon
    elif "p" in satuan:
        kon = kon*10**-12
        return kon
    elif "" in satuan:
        kon
        return kon
    else:
        print("Masukkan satuan yang benar")    
        
def convertFrekuensi(frek, satuan):
    if "G" in satuan:
        frek = frek*10**9
        return frek
    elif "M" in satuan:
        frek = frek*10**6
        return frek
    elif "k" in satuan:
        frek = frek*10**3
        return frek 
    elif "m" in satuan:
        frek = frek*10**-3
        return frek
    elif "u" in satuan:
        frek = frek*10**-6
        return frek
    elif "n" in satuan:
        frek = frek*10**-9
        return frek
    elif "p" in satuan:
        frek = frek*10**-12
        return frek
    elif "" in satuan:
        frek
        return frek
    else:
        print("Masukkan satuan yang benar")    
        
def convertKabel(kab, satuan):
    if "km" in satuan:
        kab = kab*10**3
        return kab
    elif "m" in satuan:
        kab 
        return kab 
    elif "cm" in satuan:
        kab = kab*10**-2
        return kab
    elif "mm" in satuan:
        kab = kab*10**-3
        return kab
    else:
        print("Masukkan satuan yang benar")    