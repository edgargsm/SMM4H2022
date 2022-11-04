# SMM4H2022

## Subtask 1a 

This directory holds the data and notebooks related to the solution of the Subtask 1a (Classification of tweets relating to the presence of ADEs).

The notebooks were used in an environment with dependencies already installed (Google Colab). Therefore only some of the dependencies are installed within the script (most of them are already available in the default Colab environments).  When using Google Colab the data is read from Google Drive (it is mounted in the Colab machine) and, because of that, the paths to the dataset files are the ones I used in my Google Drive.
This directory includes the following notebooks:
- "Dataset_augmenting.ipynb" - Notebook used to augment the training dataset using the TextAttack library and other random sampling techniques.
- "HugginBertClassifiers.ipynb" - Notebook used to train and evaluate BERT/Transformer based models available in HuggingFace and generate predictions using those models.
- "HugginBertClassifierHyperOpt.ipynb" - Notebook used to train and evaluate BERT/Transformer based models available in HuggingFace and finetune their hyperparmeters.


## Results

The following hyperparameters were used to train the models:

- num_epochs = 3
- batch_size = 32*
- init_lr = 2e-5
- num_warmup_steps = 0
- weight_decay=0.01

*Bert-large-uncased used a batch size of 16 instead of 32 due to memory constraints

### Testing different models (trained with same challenge test data and same params) with validation set:

| Model	| Precision | Recall | F1-score |
| --- |:-----:|:-----:|:-----:|
| Bert_base_uncased  | 0.750 | 0.692 | 0.720 |
| Bert_large_uncased | **0.797** | 0.723 | 0.758 |
| RoBERTa_base       | 0.731 | 0.754 | 0.742 |
| RoBERTa_large	     | 0.778 | **0.862** | 0.818 |
| BERTweet_base	     | 0.754 | 0.662 | 0.705 |
| BERTweet_large     | **0.797** | 0.846 | **0.821** |

### Testing the model(Bertweet_large) with different training data with challenge validation set:

| Training_set | Precision | Recall | F1-score |
| --- |:-----:|:-----:|:-----:|
| Base_set | 0.797 	| 0.846 | 0.821 |
| Text-Attack aug | **0.909** | 0.769 | **0.833** |
| Oversampled | 0.809 | 0.846 | **0.827** |
| Undersampled | 0.778 | **0.862** | 0.818 |
| Aug. and over. | 0.825 | 0.800 | 0.812 |
| Wordnet syn aug | **0.850** | 0.785 | 0.816 |