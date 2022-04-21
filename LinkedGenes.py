def convertToNum(string):
    string = string.strip()
    num = float(string)
    return num


def linked():
    print("This function returns the recombination frequency of two genes on the same chromosome as a decimal.")
    
    nums = []
    num1 = convertToNum(input("How many of the first phenotype are there? Input a number. "))
    nums.append(num1)
    num2 = convertToNum(input("How many of the second phenotype are there? Input a number. "))
    nums.append(num2)
    num3 = convertToNum(input("How many of the third phenotype are there? Input a number. "))
    nums.append(num3)
    num4 = convertToNum(input("How many of the fourth phenotype are there? Input a number. "))
    nums.append(num4)
    
    phenotypes = ["Phenotype 1", "Phenotype 2", "Phenotype 3", "Phenotype 4"]
    
    total = 0
    for i in nums:
        total += i
        
    small = []
    smallest = nums[0]
    for i in nums:
        if i < smallest:
            smallest = i
    small.append(smallest)
    nums.remove(smallest)
    
    smallest = nums[0]
    for i in nums:
        if i < smallest:
            smallest = i
    small.append(smallest)
    
    recombinants = 0
    for i in small:
        recombinants += i
    
    recombFreq = recombinants/total
    recombPerc = recombFreq * 100
    recombText = str(recombFreq) + "%"
    print("There is a", recombText, "recombination chance")
    
    return(recombFreq)
            

    
    
linked()
    
