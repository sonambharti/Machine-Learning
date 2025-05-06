<div>

#   Linear Regression
Linear regression is a statistical method used to model the relationship between a dependent variable and one or more independent variables. It provides valuable insights for prediction and data analysis. <br>

##  Understanding Linear Regression
Linear regression is also a type of supervised machine-learning algorithm that learns from the labelled datasets and maps the data points with most optimized linear functions which can be used for prediction on new datasets. It computes the linear relationship between the dependent variable and one or more independent features by fitting a linear equation with observed data. It predicts the continuous output variables based on the independent input variable. <br>

##  Why Linear Regression is Important?
The interpretability of linear regression is one of its greatest strengths. The model’s equation offers clear coefficients that illustrate the influence of each independent variable on the dependent variable, enhancing our understanding of the underlying relationships. Its simplicity is a significant advantage; linear regression is transparent, easy to implement, and serves as a foundational concept for more advanced algorithms. <br>

##  What is the best Fit Line?
Our primary objective while using linear regression is to locate the best-fit line, which implies that the error between the predicted and actual values should be kept to a minimum. There will be the least error in the best-fit line.<br>

The best Fit Line equation provides a straight line that represents the relationship between the dependent and independent variables. The slope of the line indicates how much the dependent variable changes for a unit change in the independent variable(s). <br>

```
y = m * x + b
```
where, 
m = coefficient
b = intercept


### How to update m and b values to get the best-fit line? 
The best-fit line is obtained by `minimizing the sum of the squared errors` between the observed and predicted values.
    <div align='center'>
        &sum;<sub>i=1</sub><sup>n</sup>(y&#770;<sub>i</sub> - y)
    </div>
</div>

##  Types of Linear Regression
When there is only one independent feature it is known as `Simple Linear Regression` or `Univariate Linear Regression` and when there are more than one feature it is known as `Multiple Linear Regression` or `Multivariate Regression``.

1. **Simple Linear Regression**
Simple linear regression is the simplest form of linear regression and it involves only one independent variable and one dependent variable. The equation for simple linear regression is:
```y = m * x + b```

where: <br>

y is the dependent variable <br>
x is the independent variable   <br>
b is the intercept <br>
m is the slope <br>

### Use Case of Simple Linear Regression
-   In a case study evaluating student performance analysts use simple linear regression to examine the relationship between study hours and exam scores. By collecting data on the number of hours students studied and their corresponding exam results the analysts developed a model that reveal correlation, for each additional hour spent studying, students exam scores increased by an average of 5 points. This case highlights the utility of simple linear regression in understanding and improving academic performance.  <br>
-   Another case study focus on marketing and sales where businesses uses simple linear regression to forecast sales based on historical data particularly examining how factors like advertising expenditure influence revenue. By collecting data on past advertising spending and corresponding sales figures analysts develop a regression model that tells the relationship between these variables. For instance if the analysis reveals that for every additional dollar spent on advertising sales increase by $10. This predictive capability enables companies to optimize their advertising strategies and allocate resources effectively.   <br>

2. **Multiple Linear Regression**
Multiple linear regression involves more than one independent variable and one dependent variable. The equation for multiple linear regression is:
<div align='center'>
    y = m<sub>1</sub> * x<sub>1</sub> + m<sub>2</sub> * x<sub>2</sub>+ … + m<sub>n</sub> * x<sub>n</sub> + β<sub>0</sub>
</div>

where: <br>
y is the dependent variable <br>
x<sub>1</sub>, x<sub>2</sub>, …, x<sub>n</sub>are the independent variables <br>
β<sub>0</sub> is the intercept <br>
m<sub>1</sub>, m<sub>2</sub>, …, m<sub>n</sub> are the slopes <br>

### Use Case of Multiple Linear Regression
Multiple linear regression allows us to analyze relationship between multiple independent variables and a single dependent variable. Here are some use cases: <br>
-   **Real Estate Pricing**: In real estate MLR is used to predict property prices based on multiple factors such as location, size, number of bedrooms, etc. This helps buyers and sellers understand market trends and set competitive prices.    <br>
-   **Financial Forecasting**: Financial analysts use MLR to predict stock prices or economic indicators based on multiple influencing factors such as interest rates, inflation rates and market trends. This enables better investment strategies and risk management24.  <br>
-   **Agricultural Yield Prediction**: Farmers can use MLR to estimate crop yields based on several variables like rainfall, temperature, soil quality and fertilizer usage. This information helps in planning agricultural practices for optimal productivity.    <br>
-   **E-commerce Sales Analysis**: An e-commerce company can utilize MLR to assess how various factors such as product price, marketing promotions and seasonal trends impact sales.    <br>


**✅ Real-World Applications:** <br>
📈 **Business**: Predicting sales from advertising spend. <br>
🏥 **Healthcare**: Predicting blood pressure from age.  <br>
🏫 **Education**: Predicting student test scores from study hours. <br>
🏠 **Real Estate**: Predicting rent from square footage. <br>
📊 **Finance**: Predicting stock prices from economic indicators. <br>


##  Cost function for Linear Regression
In linear regression, the cost function measures how well the predicted values `{y<sub>i</sub>}&#770;` match the actual values `{y<sub>i</sub>}`. It’s used to optimize the parameters (slope 𝑚 and intercept 𝑏) by minimizing the error. <br>
The cost function for linear regression is the Mean Squared Error (MSE) or Mean Absolute Error (MAE).
<div>
    <div align='center'>
        Cost Function, (J) = 1/n &sum;<sub>i=1</sub><sup>n</sup>(y&#770;<sub>i</sub> - y)
    </div>

</div>

