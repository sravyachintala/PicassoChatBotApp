import numpy as np
import pandas as pd

def get_random(low,high):
    return np.random.randint(low = low, high = high)

def time_fields(time_duration):
    value = [ 
        time_duration[get_random(0,len(time_duration))] ,
        time_duration[get_random(0,len(time_duration) //2)] ,
        time_duration[get_random(len(time_duration) // 2 +1, len(time_duration))] 
    ]
    return value

def filter_time(value,chunks):
    
    if value == 'in Week':
        time_value = chunks['time_week_value']
    elif value == 'in Month':
        time_value = chunks['time_month_value']
    elif value == 'in Quarter':
        time_value = chunks['time_quarter_value']
    else:
        time_value = chunks['time_year_value']
    
    return time_value

def filter_feature(value,chunks):
 
    feature_columns = {}
    
    if 'for category' in value:
        feature_value = chunks['category_value']
        feature_columns['for category'] = feature_value
    elif 'for Sub_category' in value:
        feature_value = chunks['sub_category_value']
        feature_columns['for Sub_category'] = feature_value
    elif 'for the Customer' in value:
        feature_value = chunks['customer_value']
        feature_columns['for the Customer'] = feature_value
        
    feature_value = ' ' + feature_value + ' '
    
    return feature_value,feature_columns

def get_question_chunks(intent):
    
    chunks = {}
    
    customer_value = intent.customer[get_random(0 , len(intent.customer))]
    tasks_value  = intent.tasks[get_random(0, len(intent.tasks))]
    category_value =  intent.category[get_random(0,len(intent.category))]
    sub_category_value = intent.sub_category[get_random(0,len(intent.sub_category))]
    
    time_quarter_value = time_fields(intent.time_quarter)
    time_month_value =   time_fields(intent.time_month)
    time_week_value =    time_fields(intent.time_week)
    
    chunks['customer_value'] = customer_value
    chunks['tasks_value'] = tasks_value
    chunks['category_value'] = category_value
    chunks['sub_category_value'] = sub_category_value
    chunks['time_quarter_value'] = time_quarter_value
    chunks['time_month_value'] = time_month_value
    chunks['time_week_value'] = time_week_value
    chunks['time_year_value'] = intent.time_year
    
    return chunks

def compose_questions(intent_constant,text_constant,no_of_questions):
    
    sentences = []
    task_col = []
    category_col = []
    sub_category_col = []
    customer_col = []

    for i in range(no_of_questions):
        question_chunks = get_question_chunks(intent_constant)
        
        time_frame_text = text_constant.time[get_random(0 , len(text_constant.time))]
        feature_text  = text_constant.features[get_random(0, len(text_constant.features))]
        question_action_text = text_constant.task[get_random(0,len(text_constant.task))]
        
        time_frame_value = filter_time(time_frame_text,question_chunks)
        feature_value,feature_columns = filter_feature(feature_text,question_chunks)
    
        if i % 2 == 0:
            template =  question_action_text + ' ' + question_chunks['tasks_value'] + ' '  +  feature_value + time_frame_text + ' '+ str(time_frame_value[0])
   
        else:
            if time_frame_value[0] == 2019:
                template = question_action_text + ' ' + question_chunks['tasks_value'] + ' '  + feature_value + time_frame_text + ' ' + str(time_frame_value[0])
            else:
                template = question_action_text + ' ' + question_chunks['tasks_value'] + ' '  + feature_value + time_frame_text + ' ' +time_frame_value[1] + ' to ' + time_frame_value[2] 
            
        template += '?'
        
        task_col.append(question_chunks['tasks_value'])
        
        sentences.append(template)
        
        if 'for category' in feature_columns:
            category_col.append(feature_columns['for category'])
            sub_category_col.append('NA')
            customer_col.append('NA')
        elif 'for Sub_category' in feature_columns :
            category_col.append('NA')
            sub_category_col.append(feature_columns['for Sub_category'])
            customer_col.append('NA')
        elif 'for the Customer' in feature_columns :
            category_col.append('NA')
            sub_category_col.append('NA')
            customer_col.append(feature_columns['for the Customer'])
            
    d = {'Queries': sentences, 'Task': task_col,
         'Category': category_col, 'Sub_Category': sub_category_col,
         'Customer':customer_col
        }
    df = pd.DataFrame(d)
    
    return df