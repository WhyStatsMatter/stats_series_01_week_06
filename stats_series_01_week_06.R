# Snippet 1: Introduction to Hypothesis Testing
data <- c(90, 100, 110, 120, 130)
null_hypothesis_mean <- 100
t_test_result <- t.test(data, mu = null_hypothesis_mean)

# Snippet 2: Types of Tests
data1 <- c(90, 100, 110, 120, 130)
data2 <- c(95, 105, 115, 125, 135)
t_test_two_sample <- t.test(data1, data2) # Two-Sample t-test
anova_result <- aov(data1 ~ data2) # F-test (ANOVA)

# Snippet 3: Practical Application: A/B Testing
# Simulating A/B Testing for Click-through Rate
group_a <- rbinom(n=1000, size=1, prob=0.10)
group_b <- rbinom(n=1000, size=1, prob=0.12)
t_test_ab <- t.test(group_a, group_b)
