#!/usr/bin/env python
# coding: utf-8

# # Preprocess Mars2021

# In[58]:


import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

original_df = pd.read_csv("Mars2021_Data.csv")


# In[59]:


def find_disabled(row):
    if row['Q8_Physical_Disability'] == 1 or row['Q9_Cognitive_Disability'] == 1 or row['Q10_Communication_Disability'] == 1 :
        return 1
    else: 
        return 0

def disabled_label(row):
    if row['Q8_Physical_Disability'] == 1:
        return 'Physical_Disability'
    elif row['Q9_Cognitive_Disability'] == 1:
        return 'Cognitive_Disability'
    elif row['Q10_Communication_Disability'] == 1:
        return 'Communication_Disability'
    else:
        return ''

def fix_age(row):
    # 'Child'
    if row['Q2_Age'] == 1:
        return 1
    # 'Teen'
    elif row['Q2_Age'] == 3 or row['Q2_Age'] == 2:
        return 2
    # '20s'
    elif row['Q2_Age'] == 4:
        return 3
    # '30s'
    elif row['Q2_Age'] == 5:
        return 4
    # '40s'
    elif row['Q2_Age'] == 6:
        return 5
    # '50s'
    elif row['Q2_Age'] == 7:
        return 6
    # '60s'
    elif row['Q2_Age'] == 8:
        return 7
    # 'Can't tell', 'Not Applicable' and 'Other (specify)' turn to 'N/A' 
    else:
        return 999

def fix_body_type(row):
    # 'Can't tell'
    if row['Q22_Body Type'] == 9 or row['Q22_Body Type'] == 7:
        return 888
    # 'Not applicable'
    elif row['Q22_Body Type'] == 10:
        return 999
    else:
        return row['Q22_Body Type']

def fix_gender(row):
    # 'Man'
    if row['Q3_Sex'] == 2:
        return 1
    # 'Woman'
    elif row['Q3_Sex'] == 1:
        return 2
    # 'Can't tell'
    elif row['Q3_Sex'] == 9:
        return 888
    # 'Not Applicable'
    elif row['Q3_Sex'] == 10:
        return 999

def fix_sexual_orientation(row):
    # 'Straight'
    if row['Q5_LGBTQ'] == 0:
        return 1
    # 'Gay or lesbian'
    elif row['Q5_LGBTQ'] == 1:
        return 2
    elif row['Q5_LGBTQ'] == 2:
        return 3
    else:
        return 888

def fix_queer(row):
    if row['Sexual Orientation'] == 3:
        return 1
    else:
        return 0

def fix_race(row):
    # 'White'
    if row['Q7_Race_Ethnicity'] == 1:
        return 1
    # 'Black'
    elif row['Q7_Race_Ethnicity'] == 3:
        return 2
    # 'Asian/Pacific Islander'
    elif row['Q7_Race_Ethnicity'] == 5 or row['Q7_Race_Ethnicity'] == 7:
        return 3
    # 'Latinx'
    elif row['Q7_Race_Ethnicity'] == 2:
        return 4
    # 'Native'
    elif row['Q7_Race_Ethnicity'] == 4:
        return 5
    # 'Middle Eastern / North African'
    elif row['Q7_Race_Ethnicity'] == 6:
        return 6
    # 'Multi-racial (only if you know for certain)'
    elif row['Q7_Race_Ethnicity'] == 8:
        return 8
    # 'Can't tell'
    elif row['Q7_Race_Ethnicity'] == 9:
        return 888
    # 'NA'
    elif row['Q7_Race_Ethnicity'] == 10:
        return 999

def fix_API(row):
    # 'White'
    if row['Q7_Race_Ethnicity'] == 5:
        return 888
    elif row['Q7_Race_Ethnicity'] == 7:
        return 2
    else:
        return 999


# In[60]:


df = original_df 
# Drop unrelated columns
df = df.drop(['Unnamed: 88','Unnamed: 90','Unnamed: 92','Unnamed: 93','Unnamed: 94','Unnamed: 95','Unnamed: 96','Unnamed: 97','Unnamed: 98','Unnamed: 99','Unnamed: 100','Unnamed: 101','Unnamed: 102','Unnamed: 103','Unnamed: 104','Unnamed: 105','Unnamed: 106'], axis=1)
######### Questions processed #########
# Prominence
df = df.rename(columns={"Q1_Prominence": "Prominence"})

# Animated
df = df.rename(columns={"Q6_Animated": "Animated"})
df = df.rename(columns={"Q6a_Animated_OtherSpecify": "Animated Specify"})

# Disabled
df['Disabled'] = df.apply (lambda row: find_disabled(row), axis=1)
df['Disability Specify'] = df.apply (lambda row: disabled_label(row), axis=1)
df = df.drop(['Q8_Physical_Disability','Q9_Cognitive_Disability','Q10_Communication_Disability'], axis=1)

# Age
df['Age'] = df.apply (lambda row: fix_age(row), axis=1)
df = df.drop(['Q2_Age'], axis=1)
df = df.drop(['Q2a_Age_SpecifyOther'], axis=1)

# Body Type
df['Body Type'] = df.apply (lambda row: fix_body_type(row), axis=1)
df = df.drop(['Q22_Body Type','Q22a_Body_Type_Other_Specify'], axis=1)

# Skin tone 
df['Skin tone'] = 999

# Trans
df['Trans'] = 0

# Gender fix_gender
df['Gender'] =  df.apply (lambda row: fix_gender(row), axis=1)
df = df.drop(['Q3_Sex'], axis=1)
df = df.drop(['Q4_Gender'], axis=1)

# Sexual Orientation
df['Sexual Orientation'] = df.apply (lambda row: fix_sexual_orientation(row), axis=1)
df = df.drop(['Q5_LGBTQ'], axis=1)

# Queer
df['Queer'] = df.apply (lambda row: fix_queer(row), axis=1)

# Race
df['Race'] =  df.apply (lambda row: fix_race(row), axis=1)
df['Race Other/Specify'] =  df['Q7a_RE_OtherSpecify']
df['API'] = df.apply (lambda row: fix_API(row), axis=1)
df = df.drop(['Q7_Race_Ethnicity', 'Q7a_RE_OtherSpecify'], axis=1)


# Activities 
df['Shopping'] = df['Q11a_Shopping']
df['Driving'] = df['Q11b_Driving']
df['Cleaning'] = df['Q11c_Cleaning']
df['Cooking'] = df['Q11d_Cooking']
df['Working'] = df['Q11e_Working']
df['Socializing'] = df['Q11f_Socializing']
df['Nothing'] = df['Q11g_Nothing']
df['EatingDrinking'] = df['Q11h_Eating/Drinking']
df['Exercising'] = df['Q11i_Exercising']
df['Other Activity'] = df['Q11j_Activity Other']
df['Activity Other Specify'] = df['Q11j_Activity_Other_Specify']
df = df.drop(['Q11a_Shopping', 'Q11b_Driving', 'Q11c_Cleaning', 'Q11d_Cooking', 'Q11e_Working', 'Q11f_Socializing', 'Q11g_Nothing', 'Q11h_Eating/Drinking', 'Q11i_Exercising', 'Q11j_Activity Other', 'Q11j_Activity_Other_Specify'], axis=1)

# Settings 
df['Kitchen'] = df['Q12a_Kitchen']
df['Office'] = df['Q12b_Office']
df['Car'] = df['Q12c_Car']
df['Store'] = df['Q12d_Store']
df['Outdoors'] = df['Q12e_Outdoors']
df['Living Room'] = df['Q12f_Living Room']
df['Restaurant/Bar'] = df['Q12g_Restaurant_Bar']
df['Gym'] = df['Q12h_Gym']
df['Bedroom'] = df['Q12i_Bedroom']
df['Bathroom'] = df['Q12j_Bathroom']
df['Sporting Event'] = df['Q12k_Sporting_Event']
df['Classroom'] = df['Q12l_Classroom']
df['Setting Other'] = df['Q12m_Location_Other']
df['Other Setting Specify'] = df['Q12m_Location_Other_Specify']
df = df.drop(['Q12a_Kitchen', 'Q12b_Office', 'Q12c_Car', 'Q12d_Store', 'Q12e_Outdoors', 'Q12f_Living Room', 'Q12g_Restaurant_Bar', 'Q12h_Gym', 'Q12i_Bedroom', 'Q12j_Bathroom', 'Q12k_Sporting_Event', 'Q12l_Classroom', 'Q12m_Location_Other', 'Q12m_Location_Other_Specify'], axis=1)

# Sexualization
df['Revealing Clothing'] = df['Q13_Revealing_Clothing']
df['Nudity'] = df['Q14_Nudity']
df['Visually Objectified'] = df['Q15_Visually_Objectified']
df['Verbally Objectified'] = df['Q16_Verbally_Objectified']
df = df.drop(['Q13_Revealing_Clothing', 'Q14_Nudity','Q14a_Nudity_Other_Specify', 'Q15_Visually_Objectified', 'Q16_Verbally_Objectified'], axis=1)

# Traits
df['Intelligent'] = df['Q17_Intelligence']
df['Funny'] = df['Q18_Humor']
df = df.drop(['Q17_Intelligence', 'Q18_Humor'], axis=1)

# Work & Leadership
df['Occupation'] = df['Q19_Occupation']
df['Leader'] = df['Q20_Leader']
df['Authority'] = df['Q21_Authority']
df = df.drop(['Q19_Occupation', 'Q20_Leader', 'Q21_Authority'], axis=1)

# Rest of the questions
# Rename question 23 to question 27
df = df.rename(columns={"Q23a_Disordered_Eating": "Q27a_Disordered_Eating"})
df = df.rename(columns={"Q23b_Selfy_injury": "Q27b_Selfy_injury"})
df = df.rename(columns={"Q23c_NegativeTalk": "Q27c_NegativeTalk"})
df = df.rename(columns={"Q23d_Body_Modification": "Q27d_Body_Modification"})

# Rename question 24 to question 28
df = df.rename(columns={"Q24a_Visual_Shame": "Q28a_Visual_Shame"})
df = df.rename(columns={"Q24b_Verbal_shame": "Q28b_Verbal_Shame"})
df = df.rename(columns={"Q24c_Sizeist_Slurs": "Q28c_Sizeist_Slurs"})
df = df.rename(columns={"Q24d_Punchline": "Q28d_Punchline"})
df = df.rename(columns={"Q24e_Denied_Personal_Opportunity": "Q28e_Denied_Personal_Opportunity"})
df = df.rename(columns={"Q24f_Denied_Professional_Opportunity": "Q28f_Denied_Professional_Opportunity"})
df = df.rename(columns={"Q24g_Other_Prejudice": "Q28g_Other_Prejudice"})
df = df.rename(columns={"Q24g_Prejudice_Other_Specify": "Q28g_Prejudice_Other_Specify"})

# Rename question 25 to question 29
df = df.rename(columns={"Q25a_Lazy": "Q29a_Lazy"})
df = df.rename(columns={"Q25b_Physically_Slow": "Q29b_Physically_Slow"})
df = df.rename(columns={"Q25c_Stupid": "Q29c_Stupid"})
df = df.rename(columns={"Q25d_Loser": "Q29d_Loser"})
df = df.rename(columns={"Q25e_Inactive": "Q29e_Inactive"})
df = df.rename(columns={"Q25f_Poorly_Dressed": "Q29f_Poorly_Dressed"})
df = df.rename(columns={"Q25g_Funny": "Q29g_Funny"})
df = df.rename(columns={"Q25h_Jolly": "Q29h_Jolly"})
df = df.rename(columns={"Q25i_Clumsy": "Q29i_Clumsy"})
df = df.rename(columns={"Q25j_Alone": "Q29j_Alone"})

# Rename question 26 to question 30
df = df.rename(columns={"Q26a_Comic_Relief": "Q30a_Comic_Relief"})
df = df.rename(columns={"Q26b_Sidekick": "Q30b_Sidekick"})
df = df.rename(columns={"Q26c_Mamma_Hen": "Q30c_Mamma_Hen"})
df = df.rename(columns={"Q26d_Nympho": "Q30d_Nympho"})

# Rename question 27 to question 31
df = df.rename(columns={"Q27_Fat_to_Fit": "Q31_Fat_to_Fit"})
df = df.rename(columns={"Q27. NOTES": "Q31_NOTES"})


# Rename question 28 to question 32
df = df.rename(columns={"Q28_Inspo_Porn": "Q32_Inspo_Porn"})


# In[61]:


cols = df.columns.tolist()
cols = ['Coder', 'Asset_Name', 'Brand', 'Lead_Country', 'Year_Produced', 'Year_Aired', 'Segment', 'Agency', 'Character_Name', 'Character_Description',
 'Prominence', 'Animated', 'Animated Specify','Gender','Trans','Race','Race Other/Specify', 'API','Skin tone','Sexual Orientation','Queer','Age','Disabled', 'Disability Specify','Body Type',
 'Shopping', 'Driving', 'Cleaning', 'Cooking', 'Working', 'Socializing', 'Nothing', 'EatingDrinking','Exercising', 'Other Activity', 'Activity Other Specify', 'Kitchen', 'Office', 'Car', 'Store',
 'Outdoors', 'Living Room', 'Restaurant/Bar', 'Gym', 'Bedroom', 'Bathroom', 'Sporting Event', 'Classroom', 'Setting Other', 'Other Setting Specify', 'Revealing Clothing', 'Nudity', 'Visually Objectified',
 'Verbally Objectified', 'Intelligent', 'Funny', 'Occupation', 'Leader', 'Authority','Q27a_Disordered_Eating', 'Q27b_Selfy_injury', 'Q27c_NegativeTalk', 'Q27d_Body_Modification', 'Q28a_Visual_Shame', 
 'Q28b_Verbal_Shame', 'Q28c_Sizeist_Slurs', 'Q28d_Punchline', 'Q28e_Denied_Personal_Opportunity', 'Q28f_Denied_Professional_Opportunity', 'Q28g_Other_Prejudice','Q28g_Prejudice_Other_Specify', 'Q29a_Lazy',
  'Q29b_Physically_Slow', 'Q29c_Stupid', 'Q29d_Loser', 'Q29e_Inactive', 'Q29f_Poorly_Dressed', 'Q29g_Funny', 'Q29h_Jolly', 'Q29i_Clumsy', 'Q29j_Alone', 'Q30a_Comic_Relief', 'Q30b_Sidekick', 'Q30c_Mamma_Hen', 
  'Q30d_Nympho', 'Q31_Fat_to_Fit', 'Q32_Inspo_Porn','Q31_NOTES', 'Notes on Dwelling' ]

df = df[cols]
df.head()


# In[62]:


# Fix Year_Aired to be one year before the dataset name e.g Mars2021 -> 2020
df = df[df['Year_Aired'] == 2020]
# Fix Segment inconsistent values from "Pet" to be all "Petcare"
df["Segment"].replace({"Pet": "Petcare"}, inplace=True)
df1 = df
# Save preprocessed dataset 
# df.to_csv("Preprocessed_Mars2021_Data.csv", encoding='utf-8', index=False)
df.head()


# # Preprocess Mars2020
# 

# In[63]:


original_df = pd.read_csv("Mars2020_Data.csv")
original_df.head()


# In[64]:


def find_disabled(row):
    if row['Q8.PHYSICALDISABILITY'] == 1 or row['Q9.COGNITIVEDISABILITY'] == 1 or row['Q10.COMMUNICATIONDISABILITY'] == 1 :
        return 1
    else: 
        return 0

def disabled_label(row):
    if row['Q8.PHYSICALDISABILITY'] == 1:
        return 'Physical_Disability'
    elif row['Q9.COGNITIVEDISABILITY'] == 1:
        return 'Cognitive_Disability'
    elif row['Q10.COMMUNICATIONDISABILITY'] == 1:
        return 'Communication_Disability'
    else:
        return ''

def fix_age(row):

    # 'Child'
    if row['Q2.AGE'] == 1:
        return 1
    # 'Teen'
    elif row['Q2.AGE'] == 3 or row['Q2.AGE'] == 2:
        return 2
    # '20s'
    elif row['Q2.AGE'] == 4:
        return 3
    # '30s'
    elif row['Q2.AGE'] == 5:
        return 4
    # '40s'
    elif row['Q2.AGE'] == 6:
        return 5
    # '50s'
    elif row['Q2.AGE'] == 7:
        return 6
    # '60s'
    elif row['Q2.AGE'] == 8:
        return 7
    # 'Can't tell', 'Not Applicable' and 'Other (specify)' turn to 'N/A' 
    else:
        return 999

def fix_body_type(row):
    # 'Can't tell'
    if row['Q22.BODYTYPE'] == 9 or row['Q22.BODYTYPE'] == 7:
        return 888
    # 'Not applicable'
    elif row['Q22.BODYTYPE'] == 10:
        return 999
    else:
        return row['Q22.BODYTYPE']

def fix_queer(row):
    if row['Sexual Orientation'] == 3:
        return 1
    else:
        return 0

def fix_gender(row):
    # 'Man'
    if row['Q3.SEX'] == 2:
        return 1
    # 'Woman'
    elif row['Q3.SEX'] == 1:
        return 2
    # 'Can't tell'
    elif row['Q3.SEX'] == 9:
        return 888
    # 'Not Applicable'
    elif row['Q3.SEX'] == 10:
        return 999

def fix_sexual_orientation(row):
    # 'Straight'
    if row['Q5.LGBTQ'] == 0:
        return 1
    # 'Gay or lesbian'
    elif row['Q5.LGBTQ'] == 1:
        return 2
    # 'Bi, pan, or queer'
    elif row['Q5.LGBTQ'] == 2:
        return 3
    else:
        return 888

def fix_race(row):
    # 'White'
    if row['Q7.RACEETHNICITY'] == 1:
        return 1
    # 'Black'
    elif row['Q7.RACEETHNICITY'] == 3:
        return 2
    # 'Asian/Pacific Islander'
    elif row['Q7.RACEETHNICITY'] == 5 or row['Q7.RACEETHNICITY'] == 7:
        return 3
    # 'Latinx'
    elif row['Q7.RACEETHNICITY'] == 2:
        return 4
    # 'Native'
    elif row['Q7.RACEETHNICITY'] == 4:
        return 5
    # 'Middle Eastern / North African'
    elif row['Q7.RACEETHNICITY'] == 6:
        return 6
    # 'Multi-racial (only if you know for certain)'
    elif row['Q7.RACEETHNICITY'] == 8:
        return 8
    # 'Can't tell'
    elif row['Q7.RACEETHNICITY'] == 9:
        return 888
    # 'Multi-racial (only if you know for certain)'
    elif row['Q7.RACEETHNICITY'] == 10:
        return 999

def fix_API(row):
    # 'White'
    if row['Q7.RACEETHNICITY'] == 5:
        return 888
    elif row['Q7.RACEETHNICITY'] == 7:
        return 2
    else:
        return 999


# In[65]:


df = original_df 
df = df.rename(columns={"AssetName": "Asset_Name"})
df = df.rename(columns={"LeadCountry": "Lead_Country"})
df = df.rename(columns={"Yearproduced": "Year_Produced"})
df = df.rename(columns={"yearAired": "Year_Aired"})
# Add Agency to specific place as Mars2021 dataset 
df.insert(loc=7, column='Agency', value="")
df = df.rename(columns={"CharacterName": "Character_Name"})
df = df.rename(columns={"CharacterDescription": "Character_Description"})

######### Questions processed #########
# Prominence
df = df.rename(columns={"Q1.PROMINENCE": "Prominence"})

# Animated
df = df.rename(columns={"Q6.ANIMATED": "Animated"})
df = df.rename(columns={"Q6a.AnimatedOtherSpecify": "Animated Specify"})

# Disabled
df['Disabled'] = df.apply (lambda row: find_disabled(row), axis=1)
df['Disability Specify'] = df.apply (lambda row: disabled_label(row), axis=1)
df = df.drop(['Q8.PHYSICALDISABILITY','Q9.COGNITIVEDISABILITY','Q10.COMMUNICATIONDISABILITY'], axis=1)

# Age
df['Age'] = df.apply (lambda row: fix_age(row), axis=1)
df = df.drop(['Q2.AGE'], axis=1)
df = df.drop(['Q2a.AgeOtherSpecify'], axis=1)

# Body Type
df['Body Type'] = df.apply (lambda row: fix_body_type(row), axis=1)
df = df.drop(['Q22.BODYTYPE','Q22a.BodyTypeOtherSpecify'], axis=1)

# Skin tone 
df['Skin tone'] = 999

# Trans
df['Trans'] = 0

# Gender
df['Gender'] =  df.apply (lambda row: fix_gender(row), axis=1)
df = df.drop(['Q3.SEX'], axis=1)
df = df.drop(['Q4.GENDER'], axis=1)

# Sexual Orientation
df['Sexual Orientation'] = df.apply (lambda row: fix_sexual_orientation(row), axis=1)
df = df.drop(['Q5.LGBTQ'], axis=1)

# Queer
df['Queer'] = df.apply (lambda row: fix_queer(row), axis=1)

# Race
df['Race'] =  df.apply (lambda row: fix_race(row), axis=1)
df['Race Other/Specify'] =  df['Q7a.RaceEthnicityOtherSpecify']
df['API'] = df.apply (lambda row: fix_API(row), axis=1)
df = df.drop(['Q7.RACEETHNICITY', 'Q7a.RaceEthnicityOtherSpecify'], axis=1)


# Activities 
df['Shopping'] = df['Q11a.SHOPPING']
df['Driving'] = df['Q11b.DRIVING']
df['Cleaning'] = df['Q11c.CLEANING']
df['Cooking'] = df['Q11d.COOKING']
df['Working'] = df['Q11e.WORKING']
df['Socializing'] = df['Q11f.SOCIALIZING']
df['Nothing'] = df['Q11g.NOTHING']
df['EatingDrinking'] = df['Q11h.EATINGDRINKING']
df['Exercising'] = df['Q11i.EXERCISING']
df['Other Activity'] = df['Q11j.ACTIVITYOTHER']
df['Activity Other Specify'] = df['Q11j.ActivityOtherSpecify']
df = df.drop(['Q11a.SHOPPING', 'Q11b.DRIVING', 'Q11c.CLEANING', 'Q11d.COOKING', 'Q11e.WORKING', 'Q11f.SOCIALIZING', 'Q11g.NOTHING', 'Q11h.EATINGDRINKING', 'Q11i.EXERCISING', 'Q11j.ACTIVITYOTHER', 'Q11j.ActivityOtherSpecify'], axis=1)

# Settings 
df['Kitchen'] = df['Q12a.KITCHEN']
df['Office'] = df['Q12b.OFFICE']
df['Car'] = df['Q12c.CAR']
df['Store'] = df['Q12d.STORE']
df['Outdoors'] = df['Q12e.OUTDOORS']
df['Living Room'] = df['Q12f.LIVINGROOM']
df['Restaurant/Bar'] = df['Q12g.RESTAURANTBAR']
df['Gym'] = df['Q12h.GYM']
df['Bedroom'] = df['Q12i.BEDROOM']
df['Bathroom'] = df['Q12j.BATHROOM']
df['Sporting Event'] = df['Q12k.SPORTINGEVENT']
df['Classroom'] = df['Q12l.CLASSROOM']
df['Setting Other'] = df['Q12m.LOCATIONOTHER']
df['Other Setting Specify'] = df['Q12m.LocationOtherSpecify']
df = df.drop(['Q12a.KITCHEN', 'Q12b.OFFICE', 'Q12c.CAR', 'Q12d.STORE', 'Q12e.OUTDOORS', 'Q12f.LIVINGROOM', 'Q12g.RESTAURANTBAR', 'Q12h.GYM', 'Q12i.BEDROOM', 'Q12j.BATHROOM', 'Q12k.SPORTINGEVENT', 'Q12l.CLASSROOM', 'Q12m.LOCATIONOTHER', 'Q12m.LocationOtherSpecify'], axis=1)

# Sexualization
df['Revealing Clothing'] = df['Q13.REVEALINGCLOTHING']
df['Nudity'] = df['Q14.NUDITY']
df['Visually Objectified'] = df['Q15.VISUALLYOBJECTIFIED']
df['Verbally Objectified'] = df['Q16.VERBALLYOBJECTIFIED']
df = df.drop(['Q13.REVEALINGCLOTHING', 'Q14.NUDITY','Q14a.NudityOtherSpecify', 'Q15.VISUALLYOBJECTIFIED', 'Q16.VERBALLYOBJECTIFIED'], axis=1)

# Traits
df['Intelligent'] = df['Q17.INTELLIGENCE']
df['Funny'] = df['Q18.HUMOR']
df = df.drop(['Q17.INTELLIGENCE', 'Q18.HUMOR'], axis=1)

# Work & Leadership
df['Occupation'] = df['Q19.OCCUPATION']
df['Leader'] = df['Q20.LEADER']
df['Authority'] = df['Q21.AUTHORITY']
df = df.drop(['Q19.OCCUPATION', 'Q20.LEADER', 'Q21.AUTHORITY'], axis=1)

# Rest of the questions
# Rename question 23 to question 27
df = df.rename(columns={"Q23a.DISORDEREDEATING": "Q27a_Disordered_Eating"})
df = df.rename(columns={"Q23b.SELFINJURY": "Q27b_Selfy_injury"})
df = df.rename(columns={"Q23c.NEGATIVETALK": "Q27c_NegativeTalk"})
df = df.rename(columns={"Q23d.BODYMODIFICATION": "Q27d_Body_Modification"})

# Rename question 24 to question 28
df = df.rename(columns={"Q24a.VISUALSHAME": "Q28a_Visual_Shame"})
df = df.rename(columns={"Q24b.VERBALSHAME": "Q28b_Verbal_Shame"})
df = df.rename(columns={"Q24c.SIZEISTSLURS": "Q28c_Sizeist_Slurs"})
df = df.rename(columns={"Q24d.PUNCHLINE": "Q28d_Punchline"})
df = df.rename(columns={"Q24e.DENIEDPERSONALOPPORTUNITIES": "Q28e_Denied_Personal_Opportunity"})
df = df.rename(columns={"Q24f.DENIEDPROFESSIONALOPPORTUNITIES": "Q28f_Denied_Professional_Opportunity"})
df = df.rename(columns={"Q24g.OTHERPREJUDICE": "Q28g_Other_Prejudice"})
df = df.rename(columns={"Q24g.PrejudiceOtherSpecify": "Q28g_Prejudice_Other_Specify"})

# Rename question 25 to question 29
df = df.rename(columns={"Q25a.LAZY": "Q29a_Lazy"})
df = df.rename(columns={"Q25b.PHYSICALLYSLOW": "Q29b_Physically_Slow"})
df = df.rename(columns={"Q25c.STUPID": "Q29c_Stupid"})
df = df.rename(columns={"Q25d.LOSER": "Q29d_Loser"})
df = df.rename(columns={"Q25e.INACTIVE": "Q29e_Inactive"})
df = df.rename(columns={"Q25f.POORLYDRESSED": "Q29f_Poorly_Dressed"})
df = df.rename(columns={"Q25g.FUNNY": "Q29g_Funny"})
df = df.rename(columns={"Q25h.JOLLY": "Q29h_Jolly"})
df = df.rename(columns={"Q25i.CLUMSY": "Q29i_Clumsy"})
df = df.rename(columns={"Q25j.ALONE": "Q29j_Alone"})

# Rename question 26 to question 30
df = df.rename(columns={"Q26a.COMICRELIEF": "Q30a_Comic_Relief"})
df = df.rename(columns={"Q26b.SIDEKICK": "Q30b_Sidekick"})
df = df.rename(columns={"Q26c.MAMMAHEN": "Q30c_Mamma_Hen"})
df = df.rename(columns={"Q26d.NYMPHO": "Q30d_Nympho"})

# Rename question 27 to question 31
df = df.rename(columns={"Q27.FATTOFIT": "Q31_Fat_to_Fit"})
df["Q31_NOTES"] = ""

# Rename question 28 to question 32
df = df.rename(columns={"Q28.INSPOPORN": "Q32_Inspo_Porn"})

df["Notes on Dwelling"] = ""

df = df[cols]
df.head()


# In[66]:


# Fix Year_Aired to be one year before the dataset name e.g Mars2021 -> 2020
df = df[df['Year_Aired'] == 2019]
df2 = df
# Save preprocessed dataset 
#df.to_csv("Preprocessed_Mars2020_Data.csv", encoding='utf-8', index=False)
df.head()


# # Merge Mars2020 & Mars2021

# In[67]:


# df1 = pd.read_csv("Preprocessed_Mars2021_Data.csv")
# df2 = pd.read_csv("Preprocessed_Mars2020_Data.csv")


# In[68]:


# print(df1.columns.tolist())
# len(df1)


# In[69]:


# print(df2.columns.tolist())
# len(df2)


# In[70]:


df = pd.concat([df1, df2], ignore_index=True)
len(df)


# In[71]:


df.to_csv("Merged_Preprocessed_Mars2020_2021.csv", encoding='utf-8', index=False)

