# WEBHOOK API
- This API can be used to hide a Discord webhook link to collect user data or log connections.
- API comes with ratelimit, connection and request logging (cli logging and file logging) and webhook raid alerts with protection.

# USAGE
- Change the webhook link in the `/apifiles/main.py` and host it on a private server.
- Make an **HTTP POST** request to `http://serverip:port/webhookpost`
- JSON values are given below:

```json
{
    "message":"YOUR MESSAGE HERE"    // message
}
```

# SHOWCASE
![image](img/Screenshot%202024-03-12%20215625.png)
![image](img/Screenshot%202024-03-12%20215542.png)
