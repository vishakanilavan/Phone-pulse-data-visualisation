#!/usr/bin/env python
# coding: utf-8

# In[29]:

import json
import pymysql
import pandas as pd
#importing sql library
from sqlalchemy import create_engine
import streamlit as st 
import plotly.express as px
import plotly.graph_objects as go


# In[ ]:


# To connect MySQL database
conn = pymysql.connect(
host='localhost',
user='root',
password = "1234",
)
# create a reference
# for sql library
engine = create_engine('mysql+pymysql://root:1234@localhost:3306/phonepe',
					echo = False)


# In[17]:


#Querying database from sql
TransactionsMode_statewise_df =pd.read_sql('transactions_statewise',engine)
BrandUsers_statewise_df=pd.read_sql('users_statewise',engine)
TransactionsMode_allindia_df=pd.read_sql('transactions_allindia',engine)
BrandUsers_allindia_df=pd.read_sql('users_allindia',engine)

Transactions_districtwise_df=pd.read_sql('mappingtransactions_statewise',engine)
Registrations_districtwise_df=pd.read_sql('mappingusers_statewise',engine)
Transactions_statewise_df=pd.read_sql('mappingtransactions_allindia',engine)
Registrations_statewise_df=pd.read_sql('mappingusers_allindia',engine)

TopTransactions_districtwise_df=pd.read_sql('toptransactions_statewise',engine)
TopRegistrations_districtwise_df=pd.read_sql('topusers_statewise',engine)
TopTransactions_statewise_df=pd.read_sql('toptransactions_allindia',engine)
TopRegistrations_statewise_df=pd.read_sql('topusers_allindia',engine)
TopTransactions_pincodewise_df=pd.read_sql('toptransactions_pincodewise',engine)
TopRegistrations_pincodewise_df=pd.read_sql('topusers_pincodewise',engine)

st.title(":violet[Phonepe Pulse Data:loudspeaker:]") 
tab1,tab2,tab3=st.tabs([':currency_exchange: Transactions',' :man-man-boy: Registered Users',':iphone: Brands'])        
                                         
                                      #Choropleth map for transactions
#__________________________________________________________________________________________________________________________________________
with tab1:
    st.subheader(':violet[Total Transactions (2018-2022):heavy_dollar_sign:]')

    #Preprocessing data for creating map
    india_state=json.load(open('C:/Users/Admin PC/myJson.geojson','r')) #loading geojsonfile

    state_list=[]#list of state names in geojson
    for i in range(len(india_state['features'])):
        states=india_state['features'][i]['properties']['Name']
        state_list.append(states)

    #list of state names as in the dataframe spelling but ordered as in the geojson 
    #replacing the these states names in geojson for exact match with dataframe
    a=['west bengal','andaman & nicobar islands','chandigarh','dadra & nagar haveli & daman & diu','delhi','haryana','jharkhand',
       'karnataka','kerala','lakshadweep','madhya pradesh','maharashtra','puducherry','tamil nadu','chhattisgarh','telangana',                    'andhra pradesh', 'goa','himachal pradesh','punjab','rajasthan','gujarat','uttarakhand','uttar pradesh','sikkim','assam',
       'arunachal pradesh','nagaland','manipur','mizoram','tripura','meghalaya','bihar','ladakh','jammu & kashmir','odisha']
     
    for i in range(len(india_state['features'])):
        india_state['features'][i]['properties']['Name']=a[i]

    # constructing the mapping dictionary of geojson and data frame to merge
    state_id_map1={}
    i=1
    for feature in india_state['features']:
        feature['id']= i
        state_id_map1[feature['properties']['Name']]=feature['id']
        i+=1
    # Creating the connecting column of geojson in Transaction_statewise data
    data =Transactions_statewise_df
    data['State_id']=data['State_name'].apply(lambda x:state_id_map1[x])
              
    select=st.selectbox("Select",('Transaction_counts','Transaction_Amounts'),key='sel1')
                            #-------------------------------------------------
    # creating choropleth map for the data
    fig=px.choropleth(data,
                 geojson=india_state,    
                  locations="State_id",
                  color=select,  #dataframe
                  color_continuous_scale='greens',
                  hover_data=['State_name','Transaction_Amounts','Transaction_counts'],
                  title='Total Transaction_counts across the states' ,  
                   #height=700
                  )
    fig.update_geos(fitbounds="locations", visible=False)
    st.plotly_chart(fig)
                                        # Transactions Data(statewise)
#-------------------------------------------------------------------------------------------------------------------------------------
    st.subheader(':violet[Transctions Analysis Statewise:moneybag:]')
    col1,col2=st.columns(2)
    with col1:
        year=st.selectbox("Year",Transactions_statewise_df['Year'].unique(),key='yr1')
    with col2:
        quarter=st.selectbox("Quarter",Transactions_statewise_df['Quarter'].unique(),key='qr1')    
    data_df=Transactions_statewise_df[(Transactions_statewise_df['Year']==year) & (Transactions_statewise_df['Quarter']==quarter)]
    data_df=data_df.sort_values(by=['Transaction_counts'])
    fig = px.bar(data_df,x='State_name', y='Transaction_counts',
                 hover_data=['State_name','Transaction_Amounts','Transaction_counts'], color='Transaction_counts',
                 labels={'Transactions amounts and counts-Statewise'}, text_auto='.1s')
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    st.plotly_chart(fig)  
                                         # Transaction Data of particular state(Yearwise)
#--------------------------------------------------------------------------------------------------------------------------------------
    st.subheader(':violet[Transaction Data of state over years :point_down:]')
    col3,col4=st.columns(2)
    with col3:
        state=st.selectbox("Select the state",Transactions_statewise_df['State_name'].unique(),key='s1') 
    with col4:
        option = st.radio("Choose",('Transaction_counts', 'Transaction_Amounts'),key='opt1')

    data_df=Transactions_statewise_df[(Transactions_statewise_df['State_name']==state)]
    #data_df=data_df.sort_values(by=['Transaction_counts'],ascending= False)
    data_df["Year_Quarter"] = data_df['Year'].astype(str) +"-"+"Q"+data_df["Quarter"].astype(str)

    fig1 = px.bar(data_df,x='Year_Quarter',y=option, hover_data=['Transaction_Amounts','Transaction_counts'], color=option,                                   labels={'Transactions amounts and counts-Yearwise'})
    st.plotly_chart(fig1)  
    fig = px.line(data_df,x='Year_Quarter', y=option)#hover_data=['Transaction_Amounts','Transaction_counts'],                                   #color='Transaction_counts')
    st.plotly_chart(fig)

                                                    # Transaction Mode 
#--------------------------------------------------------------------------------------------------------------------------------------
    st.subheader(':violet[Transaction mode proportions :money_with_wings]')
    col7,col8=st.columns(2)
    with col7:
        year1=st.selectbox("Select the Year",TransactionsMode_statewise_df['Year'].unique(),key='yr2')
        state1=st.selectbox("Select the state",TransactionsMode_statewise_df['State'].unique(),key='st2') 
    with col8:
        quarter1=st.selectbox("Select the Quarter",TransactionsMode_statewise_df['Quarter'].unique(),key='qr2')
        choice = st.radio("Choose",('Transaction_count', 'Transaction_amount'),key='opt2')

    data_df=TransactionsMode_statewise_df.loc[(TransactionsMode_statewise_df['State']==str(state1)) & 
             (TransactionsMode_statewise_df['Year']==str(year1)) & (TransactionsMode_statewise_df['Quarter']==int(quarter1))]       
    fig3 = px.pie(data_df,values=choice, names='Transaction_type',color_discrete_sequence=px.colors.sequential.RdBu)
    st.plotly_chart(fig3)
                                               # Registered Users data
              
#------------------------------------------------------------------------------------------------------------------------------------------
with tab2:
    st.subheader(':violet[Registered Users of Phonepe For particular Quarter and Year :man-man-boy-boy:] ')
    col9,col10=st.columns(2)
    with col9:
        year2=st.selectbox("Year",Registrations_statewise_df['Year'].unique(),key='yr_3')
    with col10:
        quarter2=st.selectbox("Quarter",Registrations_statewise_df['Quarter'].unique(),key='qr_3')    
    data_df=Registrations_statewise_df[(Registrations_statewise_df['Year']==year2) & (Registrations_statewise_df['Quarter']==quarter2)]
    data_df=data_df.sort_values(by=['Registered_users'])
    fig = px.bar(data_df,x='State_name', y='Registered_users',
                 hover_data=['State_name','Registered_users','App_opens'], color='Registered_users',
                 labels={' Registered Users Statewise'}, text_auto='.1s')
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    st.plotly_chart(fig)
    
    st.subheader(':violet[Registered Users of state over Years :point_down:]')
    col11,col12=st.columns(2)
    with col11:
        state2=st.selectbox("Select the state",Registrations_statewise_df['State_name'].unique(),key='st_3') 
    with col12:
        data_df=Registrations_statewise_df[(Registrations_statewise_df['State_name']==state2)]
        #data_df=data_df.sort_values(by=['Transaction_counts'],ascending= False)
        data_df["Year_Quarter"] = data_df['Year'].astype(str) +"-"+"Q"+data_df["Quarter"].astype(str)

    fig1 = px.bar(data_df,x='Year_Quarter',y='Registered_users', hover_data=['State_name','Registered_users','App_opens'],                                        color='Registered_users',labels={'Transactions amounts and counts-Yearwise'})
    st.plotly_chart(fig1)

    fig = px.line(data_df,x='Year_Quarter', y='Registered_users') #hover_data=['Transaction_Amounts','Transaction_counts'],                                   #color='Transaction_counts')
    st.plotly_chart(fig)
        
                                           # Mobile Brand data
# -----------------------------------------------------------------------------------------------------------------------------------

with tab3:
    st.subheader(':violet[Mobile Brand share for particular state :calling:]')
    col13,col14=st.columns(2)
    with col13:
        year4=st.selectbox("Select the Year",BrandUsers_statewise_df['Year'].unique(),key='yr4')
        state4=st.selectbox("Select the state",BrandUsers_statewise_df['State'].unique(),key='st4') 
    with col14:
        quarter4=st.selectbox("Select the Quarter",BrandUsers_statewise_df['Quarter'].unique(),key='qr4')

    data_df=BrandUsers_statewise_df.loc[(BrandUsers_statewise_df['State']==str(state4)) & 
             (BrandUsers_statewise_df['Year']==str(year4)) & (BrandUsers_statewise_df['Quarter']==int(quarter4))]       
    fig = px.pie(data_df,values='Brand_Users', names='Brand_name',color_discrete_sequence=px.colors.sequential.RdBu,hole=.3,
                labels={'Percentage of brand share for particular state and Year_quarter'})
    st.plotly_chart(fig)
#--------------------------------------------------------------------------------------------------------------------------------------
    st.subheader(':violet[Growth analysis of a Brand in all Over India :boom:]')
    col15,col16=st.columns(2)
    with col15:
        brand=st.selectbox("Select the state",BrandUsers_allindia_df['Brand_name'].unique(),key='br') 
    with col16:
        data_df=BrandUsers_allindia_df[(BrandUsers_allindia_df['Brand_name']==brand)]
        #data_df=data_df.sort_values(by=['Transaction_counts'],ascending= False)
        data_df["Year_Quarter"] = data_df['Year'].astype(str) +"-"+"Q"+data_df["Quarter"].astype(str)

    fig1 = px.bar(data_df,x='Year_Quarter',y='Brand_Users', hover_data=['Brand_name','Brand_Users','Percentage'],                                        color='Brand_Users',labels={'Brand Users counts-Yearwise'})
    st.plotly_chart(fig1)
                                                #Top contents
#------------------------------------------------------------------------------------------------------------------------------------------
with st.sidebar:
    st.header(":violet[Top Data:crown:]")
    option=st.selectbox("Select",('Registered Users','Transactions','Brands'),key='opt3')
    if option=='Registered Users':
        col17,col18=st.columns(2)
        with col17:
            year5=st.selectbox("Year",TopRegistrations_statewise_df['Year'].unique(),key='yr5')
        with col18:
            quarter5=st.selectbox("Quarter",TopRegistrations_statewise_df['Quarter'].unique(),key='qr5')    
        data_df=TopRegistrations_statewise_df[(TopRegistrations_statewise_df['Year']==year5) &                                 
                                            (TopRegistrations_statewise_df['Quarter']==quarter5)]
        data_df.drop(['index','Year','Quarter'],axis=1,inplace=True)
        st.markdown("Top "+option+" :gem:")
        st.markdown(data_df[['State_name','Registered_Users']].style.hide(axis="index").to_html(), unsafe_allow_html=True)
    if option=='Transactions':
        col19,col20=st.columns(2)
        with col19:
            year6=st.selectbox("Year",TopTransactions_statewise_df['Year'].unique(),key='yr6')
            quarter6=st.selectbox("Quarter",TopTransactions_statewise_df['Quarter'].unique(),key='qr6')
        with col20:
            choice2=st.selectbox("Choose",('Total_counts','Amounts'),key='opt4')
            
        data_df=TopTransactions_statewise_df[(TopTransactions_statewise_df['Year']==year6) &                                 
                                            (TopTransactions_statewise_df['Quarter']==quarter6)]
        data_df.drop(['index','Year','Quarter'],axis=1,inplace=True)
        st.markdown("Top "+option+" :gem:")
        st.markdown(data_df[['State_name',choice2]].style.hide(axis="index").to_html(), unsafe_allow_html=True)
    if option=='Brands':
        col21,col22=st.columns(2)
        with col21:
            year7=st.selectbox("Year",BrandUsers_allindia_df['Year'].unique(),key='yr7')           
        with col22:
            quarter7=st.selectbox("Quarter",BrandUsers_allindia_df['Quarter'].unique(),key='qr7')
        
        st.markdown("Top "+option+" :gem:")     
        data_df=BrandUsers_allindia_df[(BrandUsers_allindia_df['Year']==year7) & (BrandUsers_allindia_df['Quarter']==quarter7)]
        data_df=data_df.sort_values(by=['Brand_Users'],ascending=False).head(5)
        st.markdown(data_df[['Brand_name','Brand_Users']].style.hide(axis="index").to_html(), unsafe_allow_html=True)





