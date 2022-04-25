from tabulate import tabulate
import itertools

def alleles(gene):
    alleleList = []
    text = "Please name all alleles for "+ gene
    print(text)
    alleles = input("")
    print("\n")
    alleles = alleles.split(" ")
    for allele in alleles:
        allele = allele.strip()
        alleleList.append(allele)

    return alleleList


def alleleDictionary():
    
    geneAlleleDictionary = {}
    
    numGenes = input("How many genes are being studied? Please input an integer. ")
    numGenes = numGenes.strip()
    numGenes = int(numGenes)
    
    print("\n")
    print("Please input the possible genes in order of decreasing priority, seperated by spaces. \nE.g., Ia Ib i\n")
    for i in range(numGenes):
        geneNumber = "gene " + str(i + 1)
        alleleList = alleles(geneNumber)
        
        geneAlleleDictionary[geneNumber] = alleleList
        
    return geneAlleleDictionary


def genotype(alleles, parent, allele1, allele2):
     for term in alleles:
         if allele1 == term:
             parent = parent + allele1 + "-" + allele2 + "/"
             return parent
         if allele2 == term:
             parent = parent + allele2 + "-" + allele1 + "/"
             return parent
            
            
    
def parents(d):
    mom = ""
    i = 0
    for key in d:
        i += 1
        geneName = "gene " + str(i)
        text = "Please input parent 1's two alleles for " + geneName + " seperated by a space."
        alleles = input(text)
        alleles = alleles.split(" ")
        allele1 = alleles[0]
        allele1 = allele1.strip()
        allele2 = alleles[1]   
        allele2 = allele2.strip()
    
        alleles = d[geneName]
        
        mom = genotype(alleles, mom, allele1, allele2)
        
    print("\n")
    dad = ""
    i = 0
    for key in d:
        i += 1
        geneName = "gene " + str(i)
        text = "Please input parent 2's two alleles for " + geneName + " seperated by a space."
        alleles = input(text)
        alleles = alleles.split(" ")
        allele1 = alleles[0]
        allele1 = allele1.strip()
        allele2 = alleles[1]   
        allele2 = allele2.strip()
    
        alleles = d[geneName]
        
        dad = genotype(alleles, dad, allele1, allele2)
        
    cross = ""
    cross = mom + "|" + dad 
                    
    return cross

def reorganize(string, dictionary):
    string = string.split(" ")
    length = 0
    for i in string:
        length += 1

    genotype = ""
    number = 1
    number2 = 0
    allelesAdded = 0
    
    while allelesAdded < length:
       gene = "gene " + str(number)
       alleleCheck = dictionary[gene][number2]
       if alleleCheck in string:
           genotype += alleleCheck
           allelesAdded += 1
           string.remove(alleleCheck)
           
           if alleleCheck in string:
               genotype += alleleCheck
               allelesAdded += 1
               string.remove(alleleCheck)
             
       if allelesAdded >= 1: 
           if allelesAdded % 2 == 0:
               if genotype[-1] != " ":
                   genotype += " "
          
       if number2 < len(dictionary[gene]):
           number2 += 1
       if number2 == len(dictionary[gene]):
           number += 1
           number2 = 0

    return genotype
           
       

    
            
        
    

def punnett(cross, d):
    punnett = {}
    cross = cross.split("|")
    newCross = []
    for term in cross:
        term = term[0:-1]
        newCross.append(term)
    
    mom = newCross[0]
    dad = newCross[1]
    
    mom = mom.split("/")
    dad = dad.split("/")
    
    dadAlleles = []
    for term in dad:
        term = term.split("-")
        dadAlleles.append(term)
    
    dadGametes = []
    for list in itertools.product(*dadAlleles):
        gamete = ""
        for i in range(len(list)):
            gamete += list[i]
            if i < len(list)-1:
                gamete += " "
                
        #dadGametes.append(gamete)
        if gamete in dadGametes:
            #print(gamete)
            pass
        else:
            dadGametes.append(gamete)
            #print(gamete)
    
    momAlleles = []
    for term in mom:
        term = term.split("-")
        momAlleles.append(term)
        
    momGametes = []
    for list in itertools.product(*momAlleles):
        gamete = ""
        for i in range(len(list)):
            gamete += list[i]
            if i < len(list)-1:
                gamete += " "
        momGametes.append(gamete)
        
        
        punnett = {}
        punnett[""] = dadGametes
        
    #print(momGametes, dadGametes)
    
    allOffspring = []
    counter = 0
    for i in range(len(momGametes)):
        tempList = []
        momHeader = momGametes[counter]
        for gamete in dadGametes:
            child = momHeader + " " + gamete
            child = reorganize(child, d)
            tempList.append(child)
            allOffspring.append(child)
        punnett[momHeader] = tempList
        counter += 1
        
    square = tabulate(punnett, headers = "keys", tablefmt = "fancy_grid")
    print(square)
    
    ratios = {}
    for genotype in allOffspring:
        if genotype not in ratios:
            ratios[genotype] = 1
        else:
            ratios[genotype] += 1
            
    return ratios
           

def automaticPunnett():
    dictionary = alleleDictionary()
    cross = parents(dictionary)  
    punnett(cross, dictionary)


automaticPunnett()