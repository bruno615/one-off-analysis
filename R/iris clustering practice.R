
# Machine Learning using iris

# For the sake of repeatability, we will use set.seed to make our data analysis repeatable.
set.seed(244)

# Data Discovery #############################

# Plot will graph every combination of columns against itself
plot(iris)

# Let's see what the distribution of our data is
table(iris$Species)

# We might want to view the distribution of a single column
plot(table(iris$Sepal.Width))

# K Means Clustering #################################

# Let's see how well we can determine the plant species using clustering
# In this event, we know that there are 3 species, so K = 3

# Let's look again at the plot of iris
plot(iris)
  # It looks as though petal length and width have very little overlap between the different species.
  # We will start there 

# We use kmeans with our pared down dataset
  # Our data set is reduced to 2 columns for simplicity and ease of graphing (not a requirement)
  # centers is the K, which for our case is 3
  # nstart is the number of random initial starting points.  It will try n times to obtain the best values for the clusters

cluster_petal <- kmeans(cbind(iris$Petal.Length, iris$Petal.Width), centers = 3, nstart = 1)

# Exploring the resulting kmeans object ###################################

# General output
print(cluster_petal)

# Data grouping
ggplot(iris, aes(Petal.Length, Petal.Width, color = as.factor(cluster_petal$cluster))) + geom_point()

plot(iris$Species, cluster_petal$cluster)

# Performance
table(cluster$cluster, iris$Species)







# Create DepVar
data <- iris
data$is_setosa <- 0
data$is_setosa[data$Species == 'setosa'] <- 1



# Linear Model
lm_model <- lm(is_setosa ~ Sepal.Length + Sepal.Width + Petal.Length, data = data)
lm_model <- lm(Sepal.Width ~ Sepal.Length + Petal.Width + Petal.Length, data = data)


# Gradient Logistic Model
glm_model <- glm(Sepal.Length ~ Sepal.Width + Petal.Length, 
                 family = binomial(link = "logit"),
                 data = data)

glm_model <- glm(is_setosa ~ Sepal.Width + Petal.Length, 
                 family = binomial(link = "logit"),
                 data = data)


iris

plot(iris)
library(ggplot2)
ggplot(iris, aes(Petal.Length, Petal.Width, color = Species)) + geom_point()

