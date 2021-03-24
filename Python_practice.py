#counties = ["Arapahoe","Denver","Jefferson"]

#Check if El Paso is in counties list
#if "El Paso" in counties:
#    print("El Paso is in the list of counties.")
#else:
#    print("El Paso is not the list of counties.")

#Check if Arapahoe AND El Paso is in counties list
#if "Arapahoe" in counties and "El Paso" in counties:
#    print("Arapahoe and El Paso are in the list of counties.")
#else:
#    print("Arapahoe or El Paso is not in the list of counties.")

#Check if Arapahoe or El Paso is in counties list
#if "Arapahoe" in counties or "El Paso" in counties:
#    print("Arapahoe or El Paso is in the list of counties.")
#else:
#    print("Arapahoe and El Paso are not in the list of counties.")

#if "Arapahoe" in counties and "El Paso" not in counties:
#   print("Only Arapahoe is in the list of counties.")
#else:
#    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

### Repitition statements: https://courses.bootcampspot.com/courses/558/pages/3-dot-2-10-repetition-statements?module_item_id=159210

#Prints counties list by for looping through each part of list and printing
#for county in counties:
#    print(county)

#Prints counties list by finding length of counties list and looping through until length is reached
#for i in range(len(counties)):
#    print(counties[i])
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

#All counties in dictionary counties print to screen
#for county in counties_dict:
#   print(county)


#Print counties from dictonary using keys method
#for county in counties_dict.keys():
 #   print(county)

#Print voter count values using values method
#for voters in counties_dict.values():
#    print(voters)

#Print voter counts values of counties using key value method

#for county in counties_dict:
 #   print(counties_dict[county])

#Print counties using "get" method for values
#for county in counties_dict:
#    print(counties_dict.get(county))


#Print key-value pairs for given dictionary
#for key, value in dictionary_name.items():
#    print(key, value)

#Python autoassigns key and value base on dictionary definition
#for county, voters in counties_dict.items():
#   print(county, voters)

#Skill Drill output key(county) and value(voters) formatted
#for county, voters in counties_dict.items():
#    print(county + " county has " + str(voters) + " registered voters.")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

#for county_dict in voting_data:
#    print(county_dict)


#****https://stackoverflow.com/questions/35864007/python-3-5-iterate-through-a-list-of-dictionaries answer!
#for i in range(len(voting_data)):

#     print(voting_data[i]["county"])


#Print all values of each dictionary
#for county_dict in voting_data:
#    for value in county_dict.values():
#        print(value)

#Print registered voter values from dictionaries
#for county_dict in voting_data:

 #    print(county_dict['registered_voters'])

#Print county names values from dictionaries
#for county_dict in voting_data:
 #   print(county_dict['county'])

 #Retrieve only values from voting_data list using values() method with variable county_dict
#for county_dict in voting_data:
#    for value in county_dict.values():
#        print(value)

#Retrieve number of registered voters from each dictionary
for county_dict in voting_data:

     print(county_dict['registered_voters'])

#retrieve counties from each dictionary in voting_data
for county_dict in voting_data:
    print(county_dict['county'])