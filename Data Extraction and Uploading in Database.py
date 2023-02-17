#!/usr/bin/env python
# coding: utf-8

# Installing git from website"https://git-scm.com/download/win" manually (in case of windows)
# Run git clone https://github.com/PhonePe/pulse.git in command in desired directory.(for cloning data folder from github)


#Once created the clone of GIT-HUB repository then,Required libraries for the program
import pandas as pd
import json
import os
#importing sql library
from sqlalchemy import create_engine
import pymysql

#This is to direct the path to get the data as states

#<------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------>#
#Agg_state_list--> to get the list of states in India
path="pulse/data/aggregated/transaction/country/india/state/"  # Changeable according to the directory 
Agg_state_list=os.listdir(path)


#This is to extract the data's to create a dataframe
col={'State':[], 'Year':[],'Quarter':[],'Transaction_type':[], 'Transaction_count':[], 'Transaction_amount':[]}
for i in Agg_state_list:
    p_i=path+i+"/"
    Agg_yr=os.listdir(p_i)    
    for j in Agg_yr:
        p_j=p_i+j+"/"
        Agg_yr_list=os.listdir(p_j)        
        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            D=json.load(Data)
            for z in D['data']['transactionData']:
                Name=z['name']
                count=z['paymentInstruments'][0]['count']
                amount=z['paymentInstruments'][0]['amount']
                col['Transaction_type'].append(Name)
                col['Transaction_count'].append(count)
                col['Transaction_amount'].append(amount)
                col['State'].append(i)
                col['Year'].append(j)
                col['Quarter'].append(int(k.strip('.json'))) # String after removing '.json' from 1.json
#Succesfully created a dataframe
df1=pd.DataFrame(col)

#<------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------>#

path="pulse/data/aggregated/user/country/india/state/"  # Changeable according to the directory 
Agg_state_list=os.listdir(path)
col={'State':[], 'Year':[],'Quarter':[],'Brand_name':[], 'Brand_Users':[], 'Percentage':[],'Total_Registered_Users':[],'App_Opens':[]}
for i in Agg_state_list:
    p_i=path+i+"/"
    Agg_yr=os.listdir(p_i)    
    for j in Agg_yr:
        p_j=p_i+j+"/"
        Agg_qr_list=os.listdir(p_j)        
        for k in Agg_qr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            D=json.load(Data)
            if D['data']['usersByDevice'] is not None:
                for z in D['data']['usersByDevice']:
                    Name=z['brand']
                    count=z['count']
                    Percentage=z['percentage']
                    col['Brand_name'].append(Name)
                    col['Brand_Users'].append(count)
                    col['Percentage'].append(Percentage)
                    col['State'].append(i)
                    col['Year'].append(j)
                    col['Quarter'].append(int(k.strip('.json'))) # String after removing '.json' from 1.json
                    col['Total_Registered_Users'].append(D['data']['aggregated']['registeredUsers'])
                    col['App_Opens'].append(D['data']['aggregated']['appOpens'])
            else:
                pass
df2=pd.DataFrame(col)
#<------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------>#
path="pulse/data/map/transaction/hover/country/india/state/"  # Changeable according to the directory 
Agg_state_list=os.listdir(path)
col={'State':[], 'Year':[],'Quarter':[],'District_name':[], 'Transaction_counts':[], 'Transaction_Amounts':[]}
for i in Agg_state_list:
    p_i=path+i+"/"
    Agg_yr=os.listdir(p_i)    
    for j in Agg_yr:
        p_j=p_i+j+"/"
        Agg_qr_list=os.listdir(p_j)        
        for k in Agg_qr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            D=json.load(Data)
            #if D['data']['usersByDevice'] is not None:
            for z in D['data']['hoverDataList']:
                    Name=z['name']
                    count=z['metric'][0]['count']
                    amount=z['metric'][0]['amount']
                    col['District_name'].append(Name)
                    col['Transaction_counts'].append(count)
                    col['Transaction_Amounts'].append(amount)
                    col['State'].append(i)
                    col['Year'].append(j)
                    col['Quarter'].append(int(k.strip('.json'))) # String after removing '.json' from 1.json
df3=pd.DataFrame(col)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
path="pulse/data/map/user/hover/country/india/state/"  # Changeable according to the directory 
Agg_state_list=os.listdir(path)

col={'State':[], 'Year':[],'Quarter':[],'District_name':[], 'Registered_users':[], 'App_opens':[]}
for i in Agg_state_list:
    p_i=path+i+"/"
    Agg_yr=os.listdir(p_i)    
    for j in Agg_yr:
        p_j=p_i+j+"/"
        Agg_qr_list=os.listdir(p_j)        
        for k in Agg_qr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            D=json.load(Data)
            #if D['data']['usersByDevice'] is not None:
            for z in list(D['data']['hoverData'].keys()):
                    Name=z
                    Registeredusers=D['data']['hoverData'][z]["registeredUsers"]
                    app_opens=D['data']['hoverData'][z]["appOpens"]
                    col['District_name'].append(Name)
                    col['Registered_users'].append(Registeredusers)
                    col['App_opens'].append(app_opens)
                    col['State'].append(i)
                    col['Year'].append(j)
                    col['Quarter'].append(int(k.strip('.json'))) # String after removing '.json' from 1.json
df4=pd.DataFrame(col)

#<------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------>#
path="pulse/data/top/transaction/country/india/state/"  # Changeable according to the directory 
Agg_state_list=os.listdir(path)

col={'State':[], 'Year':[],'Quarter':[],'District_name':[], 'Total_counts':[], 'Amounts':[]}
col1={'State':[], 'Year':[],'Quarter':[],'Pincode':[], 'Total_counts':[], 'Amounts':[]}
for i in Agg_state_list:
    p_i=path+i+"/"
    Agg_yr=os.listdir(p_i)    
    for j in Agg_yr:
        p_j=p_i+j+"/"
        Agg_qr_list=os.listdir(p_j)        
        for k in Agg_qr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            D=json.load(Data)
            #if D['data']['usersByDevice'] is not None:
            dist=D["data"]["districts"]
            pincode=D['data']['pincodes']
            for z in range(len(dist)):
                    Name=dist[z]['entityName']
                    counts=dist[z]['metric']['count']
                    amounts=dist[z]['metric']['amount']
                    col['District_name'].append(Name)
                    col['Total_counts'].append(counts)
                    col['Amounts'].append(amounts)
                    col['State'].append(i)
                    col['Year'].append(j)
                    col['Quarter'].append(int(k.strip('.json')))# String after removing '.json' from 1.json
            for z1 in range(len(pincode)):
                    Name=pincode[z1]['entityName']
                    counts=pincode[z1]['metric']['count']
                    amounts=pincode[z1]['metric']['amount']
                    col1['Pincode'].append(Name)
                    col1['Total_counts'].append(counts)
                    col1['Amounts'].append(amounts)
                    col1['State'].append(i)
                    col1['Year'].append(j)
                    col1['Quarter'].append(int(k.strip('.json'))) 
df5=pd.DataFrame(col)
df5A=pd.DataFrame(col1)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
path="pulse/data/top/user/country/india/state/"  # Changeable according to the directory 
Agg_state_list=os.listdir(path)

col={'State':[], 'Year':[],'Quarter':[],'District_name':[], 'Registered_Users':[]}
col1={'State':[], 'Year':[],'Quarter':[],'Pincode':[], 'Registered_Users':[]}
for i in Agg_state_list:
    p_i=path+i+"/"
    Agg_yr=os.listdir(p_i)    
    for j in Agg_yr:
        p_j=p_i+j+"/"
        Agg_qr_list=os.listdir(p_j)        
        for k in Agg_qr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            D=json.load(Data)
            #if D['data']['usersByDevice'] is not None:
            dist=D["data"]["districts"]
            pincode=D['data']['pincodes']
            for z in range(len(dist)):
                    Name=dist[z]['name']
                    users=dist[z]['registeredUsers']
                    col['District_name'].append(Name)
                    col['Registered_Users'].append(users)
                    col['State'].append(i)
                    col['Year'].append(j)
                    col['Quarter'].append(int(k.strip('.json')))# String after removing '.json' from 1.json
            for z1 in (pincode):
                    Name=z1['name']
                    users=z1['registeredUsers']
                    col1['Pincode'].append(Name)
                    col1['Registered_Users'].append(users)
                    col1['State'].append(i)
                    col1['Year'].append(j)
                    col1['Quarter'].append(int(k.strip('.json'))) 
df6=pd.DataFrame(col)
df6A=pd.DataFrame(col1)

#<------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------>#
path="pulse/data/aggregated/transaction/country/india/"  # Changeable according to the directory 
Agg_yr=os.listdir(path)
Agg_yr=Agg_yr[:-1]

col={'Year':[],'Quarter':[],'Transaction_type':[], 'Transaction_count':[], 'Transaction_amount':[]}   
for i in Agg_yr:
    p_j=path+i+"/"
    Agg_yr_list=os.listdir(p_j)        
    for j in Agg_yr_list:
        p_k=p_j+j
        Data=open(p_k,'r')
        D=json.load(Data)
        for z in D['data']['transactionData']:
            Name=z['name']
            count=z['paymentInstruments'][0]['count']
            amount=z['paymentInstruments'][0]['amount']
            col['Transaction_type'].append(Name)
            col['Transaction_count'].append(count)
            col['Transaction_amount'].append(amount)
            col['Year'].append(i)
            col['Quarter'].append(int(j.strip('.json'))) # String after removing '.json' from 1.json
df1_india=pd.DataFrame(col)

#<------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------>#
path="pulse/data/aggregated/user/country/india/"  # Changeable according to the directory 
Agg_yr=os.listdir(path)
Agg_yr=Agg_yr[:-1]

col={'Year':[],'Quarter':[],'Brand_name':[], 'Brand_Users':[], 'Percentage':[],'Total_Registered_Users':[],'App_Opens':[]}
for j in Agg_yr:
    p_j=path+j+"/"
    Agg_qr_list=os.listdir(p_j)        
    for k in Agg_qr_list:
        p_k=p_j+k
        Data=open(p_k,'r')
        D=json.load(Data)
        if D['data']['usersByDevice'] is not None:
            for z in D['data']['usersByDevice']:
                Name=z['brand']
                count=z['count']
                Percentage=z['percentage']
                col['Brand_name'].append(Name)
                col['Brand_Users'].append(count)
                col['Percentage'].append(Percentage)
                col['Year'].append(j)
                col['Quarter'].append(int(k.strip('.json'))) # String after removing '.json' from 1.json
                col['Total_Registered_Users'].append(D['data']['aggregated']['registeredUsers'])
                col['App_Opens'].append(D['data']['aggregated']['appOpens'])
            else:
                pass
df2_india=pd.DataFrame(col)

#<------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------>#
path="pulse/data/map/transaction/hover/country/india/"  # Changeable according to the directory 
Agg_yr=os.listdir(path)
Agg_yr=Agg_yr[:-1]
col={'Year':[],'Quarter':[],'State_name':[], 'Transaction_counts':[], 'Transaction_Amounts':[]}
    
for j in Agg_yr:
    p_j=path+j+"/"
    Agg_qr_list=os.listdir(p_j)        
    for k in Agg_qr_list:
        p_k=p_j+k
        Data=open(p_k,'r')
        D=json.load(Data)
        #if D['data']['usersByDevice'] is not None:
        for z in D['data']['hoverDataList']:
            Name=z['name']
            count=z['metric'][0]['count']
            amount=z['metric'][0]['amount']
            col['State_name'].append(Name)
            col['Transaction_counts'].append(count)
            col['Transaction_Amounts'].append(amount)
            col['Year'].append(j)
            col['Quarter'].append(int(k.strip('.json'))) # String after removing '.json' from 1.json
df3_india=pd.DataFrame(col)

#<------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------>#
path="pulse/data/map/user/hover/country/india/"  # Changeable according to the directory 
Agg_yr=os.listdir(path)
Agg_yr=Agg_yr[:-1]
col={'Year':[],'Quarter':[],'State_name':[], 'Registered_users':[], 'App_opens':[]}   
for j in Agg_yr:
    p_j=path+j+"/"
    Agg_qr_list=os.listdir(p_j)        
    for k in Agg_qr_list:
        p_k=p_j+k
        Data=open(p_k,'r')
        D=json.load(Data)
        #if D['data']['usersByDevice'] is not None:
        for z in list(D['data']['hoverData'].keys()):
                Name=z
                Registeredusers=D['data']['hoverData'][z]["registeredUsers"]
                app_opens=D['data']['hoverData'][z]["appOpens"]
                col['State_name'].append(Name)
                col['Registered_users'].append(Registeredusers)
                col['App_opens'].append(app_opens)
                col['Year'].append(j)
                col['Quarter'].append(int(k.strip('.json'))) # String after removing '.json' from 1.json
df4_india=pd.DataFrame(col)


#<------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------>#
path="pulse/data/top/transaction/country/india/"  # Changeable according to the directory 
Agg_yr=os.listdir(path)
Agg_yr=Agg_yr[:-1]

col={'Year':[],'Quarter':[],'State_name':[], 'Total_counts':[], 'Amounts':[]}
    
for j in Agg_yr:
    p_j=path+j+"/"
    Agg_qr_list=os.listdir(p_j)        
    for k in Agg_qr_list:
        p_k=p_j+k
        Data=open(p_k,'r')
        D=json.load(Data)
        #if D['data']['usersByDevice'] is not None:
        state=D["data"]["states"]
        for z in range(len(state)):
                Name=state[z]['entityName']
                counts=state[z]['metric']['count']
                amounts=state[z]['metric']['amount']
                col['State_name'].append(Name)
                col['Total_counts'].append(counts)
                col['Amounts'].append(amounts)
                col['Year'].append(j)
                col['Quarter'].append(int(k.strip('.json')))# String after removing '.json' from 1.json
df5_india=pd.DataFrame(col)

#<------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------>#
path="pulse/data/top/user/country/india/"  # Changeable according to the directory 
Agg_yr=os.listdir(path)
Agg_yr=Agg_yr[:-1]

col={'Year':[],'Quarter':[],'State_name':[], 'Registered_Users':[]}
   
for j in Agg_yr:
    p_j=path+j+"/"
    Agg_qr_list=os.listdir(p_j)        
    for k in Agg_qr_list:
        p_k=p_j+k
        Data=open(p_k,'r')
        D=json.load(Data)
        #if D['data']['usersByDevice'] is not None:
        state=D["data"]["states"]
        for z in range(len(dist)):
                Name=state[z]['name']
                users=state[z]['registeredUsers']
                col['State_name'].append(Name)
                col['Registered_Users'].append(users)
                col['Year'].append(j)
                col['Quarter'].append(int(k.strip('.json')))# String after removing '.json' from 1.json
df6_india=pd.DataFrame(col) 
#------------------------------------------------------------------------------------------------------------------------------------------ 

# To connect MySQL database
conn = pymysql.connect(
    host='localhost',
    user='root',
    password = "1234",
    database='phonepe'
    )

#cur = conn.cursor()
#creating new database
#cur.execute('CREATE DATABASE phonepe') #For starting up only 

# create a reference for sql library
engine = create_engine('mysql+pymysql://root:1234@localhost:3306/phonepe',echo = False)

# Attach the data frame to the sql with a name of the table
df1.to_sql('transactions_statewise',con = engine,if_exists='replace')
df2.to_sql('users_statewise',con = engine,if_exists='replace')
df3.to_sql('mappingtransactions_statewise',con = engine,if_exists='replace')
df4.to_sql('mappingusers_statewise',con = engine,if_exists='replace')
df5.to_sql('toptransactions_statewise',con = engine,if_exists='replace')
df6.to_sql('topusers_statewise',con = engine,if_exists='replace')
df1_india.to_sql('transactions_allindia',con = engine,if_exists='replace')
df2_india.to_sql('users_allindia',con = engine,if_exists='replace')
df3_india.to_sql('mappingtransactions_allindia',con = engine,if_exists='replace')
df4_india.to_sql('mappingusers_allindia',con = engine,if_exists='replace')
df5_india.to_sql('toptransactions_allindia',con = engine,if_exists='replace')
df6_india.to_sql('topusers_allindia',con = engine,if_exists='replace')
