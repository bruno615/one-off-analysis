# Exploring the USA Names Data Set using Google bigquery

# For this analysis, I wanted to pick the most popular gender-neutral name.
# In order to do this, I find the percential ranking by each gender.
# To find the most popular name, I minimize the distance to the origin.

# Let's start by setting up R.  

# install.packages("bigrquery")
library("bigrquery")

# There is some initial setup required if this is the first time using bigquery
# Details found here: https://github.com/rstats-db/bigrquery

# Substitute the project name for the one you set up
project <- "alerts-emailer"

# Write the Query
sql <- "
select 
    name, 
    sum(case when gender = 'M' then rank end) rank_male,
    sum(case when gender = 'F' then rank end) rank_female

from(
    select 
      name, 
      gender,
      percent_rank() over (partition by gender order by number desc) as rank
    from (
        select 
          name, 
          gender, 
          sum(number) as number
        from [bigquery-public-data:usa_names.usa_1910_2013]
        where year between 2000 and 2009
        group by 1,2
        order by 1
        )
)
group by 1
"
# Execute Query
data <- query_exec(sql, project = project)
# Using Pythagorean Theorem to determine distance from origin
data$length <- (data$rank_male^2 + data$rank_female^2)^(1/2)
# Result Set
head(data[order(data$length),])
