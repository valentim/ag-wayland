from datetime import datetime

def transform(json_data):
    labels = []
    x = []
    y = []
    for data in json_data['data']:
        column = data['column']
        labels.append(column)
        sub_y = []
        for value in data['values']:
            new_x = value['x']
            date = datetime.fromtimestamp(new_x)
            date_string = date.strftime("%Y/%m/%d")
            if date_string not in x:
                x.append(date_string)
            
            sub_y.append(value['y'])
        y.append(sub_y)
    
    return (x, y, labels)