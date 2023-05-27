import csv
from flask import Flask,request,jsonify

app=Flask(__name__)

def read_csv_file(student_details):
    with open('student_details.csv','r') as file:
        reader=csv.DictReader(file)
        return list(reader)
    
def paginate_data(data,page_number,page_size):
    start_index=(page_number-1)*page_size
    end_index=start_index+page_size
    paginated_data=data[start_index:end_index]
    return paginated_data

@app.route('/get_students',methods=['GET'])
def get_students():
    page_number=int(request.args.get('page',1))
    page_size=int(request.args.get('size',10))
    student_data=read_csv_file('student_details.csv')
    paginated_data=paginate_data(student_data,page_number,page_size)
    return jsonify(paginated_data)

if __name__=='__main__':
    app.run(debug=True)