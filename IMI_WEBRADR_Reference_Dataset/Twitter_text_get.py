import requests
import pandas as pd
import csv
import re
import typer

### Variables to change if program stops halfway

# Write (w) if it is to start a new file
# Append if it is to append to an existing file
mode = 'a'
    
# Variable of where to start converting the records 
start = 30000


### Credenciais de autenticação do Twitter
bearer_token = ""

'''
Function that writes tsv files only with Twitter ID, text and label
'''
def write_dataset_task1_tsv(data, writer):
    for key in data.keys():
        label = ""
        if data[key]["Classification"]=="Non-AE Tweet":
            label = "NoADE"
        elif data[key]["Classification"]=="AE Tweet":
            label = "ADE"
        line = [key, data[key]["Text"], label]
        writer.writerow(line)

'''
Function that writes tsv files with Twitter ID, text, label and ADE spans.
Only writes tweets with the ADE label 
'''
def write_dataset_task2_tsv(data, writer):
    for key in data.keys():
        label = ""
        if data[key]["Classification"]=="Non-AE Tweet":
            label = "NoADE"
            continue
        elif data[key]["Classification"]=="AE Tweet":
            label = "ADE"
        #print("Processing data:")
        #print(data[key])
        events = data[key]["Event(s) as reported"].split(";")
        event_preferred_terms = data[key]["Event(s) coded (PT)"].split(";")
        for index in range(len(events)):
            e = events[index].lower()
            begin = data[key]["Text"].lower().find(e)
            if begin==-1:
                continue
            #print(begin)
            end = begin + len(e)
            if(index>=len(event_preferred_terms)):
                line = [key, data[key]["Text"], label, begin, end, e, event_preferred_terms[len(event_preferred_terms)-1]]
            else:
                line = [key, data[key]["Text"], label, begin, end, e, event_preferred_terms[index]]
            writer.writerow(line)
    


def main(input_file: str, task_1_output_tsv: str, task_2_output_tsv: str):
    
    # Open and read dataset file
    #df = pd.read_csv('./MyData/MOESM_only_data.csv')
    df = pd.read_csv(input_file)
    
    # Writen file names
    #task1_file = "T1_MOESM_dataset.tsv"
    #task2_file = "T2_MOESM_dataset.tsv"
    task1_file = task_1_output_tsv
    task2_file = task_2_output_tsv
    
    
    # Open files
    f1 = open(task1_file, mode)
    f2 = open(task2_file, mode)
    
    # Open casv writers
    writer1 = csv.writer(f1, delimiter='\t')
    writer2 = csv.writer(f2, delimiter='\t')
    
    # Only write headers if starting a new file
    if mode == 'w':
        f1_headers = ["tweet_id", "text", "label"]
        writer1.writerow(f1_headers)

        f2_headers = ["tweet_id", "text", "type", "begin", "end", "span", "preferred_term"]
        writer2.writerow(f2_headers)
    
    # Create http request session
    session = requests.Session()
    session.headers.update({'Authorization': 'Bearer '+ bearer_token})
    
    dataset_size = len(df["Twitter ID"])
    
    # Iterate over the records with a step of 100
    for i in range(start,dataset_size, 100):
        d = {}
        k = 0
        for k in range(0,100):
            if(i+k>=dataset_size):
                break
            attr = {}
            attr["Indicator score"] = df["Indicator score"][i+k] ##
            attr["Classification"] = df["Classification"][i+k] ##
            attr["Product(s) as reported"] = df["Product(s) as reported"][i+k]
            attr["Product coded (INN)"] = df["Product coded (INN)"][i+k]
            attr["Event(s) as reported"] = df["Event(s) as reported"][i+k] ##
            attr["Event(s) coded (PT)"] = df["Event(s) coded (PT)"][i+k] ##
            attr["Product-Event(s)"] = df["Product-Event(s)"][i+k]
            attr["Indication(s) as reported"] = df["Indication(s) as reported"][i+k]
            attr["Indication(s) coded (PT)"] = df["Indication(s) coded (PT)"][i+k]
            attr["Product-Indication(s)"] = df["Product-Indication(s)"][i+k]
            d[str(df["Twitter ID"][i+k])] = attr

        ids = [k for k in d.keys()]
        string_ids = str(ids[0])
        for index in range(1,k):
            string_ids = string_ids + "," + str(ids[index]) 

        #print(string_ids)
        
        # Getting tweet text from Twitter API
        response = session.get('https://api.twitter.com/2/tweets?ids=' + string_ids)

        if (response.status_code == 200):
            print("The request was a success!")
        else:
            print("Abnormal status detected. Terminating program.")
            print(response.json())
            break
            # Code here will react to failed requests
        
        data = {}
        response_json = response.json()
        
        for tweet in response_json["data"]:
            data[tweet["id"]] = d[tweet["id"]]
            text = tweet["text"]
            # Replace & char encoding from Twitter API
            if "&amp;" in text:
                text = text.replace("&amp;", "&")
            if "\n" in text:
                text = text.replace("\n", " ")
            if "\t" in text:
                text = text.replace("\t", " ")
            if "\r" in text:
                text = text.replace("\r", " ")
            text = re.sub('@\w+', '@USER____', text)
            text = re.sub('http\S+', 'HTTPURL____', text)
            data[tweet["id"]]["Text"] = text
            
        # Write retrieved text data into tsv files
        write_dataset_task1_tsv(data, writer1)
        write_dataset_task2_tsv(data, writer2)
        
        print(i+k+1, "records converted.")
        
    # Close files
    f1.close()
    f2.close()
    print("All records converted!")
    
    
if __name__ == "__main__":
    typer.run(main)
