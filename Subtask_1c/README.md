# SMM4H2022

## Subtask 1c

This directory holds the data and notebooks related to the solution of the Subtask 1c (Normalization of ADE mentions to their MedDRA preferred term IDs).

The notebooks were used in an environment with dependencies already installed (Google Colab). Therefore only some of the dependencies are installed within the script (most of them are already available in the default Colab environments). When using Google Colab the data is read from Google Drive (it is mounted in the Colab machine) and, because of that, the paths to the dataset files are the ones I used in my Google Drive.
This directory includes the following notebook:

- "HugginBertNormalizer.ipynb" - Notebook used to train and evaluate BERT/Transformer based models available in HuggingFace and generate predictions using those models.
- "Subtask_1c_data_merger.ipynb" - Notebook used to merge the challenge training and validation datasets into a single file.

## Results

The following hyperparameters were used to train the models:

- num_epochs = 3
- batch_size = 32*
- init_lr = 2e-5
- num_warmup_steps = 0
- weight_decay=0.01

*Bert-large-uncased used a batch size of 16 instead of 32 due to memory constraints

### Testing different models (trained with same challenge training data) with challenge validation set:

#### When the models were trained with the ADE span only the results were the follwing:

| Model			| Precision	| Recall | F1-score |
| --- |:-----:|:-----:|:-----:|
| Bert_base_uncased	| 0.138 	| 0.138 	| 0.138 |
| Bert_large_uncased	| 0.138 	| 0.138 	| 0.138 |
| RoBERTa_base		| **0.172** 	| **0.172** 	| **0.172** |
| RoBERTa_large		| 0.161 	| 0.161 	| 0.161 |
| BERTweet_base		| 0.092 	| 0.092 	| 0.092 |
| BERTweet_large		| 0.103 	| 0.103 	| 0.103 |

#### When the models were trained with the whole ADE tweet the results were the follwing:

| Model			| Precision	| Recall | F1-score |
| --- |:-----:|:-----:|:-----:|
| Bert_base_uncased	| 0.092 	| 0.092 	| 0.092 |
| Bert_large_uncased	| 0.069 	| 0.069 	| 0.069 |
| RoBERTa_base		| **0.126** 	| **0.126** 	| **0.126** |
| RoBERTa_large		| **0.126** 	| **0.126** 	| **0.126** |
| BERTweet_base		| 0.115 	| 0.115 	| 0.115 |
| BERTweet_large		| 0.103 	| 0.103 	| 0.103 |

### When training the model RoBERTa base with the challenge training data merged with the WEBRADR challenge data.

This time the model was trained solely with the ADE span

| Training_set		| Precision	| Recall	| F1-score |
| --- |:-----:|:-----:|:-----:|
| Base_set        	| 0.172 	| 0.172 	| 0.172 |
| Base_set with WEBRADR	| **0.184** 	| **0.184** 	| **0.184** |