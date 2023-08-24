import pandas as pd

cryteria = {
    "Doświadczenie (w latach)": ["0", "1-2", "3-4", "5+"],
    "Ocena": [20, 60, 80, 100]
}


class Cryteria:
    def __init__(self, cryteria: dict):
        self.cryteria = cryteria
        self.table_cryteria = pd.DataFrame(cryteria).to_string(index=False)

    def change_values(self, column, value_index, new_value):
            self.eval_cryteria[column][value_index] = new_value
            self.df = pd.DataFrame(self.eval_cryteria)
