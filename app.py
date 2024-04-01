from flask import Flask, render_template, url_for
import pandas as pd
import re

app = Flask(__name__)

# Function to extract number and street name from address
def extract_number_and_street(address):
    # Use regex to match number and street name
    pattern = r'(\d+)\s+(.*)'
    match = re.match(pattern, address)
    if match:
        number = match.group(1)
        street_name = match.group(2)
        return number, street_name
    else:
        return None, None
    
# Function to extract first and last name from owner
def extract_first_last_name(owner):
    # Check if the owner is a corporation
    if re.search(r'\b(LLC|CORP|LTD|ASSN)\b', owner):
        return owner, None
    else:
        # Use regex to match first name and last name
        pattern = r'^([^,]+)(?:,\s([^,]+(?:,\s[^,]+)*))?'
        match = re.match(pattern, owner)
        if match:
            last_name = match.group(1).strip()
            first_name = match.group(2).strip() if match.group(2) else None
            return first_name, last_name
        else:
            return None, None

@app.route('/')
def index():
    # Read data from file into a DataFrame
    file = "Parcels.txt"
    data = pd.read_csv(file, sep="|", header=0)

    # Apply the function to each address
    data['Number'], data['Street'] = zip(*data['ADDRESS'].map(extract_number_and_street))

    # Create a new DataFrame with the desired order of columns
    new_data = data[['Street', 'Number', 'PIN', 'OWNER', 'MARKET_VALUE', 'SALE_DATE', 'SALE_PRICE', 'LINK']]

    # Apply the function to each owner
    data['First Name'], data['Last Name'] = zip(*data['OWNER'].map(extract_first_last_name))

    # Create a new DataFrame with the desired order of columns
    second_data = data[['First Name', 'PIN', 'ADDRESS', 'MARKET_VALUE', 'SALE_DATE', 'SALE_PRICE', 'LINK']]

    return render_template('index.html', new_data=new_data, second_data=second_data)

if __name__ == '__main__':
    app.run(debug=True)
