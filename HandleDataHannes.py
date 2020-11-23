# Importing the necessary libraries
import pandas as pd
from collections import Counter
import nltk
# Ignore warnings for a specific error that we can ignore in this application
pd.options.mode.chained_assignment = None  # default='warn'

# Read our data from the data.csv file
stackOverflowData = pd.read_csv(
    './Data.csv',
    encoding='utf-8'
)

# Print the size of the dataset read
print('Number of Rows and Columns:')
print(stackOverflowData.shape)

# Print the column names of the data
listOfColumnNames = stackOverflowData.columns.values.tolist()
print('Column names:')
for name in listOfColumnNames:
    print(name)

# Print the dates from wich this data is produced
minValue = stackOverflowData['CreationDate'].min()
maxValue = stackOverflowData['CreationDate'].max()
print('Dates from wich the data is produced: ' +
      minValue + ' to ' + maxValue)

# Creating a Data Frame with only the necessary columns
df = stackOverflowData[['AcceptedAnswerId', 'Title',
                        'CreationDate', 'Body']]

# This is not implemented yet but here we will remove all rows witch have an accepted answer
#df = df.loc[df['AcceptedAnswerId'] != '']

# Setting the neccessary data to lowercase
df['Body'] = df['Body'].str.lower()

# List of words that we want to remove from the dataset
# We need a method to remove html tags like <p> that are right next to words without a space in between
stopWords = ['code', 'gt', 'i', '<p>i']

# Remove all the stopwords from the data
df['Body'] = df['Body'].apply(lambda x: ' '.join(
    [word for word in x.split() if word not in (stopWords)]))

# Print to test the remove stopwords function
print('Testa StopWords funktionen: \n')
print(df['Body'].head(4) + '\n')

# Create a list of the top appearing words. The nrOfWords variable defines how many words the list should contain.
nrOfWords = 10
rslt = Counter(' '.join(df['Body']).split()).most_common(nrOfWords)

# Print out the list created above.
print('\n')
for word in rslt:
    print('{} = {}'.format(word[1], word[0]))
