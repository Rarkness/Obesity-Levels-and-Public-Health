![Python](https://img.shields.io/badge/python-3.9-blue)
![License](https://img.shields.io/badge/license-MIT-green)<br>
## **Data Science Institute - Cohort 5 - Team 3 Project**

---

# 🩺 **Obesity Levels Based on<br>Eating Habits and Physical Condition**❤️
---
# **Table of Contents**

- [Team Members](#team-members)
- [Project Overview](#project-overview)
- [Introduction](#introduction)
- [Problem Statement](#problem-statement)
- [Business Goal](#business-goal)
- [Expected Benefits](#expected-benefits)
- [Data Science Approach](#data-science-approach)
- [Model Objectives](#model-objectives)
- [Methodology](#methodology)
- [Requirements](#requirements)
- [Data Overview](#data-overview)
- [Cleaning the Data](#cleaning-the-data)
- [Proposed Solution](#proposed-solution)
- [Implementation](#implementation)
- [Next Steps](#next-steps)
- [Risks and Mitigations](#risks-and-mitigations)
- [Results](#results)
- [Conclusion](#conclusion)
---
# **Team Members**
 
🧮 **Bitewulign Mekonnen**<br>
📈 **Gulrukh Aqeel**<br>
📊 **Kate Antonova**<br>
🗂️ **Richard Harkness**<br>
📉 **Yalda Rahmati**<br>

---
# **Project Overview**

As part of the Data Science Certificate program at the University of Toronto’s Data Sciences Institute, we selected the Estimation of Obesity Levels Based on Eating Habits and Physical Condition dataset and conducted a compelling study on which lifestyle factors have the greatest impact on obesity levels, applying the analytical and technical skills we developed throughout the course.
This study offers practical advice for public health authorities, health and wellness providers, and insurers looking to address obesity-related risks.
This business case proposes using a validated dataset and analytical models to accurately estimate and predict obesity levels based on eating habits, physical conditions and other factors. 

---

# **Introduction**

Obesity is an escalating global health issue that significantly contributes to a range of chronic diseases, including heart disease, diabetes, and certain cancers. It is also associated with reduced life expectancy and leads to increased healthcare expenditures due to the need for long-term management of obesity-related conditions. Addressing this issue is crucial for improving public health outcomes and reducing the economic burden on healthcare systems.<br>

This business case delves into the promising application of the dataset titled "Estimation of Obesity Levels Based on Eating Habits and Physical Condition." By utilizing this comprehensive dataset, we aim to develop sophisticated predictive models that can accurately estimate obesity levels based on individuals' eating habits and physical conditions. These models will provide valuable insights to inform public health strategies and initiatives.<br>

With the integration of data analytics, we can enhance the effectiveness of public health campaigns by targeting specific populations at risk of obesity and tailoring interventions accordingly. Furthermore, this dataset can be leveraged to personalize health interventions, offering customized recommendations and support to individuals striving to achieve and maintain a healthy weight. 
Our primary objective is to harness the power of data to improve the prediction and prevention of obesity. By doing so, we hope to foster a healthier society, extend life expectancy, and alleviate the financial strain on healthcare systems worldwide.

---
# **Problem Statement**
 
Obesity affects millions worldwide, raising healthcare costs, reducing productivity, and increasing the risk of chronic diseases like diabetes and heart disease. Traditional methods, like self-reports and BMI, often miss key factors. A data-driven approach that considers eating habits, physical activity, and lifestyle offers a clearer picture. Early identification of risks can help individuals and organizations take proactive steps to improve health outcomes.

---
# **Business Goal**

🚀 **Key Insight:**  What are the key lifestyle factors (e.g., eating habits, physical activity) that contribute most to obesity levels?

We aim to use data science to build a predictive model that estimates obesity levels based on eating habits and physical health. This kind of model can help healthcare providers, fitness companies, insurance firms, and policymakers take more targeted action when it comes to preventing obesity.

---
# **Expected Benefits**
 
It helps with the early detection of obesity risks, allowing for timely interventions that can reduce long-term healthcare costs. Insurance companies and corporate wellness programs can use it to categorize policyholders or employees by risk level, making health initiatives more targeted and effective. Healthcare providers can support preventive care and deliver personalized treatments, while governments and policymakers gain evidence-based insights to guide public health campaigns and shape policy. In the fitness and wellness space, it enhances personalized health plans, and for individuals, it provides valuable insights to make informed decisions about their health and lifestyle.

---
# **Data Science Approach**
 
We are adopting a structured Data Science Approach (DSA) to explore key lifestyle and demographic factors associated with obesity. The following outlines our initial plan, which will evolve as we continue to refine our methods and results.

### 🔎 Problem Understanding
We are in the process of clearly defining the problem, which focuses on predicting and analyzing obesity levels based on lifestyle behaviors and demographic factors. As we progress, we will continue to refine our understanding and focus areas.

### 🎯 Business Goal
Our intended goal is to help wellness providers and organizations identify the most influential factors contributing to obesity. This will guide them in designing effective health interventions and personalized wellness programs. We will revisit and adjust these goals as we uncover insights.

### 📂 Data Collection and Overview
We plan to use a widely recognized dataset from the UC Irvine Machine Learning Repository. The dataset includes synthetic data, designed to reflect real-world obesity trends while maintaining privacy. Our current focus is on understanding its structure, and we anticipate making further adjustments to how we preprocess and use the data.

### 🧹 Data Cleaning and Preparation
We have cleaning and prepared the dataset by handling missing values, and normalizing numerical features. This cleaning may evolve as we explore different preprocessing techniques and adapt our approach to improve model performance.

### 🤖 Modeling Approach and Objectives
We intend to implement learning models, with an initial focus to predict obesity levels and analyze feature importance. These modeling choices are subject to change as we experiment with different algorithms and evaluate their performance.

### 📊 Evaluation
We will evaluate our models using various metrics. Our evaluation strategy may be revised as we test different models and techniques to ensure robust and reliable outcomes.

### 🛠️ Implementation
Our plan includes deploying the final solution as a static dashboard, where users can explore obesity-related insights. The dashboard will be refined as we finalize our models and visualizations.

### 💡 Results and Conclusions
Our conclusions and recommendations will be developed as we complete our analysis.

---
# **Model Objectives**

🚀 The key objectives presented by this model are as follows:

- Utilize learning models to predict obesity levels based on lifestyle and eating habits.<br>
- Identify key risk factors contributing to obesity.<br>
- Provide insight for insurance and healthcare professionals, policymakers and fitness industries.<br>
- Develop an early warning system for individuals at a risk of obesity.<br>

---
# **Methodology**
 
We preprocess the data by cleaning it, ensuring there are no missing values or duplicates. Then, we perform exploratory data analysis to understand feature distributions and their relationships with obesity levels. Finally, we visualize these relationships between categorical features and obesity levels to support the development of a dashboard.

---
# **Requirements**

The following Python libraries are used in this project:

- **NumPy:** Fast matrix operations.<br>
- **Pandas:** Analyzing and extracting insights from datasets.<br>
- **Matplotlib:** Creating graphs and plots.<br>
- **Seaborn:** Enhancing the style of matplotlib plots.<br>
- **Scikit-learn:** Linear regression analysis.<br>
- **Plotly & Dash:** To create interactive visualization<br>

---
# **Data Overview**

This dataset provides a comprehensive view of factors linked to obesity by combining demographic, behavioral, and health-related details. It captures key aspects such as age, gender, physical condition, and BMI classifications. It also tracks eating habits, including the consumption of high-calorie foods, vegetables, and alcohol, as well as meal frequency, snacking, water intake, and physical activity levels. This diverse range of attributes enables a detailed analysis of obesity-related factors.

**Dataset Feature Description**

The dataset provides information on individuals' obesity levels based on a variety of lifestyle and health-related factors. Below is a list of the features included, along with brief descriptions:
 
- **Gender:** Male or Female.<br>
- **Age:** In years.<br>
- **Height:** In meters.<br>
- **Weight:** In kilograms.<br>
- **Family_history_with_overweight:** Family history of being overweight (yes/no).<br>
- **FAVC (Frequent Consumption of High-Calorie Food):** Frequently eats high-calorie food (yes/no).<br>
- **FCVC (Frequency of Vegetable Consumption):** Scale from 1 (low) to 3 (high), indicating how often vegetables are consumed.<br>
- **NCP (Number of Meals Per Day):** Number of main meals the person eats each day.<br>
- **CAEC (Consumption of Food Between Meals):** How often the person eats snacks: no, sometimes, frequently, or always.<br>
- **SMOKE:** Individual smokes (yes/no).<br>
- **CH2O (Daily Water Intake in Liters):** Scale from 1 (low) to 3 (high), representing daily water consumption.<br>
- **SCC (Calories Consumption Monitoring):** Individuals monitor their calorie intake (yes/no).<br>
- **FAF (Physical Activity Frequency Per Week):** Scale from 0 (no activity) to 3 (high frequency).<br>
- **TUE (Time Using Technology Devices Per Day):** Scale from 0 (low) to 2 (high), measuring daily screen time.<br>
- **CALC (Alcohol Consumption Frequency):** How often alcohol is consumed: no, sometimes, frequently, or always.<br>
- **MTRANS (Mode of Transportation):** Main mode of transport: public transportation, walking, automobile, or motorbike.<br>
- **NObeyesdad (Obesity Level Classification):** The individual's obesity category: Insufficient Weight, Normal Weight, Overweight Level I, Overweight Level II, Obesity Type I, Obesity Type II, or Obesity Type III.<br>

---
# **Cleaning the Data**

The original dataset is of good quality with no missing values. However, it contained 24 duplicate rows, likely from synthetic generation (77% via Weka and SMOTE). We removed these duplicates, retaining unique entries, to improve reliability while preserving completeness.

---
# **Proposed Solution**
 
The proposed solution uses the “Dataset for estimation of obesity levels based on eating habits and physical condition” to include visualizations to highlight the key factors that contribute most to obesity and develop a predictive model that classifies individuals into seven obesity levels. The process after data cleaning and preprocessing, identifys key factors such as diet quality, hydration, physical activity, sedentary behavior, and transport choices. The final step is creating an interactive tool or dashboard that delivers personalized health recommendations, targeted interventions, and easy monitoring for healthcare providers, fitness professionals, insurance companies, and policymakers.

---
# **Insights and Visualizations**
⚠️ **Note:** This dataset includes synthetically generated data based on real-world patterns.<br>
## Regression Plot for Height vs Weight by Obesity Level

The Regression Plot for Height vs. Weight is color-coded by Obesity Level. This plot shows the relationship between height and weight, with trend lines for each obesity category. It highlights how weight increases in relation to height and how it differs across obesity levels.

![Regression Plot](images/RegressionPlot_Height_vs_Weight_by_Obesity_Level.png)


Proposed sections for Charts, Graphs and Plots

---
# **Implementation**
 
The implementation starts with applying data analytics techniques to the dataset to build an accurate and reliable model. Once the model is ready, the next step is to make it easy for health professionals and organizations to assess and manage obesity risk. The goal is to keep it simple and intuitive so users can quickly get the insights they need.

---
# **Next Steps**
 
The next steps start with running exploratory data analysis to get a better understanding of how different variables are connected. After that, the focus will be on training and validating the predictive models to make sure they’re accurate and reliable. Once the model is solid. The plan is to provide stakeholders, including health professionals and the public, with clear insights and visualizations through a comprehensive README on GitHub. This will include key information, data interpretations, and graphs to help them better understand and address obesity risks.

---
# **Risks and Mitigations**
 
There are a few risks to consider, but each has a clear plan to address them. First is data quality, if the data is incomplete or inaccurate, it can lead to unreliable results. To avoid this, the data will go through rigorous cleaning and validation to ensure it’s consistent and accurate before analysis. Another risk is bias in the analysis, which can happen if the dataset isn’t diverse enough. To minimize this, the data will be carefully reviewed to make sure it includes a wide range of demographic and lifestyle factors, helping to produce fair and balanced insights. Privacy is also a major concern, especially when dealing with health-related data. To protect personal information, the project will follow strict data protection regulations and best practices, ensuring all data remains confidential and secure throughout the process.

---
# **Results**

The model aims to create a positive impact and raise awareness across several key sectors. In healthcare, it supports preventive measures and enables more targeted interventions. For governments and policymakers, it offers evidence-based insights to guide public health initiatives and inform policy decisions. Individuals also benefit by gaining valuable knowledge that empowers them to make informed lifestyle choices and take control of their health.

---
# **Conclusion**

By using this dataset to estimate obesity levels, we can support smarter, data-driven decisions in healthcare, wellness, insurance, and public policy. The insights gained from the analysis not only have the potential to lower obesity rates but also to reduce long-term healthcare costs and improve overall productivity. Clear visualizations and accessible information empower stakeholders, from healthcare providers and insurance professionals to policymakers and individuals, to take proactive steps toward prevention and intervention. Ultimately, this approach promotes healthier lifestyles, supports early risk detection, and contributes to better public health outcomes on a larger scale.

---
