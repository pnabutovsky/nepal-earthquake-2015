from flask import Flask
from flask import request
from flask import jsonify

import time

app = Flask(__name__)
server_run = time.time()
output_file_name = f"survey_database_{server_run}.txt"

@app.route("/survey", methods=["POST"])
def create_household_demographics():
    content_length = request.content_length
    request_json = request.get_json()
    transaction_id = request_json['transaction_id']

    output_file = open(output_file_name, 'a')
    for record in request_json['data']:
        if record['valid'] == 1:
            output_file.write(f"{','.join([transaction_id, str(content_length), record['content']])}\n")

    output_file.close()

    response = {'transaction_id': transaction_id, 'content_length': content_length, 'server_run': server_run}
    return jsonify(response), 201


if __name__ == "__main__":
    app.run()
