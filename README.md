# MoodBlaster
Submission for the 2019 BostonHacks for the Bit Bots Team

Devpost: https://devpost.com/software/moodblaster-3zhqp6

# Setup

## Setup Environment

1. Install python (Windows, Mac): https://www.python.org/downloads/
2. Install required dependencies: `pip install --upgrade libsoundtouch flask google-cloud-vision flask-cors`
3. Connect to the same network as the Bose Speaker to be controlled
4. Include .json file with Google Cloud API key.
5. Make sure the following env variables are set before running the python application
    1. `BOSE_IP`
    2. `VISION_API_KEY`
    3. `GOOGLE_APPLICATION_CREDENTIALS` which points to the api key json file
    4. `SPOTIFY_API_KEY`

## Running Application

1. Running Flask Application: `python mood_blaster.py`
2. Running React Application:
   1. `cd bostonhacks-bit-bots/front-end/moodblaster/`
   2. `npm install`
   3. `npm start`
