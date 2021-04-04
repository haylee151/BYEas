# BYEas
Say GoodBye to Biased Data

## Background
Bias in data and modeling is prevalent. Bias in machine learning can be applied when collecting the data to build the models, it can also come with testing the output of the models to verify their validity. 

Bias can come from many places, but commonly it results from a distorted population. Data is not representative of the individuals and groups we are looking to build models for. Especially when it comes to financial service industries it could be very **time consuming**, **complicated** and **expensive** to try and naturally acquire more data.

## What BYEas does
BYEas leverages deep learning algorithm to help you generate more synthetic data based on the column, condition and the amount you choose. BYEas also helps you understand the dataset you uploaded and provide data insight to you.

<img width="1245" alt="BYEas Platform" src="https://user-images.githubusercontent.com/81873621/113487651-4986d100-9487-11eb-9cb2-e440bbc05446.png">

<img width="1428" alt="Screen Shot 2021-04-03 at 2 19 05 PM" src="https://user-images.githubusercontent.com/81873621/113487706-99fe2e80-9487-11eb-84ac-c3e868d22bcf.png">

<img width="1255" alt="BYEasVis" src="https://user-images.githubusercontent.com/81873621/113487718-a97d7780-9487-11eb-97ee-8392dea2810b.png">

<img width="1245" alt="data" src="https://user-images.githubusercontent.com/81873621/113487727-ae422b80-9487-11eb-94d6-365e3d8f33cb.png">

## How we built it
**Synthetic data is our solution.** 

Synthetic data, by its name, is not collected by any real life survey or experiment. It learns from the real dataset and resembles the real data as some fake data programmatically.

Synthetic data can be used for:  
-- **Protecting data privacy**   
-- **Solving data scarcity**  
-- **Improving model performance**  

## Accomplishments that we're proud of

We helped users say goodbye to imbalanced data. We use synthetic data by making data more representative of the population you wish to model. Not only can we use BYEas in the financial service industry to help balance data, but we can also apply BYEas in many other industries as well !

Synthetic data will allow data scientists to continue ongoing work without involving real/sensitive data.

## What's next for BYEas

We are planning add an evaluator section in BYEas to show the user how synthetic data's distribution compare to real data we have. This will help the user have more confident in the data BYEas generated for them. 

## App Installation

Our application is run as a streamlit app. To install, clone the repository into a directory and make sure to install the requirements.txt to make sure you have the following dependecies while running the application:

  * sdv==0.8.0
  * numpy==1.20.1
  * streamlit==0.75.0
  * pandas==1.1.4
 
To Install Requirments:
`python -m pip install -r requirements.txt`

To run the application:
`streamlit run byeas.py`
