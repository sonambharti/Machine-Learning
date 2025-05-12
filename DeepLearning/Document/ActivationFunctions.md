<div align='center'>
    <h1>Activation Function</h1>
</div>

##  🔍 What is an Activation Function?
An activation function in a neural network defines the output of a neuron given an input or set of inputs. It introduces non-linearity, enabling the network to model complex relationships. <br>
Without an activation function, the neural network would behave like a linear regression model, no matter how many layers it has.

##  ⚙️ Why Use Activation Functions?
-   Adds non-linearity to the model. <br>
-   Helps map inputs to outputs with complex functions. <br>
-   Enables backpropagation by providing gradients. <br>
-   Controls whether a neuron should be activated or not. <br>

##  🧮 Types of Activation Functions with Math, Graph, and Use-Cases
<div>
<ol>
<li> <strong>Step Function</strong> (Not used today) <br>
Formula:
<div>
    <div align='center'>
        <code>Step(x) = { 1 if x &gt; 0 ; 0 otherwise }</code>
    </div>
</div>

-  **Use**: Early Perceptron models <br>
-  **Problem**: Non-differentiable → can’t be used with backpropagation <br>
</li>
<li><strong>Sigmoid / Logistic Function</strong> <br>
Formula:
<div>
    <div align='center'>
        <code>Sigmoid, f(x) = <span>1 / (1 + <span>e<sup>-x</sup></span>)</span></code>
    </div>
</div>

-  **Range:** (0, 1) <br>
-  **Derivative:** <br>

<div>
    <div align='center'>
        <code>Sigmoid', f'(x) = Sigmoid(x) * (1 - Sigmoid(x))</code>
    </div>
</div>

**Pros:** <br>
-  Smooth gradient <br>
-  Useful in binary classification (as output activation) <br>

**Cons:**  <br>
-  Vanishing gradient problem (when `|x|` is large) <br>
-  Outputs not centered at zero <br>
</li>
<li><strong>Tanh (Hyperbolic Tangent)</strong> <br>
Formula:
<div>
    <div align='center'>
        <code>Tanh, f(x) = (<span>e<sup>x</sup></span> - <span>e<sup>-x</sup></span>) / (<span>e<sup>x</sup></span> + <span>e<sup>-x</sup></span>)</code>
    </div>
</div>

- **Range**: (-1, 1) <br>
- **Derivative**: <br>

<div>
    <div align='center'>
        <code>Tanh', f'(x) = 1 - <span>f(X<sup>2</sup></span>)</code>
    </div>
</div>

**Pros:** <br>
-   Zero-centered <br> 
-   Better gradient flow than sigmoid <br>

**Cons:** <br>
-   Still suffers from vanishing gradient
</li>
<li><strong>ReLU (Rectified Linear Unit)</strong> <br>
Formula:
<div>
    <div align='center'>
        <code> ReLU, f(x) = max(0, x)</code>
    </div>
</div>

-  **Range:** [0, ∞) <br>
-  **Derivative:** <br>

<div>
    <div align='center'>
        <code>ReLu', f'(x) =  { 1 if x &gt; 0 ; 0 if x ≤ 0 }</code>
    </div>
</div>

**Pros:** <br>
-   Fast convergence <br>
-   Sparse activation (computational efficiency) <br>
-   Partially solves vanishing gradient <br>

**Cons:** <br>
-   “**Dead neurons**” problem (gradient = 0 for x ≤ 0) <br>
</li>
<li><strong>Leaky ReLU</strong> <br>
Formula:
<div>
    <div align='center'>
        <code>LeakyReLU, f(x) = { x if x &gt; 0 ; αx if x ≤ 0 }</code>
    </div>
</div>
Note: `α` is small (e.g., 0.01) <br>

**Pros:** <br>
-   Fixes dead neuron problem of ReLU <br>
-   Allows small gradient when x <br 0 <br>
</li>
<li><strong>Parametric ReLU (PReLU)</strong>
Similar to Leaky ReLU, but `α` is learned during training. <br>

**Pros:**  <br>
-   More flexible than Leaky ReLU <br>
</li>
<li><strong>ELU (Exponential Linear Unit)</strong> <br>
Formula:
<div>
    <div align='center'>
        <code>ELU, f(x) = { x if x &gt; 0 ; α(<span>e<sup>x</sup></span> - 1) if x ≤ 0 }</code>
    </div>
</div>

**Pros:** <br>
-   Smooth, avoids dead neurons <br>
-   Zero-centered output <br>
</li>
<li><strong>Softmax (used in output layer for multi-class classification)</strong> <br>
Formula:
<div>
    <div align='center'>
        <code>Softmax, <span>f<sub>i</sub></span>(x) = <span>e<sup>x<sub>i</sub></sup></span> / <span>∑<sub>j</sub></span> <span>e<sup>x<sub>j</sub></sup></span></code>
    </div>
</div>

- **Range:** (0, 1), sum = 1 <br>
- **Use:** Converts logits into probabilities across multiple classes </br>
</li>
</ol>
</div>
<div>

##  Summary Table

<table border="1" cellspacing="0" cellpadding="6"> 
<thead> <tr> <th>Activation</th> <th>Range</th> <th>Use-case</th> <th>Pros</th> <th>Cons</th> </tr> </thead> 
<tbody> 
    <tr> <td>Step</td> <td>{0, 1}</td> <td>Early Perceptrons</td> <td>Simple</td> <td>Non-differentiable</td> </tr> 
    <tr> <td>Sigmoid</td> <td>(0, 1)</td> <td>Output layer (binary)</td> <td>Smooth</td> <td>Vanishing gradient</td> </tr>
    <tr> <td>Tanh</td> <td>(-1, 1)</td> <td>Hidden layers</td> <td>Zero-centered</td> <td>Still vanishing gradient</td> </tr>
    <tr> <td>ReLU</td> <td>[0, ∞)</td> <td>Hidden layers</td> <td>Simple, fast</td> <td>Dead neurons</td> </tr>
    <tr> <td>Leaky ReLU</td> <td>~(-∞, ∞)</td> <td>Hidden layers</td> <td>Fixes ReLU dead units</td> <td>Needs α tuning</td> </tr> 
    <tr> <td>PReLU</td> <td>~(-∞, ∞)</td> <td>Hidden layers</td> <td>Learnable α</td> <td>Overfitting possible</td> </tr> 
    <tr> <td>ELU</td> <td>~(-α, ∞)</td> <td>Hidden layers</td> <td>Smooth, zero-centered</td> <td>Slower computation</td> </tr>
    <tr> <td>Softmax</td> <td>(0, 1) (∑=1)</td> <td>Output layer (multi-class)</td> <td>Probabilities</td> <td>Not for hidden layers</td> </tr>
</tbody> 
</table>

| Activation | Range     | Use-case                   | Pros                  | Cons                     |
| ---------- | --------- | -------------------------- | --------------------- | ------------------------ |
| Step       | {0,1}     | Early Perceptrons          | Simple                | Non-differentiable       |
| Sigmoid    | (0,1)     | Output layer (binary)      | Smooth                | Vanishing gradient       |
| Tanh       | (-1,1)    | Hidden layers              | Zero-centered         | Still vanishing gradient |
| ReLU       | \[0,∞)    | Hidden layers              | Simple, fast          | Dead neurons             |
| Leaky ReLU | \~(-∞, ∞) | Hidden layers              | Fixes ReLU dead units | Needs α tuning           |
| PReLU      | \~(-∞, ∞) | Hidden layers              | Learnable α           | Overfitting possible     |
| ELU        | \~(-α, ∞) | Hidden layers              | Smooth, zero-centered | Slower computation       |
| Softmax    | (0,1)     | Output layer (multi-class) | Probabilities         | Not for hidden layers    |

</div>