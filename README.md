# SMM4H2022

This repository holds the data and solutions regarding the Task 1 (Classification, detection and normalization of Adverse Events (AE) mentions in tweets (in English)) of the [Social Media Mining for Health 2022
Shared Task](https://healthlanguageprocessing.org/smm4h-2022/).

SMM4H 2022 Overview Paper: https://aclanthology.org/2022.smm4h-1.54/

My submission's system description: https://aclanthology.org/2022.smm4h-1.19/

## Repository Structure

Each of the "Subtask" directories holds the notebooks used for experiments relating to the subtask. In addition, each directory contains a "README.md" file that contains an explanaiton of the notebooks as well as the results obtained for each approach. It is of note that no directory contains the subtask's challenge data, since that data is not meant to be publicly available.

Each subtasks tackeld were the following:

- "Subtask_1a" - Classification of tweets reporting ADEs (Adverse Drug Events).
- "Subtask_1b" - Detection of ADE spans in the tweets.
- "Subtask_1c" - Map ADE colloquial mentions to their standard concept IDs in the MedDRA vocabulary.

The remaining directory "IMI_WEBRADR_Reference_Dataset" holds a reference dataset that can be used for valdation of the different approaches. The directory also has a python script that retrieves the text of the tweets of the dataset (using the Twitter API) and lightly processes the retrieved text so as to convert the dataset to a format similar the the one made available through the the Shared Task.
