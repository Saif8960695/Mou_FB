import requests

# Replace with your access token
ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN'

# Base URL for the Graph API
BASE_URL = 'https://graph.facebook.com/v12.0'

# Function to create a live video
def create_live_video(page_id):
    url = f'{BASE_URL}/{page_id}/live_videos'
    params = {
        'access_token': ACCESS_TOKEN,
        'status': 'LIVE_NOW',
        'title': 'My Live Video',
        'description': 'Description of my live video'
    }
    response = requests.post(url, params=params)
    return response.json()

# Function to get live video details
def get_live_video(live_video_id):
    url = f'{BASE_URL}/{live_video_id}'
    params = {
        'access_token': ACCESS_TOKEN
    }
    response = requests.get(url, params=params)
    return response.json()

# Function to end a live video
def end_live_video(live_video_id):
    url = f'{BASE_URL}/{live_video_id}'
    params = {
        'access_token': ACCESS_TOKEN,
        'end_live_video': 'true'
    }
    response = requests.post(url, params=params)
    return response.json()

# Replace with your page ID and live video ID
page_id = 'YOUR_PAGE_ID'
live_video_id = 'YOUR_LIVE_VIDEO_ID'

# Create a live video
create_response = create_live_video(page_id)
print('Create Live Video Response:', create_response)

# Get live video details
get_response = get_live_video(create_response['id'])
print('Get Live Video Response:', get_response)

# End the live video
end_response = end_live_video(create_response['id'])
print('End Live Video Response:', end_response) 
