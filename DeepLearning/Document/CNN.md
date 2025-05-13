In Neural Network, for a image if there are (1000 * 1000) pixel and 3 layers for RGB then first input layer will have (3 * 1000 * 1000)  neurons and then next layer will have 1000 neurons.
So, the number of weights will be (3 * 10^6 * 10^3).

But here is a catch, More no. of neurons and more no. of weights will lead to the overfitting of the model. Thus, it will affect the performance of the application. So, To overcome this limitation we now use convolutional neural networks.

In CNN, For such images we use convolutional layers. Here we apply filters on the image such as (vertical edge filters, horizontal edge filters, and many more) to detect edges and features of the images which reduce the no of neurons drastically (say, if we apply only these 2 filters to detect the features of the image, then we'll have 9 neurons only).  Each time while sliding through the image we will reduce the neuron size to it's half. 


Convolution Operation:
1.	This operation is used to detect the feature of the image.
	Let's say we have an image matrix, I of size (6 * 6). And a kernel (filter matrix), K of size (3 * 3).
	Now, the output matrix, O of this process will be of size (4*4).
	
2.	 And, the value of this matrix will be calculated from:
	
	O(0,0) = (( I(0,0)*K(0,0) + I(0,1)*K(0,1) + I(0,2)*K(0,2)) + (I(1,0)*K(1,0) +  I(1,1)*K(1,1) + I(1,2)*K(1,2)) +  (I(2,0)*K(2,0) +  I(2,1)*K(2,1) + I(2,2)*K(2,2)))

	Same process will be followed for each row and column of the image using stride. 

	Stride is the steps that kernel moves each time to cover each row and column of the image.

	Also, we can use padding (i.e. add zeros) around the input to maintain the output size and preserve the feature of the image.

3.	Here, we are taking stride = 1. i.e., moving 1 row or column in each iteration. And, We didn't add any padding for now.
	
	So, the size of output matrix will be calculated by

	(n*n) * (f*f) =  (n - f + 1) * (n - f + 1)
	
	This is the result for 1 filter only. If we provide c number of filters then output size will be
	(n*n) * (f*f) * c =  (n - f + 1) * (n - f + 1) * c

Note: The above calculation was for grey or black-and-white image.

Now, How do we calculate convolutional operation over the colored image.

1.	So, for color images, we will use the filter of (f * f * 3) size, which means filters having 3 channels (like RGB - channels in color image)

2.	The  output matrix will have only 1 channel which will be calculated by the same way we were calculating in the grey image but this time we'll include the 3 channels too.

3. We can use multiple filters or m no. of filters for this image.


Padding
1.	Padding means add zeros) around the input image  to maintain the output size and preserve the feature of the image. 
2.	Preserve the feature means, if we don't add padding then corner pixel will be considered only once and hence we can loose the feature detail of the image. 
3.	We can add multiple layers of padding to preserve the size of the image.

Valid Convolution Vs. Same convolution
1.	 Valid convolution means no padding. Whereas, Same convolution means add padding in such way the size of original image and the convolutional image is same.
	
		Here, in the above example if we add one row before the first row, one row after the last row, and one col before the first col, one col after the last col. Then,
	the size of the new image after padding will be (8 * 8) and kernel size is (3 * 3) and it will generate output of size (6 * 6) which is of same size of the original image.

	Here, No. of padding, p = 1 in each side
	n' = n + 2p
	
	So,
	(n' - f + 1) = n
	(n + 2p -f + 1) = n
	p = (f - 1)/2,		Note: f is usually odd.
	

Stride
1.	Stride is the number of steps that kernel moves each time to cover each row and column of the image. It can be any no.
2.	If we have stride value 2, then the kernel/filter will move by 2 pixels in the image.
3.	What will happen to the left pixels if there is only 1 row left after 2 stride and kernel size is (3 * 3). We will just discard that row from  the convolution.
4. 	Hence, the size of the output image after the stride will be
	
	Size of Output Image, O1 = floor((n - f)/s) + 1 , for the image size n * n
	
	Size of Output Image, O2 = ( floor((n1 - f)/s) + 1) * ( floor((n2 - f)/s) + 1) , for the image size n1 * n2



Max Pooling Layer in CNN
1.	There are many types of pooling layer in CNN. The function of pooling layer is to reduce the size or the dimension of the image while preserving the feature of the image.
2.	What is Max Pooling?
	-	Extract the maximum value of the output of the convolutional image window(kernel size) when filter is sliding by the given stride.
3. 	Why do we want this or need of Max Pooling?
	-	It reduces the image size. Hence, results in reducing the computational cost and getting the output faster or fasten model training.
	- 	Even though it reduces the size of the image, it still preserve the feature of the image or enhance feature. 
4.	Where do we apply Max Pooling Layer?
	-	Only after convolutional operation we apply max pooling layer
5.	We will receive the same no. of images after max pooling, that we get after convolutional layer during the operation with c no of kernels/filters.
6.	It is not always necessary to apply max pooling layer after each convolutional layer, or we can just skip max pooling layer.
7.	Use of the max pooling  layer can improve the performance of the model.
8.	Different types of Pooling layer:
	i.)	Max Pooling
	ii.)	Average Pooling - Find the average of the output of the convolutional image  window (kernel size)
9.	No parameters involved, thus no training required
10.	Same no. of channels in output as input.

 
Fully Connected CNN
1.	Fully connected layers is a dense network of neurons or connection between every 2 neurons, same as simple neuron networks.
2.	Where do we use Fully Connected CNN?
	-	We use it to categorise the category of the image after feature extraction process of the image (i.e. Convolutional Operation and after max pooling).
	-	We use it after the flattening of the image matrix of each channel and each filters 
	-	Last layer of fully connected layer will have the same no. of neurons as we have the different category to categorize the image. (i.e. No. of neurons in last layer = No. of classes to categorize the image)
3.	In last layer of Fully connected layer we will use Softmax activation function to classify image into a particular category for multi-class classification.
4.	In last layer of Fully connected layer we will have 2 neurons for binary class classification, and will use Sigmoid activation function to classify image into a particular category.
5.	The weights in the fully connected layers are trainable parameters to learn, and play a vital role in associating the relation between the features of the different categories or labels of the image.
6.	Thus, fully connected layers are the essential part of the Convolutional Neural Network (CNN) architecture.



CNN Architecture
1.	Together a convolutional layer and 1 max pooling layer is known as 1-layer. Now this output will be the input of the next convolutional layer with either same or different filter sizes.
	And, this will continue repeating these layer to get different layers of the CNN depending on the different types of applications.
2.	If we are performing complex application, then we might need large number of CNN network for complex CNN architecture, and vice versa.
3.	For large architectures we can skip / remove the max pooling layers from the CNN architecture as we don't want to reduce the size of the image too much before getting any output.
4.	But, for smaller applications we will only need smaller no. of CNN network, hence the use of max pooling will definitely increase/enhance the performance of the architecture.
5.	Once, we are done with all convolutional and max pooling layer, it's time to add fully connected layer.
6.	Before we can add fully connected layer, we need to flatten this final image output into one-dimensional array.
7.	 Once, it is flattened. Connect it with fully connected layer.
8.	Now, at final layer, we can use Sigmoid or SoftMax activation function according to the application requirement (either binary class classification or multi-class classification) to get y_pred.
9.	Now, we must have to train the model before using it or predict any value. Otherwise, how these parameter will learn what values we have to take.
10.	So, for that we need to apply cost function or loss function to find the loss between the predicted value and the actual value.
11.	The type of cost function will depend on what classification we need to execute. (such as, Binary cross entropy for Binary classification, and Category cross entropy for multiclass classification).
12.	Again, in order  to minimize the cost we will use Back propagation algorithm / technique in Artificial Neural Network (like, gradient descent, SGD (Stochastic gradient descent), adam, gradient descent with adam, gradient descent with momentum, etc).



Tensorflow Vs Keras
-	Tensorflow is a open source python library developed by Google for Machine Learning, Deep Learning purposes. Whereas, Keras is also a open source library python library.
-	Tensorflow is written in C++ . Whereas, Kera is written in Python.
-	Tensorflow is most widely used  framework for building large scale Artificial Intelligence and Deeplearning applications. Wheras, Keras is a higher level API than tensorflow.
-	Tensorflow works by creating a computational graph, and then it is later on executed by passing it input values (i.e. multi-dimensonal vectors also called as tensors). 
	Whereas, since keras is higher level API, it runs above/ on the top of the tensorflow.
-	Writing code in Tensorflow is bit challenging i.e. not easy to code. Whereas, writing code in keras is extremly easy.
-	Trining the model is fast in Tensorflow because tensorflow is light weight framework. Whereas, training in keras is slow because it is a higher level API.
-	Tensorflow is mainly used for bigger and higher level applications. Whereas, Keras is used for rapid protyping and hence we can build any application very quick and also change the features and enhancement can be done rapidly.
-	Tensorflow is bit difficult to debug. Whereas, Keras has lesser need to debug.
-	Tensorflow is used for large dataset. Whereas, Keras is used for small dataset.
-	Tensorflow has biggest community support. Whereas, Keras has smaller community support.

