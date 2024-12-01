import streamlit as st
import random

question_bank = [
    {
        "question": "What is the primary advantage of reporting effect sizes alongside hypothesis tests?",
        "options": [
            "a. They provide the exact p-value.",
            "b. They provide an objective measure for comparison.",
            "c. They replace the need for hypothesis testing.",
            "d. They determine the direction of the relationship.",
            "e. None of the above."
        ],
        "answer": "e"
    },
    {
        "question": "Why is the width of a confidence interval important in evaluating an effect size?",
        "options": [
            "a. It determines whether the null hypothesis is rejected.",
            "b. It shows the likelihood that the sample mean equals the population mean.",
            "c. It provides information about the precision of the effect size estimate.",
            "d. It identifies whether the sample data are normally distributed."
        ],
        "answer": "c"
    },
    {
        "question": "What is the primary reason two independent samples are commonly used in research designs?",
        "options": [
            "a. They are easier to analyze statistically.",
            "b. It is often difficult to find legitimate comparison values for a single sample.",
            "c. They eliminate the need for a control group.",
            "d. They allow researchers to avoid assumptions about population variances."
        ],
        "answer": "b"
    },
    {
        "question": "What does Cohen's d represent in the context of effect size?",
        "options": [
            "a. The mean difference between two groups divided by the pooled standard deviation.",
            "b. The ratio of sample sizes in two groups.",
            "c. The sum of the variances divided by the sample sizes.",
            "d. The difference in population variances between two groups."
        ],
        "answer": "a"
    },
    {
        "question": "What is a common rule of thumb to detect variance heterogeneity by comparing variances?",
        "options": [
            "a. Variance heterogeneity exists when the ratio of the largest to smallest variance is greater than 2:1 for equal sample sizes.",
            "b. Variance heterogeneity exists when the ratio of the largest to smallest variance is greater than 4:1 for unequal sample sizes.",
            "c. Variance heterogeneity exists when the ratio of the largest to smallest variance is greater than 2:1 for unequal sample sizes.",
            "d. Variance heterogeneity does not depend on variance ratios."
        ],
        "answer": "c"
    },
    {
        "question": "What is the primary purpose of using a Welch t-test instead of a Student t-test?",
        "options": [
            "a. To handle situations where sample sizes are equal.",
            "b. To account for violations of the variance homogeneity assumption.",
            "c. To ensure nonparametric testing of ranks.",
            "d. To increase Type I error rates in paired samples."
        ],
        "answer": "b"
    },
    {
        "question": "What is the purpose of an omnibus hypothesis test in the context of comparing means of multiple groups?",
        "options": [
            "a. To identify specific pairwise differences between group means.",
            "b. To determine if the population means across all groups are equal.",
            "c. To adjust for multiple comparisons and reduce Type I error.",
            "d. To calculate confidence intervals for pairwise comparisons."
        ],
        "answer": "b"
    },
    {
        "question": "Which measure of effect size represents the proportion of variability in the dependent variable explained by the independent variable?",
        "options": [
            "a. Cohen’s d",
            "b. η² (Eta-squared)",
            "c. p-value",
            "d. Standard error"
        ],
        "answer": "b"
    },
    {
        "question": "What are the main assumptions required for the validity of the ANOVA F test?",
        "options": [
            "a. Errors are non-normally distributed, and variances are unequal across populations.",
            "b. Samples are randomly and independently selected, errors are normally distributed, and variances are equal across populations.",
            "c. Distributions are skewed, and samples are dependent.",
            "d. Data is ordinal, and variances are heterogeneous."
        ],
        "answer": "b"
    },
    {
        "question": "What is the purpose of the Kruskal-Wallis test?",
        "options": [
            "a. To test for differences in means when the assumptions of ANOVA are met.",
            "b. To test whether the distributions of J populations are identical.",
            "c. To estimate the pooled variance across groups.",
            "d. To compute effect sizes for nonparametric analyses."
        ],
        "answer": "b"
    },
    {
        "question": "What is the Familywise Error Rate (FWER)?",
        "options": [
            "a. The probability of making at least one Type II error across a set of contrasts.",
            "b. The probability of making at least one Type I error across a set of contrasts.",
            "c. The total number of errors across all comparisons.",
            "d. The expected proportion of false rejections to the total number of rejections."
        ],
        "answer": "b"
    },
    {
        "question": "Which method is the most commonly used for controlling the Familywise Error Rate in all pairwise comparisons?",
        "options": [
            "a. Holm procedure",
            "b. Scheffé procedure",
            "c. Bonferroni correction",
            "d. Benjamini-Hochberg procedure"
        ],
        "answer": "c"
    },
     {
        "question": "What is the primary purpose of pairwise comparisons in J > 2 independent samples designs?",
        "options": [
            "a. To test the null hypothesis that all group means are equal.",
            "b. To identify specific differences between group means.",
            "c. To replace the need for an omnibus test.",
            "d. To compute effect sizes for all groups."
        ],
        "answer": "b"
    },
    {
        "question": "Which of the following describes a post hoc comparison?",
        "options": [
            "a. Comparisons planned before data collection.",
            "b. Comparisons that include only pairwise contrasts.",
            "c. Comparisons that arise after examining the data.",
            "d. Comparisons that require orthogonality."
        ],
        "answer": "c"
    },
    {
        "question": "What does the intercept (b0) represent in a linear model with a two-level categorical predictor?",
        "options": [
            "a. The slope of the predictor variable.",
            "b. The predicted value for the reference group.",
            "c. The residual error for the model.",
            "d. The mean of all groups."
        ],
        "answer": "b"
    },
    {
        "question": "How many dummy variables are required for a categorical predictor with 4 levels?",
        "options": [
            "a. 2",
            "b. 3",
            "c. 4",
            "d. 1"
        ],
        "answer": "b"
    },
    {
        "question": "What are the three classifications of missingness mechanisms?",
        "options": [
            "a. Random, Biased, Skewed",
            "b. Missing Completely at Random (MCAR), Missing at Random (MAR), Missing Not at Random (MNAR)",
            "c. Structural, Informative, Ignorable",
            "d. Missing Independent, Missing Dependent, Missing Irrelevant"
        ],
        "answer": "b"
    },
    {
        "question": "What is the default way missing data is represented in R?",
        "options": [
            "a. null",
            "b. NA",
            "c. missing",
            "d. None"
        ],
        "answer": "b"
    },
    {
        "question": "What is a factorial independent sample design?",
        "options": [
            "a. A design with only one independent variable.",
            "b. A design with more than one categorical independent variable, allowing for the exploration of main and interaction effects.",
            "c. A design with multiple continuous predictors.",
            "d. A design that ignores interaction effects."
        ],
        "answer": "b"
    },
    {
        "question": "In a two-way factorial design, what does the interaction effect test?",
        "options": [
            "a. The combined effect of two independent variables on a dependent variable.",
            "b. The difference in means for a single independent variable.",
            "c. The overall variability in the dependent variable.",
            "d. The error term in the model."
        ],
        "answer": "a"
    },
    {
        "question": "What is a key advantage of mixed models over traditional repeated measures ANOVA?",
        "options": [
            "a. They require fewer data points.",
            "b. They assume homogeneity of variance.",
            "c. They allow flexible treatment of missing data.",
            "d. They do not require normality assumptions."
        ],
        "answer": "c"
    },
    {
        "question": "What does π0i represent in the Level 1 model of a mixed design?",
        "options": [
            "a. The overall grand mean across all participants.",
            "b. The error term for the individual growth parameter.",
            "c. The intercept for individual i at the reference level of the repeated measure.",
            "d. The slope of the repeated measure for individual i."
        ],
        "answer": "c"
    },
    {
        "question": "How does sample size influence the width of a confidence interval?",
        "options": [
            "a. Larger sample sizes increase the width of the confidence interval.",
            "b. Larger sample sizes decrease the width of the confidence interval.",
            "c. Larger sample sizes have no impact on the width of the confidence interval.",
            "d. Larger sample sizes make the confidence interval symmetric."
        ],
        "answer": "b"
    },
    {
        "question": "You perform a hypothesis test with a large sample size and find a significant p-value, but the effect size is very small. What is the most appropriate interpretation?",
        "options": [
            "a. The null hypothesis is absolutely false.",
            "b. The result is practically significant but not statistically significant.",
            "c. The result is statistically significant but may not be practically meaningful.",
            "d. The result is both statistically and practically significant."
        ],
        "answer": "c"
    },
    {
        "question": "To understand the effect of lack of sleep on reaction time, researchers use a 2-sample design where half the participants are randomly sleep-deprived and the other half are not. We obtain an unstandardized effect size between the two groups of 0.47 seconds. What is this value referring to?",
        "options": [
            "a. Raw Mean Difference in reaction time.",
            "b. Cohen’s D.",
            "c. Raw Mean Difference which is standardized by the sample size.",
            "d. Overall mean for the reaction time scores."
        ],
        "answer": "a"
    },
    {
        "question": "Why is the assumption of variance homogeneity important in a two-sample t-test?",
        "options": [
            "a. It ensures that the sampling distribution of the test statistic is normal.",
            "b. It allows the use of a pooled variance, which weights variances by sample size.",
            "c. It reduces the impact of Type II errors.",
            "d. It eliminates the need to calculate separate variances for each group."
        ],
        "answer": "b"
    },
    {
        "question": "Why might a Welch t-test fail to find a significant difference in motivation scores between two classes, even when the Student t-test does?",
        "options": [
            "a. The Welch t-test is less sensitive to violations of normality.",
            "b. The Student t-test is biased towards Type II errors under heteroscedasticity.",
            "c. The Welch t-test is more robust to variance heterogeneity, avoiding inflated Type I errors.",
            "d. The sample sizes in the two groups were not negatively paired."
        ],
        "answer": "c"
    },
     {
        "question": "How does transforming data address nonnormality in statistical tests?",
        "options": [
            "a. It eliminates the need for parametric tests.",
            "b. It reduces variance heterogeneity by scaling data.",
            "c. It adjusts the shape of the distribution to better meet normality assumptions.",
            "d. It increases the variability of extreme scores in both groups."
        ],
        "answer": "c"
    },
    {
        "question": "Why is the Type I error rate higher when performing multiple pairwise t-tests instead of using an omnibus test like ANOVA?",
        "options": [
            "a. The critical value of t decreases with more comparisons.",
            "b. Each test is independent, increasing the likelihood of rejecting a null hypothesis by chance.",
            "c. The omnibus test does not require a pooled error term.",
            "d. Pairwise t-tests are not influenced by sample size."
        ],
        "answer": "b"
    },
    {
        "question": "What does the F-statistic in ANOVA represent?",
        "options": [
            "a. The ratio of within-group variability to between-group variability.",
            "b. The sum of squared deviations between group means.",
            "c. The ratio of between-group variability to within-group variability.",
            "d. The total variability in the data set."
        ],
        "answer": "c"
    },
    {
        "question": "What is the key advantage of using the Welch test instead of the traditional ANOVA F test?",
        "options": [
            "a. It controls for inflated Type I error when variances are equal.",
            "b. It does not assume equal variances across populations.",
            "c. It is robust to violations of the independence assumption.",
            "d. It is designed to detect directional differences between groups."
        ],
        "answer": "b"
    },
    {
        "question": "In the Kruskal-Wallis test, what does rejecting the null hypothesis indicate?",
        "options": [
            "a. The means of the populations are significantly different.",
            "b. The variances of the populations are equal.",
            "c. The population distributions are not all identical.",
            "d. The population distributions are identical."
        ],
        "answer": "c"
    },
    {
        "question": "Why might the False Discovery Rate (FDR) be preferred over the Familywise Error Rate (FWER) when conducting many tests?",
        "options": [
            "a. FDR controls the probability of at least one false rejection across all comparisons.",
            "b. FDR controls the expected proportion of false rejections to the total number of rejections, making it less conservative and more powerful than FWER.",
            "c. FDR completely eliminates Type I errors.",
            "d. FDR requires fewer tests to achieve significance."
        ],
        "answer": "b"
    },
    {
        "question": "What is the primary disadvantage of the Bonferroni correction for multiple comparisons?",
        "options": [
            "a. It is only applicable to pairwise comparisons.",
            "b. It assumes all tests are dependent, reducing power.",
            "c. It is overly conservative, especially when the number of comparisons is large.",
            "d. It does not control the Familywise Error Rate."
        ],
        "answer": "c"
    },
    {
        "question": "When conducting complex linear contrasts, what condition must the weights (a_j) satisfy?",
        "options": [
            "a. All weights must be positive.",
            "b. The sum of weights must equal zero.",
            "c. The sum of squared weights must equal the sample size.",
            "d. Weights must represent equal group sizes."
        ],
        "answer": "b"
    },
    {
        "question": "In dummy variable coding, what does the coefficient (b1) for a dummy variable represent?",
        "options": [
            "a. The difference between the grand mean and the reference category mean.",
            "b. The difference between the reference group mean and the target group mean.",
            "c. The predicted value for the reference category.",
            "d. The slope of the categorical predictor."
        ],
        "answer": "b"
    },
    {
        "question": "Which coding scheme represents the difference between each group mean and the grand mean in a categorical predictor with more than two levels?",
        "options": [
            "a. Dummy coding.",
            "b. Effect coding.",
            "c. Contrast coding.",
            "d. Weighted coding."
        ],
        "answer": "b"
    },
    {
        "question": "Which missingness mechanism assumes that missingness depends only on observed data and not on the missing data itself?",
        "options": [
            "a. MCAR.",
            "b. MAR.",
            "c. MNAR.",
            "d. Missing Independent."
        ],
        "answer": "b"
    },
    {
        "question": "What is the main disadvantage of mean imputation?",
        "options": [
            "a. It requires advanced algorithms.",
            "b. It reduces variability and inflates correlations.",
            "c. It works only for categorical data.",
            "d. It cannot handle small datasets."
        ],
        "answer": "b"
    },
    {
        "question": "What is a contrast in the context of factorial designs?",
        "options": [
            "a. A type of interaction effect.",
            "b. A focused comparison between specific levels of a factor or interaction in the model.",
            "c. A measure of total variance in the model.",
            "d. A method to assess the grand mean of all groups."
        ],
        "answer": "b"
    },
    {
        "question": "How many orthogonal contrasts can be conducted for a factor with four levels?",
        "options": [
            "a. 3.",
            "b. 4.",
            "c. 6.",
            "d. 2."
        ],
        "answer": "a"
    },
    {
        "question": "What is the purpose of using interaction contrasts in a two-way factorial design?",
        "options": [
            "a. To evaluate the main effects of each independent variable.",
            "b. To compare specific interaction effects across the levels of a second factor.",
            "c. To calculate the total variance explained by the model.",
            "d. To explore the assumptions of normality and homogeneity."
        ],
        "answer": "b"
    },
       {
        "question": "Which of the following best describes simple effects analysis?",
        "options": [
            "a. Testing the effect of one factor at all levels of a second factor",
            "b. Testing the overall interaction effect of two factors",
            "c. Testing pairwise comparisons between all levels of a single factor",
            "d. Testing for homogeneity of variance between groups"
        ],
        "answer": "a"
    },
    {
        "question": "How is an interaction contrast different from a simple effect?",
        "options": [
            "a. Interaction contrasts compare effects across levels of two factors, while simple effects analyze one factor within each level of another.",
            "b. Interaction contrasts focus only on main effects, while simple effects focus on interactions.",
            "c. Interaction contrasts analyze residuals, while simple effects analyze raw scores.",
            "d. Interaction contrasts are used in one-way designs, while simple effects are used in factorial designs."
        ],
        "answer": "a"
    },
    {
        "question": "What is the significance of the weights used in defining a contrast?",
        "options": [
            "a. Weights ensure the sum of all group means equals zero.",
            "b. Weights define the specific comparison or pattern of interest in the levels of the factor.",
            "c. Weights standardize the values across all levels of the factor.",
            "d. Weights are used to calculate the mean of the grand average."
        ],
        "answer": "b"
    },
    {
        "question": "Why are related samples designs typically more powerful than independent samples designs?",
        "options": [
            "a. They have larger sample sizes.",
            "b. They include fewer variables.",
            "c. They remove variability due to individual differences between subjects.",
            "d. They use a more complex statistical model."
        ],
        "answer": "c"
    },
    {
        "question": "What does a paired samples t-test compare?",
        "options": [
            "a. The variances of two independent samples.",
            "b. The means of two related samples, such as before-and-after measurements.",
            "c. The interaction between two categorical variables.",
            "d. The means of more than two independent samples."
        ],
        "answer": "b"
    },
    {
        "question": "In a repeated measures ANOVA, what is the primary assumption that must be met for valid results?",
        "options": [
            "a. Homogeneity of variance.",
            "b. Sphericity or compound symmetry of the data.",
            "c. Independence of the errors.",
            "d. Equal sample sizes across groups."
        ],
        "answer": "b"
    },
    {
        "question": "Which test is most commonly used to evaluate violations of the sphericity assumption?",
        "options": [
            "a. Greenhouse-Geisser test.",
            "b. Mauchly’s test of sphericity.",
            "c. Levene’s test for homogeneity.",
            "d. Bartlett’s test for equal variances."
        ],
        "answer": "b"
    },
    {
        "question": "How does the Greenhouse-Geisser correction handle violations of sphericity in repeated measures ANOVA?",
        "options": [
            "a. By increasing the numerator of the F-statistic.",
            "b. By reducing the degrees of freedom for the F-test, making it more conservative.",
            "c. By pooling the variances of all conditions.",
            "d. By creating new interaction terms in the model."
        ],
        "answer": "b"
    },
    {
        "question": "In mixed models, why is sphericity not required as an assumption?",
        "options": [
            "a. Mixed models automatically satisfy the sphericity assumption.",
            "b. Mixed models allow for unequal variances and covariances between treatment levels.",
            "c. Mixed models replace sphericity with compound symmetry.",
            "d. Mixed models use least squares estimation, which does not require sphericity."
        ],
        "answer": "b"
    },
    {
        "question": "A researcher uses a mixed model to analyze repeated measures data with time treated as continuous. How does this differ from a traditional repeated measures ANOVA?",
        "options": [
            "a. Time is treated categorically in both analyses.",
            "b. Mixed models cannot handle continuous predictors.",
            "c. Mixed models can estimate effects at intermediate time points not explicitly measured.",
            "d. Traditional ANOVA requires fewer assumptions about the data."
        ],
        "answer": "c"
    },
    {
        "question": "In a study comparing math test scores between high school students (mean = 75, standard deviation = 10) and college students (mean = 80), the test statistic is z = 1.5 with p = 0.13. What can be concluded?",
        "options": [
            "a. The result is statistically significant; high school students differ from college students in math scores.",
            "b. The result is not statistically significant; high school students do not differ significantly from college students in math scores.",
            "c. The result is practically significant because z > 1.",
            "d. The result is inconclusive because p-values cannot determine significance."
        ],
        "answer": "b"
    },
    {
        "question": "How can violations of sphericity affect the interpretation of effect sizes in repeated measures ANOVA?",
        "options": [
            "a. Violations have no effect on the reported effect sizes.",
            "b. Violations cause effect sizes to overestimate the true relationship strength.",
            "c. Violations reduce the precision of effect size estimates and may distort their interpretation.",
            "d. Violations invalidate the use of confidence intervals for effect sizes."
        ],
        "answer": "c"
    },
    {
        "question": "What happens to the Type I error rate when the larger sample size is paired with the smaller variance in a two-sample t-test?",
        "options": [
            "a. It remains unchanged.",
            "b. It decreases, making the test conservative.",
            "c. It increases, making the test liberal.",
            "d. It depends entirely on the pooled variance."
        ],
        "answer": "c"
    },
    {
        "question": "Dr. Stein conducts a two-sample t-test to compare motivation scores in two classes and obtains t = 2.23 with degrees of freedom (df) = 18. The critical t-value for a significance level of 0.10 is t = 1.734. Which conclusion is correct?",
        "options": [
            "a. Reject the null hypothesis; motivation scores differ significantly between the two classes.",
            "b. Fail to reject the null hypothesis; motivation scores do not differ significantly between the two classes.",
            "c. Reject the null hypothesis; the variance homogeneity assumption was violated.",
            "d. Fail to reject the null hypothesis; the sample sizes are too small to detect significance."
        ],
        "answer": "a"
    },
    {
        "question": "In a perceived difficulty example, the easy test group had 20 subjects, and the hard test group had 18 subjects. After trimming 20% from each tail, how many observations remain in each group?",
        "options": [
            "a. 12 in the easy group and 12 in the hard group.",
            "b. 16 in the easy group and 15 in the hard group.",
            "c. 16 in the easy group and 14 in the hard group.",
            "d. 12 in the easy group and 12 in the hard group."
        ],
        "answer": "d"
    },
    {
        "question": "Why does bootstrapping provide a solution when both normality and variance homogeneity assumptions are violated?",
        "options": [
            "a. It estimates the sampling distribution directly from the theoretical population distribution.",
            "b. It generates a sampling distribution based on the actual sample, avoiding strict parametric assumptions.",
            "c. It ensures that the sample distribution becomes perfectly symmetric.",
            "d. It replaces the need for effect size measures by focusing solely on mean differences."
        ],
        "answer": "b"
    },
    {
        "question": "In a study with three groups, the total sum of squares (SStotal) is 147.33, and the between-group sum of squares (SSbetween) is 63.33. What is the eta-squared (η²) effect size, and how should it be interpreted?",
        "options": [
            "a. 0.43; 43% of the variability in the dependent variable is explained by the independent variable.",
            "b. 0.32; 32% of the variability in the dependent variable is explained by the independent variable.",
            "c. 0.43; 43% of the differences between groups are due to chance.",
            "d. 0.32; 32% of the differences between groups are due to chance."
        ],
        "answer": "a"
    },
    {
        "question": "Why might omega-squared (ω²) be preferred over eta-squared (η²) for reporting effect size in ANOVA?",
        "options": [
            "a. It adjusts for unequal variances between groups.",
            "b. It accounts for sampling error and provides a less biased estimate.",
            "c. It provides confidence intervals for the effect size.",
            "d. It simplifies the interpretation of group mean differences."
        ],
        "answer": "b"
    },
    {
        "question": "If H (Kruskal-Wallis statistic) is 8.96 and the critical χ² value at α = 0.05 and df = 3 is 7.81, what is the appropriate conclusion?",
        "options": [
            "a. Fail to reject the null hypothesis; the distributions are identical.",
            "b. Reject the null hypothesis; at least one distribution differs.",
            "c. Fail to reject the null hypothesis; the variances are equal.",
            "d. Reject the null hypothesis; the sample means are significantly different."
        ],
        "answer": "b"
    },
    {
        "question": "Which test or method would be most suitable when comparing groups with nonnormal distributions and unequal variances?",
        "options": [
            "a. Traditional ANOVA F test.",
            "b. Kruskal-Wallis test on ranks.",
            "c. Welch test on trimmed means or ranks.",
            "d. Bootstrapped resampling of the means."
        ],
        "answer": "c"
    },
    {
        "question": "In the Holm procedure, what happens when a p-value exceeds its calculated threshold (αc)?",
        "options": [
            "a. Testing continues for all remaining p-values.",
            "b. All remaining null hypotheses are declared significant.",
            "c. All remaining null hypotheses are declared nonsignificant.",
            "d. The significance level is recalculated for the remaining tests."
        ],
        "answer": "c"
    },
    {
        "question": "When conducting a large number of post hoc tests, which procedure ensures that the Familywise Error Rate is maintained at α regardless of the number of contrasts conducted?",
        "options": [
            "a. Tukey's method.",
            "b. Holm procedure.",
            "c. Scheffé procedure.",
            "d. Benjamini-Hochberg procedure."
        ],
        "answer": "c"
    },
    {
        "question": "Why is rejecting the null hypothesis in an omnibus test not sufficient to identify specific group differences?",
        "options": [
            "a. Omnibus tests only evaluate variance, not means.",
            "b. Omnibus tests do not account for within-group variability.",
            "c. Omnibus tests do not indicate which specific group means differ.",
            "d. Omnibus tests assume all group means are equal."
        ],
        "answer": "c"
    },
    {
        "question": "In Dr. Smith's example, the mean perfectionism score for psychology students is 21.13 (SD = 4.13, n = 16), and for sociology students is 19.08 (SD = 4.10, n = 12). The error mean square (MS) is 16.12. Calculate the t-statistic for testing the null hypothesis that the mean perfectionism score for psychology students equals the mean score for sociology students.",
        "options": [
            "a. 0.85.",
            "b. 1.33.",
            "c. 2.01.",
            "d. 2.50."
        ],
        "answer": "b"
    },
    {
        "question": "A researcher uses dummy coding for a categorical predictor with 4 groups: CBT, CBTM, CBTP, and Control. Which group should be coded as 0 for all dummy variables to make it the reference category?",
        "options": [
            "a. CBT.",
            "b. CBTM.",
            "c. CBTP.",
            "d. Control."
        ],
        "answer": "d"
    },
    {
        "question": "What is the primary advantage of using regression with categorical predictors compared to a one-way ANOVA?",
        "options": [
            "a. Regression allows for robust analyses to be conducted more easily.",
            "b. Regression automatically assumes variance homogeneity.",
            "c. Regression allows for the inclusion of continuous and categorical predictors in the same model.",
            "d. Regression eliminates the need for dummy coding or effect coding."
        ],
        "answer": "c"
    },
    {
        "question": "In Multiple Imputation, how are standard errors calculated?",
        "options": [
            "a. By averaging the standard errors from the M datasets only.",
            "b. By combining the average standard errors and the standard deviations of the parameter estimates across datasets.",
            "c. By using regression imputation values only.",
            "d. By calculating the variance within each imputed dataset and summing them."
        ],
        "answer": "b"
    },
    {
        "question": "Why is Full Information Maximum Likelihood (FIML) considered unbiased for MCAR/MAR data?",
        "options": [
            "a. It deletes incomplete cases systematically.",
            "b. It imputes values with no additional variability.",
            "c. It uses all observed data to calculate the likelihood without imputation or deletion.",
            "d. It assumes MNAR data to be ignorable."
        ],
        "answer": "c"
    },
     {
        "question": "What does η² represent in the context of factorial ANOVA?",
        "options": [
            "a. The variance within each cell of the design",
            "b. The proportion of variance in the dependent variable explained by a particular effect",
            "c. The total error variance in the model",
            "d. The interaction effect size only"
        ],
        "answer": "b"
    },
    {
        "question": "When analyzing a three-way factorial design, what should you do if the three-way interaction is meaningful?",
        "options": [
            "a. Explore all main effects first",
            "b. Ignore the interaction and focus on two-way interactions",
            "c. Graph and analyze the three-way interaction and then proceed to analyze lower-order effects as appropriate",
            "d. Focus only on the main effects of the independent variables"
        ],
        "answer": "c"
    },
    {
        "question": "A researcher compares the effects of three treatments on reaction time using a repeated measures design. The variance-covariance matrix shows unequal variances for the differences between treatments. Which correction would be most appropriate for the degrees of freedom in this case?",
        "options": [
            "a. Use the Huynh-Feldt correction for conservative estimates.",
            "b. Use the Greenhouse-Geisser correction to adjust for violations of sphericity.",
            "c. Use the Mauchly’s test to confirm equality of variances.",
            "d. Use a multivariate analysis to bypass the assumption of sphericity."
        ],
        "answer": "b"
    },
    {
        "question": "In a paired t-test, how does the standard error of the mean difference differ from the standard error in an independent samples t-test, and why?",
        "options": [
            "a. It is larger because it accounts for the paired nature of the data.",
            "b. It is smaller because it removes between-subject variability, increasing power.",
            "c. It is the same as in an independent samples t-test because the calculation uses pooled variance.",
            "d. It is smaller because it only uses the variances of the two conditions being compared."
        ],
        "answer": "b"
    },
    {
        "question": "In a mixed model analysis, the residual covariance structure is specified as autoregressive (AR). What does this imply about the relationships between repeated measures?",
        "options": [
            "a. All variances are assumed equal, and covariances are equal.",
            "b. Correlations are expected to be stronger for time points closer together than for those farther apart.",
            "c. Each level of the repeated measure is treated as independent.",
            "d. Variances and covariances are allowed to vary freely across levels."
        ],
        "answer": "b"
    },
    {
        "question": "A researcher fits a mixed model to longitudinal data and reports the covariance between the individual intercept and slope (random effects) is significant. What does this indicate?",
        "options": [
            "a. The residuals at level 1 violate the assumption of normality.",
            "b. The intercept and slope at level 2 are dependent on each other.",
            "c. There is heteroscedasticity in the level 1 residuals.",
            "d. The fixed effects for the intercept and slope are invalid."
        ],
        "answer": "b"
    }
    
]

# Initialize session state to handle persistent randomization
if "selected_questions" not in st.session_state:
    st.session_state.selected_questions = random.sample(question_bank, 20)

# Randomize questions button
if st.button("Randomize Questions"):
    st.session_state.selected_questions = random.sample(question_bank, 20)

# CSS styling
st.markdown("""
    <style>
    .title {
        font-size: 36px;
        color: #4CAF50;
        text-align: center;
    }
    .question {
        font-size: 18px;
        margin-bottom: 10px;
    }
    .options {
        margin-left: 20px;
    }
    .feedback {
        font-size: 16px;
        margin-top: 5px;
        font-weight: bold;
    }
    .correct {
        color: green;
    }
    .incorrect {
        color: red;
    }
    .submit-button {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px 20px;
        font-size: 16px;
        cursor: pointer;
    }
    .submit-button:hover {
        background-color: #45a049;
    }
    .score {
        font-size: 24px;
        color: #333;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# App title
st.markdown("<div class='title'>MCQ Practice App</div>", unsafe_allow_html=True)

# Help section
with st.expander("Help Section"):
    st.write("""
    - There are 100 questions in the question bank.
    - Each session randomly samples 20 questions for practice.
    - Questions may repeat across sessions to help reinforce learning.
    - Use the "Randomize Questions" button to generate a new set of questions before starting.
    """)

# Display questions
user_answers = []
for i, question in enumerate(st.session_state.selected_questions):
    st.markdown(f"<div class='question'>{i + 1}. {question['question']}</div>", unsafe_allow_html=True)
    selected = st.radio(
        label="",
        options=["Select an option"] + question['options'],
        index=0,  # Default selection is the placeholder
        key=f"question_{i}"
    )
    user_answers.append(selected)

# Submit button
if st.button("Submit"):
    score = 0
    st.write("### Results")
    for i, question in enumerate(st.session_state.selected_questions):
        # Extract the first letter of the selected answer
        selected_letter = user_answers[i].split(".")[0] if user_answers[i] != "Select an option" else None

        # Check if the answer is correct
        if selected_letter == question['answer']:
            score += 1
            feedback = f"<div class='feedback correct'>Correct! ✅</div>"
        else:
            correct_option = next(opt for opt in question['options'] if opt.startswith(question['answer'] + "."))
            feedback = f"<div class='feedback incorrect'>Incorrect! ❌ The correct answer is: {correct_option}</div>"
        
        # Display question feedback
        st.markdown(f"<div class='question'>{i + 1}. {question['question']}</div>", unsafe_allow_html=True)
        st.markdown(f"Your answer: {user_answers[i]}", unsafe_allow_html=True)
        st.markdown(feedback, unsafe_allow_html=True)

    # Display total score
    st.markdown(f"<div class='score'>Your total score is: {score} / {len(st.session_state.selected_questions)}</div>", unsafe_allow_html=True)


# cd "/Users/arjunghumman/Downloads/VS Code Stuff/Python/Quiz"
# streamlit run quiz_univ.py