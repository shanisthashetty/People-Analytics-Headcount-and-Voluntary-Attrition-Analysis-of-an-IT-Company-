


import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

@st.cache_data
def read_data():
    edf=pd.read_csv('C:/UE2023W/DA/project/employee_hr_data.csv')
    edf['Attrition']=edf['Attrition'].apply(lambda x:1 if x=='Yes' else 0)
    # change overtime field from text yes/no to categorical 1/0
    edf['OverTime']=edf['OverTime'].apply(lambda x:1 if x=='Yes' else 0)
   

    return edf


def hcas(edf, hca):
    #st.write(edf[hca].head())
    #edf[hca].hist(bins=5, figsize=(10,8), rwidth=0.8))
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_xlabel(hca)
    ax.set_ylabel('Headcount')
    ax.set_title('')
    ax.legend(title='HC Distribution', bbox_to_anchor=(1.05, 1), loc='upper left')
    ax.tick_params(axis='x', labelrotation=45)
    sns.histplot(data=edf, hue="EmployeeCount", x=hca,bins=5)
    st.pyplot(fig)



# display attirition charts
def showatrplot(x,y,df):
  
  #plt.legend(['Active HC', 'Attrition'])
  fig, ax = plt.subplots(figsize=(10, 8))
  ax.set_xlabel(x)
  ax.set_ylabel('Count')
  ax.set_title('')
  #ax.legend(title='HC Distribution', bbox_to_anchor=(1.05, 1), loc='upper left')
  ax.tick_params(axis='x', labelrotation=45)
  sns.countplot(x=x, hue=y, data=df)
  st.pyplot(fig)
     



def Intro():

    st.title('People Analytics - Talent Mangement')
    st.write('### Integreted HR Talent Data Analysis Dashboard ###')
    
    st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    /* Change the default text color */
    body {
        color: black;
    }
    
    /* Change the header color */
    h1,h2,h3,h4,h5,h6 {
        color: gray;
    }
    /* Targeting all subheaders */
    .css-1s0hp0w {
        font-size: 10px; /* Adjust the size as needed */
    }
    /* Change font throughout the app */
    body {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    /* Custom styles for the radio buttons */
    div.row-widget.stRadio > div {
        display: flex;
        flex-direction: row;
    }
    
    /* Style each radio item (optional) */
    div.row-widget.stRadio > div > label {
        background-color: #efefef;  /* Light grey background */
        padding: 3px 5px;          /* Padding around text */
        border-radius: 10px;        /* Rounded corners */
        margin-right: 3px;          /* Space between items */
    }
    
    /* Style for checked radio item (optional) */
    div.row-widget.stRadio > div > label[data-baseweb="radio"] > div:first-child > div {
        background-color: blue !important; /* Blue background for selected item */
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.write("### Data Driven Decisions for HR")
    st.image('bannerdai.jpg', width=900, caption='')
    
    st.write("")
    st.write("")
    st.write("Dashboard created by DA Team [Ayrin, Mittu, Shanistha, Rajesh]")

# end intro




def summary_analysis():
    
    st.title("Headcount and Attrition Summary")
    
    st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    /* Change the default text color */
    body {
        color: black;
    }
    
    /* Change the header color */
    h1,h2,h3,h4,h5,h6 {
        color: gray;
    }
    /* Targeting all subheaders */
    .css-1s0hp0w {
        font-size: 10px; /* Adjust the size as needed */
    }
    /* Change font throughout the app */
    body {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    /* Custom styles for the radio buttons */
    div.row-widget.stRadio > div {
        display: flex;
        flex-direction: row;
    }
    
    /* Style each radio item (optional) */
    div.row-widget.stRadio > div > label {
        background-color: #efefef;  /* Light grey background */
        padding: 3px 5px;          /* Padding around text */
        border-radius: 10px;        /* Rounded corners */
        margin-right: 3px;          /* Space between items */
    }
    
    /* Style for checked radio item (optional) */
    div.row-widget.stRadio > div > label[data-baseweb="radio"] > div:first-child > div {
        background-color: blue !important; /* Blue background for selected item */
    }
    </style>
    """, unsafe_allow_html=True)
    
    edf=read_data()
    
    cols=['Age', 'Attrition','Education', 'Gender','Department','JobSatisfaction','EnvironmentSatisfaction', 
          'WorkLifeBalance', 'MonthlyIncome','YearsSinceLastPromotion',
          'YearsAtCompany', 'YearsInCurrentRole','JobSatisfaction','YearsAtCompany',
          'OverTime'
          ]
    edf=edf[cols]
    
    
    hedf=edf[edf['Attrition']==0]
    hedf['Attrition']=hedf['Attrition'].apply(lambda x:"Yes" if x==1 else "No")
    hedf['OverTime']=hedf['OverTime'].apply(lambda x:"Yes" if x==1 else "No")

    
    # Calculating attrition Rate
    # total employees
    tot_emp=len(edf)
    left_emp=edf[edf['Attrition']==1].count()
    stayed_emp=edf[edf['Attrition']==0].count()
                   
    st.write("\n")
    st.write('### Total Employees in Dataset: ',tot_emp)
    st.write('### Employee Separated: ',left_emp['Attrition'])
    st.write('### Current Active Employee: ',stayed_emp['Attrition'])
    st.write('### Attrition Rate(%): ',round(left_emp['Attrition']/tot_emp*100,1))
    st.write("\n")
    st.write("\n")
    
    
    st.write("### Active Population Means  ###")
    st.table(hedf. mean(numeric_only=True))
    
    st.write("### Active Population Medians  ###")
    st.table(hedf. median(numeric_only=True))

    hedf=edf[edf['Attrition']==1]
    hedf['Attrition']=hedf['Attrition'].apply(lambda x:"Yes" if x==1 else "No")
    hedf['OverTime']=hedf['OverTime'].apply(lambda x:"Yes" if x==1 else "No")
    
    st.write("### Separated Population Means  ###")
    st.table(hedf. mean(numeric_only=True))
    
    st.write("### Separated Population Medians  ###")
    st.table(hedf. median(numeric_only=True))
    



def hc_analysis():
        
    st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    /* Change the default text color */
    body {
        color: black;
    }
    
    /* Change the header color */
    h1,h2,h3,h4,h5,h6 {
        color: green;
    }
    /* Targeting all subheaders */
    .css-1s0hp0w {
        font-size: 10px; /* Adjust the size as needed */
    }
    /* Change font throughout the app */
    body {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    /* Custom styles for the radio buttons */
    div.row-widget.stRadio > div {
        display: flex;
        flex-direction: row;
    }
    
    /* Style each radio item (optional) */
    div.row-widget.stRadio > div > label {
        background-color: #efefef;  /* Light grey background */
        padding: 3px 5px;          /* Padding around text */
        border-radius: 10px;        /* Rounded corners */
        margin-right: 3px;          /* Space between items */
    }
    
    /* Style for checked radio item (optional) */
    div.row-widget.stRadio > div > label[data-baseweb="radio"] > div:first-child > div {
        background-color: blue !important; /* Blue background for selected item */
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.write("### Active Talent - Headcount Analysis ###")
    
    edf=read_data()
    hedf=edf[edf['Attrition']==0]
    #hedf.shape

    hc_name_mapping = {
        
        'YearsAtCompany': 'YearsAtCompany',
        'Age': 'Age',
        'MonthlyIncome': 'MonthlyIncome',
        'Department':'Department',
        'Gender' : 'Gender',
        
        
        
    }
    
    
    
    selected_hc_name = st.radio(
        "Select headcount type:",
        list(hc_name_mapping.keys())
    )
    
    #st.write(selected_hc_name)
    
    hcas(edf,selected_hc_name)
    
         
   

def at_analysis():
        
    st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    /* Change the default text color */
    body {
        color: black;
    }
    
    /* Change the header color */
    h1,h2,h3,h4,h5,h6 {
        color: green;
    }
    /* Targeting all subheaders */
    .css-1s0hp0w {
        font-size: 10px; /* Adjust the size as needed */
    }
    /* Change font throughout the app */
    body {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    /* Custom styles for the radio buttons */
    div.row-widget.stRadio > div {
        display: flex;
        flex-direction: row;
    }
    
    /* Style each radio item (optional) */
    div.row-widget.stRadio > div > label {
        background-color: #efefef;  /* Light grey background */
        padding: 3px 5px;          /* Padding around text */
        border-radius: 10px;        /* Rounded corners */
        margin-right: 3px;          /* Space between items */
    }
    
    /* Style for checked radio item (optional) */
    div.row-widget.stRadio > div > label[data-baseweb="radio"] > div:first-child > div {
        background-color: blue !important; /* Blue background for selected item */
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.write("### Attrition Analysis ###")

    edf=read_data()
    
    attrition_radio_options=['Department', 
                             'Education', 
                             'Age',
                             'Gender',
                             'JobRole',
                             'YearsAtCompany',
                             'JobSatisfaction',
                             'OverTime'
                             
                             ]
    #attrition_captions=['Departments','Education','By Age']
    at_label="Select Attrition Type"
    atr=st.radio(label=at_label,options=attrition_radio_options,captions=[])
    #st.write(atr) 
    
    showatrplot(atr, 'Attrition', edf)
                
                 
  

######################################################################
#Page Display

page_names_to_funcs = {
    "—": Intro,
    "HC and Attrition Summary": summary_analysis,
    "HC Analysis": hc_analysis,
    "Attrition Analysis": at_analysis,
    
}





web_name = st.sidebar.selectbox("Choose a Dashboard", page_names_to_funcs.keys())

page_names_to_funcs[web_name]()


plt.close()
