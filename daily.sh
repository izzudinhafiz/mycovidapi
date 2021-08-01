#!/bin/bash
systemctl stop mycovidapi.service
.venv/bin/python db_sync.py
systemctl restart mycovidapi.service

