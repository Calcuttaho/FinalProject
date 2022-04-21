import numpy
from tabulate import tabulate
from scipy import stats
from scipy.stats import chisquare


def chiSquaredAdv():
    
    table = {}
    numPhen = input("How many phenotypes are being studied? ")
    numPhen = numPhen.strip()
    numPhen = numPhen.strip(" .,?")
    numPhen = int(numPhen)
    
    name = []
    for i in range(numPhen):
        text = "What is phenotype " + str(i + 1) + "? "
        phenotype = input(text)
        name.append(phenotype)
    table[""] = name
    
    obs = []
    for i in name:
        text = "What is " + i + "'s observed value? Please input a number. "
        result = input(text)
        result = result.strip()
        observed = float(result)
        obs.append(observed)
    table["O"] = obs
    
    sampleSize = 0
    for i in obs:
        sampleSize += i
        
    exp = []
    for i in range(len(obs)):
        text = "Please input the ratio of offspring expected for " + name[i] + " as a fraction "
        ratio = input(text)
        ratio = ratio.strip()
        x = ratio.split("/")
        numer = x[0]
        numer = float(numer)
        denom = x[1]
        denom = float(denom)
        percent = numer/denom
        
        expected = sampleSize * percent
        exp.append(expected)
    table["E"] = exp
    
    expTotal = 0
    for i in exp:
        expTotal += i
    
    percentError = sampleSize / 20
    offset = expTotal - sampleSize
    if offset < 0:
        offset = offset * -1
        
    if offset > percentError:
        print("There is a greater than 5% difference between your sample size and your expected total. This likely indicates that your ratios do not add up to one. Would you like to restart, or to continue? \n")
        crash = input("Please input Y/YES to restart, or anything else to continue ")
        crash = crash.lower()
        crash = crash.strip()
        if crash == "y" or crash == "yes":
            return "restart"
    
    dif = []
    for i in range(len(obs)):
        difference = exp[i] - obs[i]
        if difference < 0:
            difference = difference * -1
        dif.append(difference)
    table["D"] = dif
    
    difSquared = []
    for i in dif:
        dif2 = i ** 2
        difSquared.append(dif2)
    table["D^2"] = difSquared
    
    Chi = []
    for i in range(len(difSquared)):
        chiVal = difSquared[i] / exp[i]
        Chi.append(chiVal)
    table["D^2/E"] = Chi
    
    chiSquared = 0
    for i in Chi:
        chiSquared += i
        
    pValue = input("Please input the P value used to determine significance as a decimal. ")
    pValue = float(pValue)
        
    
    p = chisquare(obs, exp) #https://github.com/scipy/scipy/blob/v1.8.0/scipy/stats/_stats_py.py#L6787-L6912
    p = str(p)
    p = p.split(",")
    p = p[1]
    p = p.split("=")
    p = p[1]
    p = p.strip(")")
    p = float(p)
    
    for i in range(3):
        print("\n")
    tabulateTable = tabulate(table, headers="keys", tablefmt = "fancy_grid")
    print(tabulateTable, "\n")
    
    print("χ² =", chiSquared, "\n")
    print("p =", p, "\n")
    
    if pValue > p:
        print("These results are statistically significant. There is enough evidence to reject the null hypothesis ")
        return True
    else:
        print("These results are not statistically significant. There is not enough evidence to reject the null hypothesis. ")
        return False
    

        
    
        
def chiSquaredCycle():
    crash = chiSquaredAdv()
    if crash == "restart":
        done = False
        while done == False:
            crash = chiSquaredAdv()
            if crash != "restart":
                done == True  
                
    return crash
