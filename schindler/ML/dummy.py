from inference import tokenize_only,predict_cluster

data_point={'name': 'Michael Delker',
 'interests': 'movie,adventure,science,politics,fashion,culture',
 'journey_frequency': 702,
 'cluster': None}

print('predict cluster')
print(predict_cluster([data_point['interests']])) 