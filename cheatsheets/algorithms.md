# Algorithms

## Supervised

### Regression Techniques
Regression algorithms are machine learning techniques for predicting continuous numerical values. They are supervised learning tasks which means they require labeled data.
Cases
* Predicting the appropriate price for a product based upon size, brand, and location.
* Predicting the number of sales each day based upon store location, public holidays, day of the week and the closest competitor store.

#### Linear Regression
Linear regression attempts to fit a straight hyperplane to your dataset that is closest to all data points. It is most suitable when there are linear relationships between the variables in the dataset.
Pros
* Quick to compute and can be updated easily with new data
* Relatively easy to understand and explain
* Regularization techniques can be used to prevent overfitting
Cons
* Unable to learn complex relationships
* Difficult to capture non-linear relationships (without first transforming data which can be complicated)


#### Decision Trees
Decision trees learn how to best split the dataset into separate branches, allowing it to learn non-linear relationships.  Random forests (RF) and Gradient Boosted Trees (GBT) are two algorithms that build many individual decision trees, pooling their predictions. As they use a collection of results to make a final decision, they are referred to as 'Ensemble techniques'.
Pros
* A single decision tree is fast to train
* Robust to noise/outliers and missing values
* RF perform very well “out-of-the-box"
Cons
* Single decision trees are prone to overfitting (which is where ensembles come in!)
* Complex trees are hard to interpret


#### K-Nearest Neighbors
K-Nearest Neighbor (KNN) makes a prediction for a new observation by searching for the most similar training observations and pooling their values.
Pros
* Simple
* Powerful
* No training involved
Cons
* Expensive & slow to predict new instances
* Performs poorly on high dimensional datasets

1. Pick a value for K.
2. Calculate the distance from the new case (holdout from each of the cases in the dataset).
3. Search for the K observations in the training data that are ‘nearest’ to the measurements of the unknown data point.
4. predict the response of the unknown data point using the most popular response value from the K nearest neighbors.
There are two parts in this algorithm that might be a bit confusing.
First, how to select the correct K; and second, how to compute the similarity between cases,
for example, among customers?


Although the predictor variables of Polynomial linear regression are not linear the relationship between the parameters or coefficients is linear.

#### Neural Networks
Neural networks can learn complex patterns using layers of neurons which mathematically transform the data. The layers between the input and output are referred to as “hidden layers”. A neural network can learn relationships between the features that other algorithms cannot easily discover.
Pros
* Extremely powerful / state of the art for many domains (e.g. computer vision, speech recognition)
* Can learn even very complex relationships
* Hidden layers reduce need for feature engineering (no need to understand underlying data)
Cons
* Require a very large amount of data!
* Prone to overfitting
* Long training time
* Requires significant computing power for large datasets (computationally expensive)
* Model is a "black box", unexplainable

### Classification Techniques
Classification algorithms are machine learning techniques for predicting which category the input data belongs to. They are supervised learning tasks which means they require labeled data.
Cases
* Predicting a clinical diagnosis based upon symptoms, laboratory results and historical diagnosis.
* Predicting whether a healthcare claim is fraudulent using data such as claim amount, drug predisposition, disease and provider

#### Logistic Regression
Logistic regression predicts the probability of a binary outcome. A new observation is predicted to be within the class if its probability is above a set threshold. There are methods to use Logistic Regression for scenarios where there are multiple classes.
Pros
* Quick to compute and can be updated easily with new data
* Output can be interpreted as probability; this can be used for ranking
* Regularization techniques can be used to prevent overfitting
Cons
* Unable to learn complex relationships
* Difficult to capture non-linear relationships (without first transforming data which can be complicated)

#### Naïve Bayes
Naïve Bayes assumes that all features are independent, that they independently contribute to the probability of the target variable's class; this does not always hold true which is why it is referred to as "Naive". Various probabilities and likelihood values are calculated based upon the frequency they appear in the data and the final probabilities calculated using a formula called Bayes Theorem.
Pros
* Simple and easy to interpret
* Computationally fast
* Good for high-dimensional space (lots of features)
Cons
* Performance will be inhibited if significant dependence between variables
* If a class that appears in the test data did not appear in the training data, it will be given a probability of zero


#### Support Vector Machines
If you plot your data in an n-dimensional space (where n is the number of features), Support Vector Machines (SVM) attempt to fit a hyperplane that best separates the categories. When you have a new data point, its position in relation to the hyperplane will predict which category the point belongs to.
Pros
* High accuracy
* Ability to find solutions even if non-linearly separable
* Good for high-dimensional space (lots of features)
Cons
* Hard to interpret
* Can be slow to train large data sets
* Memory-intensive



## Unsupervised

### Clustering
Clustering algorithms are machine learning techniques to divide data into a number of groups where points in groups have similar traits. They are unsupervised learning tasks and therefore do not require labeled data.
Cases
* Segmenting your market based upon similar collections of customers using their location, spending habits and demographics.
* Understanding topics in your documents, whether they are emails, reports, or customer call transactions by exploring the common words


#### DBSCAN
Density-Based Spatial Clustering of Applications with Noise (DBSCAN) attempts to find dense areas of data points and identifies these as a cluster. If data points are close enough to each other, and there are a sufficient number of them, they form a cluster. If not, they are labeled as noise and ignored.
Pros
* Can find arbitrarily shaped clusters
* Does not require defining the number of clusters
* Robust to outliers
Cons
* Cannot cluster datasets with large differences in densities
* Can perform poorly on high dimensional data
* Choosing the right parameters for density can be difficult


#### K-means
K-Means Clustering aims to partition the observations into k clusters. The algorithm will determine which observation is in which cluster and also the center of each cluster. A new observation is assiged the cluster whose center it is nearest to.
Pros
* Simple and easy to implement
* Easy to interpret results
* Fast
Cons
* Sensitive to outliers
* You must define the number of clusters
* Assumes the clusters are spherical
* The clusters are found using a random starting point so may not be repeatable and can require multiple runs to find an optimal solutions

#### Gaussian Mixture Model
With a Gaussian Mixture Model (GMM), we are assuming that the k clusters are of normal distribution. It's algorithm tries to find the mean and standard deviation of each of these clusters. For a new observation, the probability it belongs to each cluster is calculated, resulting in a soft assignment.
Pros
* Does not enforce the clusters to be circular
* Points can be assigned to multiple clusters
Cons
* You must define the number of clusters
* Difficult to interpret

#### Agglomerative Hierarchical Clustering
Agglomerative hierarchical clustering is an algorithm that builds a hierarchy of clusters. Initially all points start as their own cluster, then the two nearest clusters merge as the same cluster. This process continues, clusters merging until only one cluster containing all the data points remains. To identify the significant clusters a threshold would be chosen.
Pros
* Easy probabilistic model with interpretable topics
* Does not require defining the number of clusters
* Clusters can be arbitrarily shaped
Cons
* Slow and therefore not suitable for big data
* Can be hard to identify the correct number of clusters
* Interpretation can be confusing

### Anomaly Detection Techniques
Anomaly Detection is a technique used to identify unusual events or patterns that do not conform to expected behavior. Those identified are often referred to as anomalies or outliers.
Cases
* Detect abnormal behavior of equipment in a manufacturing plant using sensor data such as temperature, pressure and humidity
* Detect and prevent fraudulent spending by understanding normal customer spending amounts, locations and time between taransactions

Clustering techniques are a common approach for anomaly detection. Clusters of "normal" characteristics are identified and if the distance between a new point and all other clusters is too great, it is identified as an anomaly.

#### Autoencoder
An Autoencoder is a technique for dimensionality reduction. It is a type of neural network where the first part of the network, called the encoder, reduces the input to a lower dimension. The second part of the network, called the decoder, aims to reconstruct the original input. The goal is to create a model where the input and the output are the same. A new data point can be passed through the model and if the error between the input data and the computed output is too great, it can be flagged as an "anomaly".
Pros
* Can capture non-linearities and subtle connections between the features
* Variations result in state-of-the-art results
* If the data is temporal, LSTM (long-short-term-memory) autoencoders can be used
Cons
* Requires a very large amount of data
* Many hyperparameters to tune
* Long training time
* Requires significant computing power for large datasets

#### One-Class Support Vector Machines
If you were to plot your data in an n-dimensional space (where n is the number of features), One-Class Support Vector Machines (SVM) attempt to identify the region where most cases lie, these are considered "normal". It will then fit a hyperplane that best separates these "normal" examples from the rest. When you have a new data point, it is labeled as "normal" or an "anomaly" depending how close it is to the "normal" boundary
Pros
* No assumptions on the distribution of the data
* Ability to find normal boundary that is non-linear
* Can be used in high-dimensional space
Cons
* Choosing the right hyper-parameters to find the appropriate non-linear shape of the boundary can be difficult
* Can be slow to train large datasets
* Memory intensive

### Recommendation Engine Techniques
Recommendation Engines are created in order to predict a preference or rating that indicates a users interest in an item/product. The algorithms used to create this system find similarities between either the users, the items or both.
Cases
* Recommend clothing to a customer based on brands, colors, and price of previously purchased clothing
* Recommend a medical treatment for a patient based upon successful treatments given to similar patients using their condition, diagnosis and previous treatment information

#### Content-based Recommenders
Content-based recommenders suggest similar items to those already liked by the customer, whether explicitly (e.g. by rating) or implicitly (by purchasing). This type of system uses metadata describing the item.  Each item is represented as a vector and a distance metric compares the items' vectors to find the most similar.
Pros
* Quick to implement
* No popularity bias - can recommend new items
* Results are interpretable
Cons
* Important to have meaningful metadata, tagging can be tiresome
* "Cold start problem" for new users without history of liking items
* Limits novelty as won't suggest items too disimilar to previously liked

#### Model-based Collaborative Filtering
Collaborative filtering is a method of predicting a user's interest by analysing preferences by other users. There are two types, user-based filtering and item-based filtering.  Model-based recommenders use training data to build a model, a mathematical formula that takes the features of an observation and calculates a prediction. There are many algorithms to use, including neural networks, Bayesian networks and matrix factorization.
Pros
* Fast & scalable; doesn't require the full dataset each time
* User-based suggestions can result in a diverse set of suggestions across domains
* User-based suggestions do not require metadata
Cons
* Data sparsity can result in performance issues
* Models can be complex and slow to train
* "Cold start problem" - new items struggle to be recommended (popularity bias) and for new users with no history its hard to make good recommendations


#### Memory-based Collaborative Filtering
Collaborative filtering is a method of predicting a user's interest by analysing preferences by other users. There are two types, user-based filtering and item-based filtering.  Memory-based filtering computes similarity between users, or items, and uses other users' ratings to make a prediction; a typical approach is a neighborhood-based algorithm. The predicted rating for the user and each item is calcuated using other users' ratings and the similarity distance
Pros
* Quick to implement
* Results are interpretable
* User based suggestions can result in a diverse set of suggestions across domains
Cons
* Data sparsity can result in performance issues
* Slow & computationally expensive - requires the whole dataset to make a prediction
* "Cold start problem" - new items struggle to be recommended (popularity bias) and for new users with little history it's hard to make recommendations
