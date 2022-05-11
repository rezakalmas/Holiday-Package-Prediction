
# Holiday Package Prediction Using Machine Learning

This project predicts whether customers will be purchasing the product or not, based on customer identity and behavior.

## Context
"Trips & Travel.Com" company wants to enable and establish a viable business model to expand the customer base. One of the ways to expand the customer base is to introduce a new offering of packages. Currently, there are 5 types of packages the company is offering - Basic, Standard, Deluxe, Super Deluxe, King. Looking at the data of the last year, we observed that 18% of the customers purchased the packages. However, the marketing cost was quite high because customers were contacted at random without looking at the available information. The company is now planning to launch a new product i.e. Wellness Tourism Package. Wellness Tourism is defined as Travel that allows the traveler to maintain, enhance or kick-start a healthy lifestyle, and support or increase one's sense of well-being. However, this time company wants to harness the available data of existing and potential customers to make the marketing expenditure more efficient. 

this analysis's purpose is to identify potential customers and to change marketing strategy for no potential customers which make consumers more interested in our products, this analysis can enlarge the customer base even more.

You can download datasets and more freely. [Click Here](https://www.kaggle.com/datasets/susant4learning/holiday-package-purchase-prediction)

## Data and Assumption
### We have 20 features in this data :
- CustomerID : Unique customer ID
- ProdTaken : Product taken or not (0: No, 1: Yes)
- Age : Age of customer
- TypeofContact : How customer was contacted (Company Invited or Self Inquiry)
- CityTier : City tier depends on the development of a city, population, facilities, and living standards. The categories are ordered i.e.
- DurationOfPitch : Duration of the pitch by a salesperson to the customer
- Occupation : Occupation of customer
- Gender : Gender of customer
- NumberOfPersonVisiting : Total number of persons planning to take the trip with the customer
- NumberOfFollowups : Total number of follow-ups has been done by the salesperson after the sales pitch
- ProductPitched : Product pitched by the salesperson
- PreferredPropertyStar : Preferred hotel property rating by customer
- MaritalStatus : Marital status of customer
- NumberOfTrips : Average number of trips in a year by customer
- Passport : The customer has a passport or not (0: No, 1: Yes)
- PitchSatisfactionScore : Sales pitch satisfaction score
- OwnCar : Whether the customers own a car or not (0: No, 1: Yes)
- NumberOfChildrenVisiting : Total number of children with age less than 5 planning to take the trip with the customer
- Designation : Designation of the customer in the current organization
- MonthlyIncome : Gross monthly income of the customer

## Exploratory Data Analysis 
### Univariate Analysis
<a href="https://ibb.co/kBWwWQ4"><img src="https://i.ibb.co/bm8C8zs/univariate-analysis-cat.png" alt="univariate-analysis-cat" border="0"></a>
<a href="https://ibb.co/94vPFSm"><img src="https://i.ibb.co/SmxShGD/univariate-analysis-num.png" alt="univariate-analysis-num" border="0"></a>
### Bivariate Analysis
<a href="https://ibb.co/5jQWW8M"><img src="https://i.ibb.co/SmkXXns/multivariate-analysis-cat.png" alt="multivariate-analysis-cat" border="0"></a>
<a href="https://ibb.co/dr5WTTG"><img src="https://i.ibb.co/9Nr8DDs/multivariate-analysis-num.png" alt="multivariate-analysis-num" border="0"></a>
### Multivariate Analysis
<a href="https://ibb.co/jMt4vBR"><img src="https://i.ibb.co/J7ZkR0Q/heatmap.png" alt="heatmap" border="0"></a>


### Initial insight from EDA
<a href="https://ibb.co/bbKcHHv"><img src="https://i.ibb.co/KKrTNNs/insight1.png" alt="insight1" border="0"></a>
<a href="https://ibb.co/gFBRH6j"><img src="https://i.ibb.co/NnHyQ7V/insight2.png" alt="insight2" border="0"></a>
<a href="https://ibb.co/t86FK35"><img src="https://i.ibb.co/jgYsfHF/insight3.png" alt="insight3" border="0"></a>
<a href="https://ibb.co/Wzvyhgs"><img src="https://i.ibb.co/hdFW6DC/insight4.png" alt="insight4" border="0"></a>
<a href="https://ibb.co/QmFxQCw"><img src="https://i.ibb.co/f0YTFnw/insight5.png" alt="insight5" border="0"></a>
<a href="https://ibb.co/ByrN48h"><img src="https://i.ibb.co/ZBYmHyQ/insight6.png" alt="insight6" border="0"></a>

### Feature Selection
1. Using Variance threshold = We assume that with less variance the feature the result will be biased.
2. Using Fclassif for numerical feature
3. Using Chi Square for numerical feature
4. For getting best value using K best in each Selection
<a href="https://ibb.co/5TXsYds"><img src="https://i.ibb.co/JnWrxNr/Capture.png" alt="Capture" border="0"></a>

### Machine Learning Model and Result
I use 5 Algoritm for modeling using Accuracy Score :
- Logistic Regression
- Decision Tree
- Random Forest
- AdaBoost
- XGBoost

<a href="https://ibb.co/4p60nv0"><img src="https://i.ibb.co/GRKr4Yr/Capture.png" alt="Capture" border="0"></a>
<a href="https://ibb.co/bskCZqm"><img src="https://i.ibb.co/Htjbs14/Capture.png" alt="Capture" border="0"></a>

## Conclusions
### Feature and Model
- the features we use for modeling after selecting there are 12 :
DurationOfPitch, NumberOfFollowups, NumberOfTrips, MonthlyIncome, CityTier, ProductPitched, PreferredPropertyStar, Passport, PitchSatisfactionScore, Designation, MaritalStatus_Married, MaritalStatus_Unmarried.
- The Best model that we choose is **XGBoost**
### Feature Importance and Insight
<a href="https://ibb.co/xMXykPn"><img src="https://i.ibb.co/WcGQhqr/feature-importance.png" alt="feature-importance" border="0"></a>

Best of 2 feature is Product Pitch and Passport Ownership 
#### 

<a href="https://ibb.co/mvNCFb0"><img src="https://i.ibb.co/6vXRJr8/Capture.png" alt="Capture" border="0"></a>

From shap observations above it is known that:
1. If you have a passport, living in a tier 3 city and unmarried will be positively worth the model (buying). 
2. selection of basic products that are pitched and the more followed up, the more positive value with the model.

### Gain & Lift analysis
<a href="https://imgbb.com/"><img src="https://i.ibb.co/ZfVykR3/gain.png" alt="gain" border="0"></a>
<a href="https://imgbb.com/"><img src="https://i.ibb.co/BVHzWRc/lift.png" alt="lift" border="0"></a>

It is known from the gain table above if using 20% of the data, this model can predict 80% of all responses. And from the lift table we can see if using 20% of the data then the performance is 4x the random value. It can be concluded that this model is very good at predicting and not just coincidences.


## Advice
1. The best seller in our product is Basic, we can promote other products with some discounts or free stuff
2. For Telemarketing, the more followups are better but max time to promote the product is 20 minutes
3. Need more analysis, why customers with passport ownership more interested, are our products must go abroad.
4. Need focus at customers which live in city tier 3, have a passport, unmarried, low in designation

## Requirements

- [Pandas](https://pandas.pydata.org/)
- [Numpy](https://numpy.org/)
- [Matplotlib](https://matplotlib.org/)
- [Seaborn](https://seaborn.pydata.org/)
- [Scikit Learn](https://scikit-learn.org/stable/index.html)
- [Flask](https://flask.palletsprojects.com/en/2.1.x/)

For further information about the library that I'm using, please read the requirements.txt file

## Table of Contents
- Data Undarstanding
- Data Overview, EDA and Insight
- Data Cleaning and Preparation
- ML Modeling and Evaluation 
- Bussiness Insight and Recomendations

At last The best Algoritm for our project is XGBoost
## Screenshots Deployment

### Home Page:
![App Screenshot](https://i.ibb.co/c1rS19p/Capture.png)

### Result Page:
![App Screenshot](https://i.ibb.co/G50TDmy/Capture.png)



## 🚀 About Me
### Hi, I'm Reza Kalmas! 👋

👀 I’m interested in Data Scientist and Data analyze

🌱 I’m currently learning Power BI

💞️ I’m looking to collaborate on some projects in Machine Learning.

📫 𝗥𝗲𝗮𝗰𝗵 𝗼𝘂𝘁 𝘁𝗼 𝗺𝗲 𝗱𝗶𝗿𝗲𝗰𝘁𝗹𝘆 𝗮𝘁: kangmasrip@gmail.com or on my LinkedIn


## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://github.com/rezakalmas/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/reza-kalmas-21728a188)
## 🛠 Skills
PostgreSQL, Google Colab, Jupyter notebook, Juppyterlab, Python, Machine Learning, Analytics
