import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def generate_random_data() -> tuple[np.ndarray, pd.DataFrame]:
    """
   ما یک ماتریس 10*12 ایجاد می کنیم
   همچنین مجموعه داده ای 50 نقطه تصادفی در مجموعه دوبعدی تولید می کنیم
    Returns:
        tuple: A tuple containing a 10x12 NumPy array and a Pandas DataFrame.
    """
    np.random.seed(42)
    random_matrix = np.random.rand(10, 12)
    random_data = pd.DataFrame({'x': np.random.rand(50), 'y': 2 * np.random.rand(50) + 1 + 0.1 * np.random.randn(50)})
    return random_matrix, random_data

def plot_random_data(random_matrix: np.ndarray, random_data: pd.DataFrame) -> None:
    """
    Create a heatmap of the random matrix and a scatter plot of the random points.

    Args:
        random_matrix: A 10x12 NumPy array of random values.
        random_data: A Pandas DataFrame of 50 random points in 2D space.
    """
    fig, axs = plt.subplots(1, 2, figsize=(16, 6))

    sns.heatmap(random_matrix, annot=True, cmap='coolwarm', square=True, ax=axs[0])
    axs[0].set_title('Heatmap of Random Data')

    axs[1].scatter(random_data['x'], random_data['y'], label='Data Points')
    axs[1].set_xlabel('X')
    axs[1].set_ylabel('Y')
    axs[1].set_title('Scatter Plot of Random Data')

    slope, intercept = np.polyfit(random_data['x'], random_data['y'], deg=1)
    axs[1].plot(random_data['x'], slope * random_data['x'] + intercept, color='red', label='Regression Line')

    axs[1].legend()
    # Question 1: What is the purpose of the `np.random.seed()` function?
    np.random.seed(42)

# Generate a 10x12 NumPy array of random values
    random_matrix = np.random.rand(10, 12)

# Question 2: What is the difference between `np.random.rand()` and `np.random.randn()`?
    random_data = pd.DataFrame({'x': np.random.rand(50), 'y': 2 * np.random.rand(50) + 1 + 0.1 * np.random.randn(50)})

# Question 3: What is the purpose of the `sns.heatmap()` function?
    sns.heatmap(random_matrix, annot=True, cmap='coolwarm', square=True)

# Question 4: What is the purpose of the `axs[1].scatter()` function?
    axs[1].scatter(random_data['x'], random_data['y'], label='Data Points')

# Question 5: What is the purpose of the `np.polyfit()` function?
    slope, intercept = np.polyfit(random_data['x'], random_data['y'], deg=1)

# Question 6: What is the purpose of the `axs[1].plot()` function?
    axs[1].plot(random_data['x'], slope * random_data['x'] + intercept, color='red', label='Regression Line')

# Question 7: What is the purpose of the `np.mean()`, `np.std()`, and `np.corrcoef()` functions?
    mean_x = np.mean(random_data['x'])
    mean_y = np.mean(random_data['y'])
    std_x = np.std(random_data['x'])
    std_y = np.std(random_data['y'])
    corr_coef = np.corrcoef(random_data['x'], random_data['y'])[0, 1]

# Question 8: What is the purpose of the `print()` function?
    print(f'Mean of X: {mean_x:.2f}')
    print(f'Mean of Y: {mean_y:.2f}')
    print(f'Standard Deviation of X: {std_x:.2f}')
    print(f'Standard Deviation of Y: {std_y:.2f}')
    print(f'Correlation Coefficient: {corr_coef:.2f}')

    plt.show()

def calculate_statistics(random_data: pd.DataFrame) -> tuple:
    """
    Calculate and return some statistics about the random points.

    Args:
        random_data: A Pandas DataFrame of 50 random points in 2D space.

    Returns:
        tuple: A tuple containing the mean, standard deviation, and correlation coefficient of the random points.
    """
    mean_x = np.mean(random_data['x'])
    mean_y = np.mean(random_data['y'])
    std_x = np.std(random_data['x'])
    std_y = np.std(random_data['y'])
    corr_coef = np.corrcoef(random_data['x'], random_data['y'])[0, 1]

    return mean_x, mean_y, std_x, std_y, corr_coef

def main() -> None:
    try:
        random_matrix, random_data = generate_random_data()
        plot_random_data(random_matrix, random_data)
        mean_x, mean_y, std_x, std_y, corr_coef = calculate_statistics(random_data)

        print(f'Mean of X: {mean_x:.2f}')
        print(f'Mean of Y: {mean_y:.2f}')
        print(f'Standard Deviation of X: {std_x:.2f}')
        print(f'Standard Deviation of Y: {std_y:.2f}')
        print(f'Correlation Coefficient: {corr_coef:.2f}')
    except Exception as e:
        print(f'An error occurred: {e}')

if __name__ == "__main__":
    main()
#این کد داده های تصادفی تولید می کند
#آمارهای مربوط به داده ها را تولید می کند
#همچنین الگوی داده ای را آموزش می دهد
# آن ها را رسم می کند