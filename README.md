# Phishing Detection App

Briefly describe the purpose/result(s) of your project, the skills you applied, and the AI4ALL Ignite program:

*The purpose of our project is to help users detect whether or not an email is phishing. As the world of technology grows, it is integral to reduce cybercrime. We used many skills in this project including the cleaning, preprocessing, and combining of dataframes, visualization of data using python, application of Naive Bayes Algorithm, and deployment using Streamlit. The AI4ALL ignite program has helped us to establish a good foundation of AI and machine learning skills.*

Deployed app link: https://phishingdetectionappai4allproject.streamlit.app/


## Video Walkthrough

Here's a walkthrough of the deployed website:

<img src='https://i.imgur.com/f15tD6G.gif' title='Video Walkthrough' width='' alt='Video Walkthrough' />

## Problem Statement <!--- do not change this line -->

Describe the motivation for this project, why it is relevant, and what its impacts are:

*Our main motivation for this project is to build a classification model that helps reduce cybercrime. By detecting phishing emails, our model targets a common cybercrime that many people encounter. By having a model like this, it impacts the world and makes our modern world of technology safer.*

## Key Results <!--- do not change this line -->

Enumerate the main results of this project in a list and describe them.

1. *Combined 4 different datasets*
2. *Balanced the resulting dataset*
3. *Studied whether sender impacts results or not*
4. *Trimmed dataset to a maximum of 10,000 characters*
5. *Removed stopwords from dataset*
6. *Studied the top words of with/without stopwords*
7. *Created word clouds of phishing emails and legitimate emails*
8. *Trained classification model using Naive Bayes algorithm and achieved a 93% precision for legitimate emails and 98% for phsihing emails*
9. *Turned vectorizer and model into a pickle file and used those to create and deploy a frontend using Streamlit.*


## Methodologies <!--- do not change this line -->


*To accomplish this, we combined 4 different datasets using pandas library in python. We balanced the data and trimmed it to maximum of 10,000 characters. We removed stopwords and analyzed the top words. We used seaborn and mathplotlib to achieve this. We created word clouds too using wordcloud. Sklearn libraries were used to train model using Naive Bayes algorithm. We achieved a 93% precision for legitimate emails and 98% for phsihing emails. Then, we turned the vectorizer and the model into a pickle file and used those to create and deploy a frontend using Streamlit.*


## Data Sources <!--- do not change this line -->

Include any relevant data sources that were used in your project.

*Source Links*

*Source for CEAS_08.csv, Ling.csv, and Nazario.csv: https://www.kaggle.com/datasets/naserabdullahalam/phishing-email-dataset/data*

*Source for Phishing_validation_emails.csv: https://zenodo.org/records/13474746*

Origin of Ling.csv and CEAS_08.csv:  
The Ling Dataset includes real email data from the early 2000s. CEAS_08  is from the Challenge Lab Evaluation Corpus (CEAS-08), and includes emails dating back to the year 2008.
https://www.researchgate.net/publication/382212910_Curated_Datasets_and_Feature_Analysis_for_Phishing_Email_Detection_with_Machine_Learning

Origin of Phishing_validation_emails.csv: 
This dataset is a mix of 2000 real-world email samples and artificially generated emails that reflect realistic email scenarios.
https://zenodo.org/records/13474746
 
Origin of Nazario.csv: 
the Nazario dataset also known as Nazario Phishing Corpus includes data from 2015 - 2022. It contains real and raw collections phishing emails.
https://www.researchgate.net/publication/380614299_Why_Phishing_Emails_Escape_Detection_A_Closer_Look_at_the_Failure_Points


## Technologies Used <!--- do not change this line -->

List the technologies, libraries, and frameworks used in your project.

- Python
- pandas
- sklearn
- seaborn
- nltk
- Counter
- mathplotlib
- pickle
- wordcloud
- Streamlit


## Authors <!--- do not change this line -->

List the names and contact information (e.g., email, GitHub profiles) of the authors or contributors.

*EXAMPLE:*
*This project was completed in collaboration with:*
- *Sanika Annadate ([sannadate2023@gmail.com](mailto:sannadate2023@gmail.com))*
- *Esther Manu ([esthermanu599@gmail.com](mailto:esthermanu599@gmail.com))*
- *Eliana Kim ([yunmin626@gmail.com](mailto:yunmin626@gmail.com))*
