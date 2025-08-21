# Central Coast Crime Rates
### 9CT2 Task 2 - Central Coast Violent and non-violent crime rates + links.
---
### Hypothesis
    Violent crime, as well as non-violent crime (burglary, etc.) occurs most in areas with high populations, as well as cityscape areas with a high magnitude of abandoned urban infrastructure like Gosford. Additionally, high delinquency raises crime rates and contibutes to the overall crime rates in the Central Coast.

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
|Year|Object|XX..XX|Rates of one of the major crimes on the central coast|7|Must be a string with the format STARTING POINT|


    