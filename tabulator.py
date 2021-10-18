"""
Code and functions to tally votes and generate an ordered list from the 
csv of the google form. 
"""

import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from numpy.core.arrayprint import dtype_is_implied

import pandas as pd

# location of the csv sheet
LOCATION = "/home/praharsh/Dropbox/research-admin/Colloquia/Vote_tabulator_sheets_2021/"



filename = LOCATION + '/' + "form_responses.csv"
filedata = pd.read_csv(filename)

print(filedata.columns)
speaker_votes =filedata.drop(columns=[filedata.columns[0]]).values.flatten()


speaker_votes_arr = np.array(speaker_votes)







speaker_list_arr = np.unique(speaker_votes_arr)
print(speaker_list_arr)
print(len(speaker_list_arr))



tabulation = np.array(list(dict(Counter(speaker_votes)).items()))

speakers, votes = tabulation.T
votes = np.array(votes, dtype=int)

print(speakers)
print(votes)
sortargs = np.argsort(votes)



sorted_votes = np.flip(votes[sortargs])
sorted_speakers = np.flip(speakers[sortargs])



outputdata = pd.DataFrame(np.array([sorted_speakers, np.array(sorted_votes, dtype=str)]).T, columns=(['Speaker', 'votes']))


outputdata.to_csv(LOCATION+'vote_tabulation.csv', index=False)
print(outputdata)

# for i, speaker in enumerate(speaker_list_arr):
    











# brian jordan alvarez
# young and holmes
