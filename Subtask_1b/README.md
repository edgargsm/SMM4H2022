# SMM4H2022

## Subtask 1b

This directory holds the data and notebooks related to the solution of the Subtask 1b (Extraction of ADE mentions in tweets).

This directory contains the following directories:
- "training_data" - contains the challenge training data

The notebooks were used in an environment with dependencies already installed (Google Colab). Therefore only some of the dependencies are installed within the script (most of them are already available in the default Colab environments). When using Google Colab the data is read from Google Drive (it is mounted in the Colab machine) and, because of that, the paths to the dataset files are the ones I used in my Google Drive.
This directory includes the following notebook:

- "HuggingFaceBERT_NER.ipynb" - Notebook used to train and evaluate BERT/Transformer based models available in HuggingFace and generate predictions using those models.

## Results

The following hyperparameters were used to train the models:

- num_epochs = 3
- batch_size = 32*
- init_lr = 2e-5
- num_warmup_steps = 0
- weight_decay=0.01

*Bert-large-uncased used a batch size of 16 instead of 32 due to memory constraints

### Testing different models (trained with same challenge test data and same the params) with validation set:

#### Relaxed measures
| Model			| Precision	| Recall	| F1-score
| --- |:-----:|:-----:|:-----:|
| Bert_base_uncased	| 0.868 	| 0.673 	| 0.759
| Bert_large_uncased	| **0.924** 	| 0.629 	| 0.748
| RoBERTa_base		| 0.875 	| 0.769 	| 0.819
| RoBERTa_large		| 0.892 	| **0.841** 	| **0.865**
| BERTweet_large		| 0.885 	| 0.837 	| 0.860

#### Strict measures
| Model	| Precision	| Recall | F1-score |
| --- |:-----:|:-----:|:-----:|
| Bert_base_uncased	| 0.395 | 0.345 | 0.368 |
| Bert_large_uncased | 0.379 | 0.287 | 0.327 |
| RoBERTa_base | 0.612 | 0.563 | 0.587 |
| RoBERTa_large	| **0.639** | **0.609** | **0.624** |
| BERTweet_large | 0.598 | 0.598 | 0.598 |

### Testing the model(RoBERTA large), trained with different training data,  with the challenge validation set:

#### Relaxed measures
| Training_set	| Precision	| Recall | F1-score |
| --- |:-----:|:-----:|:-----:|
| Base_set		| 0.892 | 0.841 | 0.865 |
| Base_set with ref pos	| 0.887 | 0.798 | 0.840 |
| Base_set oversampled	| **0.905** | **0.854** | **0.879** |
| Base_set undersampled	| 0.894 | **0.854** | 0.874 |
| Base_set w/ref oversam	| 0.890 | 0.820 | 0.854 |


#### Strict measures
| Training_set	| Precision	| Recall | F1-score |
| --- |:-----:|:-----:|:-----:|
| Base_set		| 0.639 | 0.609 | 0.624 |
| Base_set with ref pos	| 0.650 | 0.598 | 0.623 |
| Base_set oversampled	| **0.667** | **0.644** | **0.655** |
| Base_set undersampled	| 0.647 | 0.632 | 0.640 |
| Base_set w/ref oversam	| 0.634 | 0.598 | 0.615 |