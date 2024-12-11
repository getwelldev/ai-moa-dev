#!/bin/bash

# Create the logs directory if it doesn't exist
mkdir -p ../logs

# Create the static directory if it doesn't exist
mkdir -p static

# Create the config directory if it doesn't exit
mkdir -p ../config

# Backup existing configs if already exist in config directory
cp ../config/config.yaml ../config/config.yaml.$(date +'%Y-%m-%d')
cp ../config/worflow-config.yaml ../config/workflow-config.yaml.$(date +'%Y-%m-%d')
cp ../config/template_providerlist.txt ../config/template_providerlist.txt.$(date +'%Y-%m-%d')

# Copy example configs and Report by Template provider search to config directory
cp template_providerlist.txt.example ../config/template_providerlist.txt
cp template_providerlist.txt ../config/
cp config.yaml.example ../config/config.yaml
cp workflow-config.yaml.example ../config/workflow-config.yaml

# Fix permissions so AI MOA can read-write
chmod ug+rw ../config -R
chown $USER:$USER ../config/*
# Protect config.yaml from Other users
chmod o-rw ../config/config.yaml

# Install Python dependencies from requirements.txt
pip install -r requirements.txt


