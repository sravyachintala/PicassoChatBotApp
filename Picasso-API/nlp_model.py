# import spacy
# import pandas as pd
# import re
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

def parse_date(doc,i):
    dict_ = {}
    if i + 2  >= len(doc) -1:      # Our sentence does not have to, and the time range is at the last of the sentence
        dict_['lower'] = doc[i+1]
        dict_['range'] = 'NO'
    elif i + 2 < len(doc):   # There might be a range, or where clause is present
        if str(doc[i + 2]) == 'to':    # this means we have a range
            
            dict_['lower'] = doc[i+1]
            dict_['upper'] = doc[i + 3]
            dict_['range'] = 'YES'
        elif str(doc[i+2]) != 'to':
            dict_['lower'] = doc[i+1]
            dict_['range'] = 'NO'
    
    return dict_

def predict_date(model,query):
    doc = model(query)
    final_date_dict = ''
    for i,token in enumerate(doc):
        if token.ent_type_ == 'DATE':
            date_dict = parse_date(doc,i)
            final_date_dict= {token.text : date_dict}

            break
        
    return final_date_dict
 

def predict_entities(model, query):
    entity_dict = {}
    doc = model(query)

    for ent in doc.ents:
        entity_dict[ent.label_] = ent.text 

    return entity_dict



def collate_output(extracted_date_dict,entity_dict):
    
    entity_dict['Date'] = extracted_date_dict
    
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
        collated_entities = collate_output(date_values,entity)

    return collated_entities

# model = spacy.load('/Users/ambarish.chitnis/Documents/GitHub/nestle_demo/Picasso/picasso-api/nlp_module/models/spacy_trained_model_v4')
## This will be used for extracitng Time Feature:
# nlp_md = spacy.load('en_core_web_md')

def predict(query):
    global model
    global nlp_md
    # output = predict_internal(nlp_md,model,query)

    json_test = '''
    {
        "Response": {
            "status": "success",
            "nlp_tokens": {
            "task": "gross sales",
            "customer": "walmart",
            "category": "breakfast",
            "subcategory": "tea",
            "ppg_id": "123",
            "upc_id": "782364746374",
            "time": "Jan to March"
            },
            "visualization": [
            {
                "type": "numeric_value",
                "value": 10
            },
            {
                "type": "pie_chart",
                "value": {
                "header": "Pie Chart",
                "data": [
                    {
                    "legend": "Sales",
                    "value": 10
                    },
                    {
                    "legend": "Supply Chain",
                    "value": 40
                    },
                    {
                    "legend": "Marketing",
                    "value": 20
                    },
                    {
                    "legend": "R & D",
                    "value": 30
                    }
                ]
                }
            },
            {
                "type": "bar_chart",
                "value": {
                "header": "Bar Graph",
                "data": [
                    {
                    "legend": "Product 1",
                    "value": 10
                    },
                    {
                    "legend": "Product 2",
                    "value": 20
                    },
                    {
                    "legend": "Product 3",
                    "value": 40
                    },
                    {
                    "legend": "Product 4",
                    "value": 60
                    },
                    {
                    "legend": "Product 5",
                    "value": 80
                    }
                ]
                }
            },
            {
                "type": "table",
                "value": {
                "header": "XYZ",
                "data": [
                    {
                    "columns": [
                        "Ranking",
                        "Cumulative %"
                    ],
                    "rows": [
                        [
                        "Manufacturing",
                        "35%"
                        ],
                        [
                        "Sales",
                        "45%"
                        ],
                        [
                        "Marketing",
                        "20%"
                        ]
                    ]
                    }
                ]
                }
            }
            ]
        }
        }
    '''

    return json_test



