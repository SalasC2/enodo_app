from flask import render_template
from app import app
from config import map_key, file_name
import jsonify
import xlrd
import json


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', map_key=map_key)

"""
Full Address [0]
Lat [1]
Lon [2]
Zip [3]
Rec_Type [4]
Pin [5]
Ovacls [6] 
Class_Description [7]
Current_land [8]
Current_building [9]
Current_total [10] 
Estimated_market_value [11]
Priot_land [12] -- Gain or decrease in market value?
Prior_building [13] -- Gain or decrease in market value?
Prior_total [14] 
Prior_land [15] -- Gain or decrease in market value?
Prior_building [16] --Gain or decrease in market value?
Prior_total [17]
Prior_year [18] 
Town [19]
Volume [20]
Location [21]
tax_code [22]
Neighbordhood [23]
House_number [24]
Direction [25]
Street [26]
Suffix [27]
APT_type (Under Construction/1bdr/2brd/etc) [28] 
City [29] -- ALL CHICAGO, worth putting in data? 
Resident_type (same as apt_type) [30]
Building_use [31]
Apt_description [32]
comm_units [33]
ext_desc [34]
full_bath [35]
half_bath [36]
bsmt_desc [37]
attic_desc [38]
AC [39]
Fireplace [40]
Garage_description [41]
Age [42]
bldg_sqre_ft [43]
land_sqre_ft [44]
bldg_sf [45]
units_total [46]
multi_sale [47]
deed_type [48]
sale_date [49]
sale_amount [50]
APPCNT [51]
Appeal_a [52]
Appeal_a_status [53]
Appeal_a_result [54]
Appeal_a_reason [55]
Appeal_a_pin_result [56]
APPEAL_A_PROPAV [57]
APPEAL_A_CURRAV [58]
APPEAL_A_RESLTDATE [59]
"""

# All data
@app.route('/api/geojson')
def geoJson():
    book = xlrd.open_workbook(file_name)
    sh1 = book.sheet_by_index(0)
    store = []
    framenames = []
    for rx in range(1, sh1.nrows):
        if sh1.row(rx)[0].value not in framenames:
            framenames.append(sh1.row(rx)[0].value)
            frame = {
                "address": sh1.row(rx)[0].value,
                "lat": sh1.row(rx)[1].value,
                "lon": sh1.row(rx)[2].value,
                "zip_code": sh1.row(rx)[3].value,
                "rec_type": sh1.row(rx)[4].value,
                "pin": sh1.row(rx)[5].value,
                "ovacls": sh1.row(rx)[6].value, 
                "class_Description": sh1.row(rx)[7].value,
                "current_land": sh1.row(rx)[8].value,
                "current_building": sh1.row(rx)[9].value,
                "current_total": sh1.row(rx)[10].value,  
                "estimated_market_value": sh1.row(rx)[11].value,
                "prior_land": sh1.row(rx)[12].value, # Gain or decrease in market value?
                "prior_building": sh1.row(rx)[13].value, # Gain or decrease in market value?
                "prior_total": sh1.row(rx)[14].value, 
                "prior_land": sh1.row(rx)[15].value, # Gain or decrease in market value?
                "prior_building": sh1.row(rx)[16].value, # Gain or decrease in market value?
                "prior_total": sh1.row(rx)[17].value,
                "prior_year": sh1.row(rx)[18].value, 
                "town": sh1.row(rx)[19].value,
                "volume": sh1.row(rx)[20].value,
                "location": sh1.row(rx)[21].value,
                "tax_code": sh1.row(rx)[22].value,
                "neighbordhood": sh1.row(rx)[23].value,
                "house_number": sh1.row(rx)[24].value,
                "direction": sh1.row(rx)[15].value,
                "street": sh1.row(rx)[26].value,
                "suffix": sh1.row(rx)[27].value,
                "apt_type": sh1.row(rx)[28].value, # (Under Construction/1bdr/2brd/etc)  
                "city": sh1.row(rx)[29].value, # ALL CHICAGO, worth putting in data? 
                "resident_type": sh1.row(rx)[30].value.strip(),
                "building_use": sh1.row(rx)[31].value,
                "apt_description": sh1.row(rx)[32].value,
                "comm_units": sh1.row(rx)[33].value,
                "ext_desc": sh1.row(rx)[34].value,
                "full_bath": sh1.row(rx)[35].value,
                "half_bath": sh1.row(rx)[36].value,
                "bsmt_desc": sh1.row(rx)[37].value,
                "attic_desc": sh1.row(rx)[38].value,
                "ac": sh1.row(rx)[39].value,
                "fireplace": sh1.row(rx)[40].value,
                "garage_description": sh1.row(rx)[41].value,
                "age": sh1.row(rx)[42].value,
                "bldg_sqre_ft": sh1.row(rx)[43].value,
                "land_sqre_ft": sh1.row(rx)[44].value,
                "bldg_sf": sh1.row(rx)[45].value,
                "units_total": sh1.row(rx)[46].value,
                "multi_sale": sh1.row(rx)[47].value,
                "deed_type": sh1.row(rx)[48].value,
                "sale_date": sh1.row(rx)[49].value,
                "sale_amount": sh1.row(rx)[50].value,
                "appcnt": sh1.row(rx)[51].value,
                "appeal_a": sh1.row(rx)[52].value,
                "appeal_a_status": sh1.row(rx)[53].value,
                "appeal_a_result": sh1.row(rx)[54].value,
                "appeal_a_reason": sh1.row(rx)[55].value,
                "appeal_a_pin_result": sh1.row(rx)[56].value,
                "appeal_a_propav": sh1.row(rx)[57].value,
                "appeal_a_currav": sh1.row(rx)[58].value,
                "appeal_a_tesltdate": sh1.row(rx)[59].value
            }
            store.append(frame)
    out = json.dumps(store, indent=4)
    return out
        


