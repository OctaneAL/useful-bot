from requests import post
from time import sleep
import random
import string

def random_char(char_num):
       return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))

ids = [226,516,833]

parameters = {
    'rf_innov_id': 226,
    'rf_name': 'Haha',
    'rf_email': 'kavo@gmail.com',
    'rf_rating': 1,
}

url = 'https://jasu2023.com/rating_crud.php'

while True:
    p = False
    for i in range(3):
        parameters['rf_innov_id'] = ids[i]

        if i == 0:
            parameters['rf_rating'] = 1
        else:
            parameters['rf_rating'] = 5

        parameters['rf_name'] = random_char(7)
        parameters['rf_email'] = random_char(random.randint(5, 20)) + '@gmail.com'
         
        request = post(url, parameters)
        if request.text.strip() != 'Rating added successfully. Thank you.':
             print('bad bad bad bad:')
             print(parameters)
             print(request)
             print('id =', id)
             p = True
    if not p:
         print('Good.')
    
    sleep(1)
