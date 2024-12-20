# Fuel Cell Performance Prediction Project

## Project Description
This project focuses on predicting the performance of fuel cells using machine learning models. The dataset used contains various features related to fuel cell performance and multiple target variables.The target variable selected for this project is `Target5`.

## Objectives
1. Load and preprocess the dataset.
2. Focus on `Target5` as the output variable.
3. Train and evaluate multiple machine learning models:
   - Linear Regression
   - Decision Tree Regressor
   - Random Forest Regressor
4. Evaluate models using Mean Squared Error (MSE) and R² Score.
5. Save evaluation results for analysis.

## Input
The input dataset is `Fuel_cell_performance_data-Full.csv`, containing:
- **Features (F1 to F15)**: Input variables for the models.
- **Target Variables (Target1 to Target5)**: Multiple output variables, with `Target5` selected for this project.

Example structure of the dataset:
| F1   | F2   | F3   | ... | Target1 | Target2 | Target3 | Target4 | Target5 |
|------|------|------|-----|---------|---------|---------|---------|---------|
| 52.9 | 1.33 | 49.1 | ... | 0.959   | 1.531   | 79.3    | 4.19    | 33.29   |

## Output
The output consists of:
1. A trained model for each algorithm.
2. Evaluation metrics for each model:
   - **Mean Squared Error (MSE)**
   - **R² Score**

### Model Evaluation Results
| Model              | Mean Squared Error (MSE) | R² Score |
|--------------------|--------------------------|----------|
| Linear Regression  | 622.36                  | 0.694    |
| Decision Tree      | 818.86                  | 0.598    |
| Random Forest      | 455.73                  | 0.776    |

The **Random Forest Regressor** achieved the best performance.

## Steps to Run the Project
1. Clone the repository:
   ```bash
   git clone https://github.com/bansal9855/Fuel-Cell-performance.git
   ```
2. Navigate to the project directory:
   ```bash
   cd FuelOptimization
   ```
3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Place the dataset `Fuel_cell_performance_data-Full.csv` in the project directory.
5. Run the script:
   ```bash
   python main.py
   ```
6. Results will be saved to `model_evaluation_results.csv`.

## File Structure
```
FuelOptimization/
├── Fuel_cell_performance_data-Full.csv   # Input dataset
├── main.py              # Main script for data processing and model evaluation
├── model_evaluation_results.csv         # Output file with evaluation results
├── README.md                            # Project documentation
├── requirements.txt                     # Python dependencies
```

## Key Learning Outcomes
- Data preprocessing and handling in Python using Pandas.
- Implementation of regression models using scikit-learn.
- Performance evaluation of machine learning models.

## Use Case
This project can be used as a demonstration of:
- Predictive modeling skills.
- Machine learning workflow understanding.
- Ability to preprocess and work with datasets effectively.

