customer = ['Walmart' ,'Kroger', 'Publix', 'UNIFI', 'Costco', 'Ahold', 'Amazon' ,'Target','Albertsons/Safeway', 'Aldi' ,'Dollar General']

category = ['Sauces', 'Breakfast' ,'Meats' ,'Cheese' ,'Candy']

sub_category = ['All others', 'Tea' ,'Hot Dogs', 'Coffee', 'Grated', 'Ketchup',
                'Processed Cheese', 'Hard' ,'Juice', 'Caramels' ,'Creamers', 
                'Bars/Snacks', 'Natural Cheese', 'Mayonaise' ,'Enhancers', 
                'Cold Cuts' ,'Shelf Stable', 'Bacon', 'Gelatin', 'Specialty Meats', 
                'BBQ' ,'Chocolate'
               ]

time_year = [2019]

time_month = ['Jan', 'Feb' ,'Mar' ,'Apr', 'May' ,'Jun', 'Jul' ,'Aug', 'Sep' ,'Oct', 'Nov' ,'Dec']

time_week = ['Week1' ,'Week2' ,'Week3' ,'Week4', 'Week5' ,'Week6' ,'Week7' ,'Week8' ,'Week9' ,'Week10' ,
             'Week11', 'Week12', 'Week13' ,'Week14', 'Week15' ,'Week16', 'Week17', 'Week18', 'Week19' ,
             'Week20', 'Week21', 'Week22' ,'Week23' ,'Week24' ,'Week25' ,'Week26' ,'Week27', 'Week28' ,
             'Week29' ,'Week30', 'Week31', 'Week32' ,'Week33', 'Week34', 'Week35' ,'Week36', 'Week37', 
             'Week38' ,'Week39' ,'Week40', 'Week41', 'Week42' ,'Week43', 'Week44' ,'Week46', 'Week47',
             'Week48', 'Week49' ,'Week50', 'Week51', 'Week52'
            ]
           
time_quarter = ['Q1', 'Q2', 'Q3', 'Q4']

tasks = ['Gross Sales','Net sales','Top Line', 'Bottom Line','Count','Max Shipment','Revenue']

json_intents = ['task','customer','category','sub_category','business_unit','dc']

#Used For UPC , PPG , Factory calculation
categories = {'Cheese': ['Processed Cheese', 'Natural Cheese', 'Grated', 'Shelf Stable'],
            'Meats': ['Bacon', 'Hot Dogs', 'Cold Cuts', 'Specialty Meats'],
            'Breakfast' : ['Coffee', 'Juice', 'Tea', 'Enhancers', 'Creamers'],
            'Sauces': ['Ketchup', 'Mayonnaise', 'BBQ', 'All others'],
            'Candy': ['Chocolate', 'Gelatin', 'Hard', 'Caramels', 'Bars/Snacks']}