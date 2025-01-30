import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from nltk.corpus import stopwords
import string
import re

#
# Removing links and artifacts
#
def clean_noise(text):
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub("\\W"," ",text) 
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)    
    return text

#
# Preprocessing 
#
def preprocess(real, fake):
    real['class'] = 1
    fake['class'] = 0
    df = pd.concat([real,fake])

    df = df.dropna()
    df = df.drop(["Unnamed: 0"],axis=1)
    # print(df)

    # There are no missing values
    missing_values = df.isnull().sum()
    
    return df


# ----- View Distribution -----

# data_count = df['class'].value_counts()

# # Create the figure and axes
# fig, ax = plt.subplots(figsize=(7, 5))

# # Plot the count plot using Matplotlib
# ax.bar(data_count.index, data_count.values)

# # Customize the plot
# ax.set_xlabel('class')
# ax.set_ylabel('Count')
# ax.set_title('Class Count Plot')

# Show the plot
# plt.show()

# ----- View Destribution -----

# Uncomment and Download for first time use 
# nltk.download('stopwords')

# --------

# wordcloud = WordCloud(width = 800, height = 800, 
#                 background_color ='white', 
#                 stopwords = stopwords.words('english'), 
#                 min_font_size = 10).generate(" ".join(df[df['class'] == 0].text)) 
  
# # plot fake news data                      
# plt.figure(figsize = (8, 8), facecolor = None) 
# plt.imshow(wordcloud) 
# plt.axis("off") 
# plt.tight_layout(pad = 0) 
# plt.show()

# --------