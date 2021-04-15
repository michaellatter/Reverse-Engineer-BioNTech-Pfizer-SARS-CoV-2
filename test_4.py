dictionary={
        'key_1' : ["blue","brown"],
        "key_2" : ["river","stream","forest"]
        }

## DICTIONARY UPDATER - COMPARES TWO DICTIONARYS, UPDATES THE FIRST , USEFUL FOR CHANGING DEFAULT DICTIONARYS
    #I did this to make a new dictionary that had all the codons for each amino acid listed
key="key_3"
value="circular"
if key in dictionary:                               #is this key in the dictionary?
    existing_values=dictionary[key]                 #check what value are mapped to that key
    dictionary[key]=existing_values,value           #update this key with the new value
else:
    dictionary[key]=value                           #create new key and value

## BEST CODON SELECTOR - FINDS VALUES, THEN SELECTS THE BEST ONE BASED ON A CONDITION (c OR g COUNT)

#INPUT CODON, CONVERT TO AMINO

#SPECIFY AMINO AS KEY
keys=["key_1"]                       #keys that need best value selected , list

#finds values in the dictionary that match
temp_count_dict={}
for i in keys:
    match=dictionary[i]      # "blue","brown","red"


keys[]=key_1
match=dictionary[keys]
#Create count dic - map character counts to matching codons
for i in match:
    count=i.count('b')+i.count('u')
    if i not in temp_count_dict:        #if avoids double ups
        temp_count_dict[i]=count        #key=count , value=codon

#find value from key function
def getKeysByValue(dictOfElements, valueToFind):
    listOfKeys = list()
    listOfItems = dictOfElements.items()
    for item  in listOfItems:
        if item[1] == valueToFind:
            listOfKeys.append(item[0])
    return  listOfKeys

#select codon with highest character count
all_values = temp_count_dict.values()   #converts values to string
max_value = max(all_values)
best_codons=getKeysByValue(temp_count_dict,max_value)           #finds max value in string

print(best_codons)

#run along codon sequence, extract codon, is same as optimised? Yes, continue, No?, replace
                                          #convert current program to input codons
