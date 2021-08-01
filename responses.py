from flask_restful import fields


cases = {
    "date": fields.String,
    "cases": fields.Integer(attribute="cases_new")
}

deaths = {
    "date": fields.String,
    "deaths": fields.Integer(attribute="deaths_new")
}

tests = {
    "date": fields.String,
    "rtk-ag": fields.Integer,
    "pcr": fields.Integer
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
