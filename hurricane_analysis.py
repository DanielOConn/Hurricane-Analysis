# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:

def damages_cleaner(list):
    cleaned_damages = []
    for item in list:
        if item == 'Damages not recorded':
            cleaned_damages.append(item)
        elif item[-1] == "M":
            A = item.strip("M")
            AA = float(A)
            AAA = AA * 1000000
            cleaned_damages.append(AAA)
        elif item[-1] == "B":
            B = item.strip("B")
            BB = float(B)
            BBB = BB * 1000000000
            cleaned_damages.append(BBB)
    return cleaned_damages

#print(damages_cleaner(damages))

master_dict = {}

for i in range(len(names)):
    master_dict[names[i]] = {"Name": names[i], "Month": months[i], "Year": years[i], "Max Sustained Wind": max_sustained_winds[i], "Areas Affected": areas_affected[i], "Damage": damages[i], "Death": deaths[i]}

#print(master_dict)

year_dict = {}

for key,value in master_dict.items():
    current_year = value["Year"]
    if value["Year"] not in year_dict:
        year_dict[current_year] = []
        year_dict[current_year].append(value)
    else:
        year_dict[current_year].append(value)

#print(year_dict)
times_affected = {}
for area_list in areas_affected:
    for area in area_list:
        if area not in times_affected:
            times_affected[area] = 0
            times_affected[area] += 1
        else:
            times_affected[area] += 1

#print(times_affected)

max_area = "Central America"
max_area_count = 0

for place,counter in times_affected.items():
    if counter > max_area_count:
        max_area_count = counter
        max_area = place
    else:
        continue

#print(max_area)
#print(max_area_count)

max_deaths_hur = "place"
max_deaths_hur_count = 0

for num in range(len(names)):
    if deaths[num] > max_deaths_hur_count:
        max_deaths_hur_count = deaths[num]
        max_deaths_hur = names[num]
    else:
        continue

#print(max_deaths_hur)
#print(max_deaths_hur_count)

mortality_scale = {0: 0, 1: 100, 2: 500, 3: 1000, 4:10000}

mortality_scale_list = []

for a in deaths:
    if a == 0:
        mortality_scale_list.append(0)
    elif 0 < a <= 100:
        mortality_scale_list.append(1)
    elif 100 < a <=500:
        mortality_scale_list.append(2)
    elif 500 < a <= 1000:
        mortality_scale_list.append(3)
    elif 1000 < a <=10000:
        mortality_scale_list.append(4)

#print(mortality_scale_list)
zero_list = []
one_list = []
two_list = []
three_list = []
four_list = []

for b in range(len(mortality_scale_list)):
    if mortality_scale_list[b] == 0:
        zero_list.append(names[b])
    elif mortality_scale_list[b] == 1:
        one_list.append(names[b])
    elif mortality_scale_list[b] == 2:
        two_list.append(names[b])
    elif mortality_scale_list[b] == 3:
        three_list.append(names[b])
    elif mortality_scale_list[b] == 4:
        four_list.append(names[b])

scales_dict = {0:zero_list, 1:one_list, 2:two_list, 3:three_list, 4:four_list}

#print(scales_dict)
dam_list = (damages_cleaner(damages))

highest_damage_place = "the place"
highest_damage_count = 0.0

for d in range(len(dam_list)):
    if dam_list[d] == "Damages not recorded":
        continue
    elif dam_list[d] > highest_damage_count:
        highest_damage_count = dam_list[d]
        highest_damage_place = names[d]
    else:
        continue

print(highest_damage_place)
print(highest_damage_count)






# write your construct hurricane dictionary function here:







# write your construct hurricane by year dictionary function here:







# write your count affected areas function here:







# write your find most affected area function here:







# write your greatest number of deaths function here:







# write your catgeorize by mortality function here:







# write your greatest damage function here:







# write your catgeorize by damage function here:
