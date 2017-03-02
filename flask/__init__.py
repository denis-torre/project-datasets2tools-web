############################################################
############################################################
############### Datasets2Tools Web Interface ###############
############################################################
############################################################

#######################################################
########## 1. Setup Python ############################
#######################################################

##############################
##### 1.1 Python Libraries
##############################
import sys
import pandas as pd
from flask import Flask, request, render_template

##############################
##### 1.2 Custom Libraries
##############################

##############################
##### 1.3 Setup App
##############################
# Initialize Flask App
app = Flask(__name__)

#######################################################
########## 2. Setup Web Page ##########################
#######################################################

##############################
##### 2.1 Homepage
##############################

### 2.1.1 Main
@app.route('/datasets2tools')
def main():
	return render_template('index.html')

#######################################################
########## 3. Run Flask App ###########################
#######################################################
# Run App
if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0')