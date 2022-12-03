import requests
import sys
import time
import uuid

input_file_name = sys.argv[1]
number_of_records = int(sys.argv[2])
with_padding = (len(sys.argv) == 4) and (sys.argv[3] == '1')

server_url = 'http://127.0.0.1:5000/survey'
input_file = open(input_file_name, 'r')
input_file.readline()

def pad(data):
    # TODO: Do padding here
    return data

data = []
for x in range(number_of_records):
    content = input_file.readline()
    data.append({'valid': 1, 'content': content})

if with_padding:
    pad(data)

start_time = time.time()
response = requests.post(
    server_url,
    headers = {'Content-Type': 'application/json'},
    json = {'transaction_id': str(uuid.uuid4()), 'data': data}
)
response_json = response.json()
response_time = time.time() - start_time

# print(response.status_code)
print(','.join([response_json['transaction_id'], str(response_json['content_length']), str(number_of_records), str(response_time)]))