# Activation Function
##  🔍 What is an Activation Function?
An activation function in a neural network defines the output of a neuron given an input or set of inputs. It introduces non-linearity, enabling the network to model complex relationships. <br>
Without an activation function, the neural network would behave like a linear regression model, no matter how many layers it has.

##  ⚙️ Why Use Activation Functions?
-   Adds non-linearity to the model. <br>
-   Helps map inputs to outputs with complex functions. <br>
-   Enables backpropagation by providing gradients. <br>
-   Controls whether a neuron should be activated or not. <br>

##  🧮 Types of Activation Functions with Math, Graph, and Use-Cases
1. Step Function (Not used today)
Formula:
<div>
    <div align='center'>
        <code>Step(x) = { 1 if x &gt; 0 ; 0 otherwise }<br><br></code>
    </div>
</div>

&nbsp;  -   Use: Early Perceptron models <br>
&nbsp;  -   Problem: Non-differentiable → can’t be used with backpropagation <br>


2. Sigmoid / Logistic Function
Formula:
<div>
    <div align='center'>
        <code>Sigmoid, f(x) = <span>1 / (1 + <span>e<sup>-x</sup></span>)</span>
    </div>
</div>

Range: (0, 1) <br>

Derivative: <br>
<div>
    <div align='center'>
        <code>Sigmoid', f'(x) = Sigmoid(x) * (1 - Sigmoid(x))</code>
    </div>
</div>

**Pros:** <br>
-   Smooth gradient <br>
-   Useful in binary classification (as output activation) <br>

**Cons:** <br>
-   Vanishing gradient problem (when `|x|` is large) <br>
-   Outputs not centered at zero <br>


3.  Tanh (Hyperbolic Tangent)
Formula:
<div>
    <div align='center'>
        <code>Tanh, f(x) = (<span>e<sup>x</sup></span> - <span>e<sup>-x</sup></span>) / (<span>e<sup>x</sup></span> + <span>e<sup>-x</sup></span>)</code>
    </div>
</div>

Range: (-1, 1) <br>

Derivative: <br>

<div>
    <div align='center'>
        <code>Tanh', f'(x) = 1 - <span>f(X<sup>2</sup></span>)</code>
    </div>
</div>


**Pros:**
-   Zero-centered <br>
-   Better gradient flow than sigmoid <br>

**Cons:**
-   Still suffers from vanishing gradient


4. ReLU (Rectified Linear Unit)
Formula:
<div>
    <div align='center'>
        <code> ReLU, f(x) = max(0, x)</code>
    </div>
</div>


Range: [0, ∞) <br>

Derivative: <br>

<div>
    <div align='center'>
        <code>ReLu', f'(x) =  { 1 if x &gt; 0 ; 0 if x ≤ 0 }</code>
    </div>
</div>

**Pros:** <br>
-   Fast convergence <br>
-   Sparse activation (computational efficiency) <br>
-   Partially solves vanishing gradient <br>

**Cons:**
-   “**Dead neurons**” problem (gradient = 0 for x ≤ 0) <br>


5. Leaky ReLU
Formula:
<div>
    <div align='center'>
        <code>LeakyReLU, f(x) = { x if x &gt; 0 ; αx if x ≤ 0 }</code>
    </div>
</div>
Note: α is small (e.g., 0.01)

**Pros:** <br>
-   Fixes dead neuron problem of ReLU <br>
-   Allows small gradient when x < 0 <br>


6. Parametric ReLU (PReLU)
Similar to Leaky ReLU, but `α` is learned during training. <br>

**Pros:** <br>
-   More flexible than Leaky ReLU <br>


7. ELU (Exponential Linear Unit)
Formula:
<div>
    <div align='center'>
        <code>ELU, f(x) = { x if x &gt; 0 ; α(<span>e<sup>x</sup></span> - 1) if x ≤ 0 }</code>
    </div>
</div>

**Pros:** <br>
-   Smooth, avoids dead neurons <br>
-   Zero-centered output <br>

8. Softmax (used in output layer for multi-class classification)
Formula:
<div>
    <div align='center'>
        <code>Softmax, <span>f<sub>i</sub></span>(x) = <span>e<sup>x<sub>i</sub></sup></span> / <span>∑<sub>j</sub></span> <span>e<sup>x<sub>j</sub></sup></span></code>
    </div>
</div>
