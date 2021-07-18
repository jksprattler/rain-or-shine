# Usage

## Overview
The `rain-or-shine.py` script performs an API call out to Weather Stack by auto-detecting the location of the user based on their IP address. The API call is run from within a Docker build file which parses arguments based on the following variables based on the API results for the day's forecast:\
`rain` - If the precipitation value forecast is greater than 5% then you're recommended to grab an umbrella\
`shine` - If the UV Index value forecast is greater than 3 then you're recommended to grab sunscreen

## Useful links
- [Weather Stack API Documentation](https://weatherstack.com/documentation)

## Pre-requisites
Docker needs to be downloaded and installed on your local machine

## Procedure
1. Clone the repo to your local machine:\
```
git clone https://github.com/jksprattler/rain-or-shine.git
```
2. From within the local directory where you've cloned the repo, Build the Dockerfile via shell:\
```
docker build -t dockerpython .
```
3. From within the same dir, Run the Dockerfile:\
```
docker run dockerpython
```
4. Review the results of the arguments that were parsed from the API results

## Future Enhancements
1. Configure the python script and Docker build to automatically run the forecast results at 6am every day
   - import schedule | schedule==1.1.0
   - import time
   - schedule.every().day.at("12:00").do(job)
   - Run via cron job from docker?
