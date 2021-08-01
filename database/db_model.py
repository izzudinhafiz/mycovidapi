from enum import auto
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKeyConstraint
from datetime import date
Base = declarative_base()


class Nation(Base):
    __tablename__ = "nationwide"
    date = Column(Date, primary_key=True)
    cases_new = Column(Integer)
    cases_import = Column(Integer)
    cases_religious = Column(Integer)
    cases_community = Column(Integer)
    cases_highrisk = Column(Integer)
    cases_education = Column(Integer)
    cases_detention_centre = Column(Integer)
    cases_workplace = Column(Integer)
    deaths_new = Column(Integer)
    tests_rtk_ag = Column(Integer)
    tests_pcr = Column(Integer)
    checkins = Column(Integer)
    checkins_unique_ind = Column(Integer)
    checkins_unique_loc = Column(Integer)
    traces_casual = Column(Integer)
    traces_hide_large = Column(Integer)
    traces_hide_small = Column(Integer)

    def as_dict(self):
        temp = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        temp["date"] = temp["date"].isoformat()
        return temp


class State(Base):
    __tablename__ = "statewide"
    date = Column(Date, primary_key=True)
    state = Column(String, primary_key=True)
    cases_new = Column(Integer)
    deaths_new = Column(Integer)
    checkins = Column(Integer)
    checkins_unique_ind = Column(Integer)
    checkins_unique_loc = Column(Integer)
    facility_hospital = relationship("Hospital", uselist=False)
    facility_quarantine = relationship("Quarantine", uselist=False)
    facility_icu = relationship("ICU", uselist=False)

    def as_dict(self):
        temp = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        temp["date"] = temp["date"].isoformat()
        return temp


class Hospital(Base):
    __tablename__ = "hospital"
    date = Column(Date, primary_key=True)
    state = Column(String, primary_key=True)
    beds = Column(Integer)
    beds_noncrit = Column(Integer)
    admitted_pui = Column(Integer)
    admitted_covid = Column(Integer)
    admitted_total = Column(Integer)
    discharged_pui = Column(Integer)
    discharged_covid = Column(Integer)
    discharged_total = Column(Integer)
    hosp_covid = Column(Integer)
    hosp_pui = Column(Integer)
    hosp_noncovid = Column(Integer)
    __table_args__ = (ForeignKeyConstraint([date, state], [State.date, State.state]), {})  # type: ignore

    def as_dict(self):
        temp = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        temp["date"] = temp["date"].isoformat()
        return temp


class Quarantine(Base):
    __tablename__ = "quarantine"
    date = Column(Date, primary_key=True)
    state = Column(String, primary_key=True)
    beds = Column(Integer)
    admitted_pui = Column(Integer)
    admitted_covid = Column(Integer)
    admitted_total = Column(Integer)
    discharged_pui = Column(Integer)
    discharged_covid = Column(Integer)
    discharged_total = Column(Integer)
    pkrc_covid = Column(Integer)
    pkrc_pui = Column(Integer)
    pkrc_noncovid = Column(Integer)
    __table_args__ = (ForeignKeyConstraint([date, state], [State.date, State.state]), {})  # type: ignore

    def as_dict(self):
        temp = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        temp["date"] = temp["date"].isoformat()
        return temp


class ICU(Base):
    __tablename__ = "icu"
    date = Column(Date, primary_key=True)
    state = Column(String, primary_key=True)
    bed_icu = Column(Integer)
    bed_icu_rep = Column(Integer)
    bed_icu_total = Column(Integer)
    bed_icu_covid = Column(Integer)
    vent = Column(Integer)
    vent_port = Column(Integer)
    icu_covid = Column(Integer)
    icu_pui = Column(Integer)
    icu_noncovid = Column(Integer)
    vent_covid = Column(Integer)
    vent_pui = Column(Integer)
    vent_noncovid = Column(Integer)

    __table_args__ = (ForeignKeyConstraint([date, state], [State.date, State.state]), {})  # type: ignore

    def as_dict(self):
        temp = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        temp["date"] = temp["date"].isoformat()
        return temp


class Cluster(Base):
    __tablename__ = "cluster"
    cluster = Column(String, primary_key=True)
    district = Column(String)
    date_announced = Column(Date)
    date_last_onset = Column(Date)
    category = Column(String)
    status = Column(String)
    cases_new = Column(Integer)
    cases_total = Column(Integer)
    cases_active = Column(Integer)
    tests = Column(Integer)
    icu = Column(Integer)
    deaths = Column(Integer)
    recovered = Column(Integer)


class Checkin(Base):
    __tablename__ = "checkin"
    date = Column(Date, primary_key=True)
    time_0000 = Column(Integer)
    time_0030 = Column(Integer)
    time_0100 = Column(Integer)
    time_0130 = Column(Integer)
    time_0200 = Column(Integer)
    time_0230 = Column(Integer)
    time_0300 = Column(Integer)
    time_0330 = Column(Integer)
    time_0400 = Column(Integer)
    time_0430 = Column(Integer)
    time_0500 = Column(Integer)
    time_0530 = Column(Integer)
    time_0600 = Column(Integer)
    time_0630 = Column(Integer)
    time_0700 = Column(Integer)
    time_0730 = Column(Integer)
    time_0800 = Column(Integer)
    time_0830 = Column(Integer)
    time_0900 = Column(Integer)
    time_0930 = Column(Integer)
    time_1000 = Column(Integer)
    time_1030 = Column(Integer)
    time_1100 = Column(Integer)
    time_1130 = Column(Integer)
    time_1200 = Column(Integer)
    time_1230 = Column(Integer)
    time_1300 = Column(Integer)
    time_1330 = Column(Integer)
    time_1400 = Column(Integer)
    time_1430 = Column(Integer)
    time_1500 = Column(Integer)
    time_1530 = Column(Integer)
    time_1600 = Column(Integer)
    time_1630 = Column(Integer)
    time_1700 = Column(Integer)
    time_1730 = Column(Integer)
    time_1800 = Column(Integer)
    time_1830 = Column(Integer)
    time_1900 = Column(Integer)
    time_1930 = Column(Integer)
    time_2000 = Column(Integer)
    time_2030 = Column(Integer)
    time_2100 = Column(Integer)
    time_2130 = Column(Integer)
    time_2200 = Column(Integer)
    time_2230 = Column(Integer)
    time_2300 = Column(Integer)
    time_2330 = Column(Integer)
