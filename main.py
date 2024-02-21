from flask import Flask, jsonify, request, render_template
import psycopg2
from psycopg2 import Error

app = Flask(__name__)

# Function to connect to the PostgreSQL database
def connect_to_db():
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="#",
                                      host="localhost",
                                      port="5432",
                                      database="postgres")
        return connection
    except (Exception, Error) as error:
        print("Error connecting to PostgreSQL:", error)

# Function to fetch applications from the database
def get_applications_from_db():
    try:
        connection = connect_to_db()
        cursor = connection.cursor()
        select_query = "SELECT * FROM public.applications"
        cursor.execute(select_query)
        applications = cursor.fetchall()
        columns = [col[0] for col in cursor.description]
        application_list = []
        for row in applications:
            application_list.append(dict(zip(columns, row)))
        return application_list
    except (Exception, psycopg2.Error) as error:
        print("Error fetching data from PostgreSQL:", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Connection to PostgreSQL closed")

# Handler to return list of applications via API
@app.route('/api/applications', methods=['GET'])
def get_applications_api():
    applications = get_applications_from_db()
    if applications:
        return jsonify(applications)
    else:
        return jsonify({"message": "Applications not found"}), 404

# Handler to render add application form
@app.route('/add_application', methods=['GET'])
def show_add_application_form():
    return render_template('add_application.html')

# Handler to add a new application record to the database
@app.route('/add_application', methods=['POST'])
def add_application():
    if request.method == 'POST':
        data = request.form
        try:
            connection = connect_to_db()
            cursor = connection.cursor()
            postgres_insert_query = """INSERT INTO public.applications (name, description, version, type, status, age_restriction, author, apk, icon, banner1, banner2, banner3) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            record_to_insert = (data['name'], data['description'], data['version'], data['type'], data['status'], data['ageRestriction'], data['author'], data['apk'], data['icon'], data['banner1'], data['banner2'], data['banner3'])
            cursor.execute(postgres_insert_query, record_to_insert)
            connection.commit()
            print("Record successfully added to applications table")
            return jsonify({"message": "Record successfully added to applications table"}), 200
        except KeyError as e:
            print("KeyError: ", e)
            return jsonify({"error": "One or more required fields are missing"}), 400
        except (Exception, psycopg2.Error) as error:
            print("Error working with PostgreSQL:", error)
            return jsonify({"error": "Error working with PostgreSQL"}), 500
        finally:
            if connection:
                cursor.close()
                connection.close()
                print("Connection to PostgreSQL closed")

if __name__ == '__main__':
    app.run(debug=True)
