from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import AnnPuResult, PollingUnit, Lga, Party
from datetime import datetime
import socket

main = Blueprint('main', __name__, template_folder='../templates')


def current_time():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def get_ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/polling_unit_result', methods=['GET', 'POST'])
def pu_result():
    pus = PollingUnit.query.all()
    if request.method == 'POST':
        number = request.form['search']
        if not number:
            flash('Please enter a number')
            return redirect(url_for('main.pu_result'))
        pus_ = PollingUnit.query.filter(PollingUnit.polling_unit_number == number).first()
        if not pus_:
            flash('No polling unit found', 'danger')
            return redirect(url_for('main.pu_result'))
        flash('Polling unit found, click to see result', 'success')
        return render_template('puresult.html', pus_=pus_, n=1, number=number)
    return render_template('puresult.html', pus=pus, n=0)


@main.route('/display_pu_result/<int:id>')
def display_pu_result(id):
    pu = PollingUnit.query.filter(PollingUnit.uniqueid == id).first()
    pu_result = AnnPuResult.query.filter(AnnPuResult.polling_unit_uniqueid == pu.uniqueid).all()
    return render_template('displayres.html', pu_result=pu_result, pu=pu)


@main.route('/results_by_lga', methods=['GET', 'POST'])
def results_by_lga():
    lga = Lga.query.all()
    if request.method == 'POST':
        PDP = []
        DPP = []
        ACN = []
        PPA = []
        CDC = []
        JP = []
        ANPP = []
        LABOUR = []
        CPP = []
        lg_name = request.form['result']
        lg = Lga.query.filter(Lga.lga_name == lg_name).first()
        pus = PollingUnit.query.filter(PollingUnit.lga_id == lg.lga_id).all()
        for pu in pus:
            pu_res = AnnPuResult.query.filter(AnnPuResult.polling_unit_uniqueid == pu.uniqueid).all()
            for pu_re in pu_res:
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
        return render_template('res_by_lga.html', lga=lga, PDP=sum(PDP), DPP=sum(DPP),
                               ACN=sum(ACN), PPA=sum(PPA), CDC=sum(CDC), JP=sum(JP), ANPP=sum(ANPP),
                               LABOUR=sum(LABOUR), CPP=sum(CPP), n=1, lg_name=lg_name)

    return render_template('res_by_lga.html', lga=lga)


@main.route('/store_result', methods=['GET', 'POST'])
def store_result():
    all_lgas = Lga.query.all()
    parties = Party.query.all()
    if request.method == 'POST':
        # lga = request.form['lga']
        pu = request.form['pu']
        user = request.form['user']

        pdp = request.form['PDP']
        dpp = request.form['DPP']
        acn = request.form['ACN']
        ppa = request.form['PPA']
        cdc = request.form['CDC']
        jp = request.form['JP']
        anpp = request.form['ANPP']
        labour = request.form['LABOUR']
        cpp = request.form['CPP']

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

        pu_exist = PollingUnit.query.filter(PollingUnit.polling_unit_number == pu.upper()).first()
        if not pu_exist:
            flash('invalid polling unit', 'danger')
            return render_template('store_result.html', lgas=all_lgas, parties=parties)

        for party in parties_form:
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
