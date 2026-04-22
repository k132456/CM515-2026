# My first script

print("Hello World")
date()
getwd()

# Assignment - assigning a value to x
x <- 5 + 7
x
ls()

# assign a series of words to the vector object called organism:
organism <- c("human", "mouse", "worm", "yeast", "maize")
summary(organism)

# Recall the vector
organism


# Recall just the first element
organism[1]

# Recall just the second element
organism[2]



# Let's create a vector for each organism's kingdom like so:
kingdom <- c("animalia", "animalia", "animalia", "fungi", "plantae")

# What is the class of this vector?
class(kingdom)

# What is its structure?
str(kingdom)

# By default, this vector is a character vector. However, we can convert it to a character vector like so. This is a reassignment expression that overwrites the old vector kingdom with a factor vector.
kingdom <- as.factor(kingdom)

# check what happened:
class(kingdom)
str(kingdom)

users <- c("alvin", "viet", "leila")
logins <- c(12, 5, 34)

class(users)
class(logins)

super_vector <- c(users, logins)
class(super_vector)

super_vector_num <- as.numeric(super_vector)
super_vector_num

nums <- c(12, 5, 7)
num_lets <- c("4", "8", "3")

super_nums_lets <- c(nums, num_lets)
class(super_nums_lets)
super_nums_lets_as_num <- as.numeric(super_nums_lets)
super_nums_lets_as_num



# Ensure you have a character vector called organism with a length of 5
str(organism)

# Ensure you have a factor vector called kingdom with a length of 5
str(kingdom)

# Create a numeric vector called chromosomes with corresponding data:
chromosomes <- c(23, 20, 5, 16, 10)
str(chromosomes)

# Create a logical vector called haploid with corresponding data
haploid <- c(FALSE, FALSE, FALSE, TRUE, FALSE)
str(haploid) 

# Now, put it all together using the function data.frame()
model_systems <- data.frame(organism, chromosomes, kingdom, haploid)

# Explore what you have created
model_systems
dim(model_systems)
str(model_systems)
class(model_systems)

head(model_systems)
tail(model_systems)

model_systems$chromosomes
model_systems$haploid

model_systems[3, ]

model_systems[ ,2]

model_systems[3,2]


# How many rows are there?
nrow(model_systems)

# How many columns are there?
ncol(model_systems)

# What are the names of the columns?
colnames(model_systems)

# What are the names of the rows?
rownames(model_systems)

# What is the dimension of the data frame?
dim(model_systems)

# What is the structure of this object?
str(model_systems)

# Can you give me a summary of the data?
summary(model_systems)

help(dim)
help(nrow)

# Heather's code:
#languages <- ("English", "Spanish", "Japanese", "French")
#_greetings_ <- c("hello", "hola", "ohio", "bonjour")
#partings < c("bye", "adios", "mata", "salut")
#dictionary <- DataFrame(languages, _greetings_, partings)
#dimens(dictionary)
#dictionary


#Corrected - Heather's code
languages <- c("English", "Spanish", "Japanese", "French")
greetings <- c("hello", "hola", "ohio", "bonjour")
partings <- c("bye", "adios", "mata", "salut")
dictionary <- data.frame(languages, greetings, partings)
dim(dictionary)
dictionary



L <- list("human", "mouse", "worm", "yeast", "maize")
L
str(L)

L <- list("human", 23, factor(c("animalia")), FALSE)
L
str(L)


organism <- c("human", "mouse", "worm", "yeast", "maize")
kingdom <- c("animalia", "animalia", "animalia", "fungi", "plantae")
kingdom <- as.factor(kingdom)
chromosomes <- c(23, 20, 5, 16, 10)
haploid <- c(FALSE, FALSE, FALSE, TRUE, FALSE)
model_systems <- data.frame(organism, chromosomes, kingdom, haploid)
str(model_systems)


help(dim)
help(mean)

animalia <- data.frame(
  organism = organism[1:3],
  chromosomes = chromosomes[1:3],
  haploid = haploid[1:3]
)
animalia

fungi <- data.frame(
  organism = organism[4],
  chromosomes = chromosomes[4],
  haploid = haploid[4]
)
fungi

plantae <- data.frame(
  organism = organism[5],
  chromosomes = chromosomes[5],
  haploid = haploid[5]
)
plantae

kingdoms <- list(animalia = animalia, fungi = fungi, plantae = plantae)
kingdoms
str(kingdoms)

# Take the average # of chromosomes
mean(chromosomes)

# Take the average # of chromosomes of 80 % of the data
mean(chromosomes, trim = 0.2)

# create a vector with an NA in it:
incompleteVector <- c(2, 5, 8, 9, 10, 200, NA, 3)
mean(incompleteVector)
mean(incompleteVector, na.rm = TRUE)

func <- function() {
  # code goes here
}

greeting <- function() {
  print("Hello world!")
}

greeting()

add_5 <- function(num) {
  return(num + 5)
}

add_5(5)


add_5 <- function(num = 0) {
  return(num + 5)
}

add_5(5)
add_5()


convert_temperature <- function(temp, unit = "farenheit") {
  if(unit == "farenheit") {
    temp <- (temp - 32) * 5/9
    return(temp)
  }
  if (unit == "celcius") {
    temp <- (temp * 9/5) + 32
    return(temp)
  }
}

convert_temperature(32)
convert_temperature(0, unit = "celcius")


#writing functions practice:
#write a function that takes as arguments: number of seeds planted, number germinated; and calculates germination %

germ_percent <- function(num_planted, num_germ) {
  return(num_germ/num_planted)
}
 
germ_percent(100, 67)


#write a function that "# This function takes a numerical grade (e.g. 75.4), and returns True or False depending on whether that grade will earn a B (between 80 and 90)"
is_it_a_b <- function(grade) {
  if (grade >= 80 && grade < 90) {
    return(TRUE)
  }
  else {
    return(FALSE)
  }
}

is_it_a_b(74)
is_it_a_b(92)
is_it_a_b(84)

#write a function that "# This function determines whether two string sequences are equivalent: returns True if they are equivalent, and False if they are not."

are_same <- function(vec1, vec2) {
  return(identical(vec1, vec2))
}

vec_a <- c("moon", "sun", "earth", "mars")
vec_b <- c("moon", "sun", "earth", "mars")
vec_c <- c("shorts", "dress", "pants", "shirt")

are_same(vec_a, vec_b)
are_same(vec_b, vec_c)


getwd()


#setwd("~/GitHub/CM515-2026/modules/wk_11_rstudio")



# Check we're in the right place
getwd() 

# Check how read.table is used
help(read.table)

# Look at the data using read.table
read.table("life-expectancy_1900-2023_CountriesOnly.csv", sep = ",", header = TRUE)


# That only printed out the data from the file, it didn't capture it.
# To capture the data, use an assignment expression:
lifeExp <- read.table("life-expectancy_1900-2023_CountriesOnly.csv", sep = ",", header = TRUE)

# EDA
dim(lifeExp)
str(lifeExp)
class(lifeExp)
summary(lifeExp)


# Amend data types
lifeExp$Entity <- as.factor(lifeExp$Entity)
lifeExp$Code <- as.factor(lifeExp$Code)

# EDA Again
dim(lifeExp)
str(lifeExp)
head(lifeExp)
class(lifeExp)
summary(lifeExp)



help(read.table)

read.table("temperature-anomaly.csv", sep = ",", header = TRUE)

temp_anom <- read.table("temperature-anomaly.csv", sep = ",", header = TRUE)
head(temp_anom)


# EDA
dim(temp_anom)
str(temp_anom)
class(temp_anom)
summary(temp_anom)


temp_anom$Entity <- as.factor(temp_anom$Entity)
temp_anom$Code <- as.factor(temp_anom$Code)



# EDA
dim(temp_anom)
str(temp_anom)
class(temp_anom)
summary(temp_anom)





# Let's subset the so we only keep data for the USA:

lifeExpUS <- lifeExp[which((lifeExp$Code) == "USA"), ]

dim(lifeExpUS)
head(lifeExpUS)

# Now, let's explore the function write.table() 
help(write.table)

getwd()



# Let's subset the so we only keep data for the USA:

lifeExpUS <- lifeExp[which((lifeExp$Code) == "USA"), ]

dim(lifeExpUS)
head(lifeExpUS)

# Now, let's explore the function write.table() 
help(write.table)



write.table(lifeExpUS, file = "lifeExpectancy_USA.txt", sep = "\t")

write.table(lifeExpUS, file = "lifeExpectancy_USA.txt", quote = FALSE, sep = "\t")

help(write.csv)

write.csv(lifeExpUS, file = "lifeExpectancy_USA.csv")

write.csv(lifeExpUS, file = "lifeExpectancy_USA.csv", row.names = FALSE)

# Do this once:
install.packages("viridis")


# Do this each time you want to use a viridis package:
library(viridis)

library(tidyverse)

sessionInfo()

x <- y <- seq(-8*pi, 8*pi, len = 40)
r <- sqrt(outer(x^2, y^2, "+"))
filled.contour(cos(r^2)*exp(-r/(2*pi)), 
               axes=FALSE,
               color.palette=viridis,
               asp=1)


# Calculate the mean Lifespan per year across all countries
lifeExp_byYear <- lifeExp %>%
  group_by(Year) %>%
  summarise(mean = mean(Period_Life_Expectancy, rm.na = TRUE) )

# Plot the LifeSpan for each year
plot(lifeExp_byYear, 
     ylim = c(0,80),
     main = "Period of Life Expectancy (in years) at birth, in a give year",
     ylab = "Life Expectancy (yr)", 
     xlab = "Year", 
     col = "grey", 
     pch=20 )

# Smooth the plot
lo10 <- loess(mean ~ Year, data=lifeExp_byYear, span=0.10)
smoothed10 <- predict(lo10) 

# Add the smoothed trendline
points(lifeExp_byYear$Year, 
       smoothed10, 
       col = "darkorange", 
       type = "l", 
       lwd = 2)


# Another way of plotting
boxplot(Period_Life_Expectancy ~ Year, data = lifeExp)