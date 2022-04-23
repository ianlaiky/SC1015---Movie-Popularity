# Welcome to Team 7 repository

## About

![image](https://user-images.githubusercontent.com/22881021/164895983-d5c00d93-9033-48a2-a41c-414fb153542b.png)
COVID-19 has cause significant impact to our society for the past 2-3 years, this is especially true for the film
industry. Cinemas were closed to prevent the spread of the virus and today requires patrons to leave gaps between each
other thus reducing the potential earnings for a particular screening. <br><br>
This is a Mini-Project for SC1015 (Introduction to Data Science and Artificial Intelligence) focuses how movie producers
can maximise their profit.

## Contributors

* @ianlaiky - Ian Lai Kheng Yan - Data Extraction,Machine Learning
* @drainboy - Koh Jia Sheng Eldrian - Exploratory data analysis
* @kavi-99 - Kavita Sriram - Exploratory data analysis

## Problem Definition

* How do different variables affect the revenue of a movie?

## Models Used

* Random Forest
* Multivariate Linear Regression
* XGBoost

## Conclusion

### Data-driven insights and recommendations:

* July as a release month brings in high revenue.

* Including elements of action, adventure, history, fantasy in the story of the movie will be beneficial as those genres
  have shown to generate high revenues.

* Keeping the runtime within a 50-150 minutes range, is optimal in ensuring high revenues.

* Popularity has a moderately strong correlation with revenue, therefore, movie producers should make an effort to
  market their movie well so that its popularity is high.

* Including actors with a consistently successful work performance in the movie may enhance the chances of generating a
  higher revenue.

### Project Outcomes and Conclusions:

* Predict revenue of a movie based on factors during the making of the movie.

* Random forest and Multivariate linear regression did give most similar accuracy, however linear regression accuracy
  was most similar in train and test.
* The moderately accurate score our models gave may be attributed to movies not releasing their budget and revenue
  information, thus our original 140k rows of data has been reduced to 2747 rows. The smaller dataset may have
  influenced the accuracy of our models.

## Project Takeaway

### What did we learn?

#### New Models

Exploring other types of models such as

* Random Forest Regression
* XGBoost
  <br>
  <br>

#### Collaboration

* Collaborating using Google Colab

### Data Extraction

Using API to extract data from TMDB website. Writing python script that extracts data from TMDB website and saves it to
a csv file. 

## References

* Derrick M. (2021 October 26). Random Forest Regression: When Does It Fail and Why? Neptune
  Blog. https://neptune.ai/blog/random-forest-regression-when-does-it-fail-and-why
* Berna B. (n.d). EDA & Random Forest & XGBoost - TMDB Box Office.
  Kaggle. https://www.kaggle.com/code/bernabas/eda-random-forest-xgboost-tmdb-box-office
* Sruthi E R. (2021 June 17). Understanding Random Forest. Analytics
  Vidhya. https://www.analyticsvidhya.com/blog/2021/06/understanding-random-forest/#:~:text=Random%20forest%20is%20a%20Supervised,average%20in%20case%20of%20regression
  .
* XGBoost (n.d). XGBoost Documentation. https://xgboost.readthedocs.io/en/stable/
* The Movie Database (n.d). The Movie Database website. https://www.themoviedb.org/ 

