import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

data = pd.read_csv('Fuel_cell_performance_data-Full.csv')

selected_target = 'Target5'
if selected_target not in data.columns:
    raise ValueError(f"{selected_target} not found in the dataset columns.")

targets = ['Target1', 'Target2', 'Target3', 'Target4', 'Target5']
data = data.drop(columns=[t for t in targets if t != selected_target])

X = data.drop(columns=[selected_target])
y = data[selected_target]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

models = {
    "Linear Regression": LinearRegression(),
    "Decision Tree": DecisionTreeRegressor(random_state=42),
    "Random Forest": RandomForestRegressor(random_state=42)
}

results = []
for model_name, model in models.items():
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    results.append({
        "Model": model_name,
        "Mean Squared Error": mse,
        "R2 Score": r2
    })

results_df = pd.DataFrame(results)
results_df.to_csv('model_evaluation_results.csv', index=False)

print("Model evaluation results saved to 'model_evaluation_results.csv'")
