#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

df_2006_2016 = pd.read_excel("BU Spark CannesLions_2006-2020.xlsx", sheet_name='2006-2016')
df_2017 = pd.read_excel("BU Spark CannesLions_2006-2020.xlsx", sheet_name='2017')
df_2018 = pd.read_excel("BU Spark CannesLions_2006-2020.xlsx", sheet_name='2018')
df_2019 = pd.read_excel("BU Spark CannesLions_2006-2020.xlsx", sheet_name='2019')


# In[2]:


def fix_age(row):
    # 'Child'
    if row['Age'] == 1:
        return 1
    # 'Teen'
    elif row['Age'] == 3 or row['Age'] == 2:
        return 2
    # '20s'
    elif row['Age'] == 4:
        return 3
    # '30s'
    elif row['Age'] == 5:
        return 4
    # '40s'
    elif row['Age'] == 6:
        return 5
    # '50s'
    elif row['Age'] == 7:
        return 6
    # '60s'
    elif row['Age'] == 8:
        return 7
    # 'Can't tell'
    elif row['Age'] == 9:
        return 8
    # 'Not Applicable'
    elif row['Age'] == 10:
        return 9

def fix_funny(row):
    if row['Funny'] > 10:
        return row['Funny'] / 10
    else:
        return row['Funny']

def find_funny_index(row):
    if row['Funny'] > 10 or row['Funny'] % 1 != 0:
        return row.name
    else:
        return -1


# ## Prepare 2006-2016 Excel sheet

# In[3]:


"""
index_list = df.apply(lambda row: find_funny_index(row), axis=1)
for index in index_list:
    if index > 0:
        answer = df.iloc[[index]]["Funny"].item()
        if answer % 1 != 0:
            answer = answer * 10
        if answer > 10:
            digits = [int(d) for d in str(int(answer))]
            df_2006_2016.iloc[[index]]["Funny"] = digits[0]
            new_row = df_2006_2016.iloc[[index]]
            new_row["Funny"] = digits[1]
            df_2006_2016 = df_2006_2016.append(new_row, ignore_index = True)
"""


# In[4]:


######################################################################################
################################# Asset Metadata #####################################
######################################################################################

# Coder Name
df_2006_2016['Coder Name'] = ""

# Year
df_2006_2016 = df_2006_2016.rename(columns={"year": "Year"})

# Category
df_2006_2016 = df_2006_2016.rename(columns={"category": "Category"})

# Catalogue Number
df_2006_2016 = df_2006_2016.rename(columns={"catalogue": "Catalogue Number"})

# Title
df_2006_2016 = df_2006_2016.rename(columns={"title": "Title"})

# Advertiser
df_2006_2016 = df_2006_2016.rename(columns={"advertiser": "Advertiser"})

# Product
df_2006_2016 = df_2006_2016.rename(columns={"product": "Product"})

# Company
df_2006_2016 = df_2006_2016.rename(columns={"company": "Company"})

# Country
df_2006_2016 = df_2006_2016.rename(columns={"country": "Country"})

# Prize Description
df_2006_2016 = df_2006_2016.rename(columns={"prize_description": "Prize Description"})

# Prize code
df_2006_2016 = df_2006_2016.rename(columns={"prize_code": "Prize code"})

# Video Name
df_2006_2016 = df_2006_2016.rename(columns={"video_name": "Video Name"})

# Link to Asset
df_2006_2016['Link to Asset'] = ""

######################################################################################
################################### Prominence #######################################
######################################################################################

# Character ID
df_2006_2016 = df_2006_2016.rename(columns={"char_id": "Character ID"})

######################################################################################
############################ Background Characteristics ##############################
######################################################################################

# Age
# df_2006_2016['Age'] = df_2006_2016.apply (lambda row: fix_age(row), axis=1)
df_2006_2016 = df_2006_2016.rename(columns={"age": "Age"})
df_2006_2016["Age"].fillna(10, inplace=True)

# Character Gender
df_2006_2016 = df_2006_2016.rename(columns={"gender": "Character Gender"})
df_2006_2016["Character Gender"].fillna(10, inplace=True)

# Race
df_2006_2016 = df_2006_2016.rename(columns={"raceethnicity": "Race"})
df_2006_2016["Race"].fillna(10, inplace=True)

######################################################################################
##################### Activity, Technology, Use & Setting ############################
######################################################################################

# Activity
df_2006_2016 = df_2006_2016.rename(columns={"activity": "Activity"})

# Tech
df_2006_2016 = df_2006_2016.rename(columns={"tech": "Tech"})

# Setting
df_2006_2016 = df_2006_2016.rename(columns={"setting": "Setting"})

# Vehicle
df_2006_2016 = df_2006_2016.rename(columns={"vehicle": "Vehicle"})

# Location
df_2006_2016 = df_2006_2016.rename(columns={"location": "Location"})

######################################################################################
################################### Sexualization ####################################
######################################################################################

# Sexually Revealing Clothing
df_2006_2016 = df_2006_2016.rename(columns={"sexuallyrevealingclothing": "Sexually Revealing Clothing"})
df_2006_2016["Sexually Revealing Clothing"].fillna(10, inplace=True)

# State of Nudity
df_2006_2016 = df_2006_2016.rename(columns={"nudity": "State of Nudity"})
df_2006_2016["State of Nudity"].fillna(10, inplace=True)

# Shown as Body Part
df_2006_2016 = df_2006_2016.rename(columns={"shownasbodyparts": "Shown as Body Part"})
df_2006_2016["Shown as Body Part"].fillna(10, inplace=True)

# Verbally Sexual Objectification
df_2006_2016 = df_2006_2016.rename(columns={"verballysexuallyobjectified": "Verbally Sexual Objectification"})
df_2006_2016["Verbally Sexual Objectification"].fillna(10, inplace=True)

######################################################################################
######################################## Traits ######################################
######################################################################################

# TODO: Ask what '4' option is about?
# Intelligence
df_2006_2016 = df_2006_2016.rename(columns={"shownasintelligent": "Intelligence"})
df_2006_2016["Intelligence"].fillna(10, inplace=True)

# Funny
df_2006_2016 = df_2006_2016.rename(columns={"shownasfunny": "Funny"})
df_2006_2016["Funny"] = df_2006_2016.apply(lambda row: fix_funny(row), axis=1)
df_2006_2016["Funny"].fillna(10, inplace=True)

######################################################################################
################################ Work and Leadership #################################
######################################################################################

# Occupation Shown
df_2006_2016 = df_2006_2016.rename(columns={"occupationshown": "Occupation Shown"})
df_2006_2016["Occupation Shown"].fillna(10, inplace=True)

# Occupation
df_2006_2016 = df_2006_2016.rename(columns={"occupation": "Occupation"})

# Leader
df_2006_2016 = df_2006_2016.rename(columns={"leader": "Leader"})
df_2006_2016["Leader"].fillna(10, inplace=True)

#All Other Variables included to other sheets
df_2006_2016['view_video'] = ""
df_2006_2016['vatic_link'] = ""
df_2006_2016['char_montage'] = ""


# In[5]:


df_2006_2016['Asset Name'] = ""
df_2006_2016["Character Name"] = ""
df_2006_2016["Character Description"] = ""
df_2006_2016["Character Prominence"] = ""
df_2006_2016["Age Specify"] = ""
df_2006_2016["Character Sex"] = ""
df_2006_2016["Character Gender"] = ""
df_2006_2016["LGBTQ+"] = ""
df_2006_2016["Animated Character"] = ""
df_2006_2016["Animated Character - Specify"] = ""
df_2006_2016["Race Specify"] = ""
df_2006_2016["Physical Disability"] = ""
df_2006_2016["Cognitive Disability"] = ""
df_2006_2016["Communication Disability"] = ""
df_2006_2016["Shopping"] = ""
df_2006_2016["Driving"] = ""
df_2006_2016["Cleaning"] = ""
df_2006_2016["Cooking"] = ""
df_2006_2016["Working"] = ""
df_2006_2016["Socializing"] = ""
df_2006_2016["Nothing"] = ""
df_2006_2016["EatingDrinking"] = ""
df_2006_2016["Exercising"] = ""
df_2006_2016["Other Activity"] = ""
df_2006_2016["Activity Other Specify"] = ""
df_2006_2016["Kitchen"] = ""
df_2006_2016["Office"] = ""
df_2006_2016["Car"] = ""
df_2006_2016["Store"] = ""
df_2006_2016["Outdoors"] = ""
df_2006_2016["Living Room"] = ""
df_2006_2016["Restaurant/Bar"] = ""
df_2006_2016["Gym"] = ""
df_2006_2016["Bedroom"] = ""
df_2006_2016["Bathroom"] = ""
df_2006_2016["Sporting Event"] = ""
df_2006_2016["Classroom/School"] = ""
df_2006_2016["Other Setting"] = ""
df_2006_2016["Other Setting Specify"] = ""
df_2006_2016["Authority"] = ""
df_2006_2016["Body Type"] = ""
df_2006_2016["Body Type Other"] = ""
df_2006_2016["Disordered/Restrictive Eating"] = ""
df_2006_2016["Other Prejudice"] = ""
df_2006_2016["Other Prejudice Specify"] = ""
df_2006_2016["Lazy"] = ""
df_2006_2016["Slow"] = ""
df_2006_2016["Stupid"] = ""
df_2006_2016["Loser"] = ""
df_2006_2016["Inactive"] = ""
df_2006_2016["Poorly dressed"] = ""
df_2006_2016["Character Funny"] = ""
df_2006_2016["Jolly"] = ""
df_2006_2016["Clumsy"] = ""
df_2006_2016["Alone"] = ""
df_2006_2016["Comic Relief"] = ""
df_2006_2016["Sidekick"] = ""
df_2006_2016["Mamma Hen"] = ""
df_2006_2016["Nympho"] = ""
df_2006_2016["Fat to Fit Stereotype"] = ""
df_2006_2016["Inspiration porn"] = ""
df_2006_2016["Entry Type"] = ""
df_2006_2016["State of Nudity Specify"] = ""
df_2006_2016["Self Injury"] = ""
df_2006_2016["Negative Talk"] = ""
df_2006_2016["Body Modification"] = ""
df_2006_2016["Visual Shame"] = ""
df_2006_2016["Verbal Shame"] = ""
df_2006_2016["Sizeist slurs"] = ""
df_2006_2016["Punchline"] = ""
df_2006_2016["Denied Personal Opportunities"] = ""
df_2006_2016["Denied Professional Opportunities"] = ""


# ## Prepare 2017 Excel sheet

# In[6]:


######################################################################################
################################# Asset Metadata #####################################
######################################################################################

# Coder Name
df_2017['Coder Name'] = ""

# Year
df_2017['Year'] = 2017
df_2017['Year'] = df_2017['Year'].astype(np.float64)

# Category
df_2017['Category'] = ""

# Catalogue Number
df_2017['Catalogue Number'] = ""

# Title
df_2017['Title'] = ""

# Advertiser
df_2017["Advertiser"] = ""

# product
df_2017["Product"] = ""

# Company
df_2017["Company"] = ""

# Country
df_2017["Country"] = ""

# Prize Description
df_2017["Prize Description"] = ""

# Prize code
df_2017["Prize code"] = ""

# Video Name
df_2017 = df_2017.rename(columns={"video_name": "Video Name"})

# Link to Asset
df_2017['Link to Asset'] = ""

######################################################################################
################################### Prominence #######################################
######################################################################################

# Character ID
df_2017 = df_2017.rename(columns={"char_id": "Character ID"})

######################################################################################
############################ Background Characteristics ##############################
######################################################################################

# Age
# df_2017['Age'] = df_2017.apply (lambda row: fix_age(row), axis=1)
df_2017 = df_2017.rename(columns={"age": "Age"})
df_2017["Age"].fillna(10, inplace=True)

# Character Gender
df_2017 = df_2017.rename(columns={"gender": "Character Gender"})
df_2017["Character Gender"].fillna(10, inplace=True)

# Race
df_2017 = df_2017.rename(columns={"raceethnicity": "Race"})
df_2017["Race"].fillna(10, inplace=True)

######################################################################################
##################### Activity, Technology, Use & Setting ############################
######################################################################################

# Activity
df_2017 = df_2017.rename(columns={"activity": "Activity"})

# Tech
df_2017 = df_2017.rename(columns={"tech": "Tech"})

# Setting
df_2017 = df_2017.rename(columns={"setting": "Setting"})

# Vehicle
df_2017 = df_2017.rename(columns={"vehicle": "Vehicle"})

# Location
df_2017 = df_2017.rename(columns={"location": "Location"})

######################################################################################
################################### Sexualization ####################################
######################################################################################

# Sexually Revealing Clothing
df_2017 = df_2017.rename(columns={"sexuallyrevealingclothing": "Sexually Revealing Clothing"})
df_2017["Sexually Revealing Clothing"].fillna(10, inplace=True)

# State of Nudity
df_2017 = df_2017.rename(columns={"nudity": "State of Nudity"})
df_2017["State of Nudity"].fillna(10, inplace=True)

# Shown as Body Part
df_2017 = df_2017.rename(columns={"shownasbodyparts": "Shown as Body Part"})
df_2017["Shown as Body Part"].fillna(10, inplace=True)

# Verbally Sexual Objectification
df_2017 = df_2017.rename(columns={"verballysexuallyobjectified": "Verbally Sexual Objectification"})
df_2017["Verbally Sexual Objectification"].fillna(10, inplace=True)

######################################################################################
######################################## Traits ######################################
######################################################################################

# TODO: Ask what '4' option is about?
# Intelligence
df_2017 = df_2017.rename(columns={"shownasintelligent": "Intelligence"})
df_2017["Intelligence"].fillna(10, inplace=True)

# Funny
df_2017 = df_2017.rename(columns={"shownasfunny": "Funny"})
df_2017["Funny"] = df_2017.apply(lambda row: fix_funny(row), axis=1)
df_2017["Funny"].fillna(10, inplace=True)

######################################################################################
################################ Work and Leadership #################################
######################################################################################

# Occupation Shown
df_2017 = df_2017.rename(columns={"occupationshown": "Occupation Shown"})
df_2017["Occupation Shown"].fillna(10, inplace=True)

# Occupation
df_2017 = df_2017.rename(columns={"occupation": "Occupation"})

# Leader
df_2017 = df_2017.rename(columns={"leader": "Leader"})
df_2017["Leader"].fillna(10, inplace=True)

# All other variables belong to other excel sheets
df_2017["file_name"] = ""


# In[7]:


df_2017['Asset Name'] = ""
df_2017["Character Name"] = ""
df_2017["Character Description"] = ""
df_2017["Character Prominence"] = ""
df_2017["Age Specify"] = ""
df_2017["Character Sex"] = ""
df_2017["Character Gender"] = ""
df_2017["LGBTQ+"] = ""
df_2017["Animated Character"] = ""
df_2017["Animated Character - Specify"] = ""
df_2017["Race Specify"] = ""
df_2017["Physical Disability"] = ""
df_2017["Cognitive Disability"] = ""
df_2017["Communication Disability"] = ""
df_2017["Shopping"] = ""
df_2017["Driving"] = ""
df_2017["Cleaning"] = ""
df_2017["Cooking"] = ""
df_2017["Working"] = ""
df_2017["Socializing"] = ""
df_2017["Nothing"] = ""
df_2017["EatingDrinking"] = ""
df_2017["Exercising"] = ""
df_2017["Other Activity"] = ""
df_2017["Activity Other Specify"] = ""
df_2017["Kitchen"] = ""
df_2017["Office"] = ""
df_2017["Car"] = ""
df_2017["Store"] = ""
df_2017["Outdoors"] = ""
df_2017["Living Room"] = ""
df_2017["Restaurant/Bar"] = ""
df_2017["Gym"] = ""
df_2017["Bedroom"] = ""
df_2017["Bathroom"] = ""
df_2017["Sporting Event"] = ""
df_2017["Classroom/School"] = ""
df_2017["Other Setting"] = ""
df_2017["Other Setting Specify"] = ""
df_2017["Authority"] = ""
df_2017["Body Type"] = ""
df_2017["Body Type Other"] = ""
df_2017["Disordered/Restrictive Eating"] = ""
df_2017["Other Prejudice"] = ""
df_2017["Other Prejudice Specify"] = ""
df_2017["Lazy"] = ""
df_2017["Slow"] = ""
df_2017["Stupid"] = ""
df_2017["Loser"] = ""
df_2017["Inactive"] = ""
df_2017["Poorly dressed"] = ""
df_2017["Character Funny"] = ""
df_2017["Jolly"] = ""
df_2017["Clumsy"] = ""
df_2017["Alone"] = ""
df_2017["Comic Relief"] = ""
df_2017["Sidekick"] = ""
df_2017["Mamma Hen"] = ""
df_2017["Nympho"] = ""
df_2017["Fat to Fit Stereotype"] = ""
df_2017["Inspiration porn"] = ""
df_2017["Entry Type"] = ""
df_2017["State of Nudity Specify"] = ""
df_2017["Self Injury"] = ""
df_2017["Negative Talk"] = ""
df_2017["Body Modification"] = ""
df_2017["Visual Shame"] = ""
df_2017["Verbal Shame"] = ""
df_2017["Sizeist slurs"] = ""
df_2017["Punchline"] = ""
df_2017["Denied Personal Opportunities"] = ""
df_2017["Denied Professional Opportunities"] = ""


# In[8]:


cols = ['Coder Name', 'Year','Category','Catalogue Number','Title','Advertiser','Product','Company','Country','Prize Description','Prize code','Video Name','Link to Asset','ID','Character ID','Asset Name', 'Character Name',
       'Character Description', 'Character Prominence', 'Age', 'Age Specify',
       'Character Sex', 'Character Gender', 'LGBTQ+', 'Animated Character',
       'Animated Character - Specify', 'Race', 'Race Specify',
       'Physical Disability', 'Cognitive Disability',
       'Communication Disability','Activity','Tech','Setting','Vehicle', 'Shopping', 'Driving', 'Cleaning',
       'Cooking', 'Working', 'Socializing', 'Nothing', 'EatingDrinking',
       'Exercising', 'Other Activity', 'Activity Other Specify', 'Location', 'Kitchen',
       'Office', 'Car', 'Store', 'Outdoors', 'Living Room', 'Restaurant/Bar',
       'Gym', 'Bedroom', 'Bathroom', 'Sporting Event', 'Classroom/School',
       'Other Setting', 'Other Setting Specify', 'Sexually Revealing Clothing',
       'State of Nudity', 'State of Nudity Specify', 'Shown as Body Part','Verbally Sexual Objectification', 'Intelligence', 'Funny',
        'Occupation Shown','Occupation', 'Leader', 'Authority', 'Body Type', 'Entry Type',
       'Body Type Other', 'Disordered/Restrictive Eating', 'Self Injury',
       'Negative Talk', 'Body Modification', 'Visual Shame', 'Verbal Shame',
       'Sizeist slurs', 'Punchline', 'Denied Personal Opportunities',
       'Denied Professional Opportunities', 'Other Prejudice',
       'Other Prejudice Specify', 'Lazy', 'Slow', 'Stupid', 'Loser',
       'Inactive', 'Poorly dressed', 'Character Funny', 'Jolly', 'Clumsy',
       'Alone', 'Comic Relief', 'Sidekick', 'Mamma Hen', 'Nympho',
       'Fat to Fit Stereotype', 'Inspiration porn','view_video','vatic_link','file_name','char_montage']


# In[9]:


df_2017 = df_2017[cols]
df_2017.head()


# In[10]:


df_2006_2016 = df_2006_2016[cols]
df_2006_2016.head()


# In[11]:


df = pd.concat([df_2006_2016, df_2017], ignore_index=True)
# df.to_csv("Merged_Preprocessed_2006-2017.csv", encoding='utf-8', index=False)


# ## Prepare 2018 Excel sheet

# In[12]:


######################################################################################
################################# Asset Information ##################################
######################################################################################

# Coder Name
df_2018 = df_2018.rename(columns={"Coder": "Coder Name"})

# Asset Name (ASSUMPTION: CommericialName = Asset Name)
df_2018 = df_2018.rename(columns={"CommercialName": "Asset Name"})

# Entry Type
df_2018['Entry Type'] = ""

######################################################################################
################################### Prominence #######################################
######################################################################################

# Character Name
df_2018 = df_2018.rename(columns={"CharacterName": "Character Name"})

# Character Description
df_2018 = df_2018.rename(columns={"CharacterDescription": "Character Description"})

# TODO: More than 1 or 2 options in original dataset.
# Character Prominence
df_2018 = df_2018.rename(columns={"Q1.PROMINENCE": "Character Prominence"})

######################################################################################
############################ Background Characteristics ##############################
######################################################################################

# Age
df_2018 = df_2018.rename(columns={"Q2.AGE": "Age"})
df_2018['Age'] = df_2018.apply (lambda row: fix_age(row), axis=1)
df_2018["Age"].fillna(10, inplace=True)


# Age Specify
df_2018 = df_2018.rename(columns={"Q2a.AgeOther": "Age Specify"})

# Character Sex
df_2018 = df_2018.rename(columns={"Q3.SEX": "Character Sex"})
df_2018["Character Sex"].fillna(10, inplace=True)

# Character Gender
df_2018 = df_2018.rename(columns={"Q4.GENDER": "Character Gender"})
df_2018["Character Gender"].fillna(10, inplace=True)

# LGBTQ+ (ASSUMPTION: Q5.SEXUALITY = LGBTQ+)
# LGBTQ+
df_2018 = df_2018.rename(columns={"Q5.SEXUALITY": "LGBTQ+"})
df_2018["LGBTQ+"].fillna(10, inplace=True)


# Animated Character
df_2018 = df_2018.rename(columns={"Animated": "Animated Character"})
df_2018["Animated Character"].fillna(10, inplace=True)

# Animated Character - Specify
df_2018 = df_2018.rename(columns={"animated other": "Animated Character - Specify"})
df_2018["Animated Character - Specify"].fillna(10, inplace=True)

# Race
df_2018 = df_2018.rename(columns={"Q6.RACEETHNICITY": "Race"})
df_2018["Race"].fillna(10, inplace=True)

# Race Specify
df_2018 = df_2018.rename(columns={"Q6a.RaceEthnicityOther": "Race Specify"})
df_2018["Race Specify"].fillna(10, inplace=True)

# TODO: (What should I do with answer "10"?)
# Physical Disability
df_2018 = df_2018.rename(columns={"Q7.PHYSICALLYDISABLED": "Physical Disability"})

# Cognitive Disability
df_2018 = df_2018.rename(columns={"Q8.COGNITIVELYDISABLED": "Cognitive Disability"})

# Communication Disability
df_2018 = df_2018.rename(columns={"Q9.COMMUNICATIONDISABLED": "Communication Disability"})
######################################################################################
#################################### Activity ########################################
######################################################################################

# Shopping
df_2018 = df_2018.rename(columns={"Q11a.SHOPPING": "Shopping"})

# Driving
df_2018 = df_2018.rename(columns={"Q11b.DRIVING": "Driving"})

# Cleaning
df_2018 = df_2018.rename(columns={"Q11c.CLEANING": "Cleaning"})

# Cooking
df_2018 = df_2018.rename(columns={"Q11d.COOKING": "Cooking"})

# Working
df_2018 = df_2018.rename(columns={"Q11e.WORKING": "Working"})

# Socializing
df_2018 = df_2018.rename(columns={"Q11f.SOCIALIZING": "Socializing"})

# Nothing
df_2018 = df_2018.rename(columns={"Q11g.NOTHING": "Nothing"})

# EatingDrinking
df_2018 = df_2018.rename(columns={"Q11h.EATINGDRINKING": "EatingDrinking"})

# Exercising
df_2018 = df_2018.rename(columns={"Q11i.WORKINGOUT": "Exercising"})

# Other Activity
df_2018 = df_2018.rename(columns={"Q11j.ACTIVITYOTHER": "Other Activity"})

# Activity Other Specify
df_2018 = df_2018.rename(columns={"Q11iA.ActivityOtherSpecify": "Activity Other Specify"})
######################################################################################
################################### Setting ##########################################
######################################################################################

# Kitchen
df_2018 = df_2018.rename(columns={"Q12a.KITCHEN": "Kitchen"})

# Office
df_2018 = df_2018.rename(columns={"Q12b.OFFICE": "Office"})

# Car
df_2018 = df_2018.rename(columns={"Q12c.CAR": "Car"})

# Store
df_2018 = df_2018.rename(columns={"Q12d.STORE": "Store"})

# Outdoors
df_2018 = df_2018.rename(columns={"Q12e.OUTDOORS": "Outdoors"})

# Living Room
df_2018 = df_2018.rename(columns={"Q12f.LIVINGROOM": "Living Room"})

# Gym
df_2018 = df_2018.rename(columns={"Q12h.GYM": "Gym"})

# Restaurant/Bar
df_2018 = df_2018.rename(columns={"Q12g.RESTAURANTBAR": "Restaurant/Bar"})

# Bedroom
df_2018 = df_2018.rename(columns={"Q12i.BEDROOM": "Bedroom"})

# Bathroom
df_2018 = df_2018.rename(columns={"Q12j.BATHROOM": "Bathroom"})

# Sporting Event
df_2018 = df_2018.rename(columns={"Q12k.SPORTINGEVENT": "Sporting Event"})

# Classroom/School
df_2018 = df_2018.rename(columns={"CLASSROOM": "Classroom/School"})

# Other Setting
df_2018 = df_2018.rename(columns={"Q12l.SETTINGOTHER": "Other Setting"})

# Other Setting Specify
df_2018 = df_2018.rename(columns={"Q12lA.SettingOtherSpecify": "Other Setting Specify"})
######################################################################################
################################### Sexualization ####################################
######################################################################################

# Sexually Revealing Clothing
df_2018 = df_2018.rename(columns={"Q13.REVEALINGCLOTHING": "Sexually Revealing Clothing"})
df_2018["Sexually Revealing Clothing"].fillna(10, inplace=True)


# State of Nudity
df_2018 = df_2018.rename(columns={"Q14.NUDITY": "State of Nudity"})
df_2018["State of Nudity"].fillna(10, inplace=True)

# State of Nudity Specify
df_2018 = df_2018.rename(columns={"Q14a.NudityOther": "State of Nudity Specify"})
df_2018["State of Nudity Specify"].fillna(10, inplace=True)

# Shown as Body Part
df_2018 = df_2018.rename(columns={"Q15.VISUALOBJECTIFICATION": "Shown as Body Part"})
df_2018["Shown as Body Part"].fillna(10, inplace=True)

# Verbally Sexual Objectification
df_2018 = df_2018.rename(columns={"Q16.VERBALOBJECTIFICATION": "Verbally Sexual Objectification"})
df_2018["Verbally Sexual Objectification"].fillna(10, inplace=True)
######################################################################################
######################################## Traits ######################################
######################################################################################

# Intelligence
df_2018 = df_2018.rename(columns={"Q17.INTELLIGENCE": "Intelligence"})
df_2018["Intelligence"].fillna(10, inplace=True)

# Funny
df_2018 = df_2018.rename(columns={"Q18.FUNNY": "Funny"})
df_2018["Funny"] = df_2018.apply(lambda row: fix_funny(row), axis=1)
df_2018["Funny"].fillna(10, inplace=True)
######################################################################################
################################ Work and Leadership #################################
######################################################################################

# Occupation
df_2018 = df_2018.rename(columns={"Q19.OCCUPATION": "Occupation"})

df_2018 = df_2018.drop('Q20.OCCTYPE', 1)
df_2018 = df_2018.drop('Q20a.OccupationOther',1)

# Leader
df_2018 = df_2018.rename(columns={"Q21.LEADER": "Leader"})
df_2018["Leader"].fillna(10, inplace=True)

# Authority
df_2018 = df_2018.rename(columns={"authority": "Authority"})
######################################################################################
################################ Body Size Variables #################################
######################################################################################

# Body Type
df_2018 = df_2018.rename(columns={"body type": "Body Type"})

# Body Type Other
df_2018["Body Type Other"] = ""

# Disordered/Restrictive Eating
df_2018["Disordered/Restrictive Eating"] = ""

# Self Injury
df_2018["Self Injury"] = ""

# Negative Talk
df_2018["Negative Talk"] = ""

# Body Modification
df_2018["Body Modification"] = ""

# Visual Shame
df_2018["Visual Shame"] = ""

# Verbal Shame
df_2018["Verbal Shame"] = ""

# Sizeist slurs
df_2018["Sizeist slurs"] = ""

# Punchline
df_2018["Punchline"] = ""

# Denied Personal Opportunities
df_2018["Denied Personal Opportunities"] = ""

# Denied Professional Opportunities
df_2018["Denied Professional Opportunities"] = ""

# Other Prejudice
df_2018["Other Prejudice"] = ""

# Other Prejudice Specify
df_2018["Other Prejudice Specify"] = ""

# Lazy
df_2018["Lazy"] = ""

# Slow
df_2018["Slow"] = ""

# Stupid
df_2018["Stupid"] = ""

# Loser
df_2018["Loser"] = ""

# Inactive
df_2018["Inactive"] = ""

# Poorly dressed
df_2018["Poorly dressed"] = ""

# Character Funny
df_2018["Character Funny"] = ""

# Jolly
df_2018["Jolly"] = ""

# Clumsy
df_2018["Clumsy"] = ""

# Alone
df_2018["Alone"] = ""

# Comic Relief
df_2018["Comic Relief"] = ""

# Sidekick
df_2018["Sidekick"] = ""

# Mamma Hen
df_2018["Mamma Hen"] = ""

# Nympho
df_2018["Nympho"] = " "

# Fat to Fit Stereotype
df_2018["Fat to Fit Stereotype"] = ""

# Inspiration porn
df_2018["Inspiration porn"] = ""

df_2018 = df_2018.drop('Q22.VEHICLEUSE', 1)
df_2018 = df_2018.drop('Q23.TECHUSE',1)
df_2018 = df_2018.drop('Q10.MENTALILLNESS',1)


# In[13]:


df_2018["Year"] = 2018
df_2018["Category"] = ""
df_2018["Catalogue Number"] = ""
df_2018["Title"] = ""
df_2018["Advertiser"] = ""
df_2018["Product"] = ""
df_2018["Company"] = ""
df_2018["Country"] = ""
df_2018["Prize Description"] = ""
df_2018["Prize code"] = ""
df_2018["Video Name"] = ""
df_2018["Link to Asset"] = ""
df_2018["ID"] = ""
df_2018["Character ID"] = ""
df_2018["Activity"] = ""
df_2018["Tech"] = ""
df_2018["Setting"] = ""
df_2018["Vehicle"] = ""
df_2018["Location"] = ""
df_2018["Occupation Shown"] = ""
df_2018["view_video"] = ""
df_2018["vatic_link"] = ""
df_2018["file_name"] = ""
df_2018["char_montage"] = ""


# 

# ## Prepare 2019 Excel sheet

# In[14]:


######################################################################################
################################# Asset Information ##################################
######################################################################################

# Coder Name
df_2019 = df_2019.rename(columns={"Coder": "Coder Name"})

# Asset Name (ASSUMPTION: CommericialName = Asset Name)
df_2019 = df_2019.rename(columns={"AssetName": "Asset Name"})

# Entry Type
df_2019 = df_2019.rename(columns={"Q29.EntryType": "Entry Type"})

######################################################################################
################################### Prominence #######################################
######################################################################################

# Character Name
df_2019 = df_2019.rename(columns={"CharacterName": "Character Name"})

# Character Description
df_2019 = df_2019.rename(columns={"CharacterDescription": "Character Description"})

# TODO: More than 1 or 2 options in original dataset.
# Character Prominence
df_2019 = df_2019.rename(columns={"Q1.PROMINENCE": "Character Prominence"})

######################################################################################
############################ Background Characteristics ##############################
######################################################################################

# Age
df_2019 = df_2019.rename(columns={"Q2.AGE": "Age"})
df_2019['Age'] = df_2019.apply (lambda row: fix_age(row), axis=1)
df_2019["Age"].fillna(10, inplace=True)


# Age Specify
df_2019 = df_2019.rename(columns={"Q2a.AgeOtherSpecify": "Age Specify"})

# Character Sex
df_2019 = df_2019.rename(columns={"Q3.SEX": "Character Sex"})
df_2019["Character Sex"].fillna(10, inplace=True)

# Character Gender
df_2019 = df_2019.rename(columns={"Q4.GENDER": "Character Gender"})
df_2019["Character Gender"].fillna(10, inplace=True)

# LGBTQ+
df_2019 = df_2019.rename(columns={"Q5.LGBTQ": "LGBTQ+"})
df_2019["LGBTQ+"].fillna(10, inplace=True)

# Animated Character
df_2019 = df_2019.rename(columns={"Q6.ANIMATED": "Animated Character"})
df_2019["Animated Character"].fillna(10, inplace=True)

# Animated Character - Specify
df_2019 = df_2019.rename(columns={"Q6a.AnimatedOtherSpecify": "Animated Character - Specify"})
df_2019["Animated Character - Specify"].fillna(10, inplace=True)

# Race
df_2019 = df_2019.rename(columns={"Q7.RACEETHNICITY": "Race"})
df_2019["Race"].fillna(10, inplace=True)

# Race Specify
df_2019 = df_2019.rename(columns={"Q7a.RaceEthnicityOtherSpecify": "Race Specify"})
df_2019["Race Specify"].fillna(10, inplace=True)

# TODO: (What should I do with answer "10"?)
# Physical Disability
df_2019 = df_2019.rename(columns={"Q8.PHYSICALDISABILITY": "Physical Disability"})

# Cognitive Disability
df_2019 = df_2019.rename(columns={"Q9.COGNITIVEDISABILITY": "Cognitive Disability"})

# Communication Disability
df_2019 = df_2019.rename(columns={"Q10.COMMUNICATIONDISABILITY": "Communication Disability"})
######################################################################################
#################################### Activity ########################################
######################################################################################

# Shopping
df_2019 = df_2019.rename(columns={"Q11a.SHOPPING": "Shopping"})

# Driving
df_2019 = df_2019.rename(columns={"Q11b.DRIVING": "Driving"})

# Cleaning
df_2019 = df_2019.rename(columns={"Q11c.CLEANING": "Cleaning"})

# Cooking
df_2019 = df_2019.rename(columns={"Q11d.COOKING": "Cooking"})

# Working
df_2019 = df_2019.rename(columns={"Q11e.WORKING": "Working"})

# Socializing
df_2019 = df_2019.rename(columns={"Q11f.SOCIALIZING": "Socializing"})

# Nothing
df_2019 = df_2019.rename(columns={"Q11g.NOTHING": "Nothing"})

# EatingDrinking
df_2019 = df_2019.rename(columns={"Q11h.EATINGDRINKING": "EatingDrinking"})

# Exercising
df_2019 = df_2019.rename(columns={"Q11i.EXERCISING": "Exercising"})

# Other Activity
df_2019 = df_2019.rename(columns={"Q11j.ACTIVITYOTHER": "Other Activity"})

# Activity Other Specify
df_2019 = df_2019.rename(columns={"Q11j.ActivityOtherSpecify": "Activity Other Specify"})
######################################################################################
################################### Setting ##########################################
######################################################################################

# Kitchen
df_2019 = df_2019.rename(columns={"Q12a.KITCHEN": "Kitchen"})

# Office
df_2019 = df_2019.rename(columns={"Q12b.OFFICE": "Office"})

# Car
df_2019 = df_2019.rename(columns={"Q12c.CAR": "Car"})

# Store
df_2019 = df_2019.rename(columns={"Q12d.STORE": "Store"})

# Outdoors
df_2019 = df_2019.rename(columns={"Q12e.OUTDOORS": "Outdoors"})

# Living Room
df_2019 = df_2019.rename(columns={"Q12f.LIVINGROOM": "Living Room"})

# Gym
df_2019 = df_2019.rename(columns={"Q12h.GYM": "Gym"})

# Restaurant/Bar
df_2019 = df_2019.rename(columns={"Q12g.RESTAURANTBAR": "Restaurant/Bar"})

# Bedroom
df_2019 = df_2019.rename(columns={"Q12i.BEDROOM": "Bedroom"})

# Bathroom
df_2019 = df_2019.rename(columns={"Q12j.BATHROOM": "Bathroom"})

# Sporting Event
df_2019 = df_2019.rename(columns={"Q12k.SPORTINGEVENT": "Sporting Event"})

# Classroom/School
df_2019 = df_2019.rename(columns={"Q12l.CLASSROOM": "Classroom/School"})

# Other Setting
df_2019 = df_2019.rename(columns={"Q12m.LOCATIONOTHER": "Other Setting"})

# Other Setting Specify
df_2019 = df_2019.rename(columns={"Q12m.LocationOtherSpecify": "Other Setting Specify"})
######################################################################################
################################### Sexualization ####################################
######################################################################################

# Sexually Revealing Clothing
df_2019 = df_2019.rename(columns={"Q13.REVEALINGCLOTHING": "Sexually Revealing Clothing"})
df_2019["Sexually Revealing Clothing"].fillna(10, inplace=True)


# State of Nudity
df_2019 = df_2019.rename(columns={"Q14.NUDITY": "State of Nudity"})
df_2019["State of Nudity"].fillna(10, inplace=True)

# State of Nudity Specify
df_2019 = df_2019.rename(columns={"Q14a.NudityOtherSpecify": "State of Nudity Specify"})
df_2019["State of Nudity Specify"].fillna(10, inplace=True)

# Shown as Body Part
df_2019 = df_2019.rename(columns={"Q15.VISUALLYOBJECTIFIED": "Shown as Body Part"})
df_2019["Shown as Body Part"].fillna(10, inplace=True)

# Verbally Sexual Objectification
df_2019 = df_2019.rename(columns={"Q16.VERBALLYOBJECTIFIED": "Verbally Sexual Objectification"})
df_2019["Verbally Sexual Objectification"].fillna(10, inplace=True)
######################################################################################
######################################## Traits ######################################
######################################################################################

# Intelligence
df_2019 = df_2019.rename(columns={"Q17.INTELLIGENCE": "Intelligence"})
df_2019["Intelligence"].fillna(10, inplace=True)

# Funny
df_2019 = df_2019.rename(columns={"Q18.HUMOR": "Funny"})
df_2019["Funny"] = df_2018.apply(lambda row: fix_funny(row), axis=1)
df_2019["Funny"].fillna(10, inplace=True)
######################################################################################
################################ Work and Leadership #################################
######################################################################################

# Occupation
df_2019 = df_2019.rename(columns={"Q19.OCCUPATION": "Occupation"})

# Leader
df_2019 = df_2019.rename(columns={"Q20.LEADER": "Leader"})
df_2019["Leader"].fillna(10, inplace=True)

# Authority
df_2019 = df_2019.rename(columns={"Q21.AUTHORITY": "Authority"})
######################################################################################
################################ Body Size Variables #################################
######################################################################################

# Body Type
df_2019 = df_2019.rename(columns={"Q22.BODYTYPE": "Body Type"})

# Body Type Other
df_2019 = df_2019.rename(columns={"Q22a.BodyTypeOtherSpecify": "Body Type Other"})

# Disordered/Restrictive Eating
df_2019 = df_2019.rename(columns={"Q23a.DISORDEREDEATING": "Disordered/Restrictive Eating"})

# Self Injury
df_2019 = df_2019.rename(columns={"Q23b.SELFINJURY": "Self Injury"})

# Negative Talk
df_2019 = df_2019.rename(columns={"Q23c.NEGATIVETALK": "Negative Talk"})

# Body Modification
df_2019 = df_2019.rename(columns={"Q23d.BODYMODIFICATION": "Body Modification"})

# Visual Shame
df_2019 = df_2019.rename(columns={"Q24a.VISUALSHAME": "Visual Shame"})

# Verbal Shame
df_2019 = df_2019.rename(columns={"Q24b.VERBALSHAME": "Verbal Shame"})

# Sizeist slurs
df_2019 = df_2019.rename(columns={"Q24c.SIZEISTSLURS": "Sizeist slurs"})

# Punchline
df_2019 = df_2019.rename(columns={"Q24d.PUNCHLINE": "Punchline"})

# Denied Personal Opportunities
df_2019 = df_2019.rename(columns={"Q24e.DENIEDPERSONALOPPORTUNITIES": "Denied Personal Opportunities"})

# Denied Professional Opportunities
df_2019 = df_2019.rename(columns={"Q24f.DENIEDPROFESSIONALOPPORTUNITIES": "Denied Professional Opportunities"})

# Other Prejudice
df_2019 = df_2019.rename(columns={"Q24g.OTHERPREJUDICE": "Other Prejudice"})

# Other Prejudice Specify
df_2019 = df_2019.rename(columns={"Q24g.PrejudiceOtherSpecify": "Other Prejudice Specify"})

# Lazy
df_2019 = df_2019.rename(columns={"Q25a.LAZY": "Lazy"})

# Slow
df_2019 = df_2019.rename(columns={"Q25b.PHYSICALLYSLOW": "Slow"})

# Stupid
df_2019 = df_2019.rename(columns={"Q25c.STUPID": "Stupid"})

# Loser
df_2019 = df_2019.rename(columns={"Q25d.LOSER": "Loser"})

# Inactive
df_2019 = df_2019.rename(columns={"Q25e.INACTIVE": "Inactive"})

# Poorly dressed
df_2019 = df_2019.rename(columns={"Q25f.POORLYDRESSED": "Poorly dressed"})

# Character Funny
df_2019 = df_2019.rename(columns={"Q25g.FUNNY": "Character Funny"})

# Jolly
df_2019 = df_2019.rename(columns={"Q25h.JOLLY": "Jolly"})

# Clumsy
df_2019 = df_2019.rename(columns={"Q25i.CLUMSY": "Clumsy"})

# Alone
df_2019 = df_2019.rename(columns={"Q25j.ALONE": "Alone"})

# Comic Relief
df_2019 = df_2019.rename(columns={"Q26a.COMICRELIEF": "Comic Relief"})

# Sidekick
df_2019 = df_2019.rename(columns={"Q26b.SIDEKICK": "Sidekick"})

# Mamma Hen
df_2019 = df_2019.rename(columns={"Q26c.MAMMAHEN": "Mamma Hen"})

# Nympho
df_2019 = df_2019.rename(columns={"Q26d.NYMPHO": "Nympho"})

# Fat to Fit Stereotype
df_2019 = df_2019.rename(columns={"Q27.FATTOFIT": "Fat to Fit Stereotype"})

# Inspiration porn
df_2019 = df_2019.rename(columns={"Q28.INSPOPORN": "Inspiration porn"})


# Remove columns we do not need
df_2019 = df_2019.drop('Q30a.FoodampDrink', 1)
df_2019 = df_2019.drop('Q30aa.ProductionDesignArtDirection', 1)
df_2019 = df_2019.drop('Q30b.OtherFMCG', 1)
df_2019 = df_2019.drop('Q30bb.Cinematography', 1)
df_2019 = df_2019.drop('Q30c.ConsumerDurables', 1)
df_2019 = df_2019.drop('Q30cc.Editing', 1)
df_2019 = df_2019.drop('Q30d.Automotive', 1)
df_2019 = df_2019.drop('Q30dd.UseofOriginalMusic', 1)
df_2019 = df_2019.drop('Q30e.Retail', 1)
df_2019 = df_2019.drop('Q30ee.UseofLicensedAdaptedMusic', 1)
df_2019 = df_2019.drop('Q30f.Travel', 1)
df_2019 = df_2019.drop('Q30ff.SoundDesign', 1)
df_2019 = df_2019.drop('Q30g.Leisure', 1)
df_2019 = df_2019.drop('Q30gg.Animation', 1)
df_2019 = df_2019.drop('Q30i.ConsumerServicesBusinesstoBusiness', 1)
df_2019 = df_2019.drop('Q30h.MediaEntertainment', 1)
df_2019 = df_2019.drop('Q30hh.VisualEffects', 1)
df_2019 = df_2019.drop('Q30j.NotforprofitCharityGovernment', 1)
df_2019 = df_2019.drop('Q30k.CorporateSocialResponsibilityCSRCorporateImage', 1)
df_2019 = df_2019.drop('Q30l.Healthcare', 1)
df_2019 = df_2019.drop('Q30m.ViralFilm', 1)
df_2019 = df_2019.drop('Q30n.ScreensampEvents', 1)
df_2019 = df_2019.drop('Q30o.Microfilm', 1)
df_2019 = df_2019.drop('Q30p.360°VRFilm', 1)
df_2019 = df_2019.drop('Q30q.TVCinemaFilm', 1)
df_2019 = df_2019.drop('Q30r.OnlineampViralFilm', 1)
df_2019 = df_2019.drop('Q30s.LocalBrand', 1)
df_2019 = df_2019.drop('Q30t.ChallengerBrand', 1)
df_2019 = df_2019.drop('Q30u.SinglemarketCampaign', 1)
df_2019 = df_2019.drop('Q30v.SocialBehaviourampCulturalInsight', 1)
df_2019 = df_2019.drop('Q30w.BreakthroughonaBudget', 1)
df_2019 = df_2019.drop('Q30x.Direction', 1)
df_2019 = df_2019.drop('Q30y.Script', 1)
df_2019 = df_2019.drop('Q30z.Casting', 1)


# In[15]:


df_2019["Year"] = 2019
df_2019["Category"] = ""
df_2019["Catalogue Number"] = ""
df_2019["Title"] = ""
df_2019["Advertiser"] = ""
df_2019["Product"] = ""
df_2019["Company"] = ""
df_2019["Country"] = ""
df_2019["Prize Description"] = ""
df_2019["Prize code"] = ""
df_2019["Video Name"] = ""
df_2019["Link to Asset"] = ""
df_2019["ID"] = ""
df_2019["Character ID"] = ""
df_2019["Activity"] = ""
df_2019["Tech"] = ""
df_2019["Setting"] = ""
df_2019["Vehicle"] = ""
df_2019["Location"] = ""
df_2019["Occupation Shown"] = ""
df_2019["view_video"] = ""
df_2019["vatic_link"] = ""
df_2019["file_name"] = ""
df_2019["char_montage"] = ""


# In[16]:


cols = ['Coder Name', 'Year','Category','Catalogue Number','Title','Advertiser','Product','Company','Country','Prize Description','Prize code','Video Name','Link to Asset','ID','Character ID','Asset Name', 'Character Name',
       'Character Description', 'Character Prominence', 'Age', 'Age Specify',
       'Character Sex', 'Character Gender', 'LGBTQ+', 'Animated Character',
       'Animated Character - Specify', 'Race', 'Race Specify',
       'Physical Disability', 'Cognitive Disability',
       'Communication Disability','Activity','Tech','Setting','Vehicle', 'Shopping', 'Driving', 'Cleaning',
       'Cooking', 'Working', 'Socializing', 'Nothing', 'EatingDrinking',
       'Exercising', 'Other Activity', 'Activity Other Specify', 'Location', 'Kitchen',
       'Office', 'Car', 'Store', 'Outdoors', 'Living Room', 'Restaurant/Bar',
       'Gym', 'Bedroom', 'Bathroom', 'Sporting Event', 'Classroom/School',
       'Other Setting', 'Other Setting Specify', 'Sexually Revealing Clothing',
       'State of Nudity', 'State of Nudity Specify', 'Shown as Body Part','Verbally Sexual Objectification', 'Intelligence', 'Funny',
        'Occupation Shown','Occupation', 'Leader', 'Authority', 'Body Type', 'Entry Type',
       'Body Type Other', 'Disordered/Restrictive Eating', 'Self Injury',
       'Negative Talk', 'Body Modification', 'Visual Shame', 'Verbal Shame',
       'Sizeist slurs', 'Punchline', 'Denied Personal Opportunities',
       'Denied Professional Opportunities', 'Other Prejudice',
       'Other Prejudice Specify', 'Lazy', 'Slow', 'Stupid', 'Loser',
       'Inactive', 'Poorly dressed', 'Character Funny', 'Jolly', 'Clumsy',
       'Alone', 'Comic Relief', 'Sidekick', 'Mamma Hen', 'Nympho',
       'Fat to Fit Stereotype', 'Inspiration porn','view_video','vatic_link','file_name','char_montage']


# In[17]:


df_2019 = df_2019[cols]
df_2019.head()


# In[18]:


df_2018 = df_2018[cols]
df_2018.head()


# In[19]:


df2 = pd.concat([df_2018, df_2019], ignore_index=True)
# df2.to_csv("Merged_Preprocessed_2018-2019.csv", encoding='utf-8', index=False)


# In[20]:


final_df = pd.concat([df, df2], ignore_index=True)


# In[21]:


final_df.to_csv("Merged_Cannes_Dataset_2006-2020.csv", encoding='utf-8', index=False)

