import re
import os
import spacy
import random

def return_index(sent,word):
    match = re.search(word, sent)
    if match:
        return (match.start(), match.end())

def prepare_data(df):
    data = []
    for index,row in df.iterrows():
 
        text = row['Queries']
        entities_lst = []

        if row['Task'] != 'NA':
            task = row['Task']
            index_start,index_end =return_index(text,task)
            entities_lst.append( (index_start,index_end,'Task') )

        if row['Category'] != 'NA':
            category = row['Category']
            index_start,index_end =return_index(text,category)
            entities_lst.append( (index_start,index_end,'Category') )

        if row['Sub_Category'] != 'NA':
            sub = row['Sub_Category']
            index_start,index_end =return_index(text,sub)
            entities_lst.append( (index_start,index_end,'Sub_Category') )

        if row['Customer'] != 'NA':
            cust = row['Customer']
            index_start,index_end =return_index(text,cust)
            entities_lst.append( (index_start,index_end,'Customer') )


        tuple_data = (text, {'entities' : entities_lst })
        data.append(tuple_data)
    return data

def initialize(data):
    nlp = spacy.blank('en')   
    if 'ner' not in nlp.pipe_names:
        ner = nlp.create_pipe('ner')
        nlp.add_pipe(ner, last=True)
     
    for _, annotations in data:
         for ent in annotations.get('entities'):
            ner.add_label(ent[2])
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']
    
    return nlp,other_pipes

def train(df,path,iterations=5):

    data  = prepare_data(df)
    
    nlp ,other_pipes = initialize(data)
    
    with nlp.disable_pipes(*other_pipes):  # only train NER
        optimizer = nlp.begin_training()

        for itn in range(iterations):
            print("Statring iteration " + str(itn))
            random.shuffle(data)
            losses = {}
            for text, annotations in data:
                nlp.update(
                    [text],  # batch of texts
                    [annotations],  # batch of annotations
                    drop=0.2,  # dropout - make it harder to memorise data
                    sgd=optimizer,  # callable to update weights
                    losses=losses)
            print(losses)


    save_model(nlp,path)
    
    
def save_model(nlp,path):
    if not os.path.exists(path):
        os.mkdir(path)
        
    #TO DO : Write multiple models
    nlp.to_disk(path+ '/'+ 'spacy_trained_model_v2')
    
    
    
    