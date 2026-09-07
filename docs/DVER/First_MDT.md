##### 1. List data types available in R and provide one example of each tyре.
Ans. 

- Numeric:  Set of all real numbers , "numeric_value <-3.14"
- Integer:  Set of all integers,       "integer_value <- 42L"
- Logical:  TRUE and FALSE,            "logical_value <- TRUE"
- Complex:  Set of complex numbers,    "complex_value <- 1+2i"
- Character:                            "character value <- "Hello Geeks"
- raw:      as.raw(),                   "single_raw <- as.raw(255)"


##### 2. Define univariate graphs.
Ans.

Univariate graphs are visual representations that display the distribution 
of a single variable. They help in understanding the characteristics of one
variable, such as its central tendency, spread, and shape. Common types include
histograms, box plots, and bar charts. These graphs focus on summarizing data 
related to one variable only.


##### 3. Explain the structure and use of arrays in R.
Ans.

In R, arrays are multi-dimensional data structures that store elements of the 
same data type (numeric, character,etc.). Arrays are created using the array()
function and are used for mathematical operations, data manipulation, and
organizing data systematically.


##### 4. Discuss the types of graphs that can be created in R.
Ans.

R supports various graph types, including:

1. Bar graphs for categorical data.
2. Histograms for frequency distribution.
3. Box plots for statistical summaries.
4. Scatter plots for relationships between variables.
5. Line graphs for trends over time.


##### 5. Illustrate bar graphs and histograms in terms of data representation.
Ans.

Bar Graphs:

   - Definition: Bar graphs display categorical data with rectangular bars representing different
   categories.
   - Usage: Each bar's height corresponds to the frequency or value of the category, making it easy
   to compare different groups visually. For example, a bar graph can show the sales figures for different products.

Histograms:

   - Definition: Histograms represent the distribution of continuous numerical data by dividing the
   data into intervals (bins) and counting the frequency of data points within each bin.
   - Usage: The height of each bar reflects the number of observations in each interval, allowing for
   the visualization of data distribution, skewness, and central tendency. It is used for displaying
   the distribution of continuous data.
   For example, a histogram can illustrate the distribution of exam scores among students.


##### 6. Demonstrate the structure of a list that contains vectors and data frames.
Ans.

- List: A list can contain elements of different types and sizes, making it suitable for storing heterogeneous data.
- Vectors: These are one-dimensional arrays that hold elements of the same type, such as numeric or character
data.
- Data Frames: These are two-dimensional, table-like structures that can hold different types of data across
columns, similar to a spreadsheet.

Example : 
```python
# Create vectors
ages <- c(18, 19, 20)
names <- c("Alice", "Bob", "Charlie")

# Create a data frame
scores <- data.frame(
Subject = c("Math", "Science", "English"),
Score = c(85, 90, 95)
)

# Create a list containing the vectors and data frame
my_list <-list(Ages = ages, Names = names, Scores = scores)
```


::page break::



##### 7. Discuss role of ggplot2 themes to enhance the readability of complex graphs.
Ans.

In ggplot2, themes control non-data elements like background, gridlines, fonts, and
legends. They enhance readability of complex graphs by reducing clutter and
highlighting key insights. Built-in themes (theme_bw, theme_minimal, etc.)
or custom themes improve clarity, making visualizations more professional,
interpretable and effective for data communication.



##### 8.  Describe following base R graphics -bar chart, pie chart, and line chart 
Ans. 

- Bar Chart:
A bar chart represents categorical data using rectangular bars with lengths proportional to the frequencies. It is useful for comparing
categories.


- Pie Chart:
A pie chart shows proportions of categories as slices of a circle. It is best suited for visualizing percentage contributions.

- Line Chart:
A line chart is generally used for continuous or time-series data, showing trends and changes over an interval.




##### 9. Apply R data frames to store student details (Roll No, Name, Marks). Demonstrate code to:
##### a) Display names of students scoring more than 75.
##### b) Add a new column 'Grade' using conditional logic.

```python
# Create data frame of student details
students <- data.frame(
RollNo = c(101, 102, 103, 104, 105),
Name = c("Amit", "Neha", "Ravi", "Priya", "Karan"),
Marks = c(88, 72, 95, 64, 81)
)


#a) Display names of students scoring more than 75
high_scorers <- students$Name[students$Marks > 75]
print("Students scoring more than 75:")
print(high_scorers)

#b) Add new column 'Grade' using conditional logic
studentsSGrade <- ifelse(students$Marks >= 85, "A",
ifelse(students$Marks >= 70, "B", "C"))

#Display updated data frame
print("Student details with Grades:")
print(students)
```

##### 10.  Apply ggplot2 features including aesthetic mappings and facets using the built-in mpg dataset.
- a) Create a scatter plot of displ vs. hwy, mapped with color = class and size = cyl.
- b) Add facets by drv
- c) Use summary() function to provide statistical overview of a given dataset.

```python
#Load ggplot2
library(ggplot2)

#a) Scatter plot of displ vs hwy with color=class and size=cyl
ggplot(mpg, aes(x = displ, y = hwy, color = class, size = cyl)) +
geom_point()+
labs(title = "Displacement vs Highway Mileage",
x= "Engine Displacement (liters)", y = "Highway MPG")

#b) Add facets by 'dry
ggplot(mpg, aes(x = displ, y = hwy, color = class, size = cyl)) +
geom_point()+
facet_wrap(~drv) +
labs(title = "Displacement vs Highway MPG Faceted by Drive Type")

#c) Statistical overview of dataset
summary(mpg)

```


##### 11. Apply ggplot2 features including annotations, zooming and scales using the built-in diamonds dataset.
- a) Create a scatter plot of carat vs. price.
- b) Add an annotation marking the diamond with maximum price.
c) Use coord_cartesian() to zoom in on diamonds with price < 20000.


```python
#Load library
library(ggplot2)

#a) Scatter plot of carat vs. price
p<- ggplot(diamonds, aes(x = carat, y = price)) +
geom_point(alpha = 0.5, color = "blue") +
labs(title = "Scatter Plot of Carat vs Price in Diamonds Dataset".
x = "Carat",
y= "Price")

#b) Add annotation for the diamond with maximum price
max_point<- diamonds[which.max(diamonds$price), ]
p<-p+ geom_point(data = max_point, aes(x = carat, y= price),
color = "red", size = 4) +
annotate("text", x = max_point$carat, y = max_pointSprice,
label = paste("Max Price:", max_pointSprice),
vjust =-1, color = "red")

# c) Zoom in on diamonds with price < 20000
p<-p+ coord_cartesian(ylim = c(0, 20000)) +
scale_x_continuous(limits = c(0, 5)) + # optional scaling of x-axis
theme_minimal()
```


##### 12. Evaluate the potential errors in interpretation when using a heat map with insufficient data.
Ans.

Potential Errors in Interpretation When Using a Heat Map with Insufficient Data
1. Misleading Patterns:
     Insufficient data can lead to the visualization of spurious patterns or trends that do not accurately reflect
the underlying relationships. Random fluctuations in a small dataset may appear significant in a heat
map, leading to incorrect conclusions.

2. Overgeneralization:
Heat maps are often used to summarize data across categories or groups. With limited data, the results
may be overgeneralized, ignoring variations within categories. This can misrepresent the diversity of the
data and lead to erroneous interpretations about the entire dataset.

3. Poor Statistical Representation:
Heat maps typically rely on aggregating values, such as averages or sums. If the data sample is too
small, these aggregated values may not represent the true characteristics of the population, resulting in
misleading heat map visuals.

4. Color Interpretation Issues:
o The choice of color gradients in heat maps can significantly affect interpretation. With insufficient data,
even slight changes in color can lead to overemphasized differences, misleading the viewer about the
importance or significance of those differences.
5. Neglecting Context:
o Without sufficient data, important contextual factors may be overlooked. Heat maps can simplify
complex datasets, but insufficient data might fail to capture critical influences or correlations, leading to
incomplete or flawed interpretations.
6. False Sense of Confidence:
• Viewers may perceive heat maps as definitive due to their visual appeal and clarity. When based on
insufficient data, this can create a false sense of confidence in the findings, leading stakeholders to make
decisions based on unreliable information.

A heat map with insufficient data can lead to various errors in interpretation, including misleading patterns,
overgeneralization, poor statistical representation, color interpretation issues, neglecting context, and a false
sense of confidence. Careful consideration of data sufficiency is essential for accurate visual representation
and analysis.

::page break::


##### 13. Evaluate the relationship between three variables using a 3D scatter plot.
Ans. 
A 3D scatter plot allows for the visualization of relationships among three variables simultaneously, providing
insights that cannot be captured in two dimensions. 
1. Visualization of Relationships:
A 3D scatter plot displays data points in a three-dimensional 'space, with each axis representing one of
the three variables. This allows for a clear visualization of how the variables interact. For example, if
variables are labeled as X, Y, and Z, each point in the plot representsa unique combination of these
three variables.

2. Identifying Correlations:
• By examining the distribution of points in the 3D space, you can identify potential correlations among
the variables. For instance, if the points tend to cluster along a diagonal or a plane, this may suggest a
linear relationship between the variables. Conversely, a random scattering of points may indicate no
correlation.
3. Understanding Interactions:
o 3D scatter plots enable the exploration of interactions between variables. For example, if you have a
third variable that changes the relationship between the other two (e.g., moderating or mediating
effects), this can be observed visually. Clusters of points might emerge at different levels of the third
variable, suggesting varying relationships depending on its value.
4. Detecting Outliers:
A 3D scatter plot can help in identifying outliers that may skew the analysis. Points that lie far from the
general distribution of the data can indicate anomalies or errors in data collection, which may warrant
further investigation.
5. Dynamic Interaction:
• Utilizing interactive 3D scatter plot tools (e.g., Plotly, R's rgl package) allows for rotating and zooming
in on the plot, providing a deeper understanding of the data structure and relationships. This interactivity
can reveal patterns that might be missed in static plots.
6. Limitations and Considerations:
• While 3D scatter plots provide valuable insights, they can also be misleading. Over plotting can occur
when many data points overlap, making it difficult to discern relationships. Additionally, viewers may
struggle to accurately interpret depth and distances in 3D visualizations. It's important to complement
the visual analysis with statistical measures, such as correlation coefficients, to confirm findings.


A 3D scatter plot is a powerful tool for evaluating the relationships between three variables. It aids in visualizing
correlations, understanding interactions, detecting outliers, and providing a dynamic exploration of data. However,
careful consideration of its limitations is essential for accurate interpretation.
