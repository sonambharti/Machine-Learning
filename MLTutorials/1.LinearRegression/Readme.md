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

where, 
m = coefficient
b = intercept
```

### How to update m and b values to get the best-fit line? 
The best-fit line is obtained by minimizing the sum of the squared errors between the observed and predicted values.
    <div>
        &sum;<sub>i=1</sub><sup>n</sup>(y&#770;<sub>i</sub> - y)
    </div>
</div>