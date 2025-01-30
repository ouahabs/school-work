import warnings 
warnings.filterwarnings(action='ignore')

from pathlib import Path
import sys
path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))
print(sys.path)

# Custom imports
from utils.preprocessing import preprocess, clean_noise

import numpy as np
import pandas as pd

from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score
import sklearn.metrics as metrics                                                 
from mlxtend.plotting import plot_confusion_matrix
from sklearn.metrics import confusion_matrix, f1_score
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score

from mealpy import FloatVar, StringVar, IntegerVar, BoolVar, MixedSetVar, SMA, Problem, TWO

class SvmOptimizedProblem(Problem):
    def __init__(self, bounds=None, minmax="max", data=None, **kwargs):
        self.data = data
        super().__init__(bounds, minmax, **kwargs)

    def obj_func(self, x):
        x_decoded = self.decode_solution(x)
        C_paras, kernel_paras = x_decoded["C_paras"], x_decoded["kernel_paras"]
        gamma = x_decoded["gamma_paras"]
        # probability = x_decoded["probability_paras"]

        pipe_with_params = Pipeline([
        ('vect', CountVectorizer()),
        ('tfidf', TfidfTransformer()),
        # ('clf', SVC(C=C_paras, kernel=kernel_paras, gamma=gamma, probability=probability, random_state=1))
        ('clf', SVC(C=C_paras, kernel=kernel_paras, gamma=gamma, random_state=1))
        ])

        # Fit the model
        print("[+] Running model... (This can take a while)")
        model = pipe_with_params.fit(self.data["X_train"], self.data["y_train"])
        # Make the predictions
        y_predict = model.predict(self.data["X_test"])
        # Measure the performance
        return metrics.accuracy_score(self.data["y_test"], y_predict)

real = pd.read_csv('/home/habs/tp_sma/LGO/dataset/DataSet_Misinfo_TRUE.csv')
fake = pd.read_csv('/home/habs/tp_sma/LGO/dataset/DataSet_Misinfo_FAKE.csv')

df = preprocess(real, fake)
print("[+] Cleaning the data...")
df['text'] = df['text'].apply(clean_noise)

X_train,X_test,y_train,y_test = train_test_split(df['text'], df['class'], test_size=0.3)

data = {
    "X_train": X_train,
    "X_test": X_test,
    "y_train": y_train,
    "y_test": y_test
}

my_bounds = [
    FloatVar(lb=0.01, ub=300., name="C_paras"),
    StringVar(valid_sets=('linear', 'poly', 'rbf', 'sigmoid'), name="kernel_paras"),
    # IntegerVar(lb=1, ub=5, name="degree_paras"),
    MixedSetVar(valid_sets=('scale', 'auto', 0.01, 0.05, 0.1, 0.5, 1.0), name="gamma_paras"),
    # BoolVar(n_vars=1, name="probability_paras"),
]

problem = SvmOptimizedProblem(bounds=my_bounds, minmax="max", data=data)
# model = SMA.OriginalSMA(epoch=100, pop_size=20)
model_2 = TWO.OriginalTWO(epoch=100, pop_size=20)
# model.solve(problem)
model_2.solve(problem)

print(f"Best agent: {model.g_best}")
print(f"Best solution: {model.g_best.solution}")
print(f"Best accuracy: {model.g_best.target.fitness}")
print(f"Best parameters: {model.problem.decode_solution(model.g_best.solution)}")


# score = metrics.accuracy_score(y_test, prediction)
# print("accuracy:   %0.3f" % (score*100))
# cm = metrics.confusion_matrix(y_test, prediction, labels=[0,1])



# fig, ax = plot_confusion_matrix(conf_mat=cm,
#                                 show_absolute=True,
#                                 show_normed=True,
#                                 colorbar=True)
# plt.show()



