import joblib
import streamlit as st
import json
import pandas as pd 
import numpy as np
import urllib3
import matplotlib.pyplot as plt
import requests
import os
api_key=st.secrets["api_key"]
 
# base_url variable to store url
base_url = "http://api.weatherapi.com/v1/current.json"
 
# Give city name
city_name = 'Jodhpur'
 
# complete_url variable to store
# complete url address

complete_url = base_url+'?q='+city_name+'&key='+api_key
 
# get method of requests module
# return response object
response1 = requests.get(complete_url)
 
# json method of response object
# convert json format data into
# python format data
x = response1.json()
precp_mm=x['current']['precip_mm']
# Now x contains list of nested dictionaries
# Check the value of "cod" key is equal to
# "404", means city is found otherwise,
# city is not found
st.write(os.getcwd())
st.write("""
# KRISHIMITRA
## स्मार्ट खेती समाधान
वास्तविक समय की निगरानी के लिए
""")
def dist_fromModel(model,X):
  temp=model.mahalanobis(X)
  dist_vector = np.matmul(np.linalg.pinv(model.covariance_),(np.array([X])-np.array(model.location_)).reshape(-1,1))
  dist_vector=dist_vector.reshape(1,-1)
  return dist_vector
def predict_from_model(dist_v):
  stringtemp=''
  stringHum=''
  stringRainfall=''
  if(dist_v[0]>0.5):
    stringtemp='तापमान इष्टतम से कम है।'
  elif(dist_v[0]<-0.5):
    stringtemp='तापमान इष्टतम से अधिक है।'
  if(dist_v[1]>0.5):
    stringtemp='आर्द्रता इष्टतम से कम है।'
  elif(dist_v[1]<-0.5):
    stringtemp='आर्द्रता इष्टतम से अधिक है।'
  if(dist_v[2]>0.5):
    stringtemp='वर्षा इष्टतम से कम है।'
  elif(dist_v[2]<-0.5):
    stringtemp='वर्षा इष्टतम से अधिक है।'
  return stringtemp + stringHum  + stringRainfall

path_to_models='/app/krishimitra/InterIIT/Models_statistical'
baseURL= st.secrets["ThingspeakAPI"]
option = st.selectbox(
     'फसल का चयन करें',
     ('rice', 'maize', 'chickpea', 'kidneybeans', 'pigeonpeas', 'mothbeans', 'mungbean', 'blackgram', 'lentil', 'pomegranate', 'banana', 'mango', 'grapes', 'watermelon', 'muskmelon', 'apple', 'orange', 'papaya', 'coconut', 'cotton', 'jute', 'coffee'))
st.write('आपने चुना:', option)
if st.button('अवस्था जांच'):
    http = urllib3.PoolManager()
    response = http.request('GET', baseURL)
    data = json.loads(response.data)
    Inference_DF = pd.DataFrame(data['feeds'])
    Inference_DF=Inference_DF.drop(['entry_id'],axis=1)
    Inference_DF['field1']=pd.to_numeric(Inference_DF['field1'])
    Inference_DF['field2']=pd.to_numeric(Inference_DF['field2'])
    Inference_DF['field3']=pd.to_numeric(Inference_DF['field3'])
    st.write(
    """
    तापमान डेटा (पिछले 60 रीडिंग)

    """
    )
    with st.expander('तापमान डेटा देखें'):
        fig = plt.figure()
        plt.plot(Inference_DF.index,Inference_DF['field1'])
        plt.xlabel('Reading Number')
        plt.ylabel('Temperature (C)')
        st.write(fig)

    st.write(
    """
आर्द्रता डेटा (पिछले 60 रीडिंग)

    """
    )
    with st.expander('आर्द्रता डेटा देखें'):
        fig1 = plt.figure()
        plt.plot(Inference_DF.index,Inference_DF['field2'])
        plt.xlabel('Reading Number')
        plt.ylabel('Moisture (%)')
        st.write(fig1)

    st.write(
    """
    मृदा नमी डेटा (पिछले 60 रीडिंग)

    """
    )
    with st.expander('मृदा नमी डेटा देखें'):
        fig2 = plt.figure()
        plt.plot(Inference_DF.index,Inference_DF['field3'])
        plt.xlabel('Reading Number')
        plt.ylabel('Soil Moisture (%)')
        st.write(fig2)
        plt.show()

    st.write("""
    ## एआई आधारित फसल की स्थिति और सुझाव 
    """)
    
    model=joblib.load(path_to_models+'\model_'+option+'.joblib')
    prediction=predict_from_model(dist_fromModel(model,np.array([[Inference_DF['field1'].mean(),Inference_DF['field2'].mean(),precp_mm]]))[0]) 
    st.write("""## फसल की स्थिति""")
    st.write( prediction)

    st.write("""## दिन की कृषि भविष्यवाणियां""")
    with st.expander('दिन की कृषि भविष्यवाणियां देखें'):
        st.write(""" दिन की कृषि भविष्यवाणियां""")
    st.write("""## दिन की बाजार भविष्यवाणियां""")
    with st.expander('आज के बाजार की भविष्यवाणी देखें'):
        st.write(""" दिन की बाजार भविष्यवाणियां""")

    

