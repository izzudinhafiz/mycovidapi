from flask_restful import fields

timeseries = {
    "date": fields.String,
    "cases": fields.Integer(attribute="confirmed"),
    "deaths": fields.Integer,
    "recovered": fields.Integer
}

cases_country = {
    "date": fields.String,
    "cases": fields.Integer(attribute="cases_new"),
    "clusterImport": fields.Integer(attribute="cases_import"),
    "clusterReligious": fields.Integer(attribute="cases_religious"),
    "clusterCommunity": fields.Integer(attribute="cases_community"),
    "clusterHighRisk": fields.Integer(attribute="cases_highrisk"),
    "clusterEducation": fields.Integer(attribute="cases_education"),
    "clusterDetentionCentre": fields.Integer(attribute="cases_detention_centre"),
    "clusterWorkplace": fields.Integer(attribute="cases_workplace")
}

cases_state = {
    "date": fields.String,
    "cases": fields.Integer(attribute="cases_new")
}

deaths = {
    "date": fields.String,
    "deaths": fields.Integer(attribute="deaths_new")
}

tests = {
    "date": fields.String,
    "rtk-ag": fields.Integer(attribute="tests_rtk_ag"),
    "pcr": fields.Integer(attribute="tests_pcr")
}

checkins = {
    "date": fields.String,
    "checkIn": fields.Integer(attribute="checkins"),
    "uniqueIndividual": fields.Integer(attribute="checkins_unique_ind"),
    "uniqueLocation": fields.Integer(attribute="checkins_unique_loc")
}

traces = {
    "date": fields.String,
    "casual": fields.Integer(attribute="traces_casual"),
    "hideLarge": fields.Integer(attribute="traces_hide_large"),
    "hideSmall": fields.Integer(attribute="traces_hide_small")
}

hospital = {
    "date": fields.String,
    "bedsTotal": fields.Integer(attribute="beds"),
    "bedsNonCrit": fields.Integer(attribute="beds_noncrit"),
    "admissionTotal": fields.Integer(attribute="admitted_total"),
    "admissionCovid": fields.Integer(attribute="admitted_covid"),
    "admissionPUI": fields.Integer(attribute="admitted_pui"),
    "dischargedTotal": fields.Integer(attribute="discharged_total"),
    "dischargedCovid": fields.Integer(attribute="discharged_covid"),
    "dischargedPUI": fields.Integer(attribute="discharged_pui"),
    "activeCovid": fields.Integer(attribute="hosp_covid"),
    "activePUI": fields.Integer(attribute="hosp_pui"),
    "activeNonCovid": fields.Integer(attribute="hosp_noncovid")
}

icu = {
    "date": fields.String,
    "bedsTotal": fields.Integer(attribute="beds_icu_total"),
    "bedsReserved": fields.Integer(attribute="beds_icu_rep"),
    "bedsAvailable": fields.Integer(attribute="beds_icu"),
    "bedsCovid": fields.Integer(attribute="beds_icu_covid"),
    "ventilator": fields.Integer(attribute="vent"),
    "ventilatorPortable": fields.Integer(attribute="vent_port"),
    "activeCovid": fields.Integer(attribute="icu_covid"),
    "activePUI": fields.Integer(attribute="icu_pui"),
    "activeNonCovid": fields.Integer(attribute="icu_noncovid"),
    "ventilatorCovid": fields.Integer(attribute="vent_covid"),
    "ventilatorPUI": fields.Integer(attribute="vent_pui"),
    "ventilatorNonCovid": fields.Integer(attribute="vent_noncovid"),
}

quarantine = {
    "date": fields.String,
    "bedsTotal": fields.Integer(attribute="beds"),
    "admissionTotal": fields.Integer(attribute="admitted_total"),
    "admissionCovid": fields.Integer(attribute="admitted_covid"),
    "admissionPUI": fields.Integer(attribute="admitted_pui"),
    "dischargedTotal": fields.Integer(attribute="discharged_total"),
    "dischargedCovid": fields.Integer(attribute="discharged_covid"),
    "dischargedPUI": fields.Integer(attribute="discharged_pui"),
    "activeCovid": fields.Integer(attribute="pkrc_covid"),
    "activePUI": fields.Integer(attribute="pkrc_pui"),
    "activeNonCovid": fields.Integer(attribute="pkrc_noncovid")
}

vax_registration = {
    "date": fields.String,
    "reg_total": fields.Integer,
    "reg_phase_2": fields.Integer,
    "reg_via_mysejahtera": fields.Integer,
    "reg_via_call": fields.Integer,
    "reg_via_web": fields.Integer,
    "reg_children": fields.Integer,
    "reg_elderly": fields.Integer,
    "reg_comorb": fields.Integer,
    "reg_oku": fields.Integer
}

vaccination = {
    "date": fields.String,
    "dose1_daily": fields.Integer,
    "dose2_daily": fields.Integer,
    "total_daily": fields.Integer,
    "dose1_cumulative": fields.Integer,
    "dose2_cumulative": fields.Integer,
    "total_cumulative": fields.Integer
}
