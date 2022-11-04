# SMM4H2022

## IMI WEBRADR Reference dataset

This directory holds the IMI WEBRADR reference dataset in different formats as well as a script ro retrieve the text of the tweets present in the dataset. The script is "Twitter_text_get.py" and is used as follows:

```
python Twitter_text_get.py INPUT_FILE TASK_1_OUTPUT_TSV TASK_2_OUTPUT_TSV
```

The input file should be the IMI WEBRADR dataset in a csv format  and th outputs will be tsv files. Example:

```
python Twitter_text_get.py "MOESM_only_data.csv" "Output1.tsv" "Output2.tsv"
```

It is of note that the script might take a while to run and it may stop on account of an error depending on the reponse of the API. In case the script stops halfway, the variables "mode" and "start" should be changed to "a" and the number of records processed (printed in the terminal) respectively and then, the script should be run the same way again (with the same arguments) until all the records are processed.
As an example, if the latest output present in the terminal was "500 records converted." the variable "mode" should be changed to "a" and the variable start should be changed to 500.

Files present in this directory:

- MOESM1_ESM.xlsx - Original dataset with tweet IDs, but not their text.
- MOESM_only_data.csv - Same data as the original dataset, but in a csv format.
