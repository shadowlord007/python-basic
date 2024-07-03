user_url = input("Enter your URL: ")

# Remove the 'https://www.' prefix if present
if user_url.startswith('https://www.'):
    user_url = user_url[len('https://www.'):]

# Remove the '.com' suffix if present
if user_url.endswith('.com'):
    user_url = user_url[:-len('.com')]

print(user_url)