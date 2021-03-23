import spacy
import pandas as pd
import re
from constants import intents,text_constant
"""
def predict_date(model,query):
    date_tokens = model(query)
    extracted_date = []
    extracted_date_dict = {}
    for token in date_tokens:
        if token.ent_type_ == 'DATE':
            extracted_date.append(token)
    
    if len(extracted_date) != 0:
        filter_date =  get_time_range(extracted_date,query)
    else:
        filter_date = []
    
    if len(filter_date) > 1:
        extracted_date[-1] = str(extracted_date[-1]) + filter_date[0:len(filter_date)-1]
        
    extracted_date_dict['Date'] = extracted_date
    return extracted_date_dict
"""
def normalize_date(value,date_domain):
    
    if date_domain.lower() == 'month':
    
        normalized_date_value = text_constant.month_formats.get(str(value).lower())
    else:
        normalized_date_value = value
    return normalized_date_value

def parse_date(doc,i,date_domain):
    dict_ = {}
    if i + 2  >= len(doc) -1:      # Our sentence does not have to, and the time range is at the last of the sentence
        dict_['lower'] = normalize_date(doc[i+1],date_domain)
        dict_['range'] = 'NO'
    elif i + 2 < len(doc):   # There might be a range, or where clause is present
        if str(doc[i + 2]) == 'to':    # this means we have a range
            
            dict_['lower'] = normalize_date(doc[i+1],date_domain)
            dict_['upper'] = normalize_date(doc[i+3],date_domain)
            dict_['range'] = 'YES'
        elif str(doc[i+2]) != 'to':
            dict_['lower'] = normalize_date(doc[i+1],date_domain)
            dict_['range'] = 'NO'
    
    return dict_

def predict_date(model,query):
    doc = model(query)
    final_date_dict = {}
    for i,token in enumerate(doc):
        if token.ent_type_ == 'DATE':
            date_dict = parse_date(doc,i,token.text)
            final_date_dict= {token.text : date_dict}
            break
        
    return final_date_dict
 

def predict_entities(model, query):
    entity_dict = {}
    doc = model(query)

    for ent in doc.ents:
        entity_dict[ent.label_.lower()] = ent.text 

    return entity_dict


def predict_ppg_upc_factory(model,query):
    doc = model(query)
    ppg_upc_factory = {}
    for token in doc:
        
        if token.pos_ == 'NUM':
            if len(token) == 13:
                ppg_upc_factory['upc'] = str(token)
            if len(token) == 3:
                before, term, after = query.partition(str(token))
                before = before.rsplit(maxsplit=2)[-2:]
                if before[0] in intents.categories:
                    if before[1] in intents.categories[before[0]]:
                        ppg_upc_factory['ppg'] = before[0]+' '+before[1]+' '+str(token)
            if len(token) < 3:
                before, term, after = query.partition(str(token))
                before = before.rsplit(maxsplit=1)[-1:]
                if before[0].lower()=='factory':
                    ppg_upc_factory['factory'] = before[0]+' '+str(token)

    return ppg_upc_factory

def collate_output(extracted_date_dict,entity_dict,ppg_upc_factory):
    
    entity_dict['date'] = extracted_date_dict
    
    if ppg_upc_factory.get('upc') != None:
        entity_dict['upc'] = ppg_upc_factory.get('upc')
    else:
        entity_dict['upc'] = ''
        
    if ppg_upc_factory.get('ppg') != None:
        entity_dict['ppg'] = ppg_upc_factory.get('ppg')
    else:
        entity_dict['ppg'] = ''
        
    if ppg_upc_factory.get('factory') != None:
        entity_dict['factory'] = ppg_upc_factory.get('factory')
    else:
        entity_dict['factory'] = ''
    return entity_dict
    

def get_time_range(extracted_date,query):
    date_var = extracted_date[-1]
   
    match = re.search(str(date_var),query)
    
    return query[match.end():len(query)]
    
def predict_internal(date_model,entity_model,queries,column_name = 'English_Queries', path = None):
    if type(queries) == list :
        input_queries = queries
                
    elif type(queries) == pd.core.frame.DataFrame:
        input_queries = list(queries[column_name])
    
    else:
        input_queries = [queries]
  
    for query in input_queries:
        entity = predict_entities(entity_model, query)
        date_values = predict_date(date_model, query)
        ppg_upc_factory = predict_ppg_upc_factory(date_model, query)
        
        collated_entities = collate_output(date_values,entity,ppg_upc_factory)
    
    #set blank for the intents that do not have any value
    for item in intents.json_intents:
        if collated_entities.get(item) == None:
            collated_entities[item] = '' 
    return collated_entities
    

model = spacy.load('models/spacy_trained_model_v4')
## This will be used for extracitng Time Feature:
nlp_md = spacy.load('en_core_web_md')
    
def predict(query):
    global model, nlp_md 
    
    output = predict_internal(nlp_md,model,query)
    
    return output



