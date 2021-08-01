#!/bin/bash
systemctl stop mycovidapi.service
.venv/bin/python db_sync.py >> sync.log 2>&1
systemctl restart mycovidapi.service

