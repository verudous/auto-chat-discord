import requests

channel_id = 
token = ""
channel_url = ""
url = f"https://discordapp.com/api/v9/channels/{channel_id}/messages"

message = ""
header = {
    "authorization": token,
    "referrer": channel_url
}
data = {
    "content": message
}

requests.post(url, json=data, headers=header)
