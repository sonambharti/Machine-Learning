<div>
<head>
  <meta charset="UTF-8">
  <!-- Load MathJax for LaTeX rendering -->
  <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
  <script id="MathJax-script" async
    src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
  </script>
</head>
<body align='center'>

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
  <p>
    \[
    \text{minimize } \frac{1}{n} \sum_{i=1}^{n} \left( \hat{y}_i - y_i \right)^2
    \]
  </p>
</body>

<div>
    <math xmlns="http://www.w3.org/1998/Math/MathML" display="block">
        <mi>minimize</mi>
        <mrow>
        <mo>&#x2211;</mo> <!-- summation -->
        <mo>(</mo>
        <msub><mi>y</mi><mi>i</mi></msub>
        <mo>&#x2212;</mo>
        <mover><mi>y&#773;</mi></mover>
        <mo>)</mo>
        </mrow>
    </math>
</div>


<div>
    <math xmlns="http://www.w3.org/1998/Math/MathML" display="block">
    <mi>m</mi>
    <mo>=</mo>
    <mfrac>
        <mrow>
        <mo>&#x2211;</mo> <!-- summation -->
        <mo>(</mo>
        <msub><mi>x</mi><mi>i</mi></msub>
        <mo>&#x2212;</mo>
        <mover><mi>x&#773;</mi></mover>
        <mo>)</mo>
        <mo>(</mo>
        <msub><mi>y</mi><mi>i</mi></msub>
        <mo>&#x2212;</mo>
        <mover><mi>y&#773;</mi></mover>
        <mo>)</mo>
        </mrow>
        <mrow>
        <mo>&#x2211;</mo>
        <mo>(</mo>
        <msub><mi>x</mi><mi>i</mi></msub>
        <mo>&#x2212;</mo>
        <mover><mi>x&#773;</mi></mover>
        <msup><mo>)</mo><mn>2</mn></msup>
        </mrow>
    </mfrac>
    </math>
</div>
</div>