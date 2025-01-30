# Ludo Game Optimizer - LGO

## How to use
1. Install
In order to run the code, a few libraries are required, please use the following command to install them.
```
pip install -r requirements.txt
```
2. Download the dataset from this [link](https://www.kaggle.com/datasets/stevenpeutz/misinformation-fake-news-text-dataset-79k/)
3. (If you would like to see the word cloud (commented in the file utils/preprocessing.py)), Uncomment the line (63) to download the necessary english stop words 
4. Finally, run the following command (for the sake of time, we'll optimize through one optimizer (even that take ages, TWO)):
```
python utils/SVM.py
```
## Explaining folder structure
We have a few folders (excluding root).
* **./ludo.py** (contains our ludo game)
* **utils/**: contains utilities like fitness functions, preprocessing, and our SVM problem to be optimized
* **metaheuristics/**: contains our metaheuristic classes.
* **dataset/**: our folder that contains csv files (will be empty, for size purposes).

Thank you, have a good day.
*Abdelouahab Benchikh, G1 (ISI)*