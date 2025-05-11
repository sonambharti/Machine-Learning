#   Neural Networks
##  Definition & Overview
A Neural Network (NN) is a computational model inspired by the structure and function of biological brains. It consists of interconnected nodes (artificial neurons) organized in layers, designed to recognize patterns, make decisions, or approximate complex functions. Neural networks are the foundation of deep learning and excel at tasks involving unstructured data (e.g., images, text, audio).

##  Theory & Intuition
###  Key Components:
1.  **Neurons (Nodes)**: Basic computational units that process inputs using weights, biases, and activation functions.
2.  Layers: <br>
&nbsp; -   Input Layer: Receives raw data (e.g., pixel values, text embeddings). <br>
&nbsp; -   Hidden Layers: Intermediate layers that transform inputs into higher-level features. <br>
&nbsp; -   Output Layer: Produces final predictions (e.g., class labels, regression values). <br>
3.  Weights & Biases: Learnable parameters that adjust during training to minimize errors.
4.  Activation Functions: Introduce non-linearity to model complex relationships (e.g., ReLU, Sigmoid).

### How It Works:
1.  **Forward Propagation**: Data flows from input to output layer via weighted connections.
2.  **Loss Calculation**: Compares predictions with ground truth (e.g., Mean Squared Error, Cross-Entropy).
3.  **Backpropagation**: Adjusts weights/biases by propagating errors backward through the network.
4.  **Optimization**: Updates parameters using algorithms like Gradient Descent.

##  Mathematics
**Forward Propagation for a Single Neuron**: <br>
For neuron 
<div>
    <div align='center'>
        <code>
            z<sub>j</sub><sup>(l)<sup> = &sum;<sub>i</sub> w<sub>ji</sub><sup>l</sup> a<sub>i</sub><sup>(l-1)</sup> +  b<sub>j</sub><sup>(l)</sup>
            <br><br>
            a<sub>j</sub><sup>(l)<sup> = g(z<sub>j</sub><sup>l</sup>)
        </code>
    </div>
</div>

-   <code>w<sub>ji</sub><sup>l</sup></code> : Weight from neuron i (layer l-1) to neuron j. <br>
-   <code>a<sub>i</sub><sup>(l-1)</sup></code> : Activation of neuron i in previous layer. <br>
-   <code>b<sub>j</sub><sup>(l)</sup></code>: Bias term. <br>
-   g: Activation function (e.g., ReLU: `g(z) = max(0, z))`.

Example: Simple 3-Layer Network <br>
&nbsp;  -   Input layer x, hidden layer h, output layer <br>

<div align='center'>
    <code>
        <code>h = g(<span>W<sub>1</sub>x</span> + <span>b<sub>1<sub></span>)</code> <br>
        <code>y = g(W<sub>2</sub>x + b<sub>2<sub>)</code>
    </code>
</div>



##  Applications
Neural networks are used in:
1.  **Computer Vision**: Image classification (CNNs), object detection. <br>
2.  **Natural Language Processing (NLP)**: Text generation, translation (Transformers). <br>
3.  **Speech Recognition**: Voice assistants, transcription. <br>
4.  **Recommendation Systems**: Personalized content (e.g., Netflix, Spotify). <br>
5.  **Reinforcement Learning**: Game-playing agents (e.g., AlphaGo).


