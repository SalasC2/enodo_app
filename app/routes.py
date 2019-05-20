from flask import render_template
from app import app
from config import map_key, file_name
import jsonify
import xlrd


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', map_key=map_key)

@app.route('/api/geojson')
def geoJson():
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
    Current_total [9] 
    Estimated_market_value [10]
    Priot_land [11] -- Gain or decrease in market value?
    Prior_building [12] -- Gain or decrease in market value?
    Prior_total [13] 
    Prior_land [14] -- Gain or decrease in market value?
    Prior_building [15] --Gain or decrease in market value?
    Prior_total [16]
    Prior_year [17] 
    Town [18]
    Volume [19]
    Location [20]
    tax_code [21]
    Neighbordhood [22]
    House_number [23]
    Direction [24]
    Street [25]
    Suffix [26]
    APT_type (Under Construction/1bdr/2brd/etc) [27] 
    City [28] -- ALL CHICAGO, worth putting in data? 
    Resident_type (same as apt_type) [29]
    Building_use [30]
    Apt_description [31]
    comm_units [32]
    ext_desc [33]
    full_bath [34]
    half_bath [35]
    bsmt_desc [36]
    attic_desc [37]
    AC [38]
    Fireplace [39]
    Garage_description [40]
    Age [41]
    bldg_sqre_ft [42]
    land_sqre_ft [43]
    bldg_sf [44]
    units_total [45]
    multi_sale [46]
    deed_type [47]
    sale_date [48]
    sale_amount [49]
    APPCNT [50]
    Appeal_a [51]
    Appeal_a_status [52]
    Appeal_a_result [53]
    Appeal_a_reason [54]
    Appeal_a_pin_result [55]
    APPEAL_A_PROPAV [56]
    APPEAL_A_CURRAV [57]
    APPEAL_A_RESLTDATE [58]


    """
    book = xlrd.open_workbook(file_name)
    sh1 = book.sheet_by_index(0)
    for rx in range(1, sh1.nrows):
        print(sh1.row(rx)[0])


