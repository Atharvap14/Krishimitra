# Krishimitra
## Overview

Project was a part of Silicon Lab Social Entrepreneurship Challenge.
* Implemented End to End IoT based solution for precision farming
* Developed statistical models for prediction of crop states
* Deployed a multilingual web app for farmers to track the real time state of their farms.

## File Structure : 

	|
	|-ML model Training Files
	|	|-ML-DL model
	|	|	|-SLSE_AI_Model.ipynb
	|	|	|-Crop_yield_dataset.csv
	|	|-Statistical Modelling
	|	|	|-Crop_recommendation.csv
	|	|	|-Statistical_Model.ipynb
	|
	|-StreamLit Deployment
	|	|-Models_statistical
	|	|	|-model_apple.joblib
	|	|	|-model_banana.joblib
	|	|	|-...................
	|	|-Interface.py
	|	|-requirements.txt
	|-SendDataIoT.ino

SLSE_AI_Model.ipynb -> Python notebook in which various ML/ DL algorithms were explored for calculation of crop yield


Crop_yield_dataset.csv -> Dataset used in SLSE_AI_Model.ipynb


Crop_recommendation.csv -> Dataset used in Statistical_Model.ipynb


Statistical_Model.ipynb -> Python notebook in which Statistical models were trained for various crops for estimating optimum conditions for crop cultivation.


Models_statistical -> Statistical Models trained in Statistical_Model.ipynb are dumped.


Interface.py -> Interface for farmer's web app deployed at Streamlit.


requirements.txt -> Dependencies for depolyment on Streamlit cloud.


SendDataIoT.ino -> Code uploaded to NodeMCU micro-controller fot IoT device.


## USAGE:
	1. SendDataIoT.ino file is uploaded to the NodeMCU microcontroller. It should connect to a Wifi-Hotspot with ssid "V2040" and password "12345678". Replace the api-key in the code with your api-key for Thingspeak IoT cloud platform.
	2. Upload the StreamLit Deployment folder on github as a repository and deploy it on StreamLit by following the steps in given link : https://docs.streamlit.io/streamlit-cloud/get-started/deploy-an-app .
	3. Add API keys for weatherAPI and Thingspeak in StreamLit's Secret Management as shown below in TOML format.
		api_key="Your_WeatherAPI_API_Key"
		ThingspeakAPI="Your_Thingspeak_API_Key"
	4. Change the path_to_models in Interface.py to Models_statistical folder.

To Run our Interface that is already deployed on Streamlit cloud server, open the link given below.
PROTOTYPE INTERFACE LINK FOR THE FARMERS: https://share.streamlit.io/hp-sl/hp_sl_t13/main/InterIIT/Interface.py
