def A(msg,dna,i):
    if int(msg[i]) == 0:
        dna+="T"
        if len(dna) == len(msg) + 1:
            return (dna)
        i+=1
        T(msg,dna,i)
    elif int(msg[i]) == 1:		
        dna+="G"
        if len(dna) == len(msg) + 1:
            return (dna)
        i+=1
        G(msg,dna,i)
    elif int(msg[i]) == 2:
        dna+="C"
        if len(dna) == len(msg) + 1:
            return (dna)
        i+=1
        C(msg,dna,i)
################################################
def T(msg,dna,i):
    if int(msg[i]) == 0:
        dna+="A"
        if len(dna) == len(msg) + 1:
            return (dna)
        i+=1
        A(msg,dna,i)
    elif int(msg[i]) == 1:
        dna+="G"
        if len(dna) == len(msg) + 1:
            return (dna)
        i+=1
        G(msg,dna,i)
    elif int(msg[i]) == 2:
        dna+="C"
        if len(dna) == len(msg) + 1:
            return (dna)
        i+=1
        C(msg,dna,i)    
################################################
def G(msg,dna,i):
    if int(msg[i]) == 0:
        dna+="A"
        if len(dna) == len(msg) + 1:
            return (dna)
        i+=1
        A(msg,dna,i)
    elif int(msg[i]) == 1:
        dna+="T"
        if len(dna) == len(msg) + 1:
            return (dna)
        i+=1
        T(msg,dna,i)
    elif int(msg[i]) == 2:
        dna+="C"
        if len(dna) == len(msg) + 1:
            return (dna)
        i+=1
        C(msg,dna,i)
################################################
def C(msg,dna,i):
    if int(msg[i]) == 0:
        dna+="A"
        if len(dna) == len(msg) + 1:
            return (dna)
        i+=1
        A(msg,dna,i)
    elif int(msg[i]) == 1:
        dna+="T"
        if len(dna) == len(msg) + 1:
            return(dna)
        i+=1
        T(msg,dna,i)
    elif int(msg[i]) == 2:
        dna+="G"
        if len(dna) == len(msg) + 1:
            return (dna)
        i+=1
        G(msg,dna,i)







msg = input("Enter the message: ")
dna = ""
dna+="A"
A(msg,dna,0)
