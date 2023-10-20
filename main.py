import requests
def report_user(username):
 url = f"https://www.instagram.com/{username}/reports/"
 response = requests.get(url)
 if response.status_code == 200:
 return "User reported successfully!"
 else:
 return "Failed to report user."
for username in ["username1", "username2", ...]:
 print(report_user(username))
