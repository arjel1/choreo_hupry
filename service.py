from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Define the configurable HR endpoint
hr_endpoint = "test"

@app.route('/employees', methods=['POST'])
def get_employees():
    if request.method == 'POST':
        employee_ids = request.json.get('employeeIds', [])

        employee_info_list = []
        for emp_id in employee_ids:
            emp_response = requests.get(f"{hr_endpoint}/employee/{emp_id}")
            if emp_response.status_code == 200:
                employee_info_list.append(emp_response.json())

        aggregated_response = {'employeeDetails': employee_info_list}
        return jsonify(aggregated_response)

if __name__ == '__main__':
    app.run(port=9090)  # Run the Flask app on port 9090
