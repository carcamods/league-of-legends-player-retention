import requests

def send_discord_message(webhook_url = "https://discord.com/api/webhooks/1279557815161196616/NnnU6xQ0GliTDytnmqyUIH4-ZiUsbTNwUvs1_ZoeHA0GVQpmxrZ1WsVBmzX0uxKTtnAK", 
                         user_id = '698281435932655707', 
                         message = "Script Finished. Get back to work!!"):
    # Create the content with a mention
    content = f"<@{user_id}> {message}"
    
    # Prepare the payload
    data = {
        "content": content,
        "username": "Webhook Bot"  # Optional: Customize the webhook message sender name
    }
    
    # Send the message
    response = requests.post(webhook_url, json=data)
    return response.text

''' 
# Replace 'your_webhook_url' with your actual Discord webhook URL
webhook_url = 'https://discord.com/api/webhooks/1279557815161196616/NnnU6xQ0GliTDytnmqyUIH4-ZiUsbTNwUvs1_ZoeHA0GVQpmxrZ1WsVBmzX0uxKTtnAK'

# Replace 'your_user_id' with your actual Discord user ID
user_id = '698281435932655707'

# Message you want to send
message = "Hello! This is a test message."

# Send the message
result = send_discord_message()
print("Response from Discord:", result)
'''