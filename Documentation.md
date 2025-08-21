# Central Coast Crime Rates
### 9CT2 Task 2 - Central Coast Violent and non-violent crime rates + links.
---
### Hypothesis
    Violent crime, as well as non-violent crime (burglary, etc.) occurred most over the past 10 years in times of high social interaction. There was an reduction of crime during times of lower public interaction and increased screen time.

---

### Research and Findings
I acquired my dataset from the BOCSAR (NSW Bureau of Crime Statistics and Research), where I acquired a Central Coast dataset that I transferred onto a separate, smaller CSV file to read into pandas.

My dataset has benefits and also negative attributes that add to, or lessen the validity of the dataset. The data has been taken from a reputable and official government source, and does not contain empty fields (as it is a small dataset). In contrast, the dataset is small, which contributes less to the overall ability of the data to recognise deeper hidden trends and pattern. Additionally, the dataset mostly doesn't factor in the possibility of crimes being domestic or non-domestic, which could explain some results (like an influx of crime during the pandemic, likely domestic crime as a result of the lockdowns). In a professional setting, data like this could result in focus on crime control during periods of low social interaction, which would be a wrongful decision as non-domestic crime would usually occur more outside of isolation.

---
### Functional and Non-Functional Requirements

#### **Functional Requirements**

1. Data Loading

     The data loading process should be efficient,and should be versatile enough to load different filetypes (such as .xlsr and .csv files). Additionally, it should be able to manage issues like wrong formatting.


2. Data Cleansing

    The  data cleansing process should be able to recognize and correct issues such as missing values. This should be done based on patterns and trends. Additionally, The program should employ the use of statistical mathematics, including mean, median and mode.

3. Visual Information Clarity

    After processing, information should be displayed in a clear, visual manner (using pandas and matplotlib). The information should be well-layed out, as well as understandable with minimal pre-known knowledge/context. Additionally, essential context should be displayed in all data visualisations.

#### **Non-Functional Requirements**

1. Efficiency

    The data transmission process between different systems and/or platforms should be efficient, functioning fast, while managing resources. 

2. Security

    Data security is important during the storing of data and transmission of data. It is important that data storage is protected from malicious attacks and/or changes and invalid data from other parties. Transmission encryption is important to ensure data privacy is regulated.

3. Accessibility

    Data should be easily accessible for users, in a raw state, visual state and in a search-specific state. This can be achieved through data visualisation using matplotlib and pandas, and the implementation of a search function using pandas features like iloc, loc and more.

#### **Use-Cases**
1.  Access

    Actor: User

    Goal: To gain access to data about the crime rates over 10 years in the Central Coast via a user interface.

    Preconditions: The Dataset has been preloaded onto the system, and the system interface (python based) is accessible and executable.

    Main Flow:
    1. User runs the program and is     presented
     with 4 input options on a text-based menu.
    2.  User accesses different parts and functions based on their inputs, being able to access either:

        1. The Raw Dataset
        2. MatPlotLib Based Visualisations
        3. Data Searching and/or Filtering
    3. The program should output the correct response to the users input.

    Post-Conditions: 
    - User can interact with, visualise, search and view the data.
    - Data is not lost or damaged throughout the process.
---
### Data Dictionary
|Field|Datatype|Format for Display|Description|Example|Validation|
|:---:|:------:|:----------------:|:---------:|:-----:|:--------:|
|Murder|int|N|Rates of one of the major crimes on the central coast|7|Must be a whole number|
|Non-Domestic Assault|int|NNNN|Rates of one of the major crimes on the central coast|7|Must be a whole number|
|Breaking and Entering Dwelling|int|NNNN|Rates of one of the major crimes on the central coast|7|Must be a whole number|
|Robbery|int|NNN|Rates of one of the major crimes on the central coast|7|Must be a whole number|
|Attempted Murder|int|N|Rates of one of the major crimes on the central coast|7|Must be a whole number|
|Sexual Assault|int|NN|Rates of one of the major crimes on the central coast|7|Must be a whole number|
|Year|Object|XX..XX - XX..XX|Rates of one of the major crimes on the central coast|April 2019 - March 2020|Must be a string with the format [STARTING POINT - END POINT]|

---
### SEE-I Paragraph
Although my program had a variety of inconsistencies, the main functions of the program were operating correctly for the most part. The dataset I used was a small sample from a larger dataset, which made it easier to manipulate, but gave less concise findings. Based on my visualisations and raw data, most crime (except for non-domestic crimes) were at their highest during the pandemic, which would suggest an influx of aggressive and violent crime within lockdown areas, and quarantine, likely suggesting that domestic crime was the major factor for the rise in crime. While my hypothesis stated that violent and major crime was at it's highest during times of social interaction, the trend throughout most of the data suggests that the pandemic saw a rise in crime. This is likely only seen as the data is given out of context, without taking into consideration domestic and non-domestic crime, where domestic crime would take place a lot more often during times of isolation.

---
### Evaluation
My user interface is a bit messy in some areas, which could lead to confusion for users. The dataset I used is small, which makes it less viable for finding deep trends and recognising patterns. Additionally, the dataset is somewhat biased as it does not factor in domestic and non-domestic crime for a majority of the data. Many of my requirement outlines were achieved in the program, like visual clarity with my graphs (as a result of matplotlib) and data searching, but some were also not, like data cleansing (as the dataset already had full values in all cells) and data efficiency (as the program can sometimes be a bit slow).

In terms of my project, I managed my time in a less than ideal way, as a majority of my task was done in the last periods of time (as seen by my commits). I did ask for help from teachers and peers, as well as other sources online for help with optimizing my code, allowing me to remove some hardcoded areas that would have taken a lot of resources/area and made the code messy.
    