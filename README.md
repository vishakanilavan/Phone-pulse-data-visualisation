
# PHONEPE  DATA VISUALIZATION


Phonepe is one of most used payment apps in india nowadays.This project helps in collecting data from phonepe pulse  and visualize the data's for the deep understanding of momney transactions and payments industry in India.

## DATA LINK:
```bash
https://github.com/PhonePe/pulse
```

## WORKFLOW OF THE PROJECT:
```bash
1)GITHUB CLONING AND DATA EXTRACTION:
 ```
 Get the data from the phonepe pulse data folder by git clone to local system.Then extract the data from the local data folder.
```bash
 2)UPLOADING DATAS TO MYSQL DATABASE:
 ```
 After getting data,upload the data in sql database using mysql connector or pymsql.

 ```bash
 3)QUERYING PHONEPE DATA FROM SQL:
 ```
 Next, Retrieve the data from sql database using pymsql for connecting python with sql and sqlalchemy for easy handling of dataframes in mysql
```bash
 4)DATA VISUALIZATION USING PLOTLY IN STREAMLIT WEB:
 ```
 The final step is visualising the phonepe data.Some of the visualisation are geo visualisation for visualising based on locations,bar charts, pie charts. These visualisation helps in deep understanding of growth and progression of phonepe app.

## EXECUTION OF PROJECT 

## Pre requisite Installation
You should install the latest version of python for executing this project
```bash
  pip install streamlit
  pip install pymsql
  pip install pandas
  pip install sqlalchemy
  pip install plotly
```
## Run Locally
Clone the project

```bash
  git clone https://github.com/vishakanilavan/Phone-pulse-data-visualisation
``
```


Change the directory to directory of project file

```bash
Go to the downloaded/cloned project directory in prompt cmd
```

```bash
for example:
  cd C:\Users\Admin PC\Downloads
```

Now Run the below command
```bash
streamlit run "filename.py"
```
```bash 
for example:
streamlit run "phonepe data visualisation.py"
```

Accessing the localhost server

```bash
 You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.43.83:8501
```

  click the above link to display the created Twitter scraping web app
## Screenshots:

[![Phonepe-data-visualisation.png](https://i.postimg.cc/x1Q2Z4CG/Phonepe-data-visualisation.png)](https://postimg.cc/VdKpr4X5)

## Demo:
Here's My demo video  of the project
in linkedin's profile

https://www.linkedin.com/in/vishaka-nilavan-9345aa138/


A brief description of functional work of this project.
