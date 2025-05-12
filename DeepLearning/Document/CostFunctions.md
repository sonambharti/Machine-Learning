<div align='center'>
    <h1>Cost Functions</h1>
</div>
<div>

##  💡 What is a Cost Function?
A Cost Function (also known as a Loss Function) is a mathematical function used in optimization and machine learning to measure the error between the predicted value and the actual value. It guides model training by showing how wrong the predictions are.

##  📚 Types of Cost Functions
<ol>
<li><strong>Mean Squared Error (MSE)</strong>

-  **Use Case:** Regression problems <br>
-  **Math:** Penalizes large errors heavily <br>

<div>
    <div align='center'>
        <code>J(θ) = (1/n) ∑<sub>i=1</sub><sup>n</sup> (y&#770;<sub>i</sub> - y<sub>i</sub>)²</code>
    </div>
</div>

-   <strong><code>ŷ<sub>i</sub></code></strong>: predicted value <br>
-   <Strong><code>y<sub>i</sub></code></strong>: actual value   <br>
-   <strong><code>n</code></strong>: number of data points  <br>

**Pros:**
-   Differentiable and convex <br>
-   Smooth gradient for optimization <br>

**Cons:**
-   Sensitive to outliers (squares large errors) <br>

<li><strong>Mean Absolute Error (MAE)</strong><br>

-   **Use Case:** Regression problems where robustness to outliers is desired <br>
Formula: 

<div>
    <div align='center'>
        <code>J(θ) = (1/n) ∑<sub>i=1</sub><sup>n</sup> |y&#770;<sub>i</sub> - y<sub>i</sub>|</code>
    </div>
</div>

**Pros:**
-   Robust to outliers <br>
-   More interpretable error metric <br>

**Cons:**
-   Not differentiable at 0 (gradient-based methods require subgradient) <br>
</li>
<li><strong>Huber Loss</strong>

-   **Use Case:** Combines advantages of MSE and MAE <br>
Formula (for δ = threshold): <br>

<div>
    <div align='center'>
        <code><span>L<sub>δ</sub></span>(<span>y<sub>i</sub></span>, <span>y&#770;<sub>i</sub></span>) = { (1/2)(<span>y&#770;<sub>i</sub></span> - <span>y<sub>i</sub></span>)² if |<span>y&#770;<sub>i</sub></span> - <span>y<sub>i</sub></span>| ≤ δ  <br>
                δ * (|<span>y&#770;<sub>i</sub></span> - <span>y<sub>i</sub></span>| - δ/2) otherwise }</code>
    </div>
</div>

**Pros:**
-   Differentiable <br>
-   Balances MSE and MAE <br>

**Cons:**
-   Needs tuning of δ <br>
</li>
<li><strong>Cross-Entropy Loss (Log Loss)</strong>
This is also known as `Logistic Regression Cost Function`.<br>

-   **Use Case:** Binary or multiclass classification <br>
Binary Classification Formula:

<div>
    <div align='center'>
        <code>J(θ) = - (1/n) <span>∑<sub>i=1</sub><sup>n</sup></span> [<span>y<sub>i</sub></span> log(<span>y&#770;<sub>i</sub></span>) + (1 -<span> y<sub>i</sub></span>) log(1 - <span>y&#770;<sub>i</sub></span>)]</code>
    </div>
</div>

**Pros:**
-   Well-suited for classification <br>
-   Strong theoretical grounding in probability <br>

**Cons:**
-   Can be numerically unstable if <code>ŷ<sub>i</sub></code> is very close to 0 or 1
</li>
<li><strong>Catogerical Cross-Entropy Loss</strong>

-   **Use Case:** Multiclass classification <br>
Multiclass Classification Formula:

<div>
    <div align='center'>
        <code>J(θ) = - (1/n) <span>∑</span> [<span>y<sub>i1</sub></span> log(<span>a<sub>i1</sub></span>) + <span>y<sub>i1</sub></span> log (<span>a<sub>i1</sub></span>)+ ... <span>y<sub>ij</sub></span> log(<span>a<sub>ij</sub></span>)] <br>
        cost = - <span>&sum;<sub>j=0</sub><sup>m</sup></span> <span>&sum;<sub>i=0</sub><sup>n</sup></span> (<span>y<sub>ij</sub></span> * log(<span>a<sub>ij</sub></span></code>
    </div>
</div>

**Pros:**
-   Well-suited for classification <br>
-   Strong theoretical grounding in probability <br>

**Cons:**
-   Can be numerically unstable if <code>ŷ<sub>i</sub></code> is very close to 0 or 1
</li>
<li><strong>Hinge Loss</strong>

-  **Use Case:** Support Vector Machines (SVMs) <br>
Formula:
<div>
    <div align='center'>
        <code>J(θ) = <span>∑<sub>i=1</sub><sup>n</sup></span> max(0, 1 - <span>y<sub>i</sub></span> * <span>y&#770;<sub>i</sub></span>)</code>
    </div>
</div>
<code>y<sub>i</sub> ∈ {-1, 1}</code> (actual label)

<code>ŷ<sub>i</sub></code>: raw model output

**Pros:**
-   Promotes margin maximization <br>
-   Great for large-margin classification <br>

**Cons:**
-   Not probabilistic (doesn’t output probabilities) <br>
</ol>
</div>
<div>

##  ✅ Benefits Comparison 
| Cost Function | Handles Outliers | Smooth Gradient | Classification | Robust | Probabilistic |
| ------------- | ---------------- | --------------- | -------------- | ------ | ------------- |
| MSE           | ❌                | ✅               | ❌              | ❌      | ❌             |
| MAE           | ✅                | ❌               | ❌              | ✅      | ❌             |
| Huber         | ✅                | ✅               | ❌              | ✅      | ❌             |
| Cross-Entropy | ❌                | ✅               | ✅              | ❌      | ✅             |
| Hinge Loss    | ❌                | ✅               | ✅              | ❌      | ❌             |

</div>