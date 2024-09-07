import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder


class TrendAlg:
    def __init__(self):
        # This code will read the game_data sheet from the book1.xlsx file and store it in the data DataFrame..
        data = pd.read_excel('dataset/Book1.xlsx', sheet_name='game_data')

        # Get the data from columns below.
        self.x_data = data[['Column1.player_value']]
        self.y_data = data[['Column1.computer_value']]

    def model_creation(self):
        encoder = LabelEncoder()
        # This will replace the strings in your dataframes with numerical labels (e.g., "rock" might be encoded as 0, "paper" as 1, and "scissors" as 2)
        x_train, x_test, y_train, y_test = train_test_split(
            self.x_data, # ['Column1.player_value'],
            self.y_data, # ['Column1.computer_value'],
            test_size=0.2, random_state=42)

        # # Reshape the data to 2D arrays
        # x_train = x_train.reshape(-1, 1)
        # x_test = x_test.reshape(-1, 1)

        model = DecisionTreeClassifier()
        model.fit(x_train, y_train)

        y_pred = model.predict(x_test)
        accuracy = accuracy_score(y_test, y_pred)
        print("Accuracy:", accuracy)

    def runner(self):
        self.model_creation()

