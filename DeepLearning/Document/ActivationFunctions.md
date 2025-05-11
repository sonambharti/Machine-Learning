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

-   Use: Early Perceptron models <br>
-   Problem: Non-differentiable → can’t be used with backpropagation <br>

2. Sigmoid / Logistic Function
Formula: