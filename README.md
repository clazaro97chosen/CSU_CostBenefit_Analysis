
# Welcome! 

Abstract: "Student recruitment efforts require substantial institutional expenditures (e.g., hiring of staff, travel funding, and marketing costs). In contrast, retention initiatives designed to manage student enrollment are estimated to be 3-5 times more cost-effective than recruitment efforts, i.e., it takes 3-5 times as much money to recruit a new student than it does to retain an already enrolled student (Noel, Levitz, & Saluri, 1985; Rosenberg & Czepiel, 1983; Tinto, 1975). Bean and Hossler (1990) report that a student who is retained at an institution for four years will generate the same income as four new students who leave after one year. One Canadian university factored in its average cost to recruiting a new student, and calculated that it loses \\$4,230 for each recruited student that is not retained to the second year (Okanagan University College, cited in Grayson & Grayson, 2003). At the University of St. Louis, each 1\% increase in first-year retention rate was found to generate approximately \$500,000 in revenue by the time these first-year students eventually graduate (Nicholl & Sutton, in Grayson & Grasyon, 2003)."(Joe Cuseao,MarymountCollege). This Notebook is a costs/benefit analysis of a retention program initiative which has an administrative cost of 3,400 dollars per student.Currently the estimated loss for a freshman that does not persist into his/her second year has a loss of 54,000 dollars in gross revenue.  Currently if the University predicted no student would churn i.e. no initiative our cost per student would be : \\$3082 per student. With a metric of performance that adheres to the business function keeping cost down. A trained random forest machine learning model trained with several [variables](https://github.com/clazaro97chosen/CSU_CostBenefit_Analysis/blob/master/references/Data_Dictionary.txt) about students. **Reduced our cost per student from 3082 to 3065 for a percent change of 55%**.

~[alt test](images/costcurve.png)

#### Keywords
California Public Universities, Freshman Retention, Classification, Cost–benefit analysis (CBA), machine learning


#Example of another applicable results from the project
The university wanted to see what it would take to increase their 94% freshman retention rate to match or beath UCLA which has the best retention rate in california with 97% how much would the university have to endure per student to reach that goal. In our preparred training data used in this project 960 out 16816 students churned. Our machine learning classifier predicted 111 out of the 960 with a threshold of .2 and a cost per student of 3065. In order to reach a 97% retention rate our machine learning classifier would have to predict 504 out of the 960 students who churn. We investigate what threshold is necessary for this to happen and what our cost per student would come out to be. We find that a threshold of .06 i.e. if a student has a greater than 6.9 % probability of churning we are going to predict that the student will churn and offer the retention program initiative which has an administrative cost of 3,400 dollars. This would theoretically result in a 97% freshman retention rate but at the cost of $\\3402.10 per student.


Project Organization
------------

    ├── LICENSE
    ├── README.md          <- The top-level README for developers using this project.
    │
    ├── models             <- Trained and serialized models, model predictions
    │
    ├── notebooks          <- Jupyter notebooks.
    │
    ├── references         <- Data Information (sources, data dictionaries, manuals)
    │
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   │
    │   ├── modeling        <- Scripts to train models, prepare data or perform         |   |                      feature selection, and to train and predict on final     |   |                      test data         
    │   │   ├── prep_data.py
    │   │
    │   └── visualizing  <- Scripts to create exploratory and results oriented visualizations
    │       └── cost_curve.py 
    
    


--------
