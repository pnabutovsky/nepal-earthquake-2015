import requests
import numpy
import sys
import time
import uuid

input_file_name = sys.argv[1]
number_of_records = int(sys.argv[2])
padding = sys.argv[3]
epsilon = float(sys.argv[4])

number_of_records_limit = 500
if number_of_records > number_of_records_limit:
    sys.exit(f"Terminating upload! Total number of records exceeded: {number_of_records}")


server_url = 'http://127.0.0.1:5000/survey'
input_file = open(input_file_name, 'r')
input_file.readline()


def pad(data):
    pad_size = number_of_records_limit - len(data)
    pad_content = data[0]['content']
    for i in range(pad_size):
        data.append({'valid': 0, 'content': pad_content})

def pad_noisy(data, epsilon = 0.004):
    scale = 1 / epsilon
    noise = round(numpy.random.laplace(loc = 0, scale = scale))

    pad_size = number_of_records_limit - len(data) - noise
    if pad_size > number_of_records_limit:
        pad_size = number_of_records_limit - len(data)
    elif pad_size < 0:
        pad_size = 0

    pad_content = data[0]['content']
    for i in range(pad_size):
        data.append({'valid': 0, 'content': pad_content})


data = []
for x in range(number_of_records):
    content = input_file.readline()
    data.append({'valid': 1, 'content': content})

if(padding == 'pad'):
    pad(data)
elif(padding == 'pad_noisy'):
    pad_noisy(data, epsilon)

start_time = time.time()
response = requests.post(
    server_url,
    headers = {'Content-Type': 'application/json'},
    json = {'transaction_id': str(uuid.uuid4()), 'data': data}
)
response_json = response.json()
response_time = time.time() - start_time

# print(response.status_code)
print(
    ','.join([
        response_json['transaction_id'],
        str(epsilon),
        str(number_of_records),
        str(response_json['content_length']),
        str(response_time)
    ])
)

