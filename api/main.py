import time
from flask import Flask, request
import requests

webhookurl = ""

app = Flask(__name__)
red = "\033[1;31m"
green = "\033[1;32m"
purple = "\033[1;35m"
white = "\033[1;37m"
ip_addresses = {}
ratelimit = 5     # 1 request in 30 seconds

@app.route('/webhookpost', methods=['POST'])
def save_data():
    global ip_addresses

    data = request.json
    if not data:
        return 'Invalid JSON data', 400

    message = data.get('message', '')
    ip_address = request.remote_addr

    if ip_address in ip_addresses and ip_addresses[ip_address] > time.time():
        return 'Rate limit exceeded', 429

    if message in {"@everyone", "@here"}:
        raid = f"""{red} [RAID] {white} Raid attempt by:
{purple} [+] {white} IP: {ip_address}
"""
        print(raid)
        with open("log.txt", "a") as file:
            file.write(f"\n{raid}")
        return 'Raid', 429

    content = f"""
{green}[POST]{white} Got data:
Content: {message} 
IP: {ip_address}
"""
    print(content)
    try:
        r = requests.post(webhookurl, json={"content": f"""{message}\n\nCoded By KSHV"""})
        r.raise_for_status()  # Raise an exception for bad status codes
    except Exception as e:
        print(e)
        
    with open("log.txt", "a") as file:
        file.write(f"\n{content}")
    ip_addresses[ip_address] = time.time() + ratelimit

    return 'Data received successfully'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8821, debug=False)
