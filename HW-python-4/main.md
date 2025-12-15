---
title: "R Tutorial Homework: Gene Expression Analysis"
author: "Your Name Here"
date: "`r Sys.Date()`"
output: 
  html_document:
    toc: true
    toc_float: true
    theme: cosmo
---

# Welcome! 👋

This is your guided homework tutorial. Work through each section step-by-step. 
Run the example code, then complete the exercises marked with **YOUR TURN**.

**Estimated time:** 2-3 hours (take breaks!)  
**Total points:** 10

---

# Setup

First, let's set up your workspace:
```{r setup}
# Set your working directory (change this to your folder path!)
# setwd("C:/Users/YourName/R_Homework")  # Windows
# setwd("/Users/YourName/R_Homework")    # Mac/Linux

# Clear the environment (optional - starts fresh)
rm(list = ls())

# Print message to confirm setup
cat("Setup complete! Let's begin! 🎉\n")
```

---

# Part 1: Creating Data (3 points)

## Step 1.1: Understanding Data Frames (1 point)

### 📚 LEARN: What is a Data Frame?

A data frame is like an Excel table - it has rows and columns. Each column can 
have a different type of data (numbers, text, TRUE/FALSE).

### 🔍 EXAMPLE: Let's create a simple data frame
```{r example_dataframe}
# Create a small example
simple_data <- data.frame(
  name = c("Alice", "Bob", "Carol"),
  age = c(25, 30, 28),
  scientist = c(TRUE, FALSE, TRUE)
)

# Look at it
print(simple_data)

# Check the structure
str(simple_data)
```

**What you see:**
- `name` column has text (character)
- `age` column has numbers (numeric)  
- `scientist` column has TRUE/FALSE (logical)

---

### ✏️ YOUR TURN: Create the Gene Expression Dataset

Now create a larger data frame with gene expression data. 

**Copy this code and run it:**
```{r create_gene_data}
# Create gene expression data frame
gene_data <- data.frame(
  gene_id = c("Gene_A", "Gene_B", "Gene_C", "Gene_D", "Gene_E", 
              "Gene_F", "Gene_G", "Gene_H", "Gene_I", "Gene_J"),
  control_1 = c(5.2, 3.8, 7.1, 4.5, 6.3, 2.9, 8.7, 5.9, 4.2, 6.8),
  control_2 = c(5.5, 3.6, 7.3, 4.7, 6.1, 3.1, 8.5, 6.2, 4.0, 6.5),
  control_3 = c(5.0, 4.0, 7.0, 4.3, 6.5, 2.8, 8.9, 5.7, 4.4, 7.0),
  treatment_1 = c(8.1, 3.9, 3.2, 4.6, 9.8, 2.7, 8.6, 11.2, 4.3, 6.9),
  treatment_2 = c(8.3, 3.7, 3.0, 4.8, 10.1, 3.0, 8.4, 11.5, 4.1, 6.7),
  treatment_3 = c(7.9, 4.1, 3.4, 4.4, 9.5, 2.9, 8.8, 10.9, 4.5, 7.1)
)

# View your data
print(gene_data)
```

**✅ Checkpoint:** You should see a table with 10 genes and 7 columns (1 for gene_id + 6 for samples)

---

## Step 1.2: Exploring Your Data (1 point)

### 📚 LEARN: How to Explore Data

Before analyzing, always explore your data to understand it!

### 🔍 EXAMPLE: Useful exploration functions
```{r example_explore}
# Try these commands with our simple_data
cat("Number of rows:", nrow(simple_data), "\n")
cat("Number of columns:", ncol(simple_data), "\n")
cat("Column names:", names(simple_data), "\n")
```

---

### ✏️ YOUR TURN: Explore the gene_data

**Task:** Answer these questions using R code:
```{r explore_gene_data}
# 1. How many rows (genes) are in the data?
cat("Number of genes:", nrow(gene_data), "\n")

# 2. How many columns are in the data?
cat("Number of columns:", ncol(gene_data), "\n")

# 3. What are the column names?
cat("Column names:", names(gene_data), "\n")

# 4. Show the first 3 rows
head(gene_data, 3)

# 5. Show the structure
str(gene_data)

# 6. Get a summary
summary(gene_data)
```

**✅ Checkpoint:** 
- Should have 10 rows (genes)
- Should have 7 columns (1 gene_id + 6 expression values)
- All expression columns should be numeric

---

## Step 1.3: Saving and Loading Data (1 point)

### 📚 LEARN: Working with CSV Files

CSV = Comma Separated Values. It's a universal format that Excel and R can both read!

### 🔍 EXAMPLE: Save and reload
```{r save_load_data}
# Save the data frame as CSV
write.csv(gene_data, "my_gene_expression.csv", row.names = FALSE)
cat("✅ File saved as 'my_gene_expression.csv'\n")

# Load it back to verify
loaded_data <- read.csv("my_gene_expression.csv")
cat("✅ File loaded successfully!\n")

# Check if it matches original
cat("Are they identical?", identical(gene_data, loaded_data), "\n")

# Show first few rows
head(loaded_data, 3)
```

**✅ Checkpoint:** 
- Check your folder - you should see "my_gene_expression.csv"
- `identical()` should return TRUE
- The loaded data should look the same as original

---

# Part 2: Calculating Statistics (3 points)

## Step 2.1: Mean Expression per Gene (1.5 points)

### 📚 LEARN: Calculating Row Means

We want to know the average expression for each gene across all 6 samples.

### 🔍 EXAMPLE: How rowMeans() works
```{r example_rowmeans}
# Small example
example_data <- data.frame(
  id = c("A", "B", "C"),
  value1 = c(10, 20, 30),
  value2 = c(15, 25, 35),
  value3 = c(12, 22, 32)
)

print(example_data)

# Calculate mean of value1, value2, value3 for each row
example_data$average <- rowMeans(example_data[, 2:4])
print(example_data)

# For row A: (10 + 15 + 12) / 3 = 12.33
```

---

### ✏️ YOUR TURN: Calculate mean expression

The expression values are in columns 2 through 7 (control_1 through treatment_3).
```{r calculate_mean_expression}
# Calculate mean expression across all 6 samples
gene_data$mean_expression <- rowMeans(gene_data[, 2:7])

# Show gene IDs with their mean expression
result <- gene_data[, c("gene_id", "mean_expression")]
print(result)

# Round to 2 decimal places for easier reading
result$mean_expression <- round(result$mean_expression, 2)
print(result)
```

**✅ Checkpoint:** 
- New column `mean_expression` should be added
- Each gene should have one mean value
- Values should be between 2 and 10 (approximately)

---

## Step 2.2: Control vs Treatment Means (1.5 points)

### 📚 LEARN: Comparing Groups

In experiments, we compare control (untreated) vs treatment (treated) samples.
Let's calculate separate means for each group.

### 🔍 EXAMPLE: Selecting specific columns
```{r example_column_selection}
# Using our example_data
# Select columns 2 and 3 only
subset_cols <- example_data[, 2:3]
print(subset_cols)

# Calculate mean of just those columns
rowMeans(subset_cols)
```

---

### ✏️ YOUR TURN: Calculate group means

**Remember:**
- Control samples: columns 2, 3, 4 (control_1, control_2, control_3)
- Treatment samples: columns 5, 6, 7 (treatment_1, treatment_2, treatment_3)
```{r calculate_group_means}
# Calculate mean for control samples (columns 2-4)
gene_data$control_mean <- rowMeans(gene_data[, 2:4])

# Calculate mean for treatment samples (columns 5-7)
gene_data$treatment_mean <- rowMeans(gene_data[, 5:7])

# Show all means together
comparison <- gene_data[, c("gene_id", "control_mean", "treatment_mean", "mean_expression")]
comparison <- round(comparison[, -1], 2)  # Round numbers, keep gene_id
comparison <- cbind(gene_data$gene_id, comparison)
names(comparison)[1] <- "gene_id"
print(comparison)
```

**✅ Checkpoint:** 
- Two new columns added: `control_mean` and `treatment_mean`
- Look at Gene_A: treatment mean should be much higher than control mean
- Look at Gene_C: control mean should be higher than treatment mean

---

# Part 3: Finding Interesting Genes (2 points)

## Step 3.1: Calculate Fold Change (1 point)

### 📚 LEARN: What is Fold Change?

**Fold Change (FC)** tells us how much expression changed between groups:
- FC = 2.0 means expression **doubled** in treatment
- FC = 0.5 means expression **halved** in treatment  
- FC = 1.0 means **no change**

Formula: `FC = treatment_mean / control_mean`

### 🔍 EXAMPLE: Understanding fold change
```{r example_fold_change}
# If a gene has:
control <- 5.0
treatment <- 10.0

# Fold change is:
fold_change <- treatment / control
cat("Fold change:", fold_change, "\n")
cat("Interpretation: Expression is", fold_change, "times higher in treatment\n")

# Another example:
control2 <- 8.0
treatment2 <- 4.0
fc2 <- treatment2 / control2
cat("\nFold change:", fc2, "\n")
cat("Interpretation: Expression is", fc2, "times (half) in treatment\n")
```

---

### ✏️ YOUR TURN: Calculate fold change for all genes
```{r calculate_fold_change}
# Calculate fold change
gene_data$fold_change <- gene_data$treatment_mean / gene_data$control_mean

# Round for easier reading
gene_data$fold_change <- round(gene_data$fold_change, 2)

# Show results
fc_results <- gene_data[, c("gene_id", "control_mean", "treatment_mean", "fold_change")]
fc_results[, 2:4] <- round(fc_results[, 2:4], 2)
print(fc_results)
```

**✅ Checkpoint:** 
- Gene_A should have FC around 1.5-1.6 (increased)
- Gene_C should have FC around 0.4-0.5 (decreased)
- Gene_B should have FC around 1.0 (no change)

---

## Step 3.2: Identify Upregulated Genes (1 point)

### 📚 LEARN: Filtering Data

We want to find genes that increased significantly. Scientists often use FC > 1.5 
as a cutoff (meaning expression increased by at least 50%).

### 🔍 EXAMPLE: Filtering with logical conditions
```{r example_filtering}
# Create example data
test_data <- data.frame(
  name = c("A", "B", "C", "D", "E"),
  value = c(1.2, 1.8, 2.5, 0.8, 1.6)
)

print(test_data)

# Filter for values > 1.5
high_values <- test_data[test_data$value > 1.5, ]
print(high_values)

# Count how many
cat("Number of high values:", nrow(high_values), "\n")
```

---

### ✏️ YOUR TURN: Find upregulated genes
```{r find_upregulated}
# Filter for genes with fold change > 1.5
upregulated <- gene_data[gene_data$fold_change > 1.5, ]

# Show only relevant columns
upregulated_results <- upregulated[, c("gene_id", "control_mean", "treatment_mean", "fold_change")]
upregulated_results[, 2:4] <- round(upregulated_results[, 2:4], 2)
print(upregulated_results)

# Count how many genes are upregulated
n_upregulated <- nrow(upregulated)
cat("\n📊 Number of upregulated genes (FC > 1.5):", n_upregulated, "\n")

# BONUS: Also find downregulated genes (FC < 0.67, which is 1/1.5)
downregulated <- gene_data[gene_data$fold_change < 0.67, ]
downregulated_results <- downregulated[, c("gene_id", "fold_change")]
cat("\n📊 Downregulated genes (FC < 0.67):\n")
print(downregulated_results)
```

**✅ Checkpoint:** 
- Should find 3 upregulated genes (Gene_A, Gene_E, Gene_H)
- Should find 1 downregulated gene (Gene_C)

---

# Part 4: Visualization (2 points)

## Step 4.1: Barplot of Mean Expression (1 point)

### 📚 LEARN: Creating Barplots

Barplots show the value for each category. Perfect for comparing genes!

### 🔍 EXAMPLE: Simple barplot
```{r example_barplot, fig.width=6, fig.height=4}
# Simple example
fruits <- c(5, 8, 3, 6)
names(fruits) <- c("Apples", "Bananas", "Oranges", "Grapes")

barplot(fruits,
        main = "Fruit Count",
        col = "lightblue",
        ylab = "Number")
```

---

### ✏️ YOUR TURN: Create expression barplot
```{r barplot_expression, fig.width=10, fig.height=6}
# Create barplot of mean expression
barplot(gene_data$mean_expression,
        names.arg = gene_data$gene_id,
        main = "Mean Gene Expression Across All Samples",
        xlab = "Genes",
        ylab = "Mean Expression Level",
        col = "steelblue",
        las = 2,  # Rotate labels vertical
        ylim = c(0, max(gene_data$mean_expression) * 1.1))  # Add space at top

# Add a horizontal line at mean of all values
abline(h = mean(gene_data$mean_expression), col = "red", lty = 2, lwd = 2)
legend("topright", legend = "Overall Mean", col = "red", lty = 2, lwd = 2)
```

**✅ Checkpoint:** 
- All 10 genes should be shown
- Gene_H should have highest bar
- Gene_F should have lowest bar
- Red dashed line shows the overall average

---

## Step 4.2: Control vs Treatment Comparison (1 point)

### 📚 LEARN: Scatter Plots

Scatter plots compare two variables. Each point = one gene.

### 🔍 EXAMPLE: What the diagonal line means
```{r example_scatter, fig.width=5, fig.height=5}
# Example showing the concept
control_ex <- c(2, 4, 6, 8)
treatment_ex <- c(2, 5, 3, 10)

plot(control_ex, treatment_ex,
     main = "Example: Understanding the Plot",
     xlab = "Control",
     ylab = "Treatment",
     pch = 19,
     cex = 2)

# Add diagonal line (y = x)
abline(0, 1, col = "red", lty = 2, lwd = 2)

# Add labels
text(control_ex, treatment_ex, labels = c("No change", "Up", "Down", "Up"), pos = 4)
```

**Understanding the plot:**
- **On the red line**: No change (treatment = control)
- **Above the red line**: Upregulated (treatment > control)
- **Below the red line**: Downregulated (treatment < control)

---

### ✏️ YOUR TURN: Create comparison plot
```{r scatter_comparison, fig.width=8, fig.height=8}
# Create scatter plot
plot(gene_data$control_mean, 
     gene_data$treatment_mean,
     main = "Control vs Treatment Expression Levels",
     xlab = "Control Mean Expression",
     ylab = "Treatment Mean Expression",
     pch = 19,  # Solid circles
     cex = 1.5,  # Size
     col = "darkgreen")

# Add the diagonal reference line (y = x)
abline(0, 1, col = "red", lty = 2, lwd = 2)

# Add labels for interesting genes
# Label upregulated genes
up_genes <- gene_data[gene_data$fold_change > 1.5, ]
text(up_genes$control_mean, 
     up_genes$treatment_mean,
     labels = up_genes$gene_id,
     pos = 4,  # Position to the right
     col = "blue",
     cex = 0.8)

# Label downregulated genes
down_genes <- gene_data[gene_data$fold_change < 0.67, ]
text(down_genes$control_mean, 
     down_genes$treatment_mean,
     labels = down_genes$gene_id,
     pos = 2,  # Position to the left
     col = "red",
     cex = 0.8)

# Add legend
legend("topleft",
       legend = c("No change", "Upregulated", "Downregulated"),
       col = c("red", "blue", "red"),
       lty = c(2, NA, NA),
       pch = c(NA, 19, 19),
       cex = 0.8)
```

**✅ Checkpoint:** 
- Points above red line = increased in treatment
- Points below red line = decreased in treatment
- Gene_A, Gene_E, Gene_H should be labeled above the line
- Gene_C should be labeled below the line

---

# Summary Questions (Answer These!)

After completing all the analysis, answer these questions:

## Question 1: Which gene showed the highest fold change?

**YOUR ANSWER:** ___________
```{r answer_q1}
# Find the gene with maximum fold change
max_fc_gene <- gene_data[which.max(gene_data$fold_change), ]
cat("Gene with highest fold change:", max_fc_gene$gene_id, 
    "with FC =", max_fc_gene$fold_change, "\n")
```

---

## Question 2: How many genes were significantly upregulated (FC > 1.5)?

**YOUR ANSWER:** ___________
```{r answer_q2}
cat("Number of upregulated genes:", sum(gene_data$fold_change > 1.5), "\n")
```

---

## Question 3: In the scatter plot, what does it mean if a point is ABOVE the red diagonal line?

**YOUR ANSWER (in your own words):** 

_________________________________________________________

_________________________________________________________

**Correct answer:** It means the gene's expression is higher in the treatment 
group than in the control group (upregulated).

---

## Question 4: What was the mean expression level across all genes and all samples?

**YOUR ANSWER:** ___________
```{r answer_q4}
overall_mean <- mean(gene_data$mean_expression)
cat("Overall mean expression:", round(overall_mean, 2), "\n")
```

---

# Final Checklist ✅

Before submitting, make sure you have:

- [ ] All code chunks run without errors
- [ ] Both plots display correctly
- [ ] CSV file saved in your folder
- [ ] Answered all 4 summary questions
- [ ] Your name is at the top of this document

---

# How to Submit

1. **Knit this document** to HTML:
   - Click "Knit" button at the top
   - This creates an HTML file with all your code and outputs

2. **Submit TWO files:**
   - `Tutorial_Homework.Rmd` (this file with your code)
   - `Tutorial_Homework.html` (the knitted output)

3. **File naming:** 
   - `YourLastName_FirstName_Homework.Rmd`
   - `YourLastName_FirstName_Homework.html`

---

# Grading (10 points total)

| Section | Points | What's Graded |
|---------|--------|---------------|
| Part 1.1: Created data | 1 | Data frame created correctly |
| Part 1.2: Explored data | 1 | All exploration commands work |
| Part 1.3: Saved/loaded | 1 | CSV saved and reloaded |
| Part 2.1: Mean expression | 1.5 | Calculated correctly |
| Part 2.2: Group means | 1.5 | Control & treatment means correct |
| Part 3.1: Fold change | 1 | Calculated correctly |
| Part 3.2: Upregulated genes | 1 | Filtered and identified |
| Part 4.1: Barplot | 1 | Clear, labeled plot |
| Part 4.2: Scatter plot | 1 | Comparison plot with line |
| **TOTAL** | **10** | |

**Bonus:** Well-organized, commented code (+0.5 points)

---

# You're Done! 🎉

Great job completing this tutorial! You've learned:

- ✅ Creating and exploring data frames
- ✅ Saving and loading data
- ✅ Calculating statistics (means, fold changes)
- ✅ Filtering data with conditions
- ✅ Creating visualizations
- ✅ Basic data analysis workflow

**These are fundamental R skills you'll use in every analysis!** 💪

---

# Need Help?

- **Error messages**: Copy the exact error into Google with "R error"
- **Office hours**: [Your times here]
- **Email**: [Your email]
- **R Help**: Type `?function_name` in console (e.g., `?mean`)

Remember: Everyone struggles with R at first. Be patient with yourself! 🌱