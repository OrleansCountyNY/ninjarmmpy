import ninjarmmpy
import os
import json

# Create our client
# Assuming we are storing our keys in environment variables we can access
client = ninjarmmpy.Client(
    AccessKeyID=os.environ.get('NRMM_KEY_ID'),
    SecretAccessKey=os.environ.get('NRMM_SECRET'),
    Europe=False
)
organizationId = 'YOUR_ORG_ID'
# Get usernames and logon times for all devices as Python dictionaries
end_users = client.getEndUsers(organizationId)
# For this example, we're just going to convert the dictionaries to JSON and write them to a file.
end_users = json.dumps(end_users)
# Now we can write the results to a JSON file.
with open('logged_on_users.json', 'w', newline='') as f:
    print(end_users, file=f)
