from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import AnnPuResult, PollingUnit, Lga, Party
from datetime import datetime
import socket

# create a blueprint
main = Blueprint('main', __name__, template_folder='../templates')


# create a function to get the current time
def current_time():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


# create a function to get the current ip address
def get_ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address


# index route for the main blueprint
@main.route('/')
def index():
    return render_template('index.html')


# route for the about page
@main.route('/polling_unit_result', methods=['GET', 'POST'])
def pu_result():
    # get all the polling units
    pus = PollingUnit.query.all()
    # check if the request method is post
    if request.method == 'POST':
        # get the polling unit number from the form
        number = request.form['search']
        # check if the number is empty
        # if it is empty, flash a message and redirect to the same page
        if not number:
            flash('Please enter a number')
            return redirect(url_for('main.pu_result'))
        # if the number is not empty, query the database for the polling unit
        pus_ = PollingUnit.query.filter(PollingUnit.polling_unit_number == number).first()
        # check if the polling unit is found
        if not pus_:
            # if the polling unit is not found, flash a message and redirect to the same page
            flash('No polling unit found', 'danger')
            return redirect(url_for('main.pu_result'))
        # if the polling unit is found, flash a message and render the template
        flash('Polling unit found, click to see result', 'success')
        return render_template('puresult.html', pus_=pus_, n=1, number=number)
    # if the request method is not post, render the template
    return render_template('puresult.html', pus=pus, n=0)


# route to display the result of a polling unit
# the id is the unique id of the polling unit
@main.route('/display_pu_result/<int:id>')
def display_pu_result(id):
    # query the database for the polling unit
    pu = PollingUnit.query.filter(PollingUnit.uniqueid == id).first()
    # query the database for the result of the polling unit
    # the result is stored in the AnnPuResult table
    # the polling unit unique id is used to query the result
    pu_result = AnnPuResult.query.filter(AnnPuResult.polling_unit_uniqueid == pu.uniqueid).all()
    # render the template
    return render_template('displayres.html', pu_result=pu_result, pu=pu)


# route etp display total result of polling units in a local government area
@main.route('/results_by_lga', methods=['GET', 'POST'])
def results_by_lga():
    # get all the local government areas
    lga = Lga.query.all()
    # check if the request method is post
    if request.method == 'POST':
        # declare an empty list for each party
        PDP = []
        DPP = []
        ACN = []
        PPA = []
        CDC = []
        JP = []
        ANPP = []
        LABOUR = []
        CPP = []
        # get the local government area name from the form
        lg_name = request.form['result']
        # query the database for the local government area
        lg = Lga.query.filter(Lga.lga_name == lg_name).first()
        # query the database for the polling units in the local government area
        pus = PollingUnit.query.filter(PollingUnit.lga_id == lg.lga_id).all()
        # loop through the polling units
        for pu in pus:
            # query the database for the result of the polling unit
            pu_res = AnnPuResult.query.filter(AnnPuResult.polling_unit_uniqueid == pu.uniqueid).all()
            # loop through the result
            for pu_re in pu_res:
                # check the party abbreviation and append the party score to the appropriate list
                if pu_re.party_abbreviation == 'PDP':
                    PDP.append(pu_re.party_score)
                elif pu_re.party_abbreviation == 'DPP':
                    DPP.append(pu_re.party_score)
                elif pu_re.party_abbreviation == 'ACN':
                    ACN.append(pu_re.party_score)
                elif pu_re.party_abbreviation == 'PPA':
                    PPA.append(pu_re.party_score)
                elif pu_re.party_abbreviation == 'CDC':
                    CDC.append(pu_re.party_score)
                elif pu_re.party_abbreviation == 'JP':
                    JP.append(pu_re.party_score)
                elif pu_re.party_abbreviation == 'ANPP':
                    ANPP.append(pu_re.party_score)
                elif pu_re.party_abbreviation == 'LABOUR':
                    LABOUR.append(pu_re.party_score)
                elif pu_re.party_abbreviation == 'CPP':
                    CPP.append(pu_re.party_score)
        # render the template, passing the local government area name, the total score of each party and the number of polling units
        return render_template('res_by_lga.html', lga=lga, PDP=sum(PDP), DPP=sum(DPP),
                               ACN=sum(ACN), PPA=sum(PPA), CDC=sum(CDC), JP=sum(JP), ANPP=sum(ANPP),
                               LABOUR=sum(LABOUR), CPP=sum(CPP), n=1, lg_name=lg_name)
    # if the request method is not post, render the template
    return render_template('res_by_lga.html', lga=lga)


# route to store the result of a polling unit
@main.route('/store_result', methods=['GET', 'POST'])
def store_result():
    # get all the local government areas
    all_lgas = Lga.query.all()
    # get all the parties
    parties = Party.query.all()
    # check if the request method is post
    if request.method == 'POST':
        # lga = request.form['lga']
        # get the polling unit number from the form
        pu = request.form['pu']
        # get the user who entered the result from the form
        user = request.form['user']
        # get the party score from the form
        pdp = request.form['PDP']
        dpp = request.form['DPP']
        acn = request.form['ACN']
        ppa = request.form['PPA']
        cdc = request.form['CDC']
        jp = request.form['JP']
        anpp = request.form['ANPP']
        labour = request.form['LABOUR']
        cpp = request.form['CPP']

        # create a dictionary of the party score with the party abbreviation as the key
        parties_form = {
            'PDP': pdp,
            'DPP': dpp,
            'ACN': acn,
            'PPA': ppa,
            'CDC': cdc,
            'JP': jp,
            'ANPP': anpp,
            'LABOUR': labour,
            'CPP': cpp
        }

        # check if the polling unit number is valid
        pu_exist = PollingUnit.query.filter(PollingUnit.polling_unit_number == pu.upper()).first()
        # if the polling unit number is not valid, flash a message and render the template
        if not pu_exist:
            flash('invalid polling unit', 'danger')
            return render_template('store_result.html', lgas=all_lgas, parties=parties)
        # loop through the dictionary
        for party in parties_form:
            # send the details to the database
            send_details = AnnPuResult(
                polling_unit_uniqueid=pu_exist.uniqueid,
                party_abbreviation=party,
                party_score=parties_form[party],
                entered_by_user=user,
                date_entered=current_time(),
                user_ip_address=get_ip()
            )
            send_details.save()
        flash('Result successfully stored', 'success')
        return render_template('store_result.html', lgas=all_lgas, parties=parties)

    return render_template('store_result.html', lgas=all_lgas, parties=parties)
