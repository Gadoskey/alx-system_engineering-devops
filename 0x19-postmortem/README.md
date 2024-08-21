**My First Postmortem: Why Nginx Wasn’t Running on Port 80 (And How I Fixed It)**
Author: Mustapha Opeyemi Yusuf
Date: August 18, 2024

Nginx is the cool kid on the block in web servers, especially when it’s supposed to listen on port 80 for all your HTTP traffic. So imagine my surprise when my website decided to take an unexpected nap! This postmortem reflects on the incident where Nginx wasn’t running on port 80 and the detective work that followed.


**Issue Summary**

Duration of the Outage: 2 hours (3:00 PM UTC - 5:00 PM UTC)
Impact: Complete service outage, 100% of users affected. Visitors experienced “connection refused” errors as Nginx wasn’t listening on port 80.
Root Cause: Nginx was misconfigured to listen on port 8080 instead of port 80.

**Timeline**

3:00 PM UTC: Issue detected, website inaccessible with “connection refused” error.
3:05 PM UTC: Assumed Nginx service crash or server downtime.
3:10 PM UTC: Checked Nginx status and confirmed it was running but not on port 80.
3:15 PM UTC: Investigated Nginx configuration in /etc/nginx/sites-enabled/ for port misconfiguration.
3:25 PM UTC: Checked UFW settings, found no issues with the firewall.
3:40 PM UTC: Confirmed Nginx was set to listen on port 8080.
3:45 PM UTC: Escalated the issue to myself for resolution.
4:00 PM UTC: Wrote and executed a bash script to correct the Nginx configuration and restart the service.
4:10 PM UTC: Confirmed service was back up on port 80.
5:00 PM UTC: Monitored the system for an hour; no further issues detected.

**Root Cause: The Incident**

Picture this: I’m happily running my website, and suddenly… boom, it goes down. I tried accessing it, only to be met with the dreaded “connection refused” error. My server was ghosting me.

After some investigation, I discovered that Nginx was running on port 8080 instead of the usual port 80. Cue facepalm! This misconfiguration was the culprit, so I had to dig deeper into the server setup to figure out why my web server had switched ports without telling me.

Corrective and Preventative Measures
First, I ran the classic check on Nginx’s status:

sudo service nginx status
As expected, Nginx was alive but not on speaking terms with port 80. After checking the Nginx configuration file in /etc/nginx/sites-enabled/default, I found it was set to listen on port 8080 instead of 80. Now I knew what needed fixing, and I was ready to roll up my sleeves and make things right.

**The Fix**

To get Nginx back on track and listening on the correct port, I wrote a quick bash script to fix the configuration and restart the service. Here’s the code that saved the day:

#!/usr/bin/env bash

# Sets Nginx for listening to port 80
sed -i "s/8080/80/" /etc/nginx/sites-enabled/default
sudo service nginx restart
kill -9 "$(cat /var/run/nginx.pid)"

**Breakdown:**

sed -i "s/8080/80/": Replaces port 8080 with 80 in the Nginx config file.
sudo service nginx restart: Restarts Nginx so the change takes effect.
kill -9 "$(cat /var/run/nginx.pid)": Forcefully kills the Nginx process if it acts up, allowing it to restart cleanly.
After running this script, I gave Nginx a good restart, and voila! My website was back online, happily accepting visitors on port 80, like it was supposed to.

**Postmortem Reflections**

Here’s the thing: I learned that small mistakes (like incorrect port numbers) can lead to big headaches. Going forward, I’ll be extra careful to double-check configuration files after updates or changes.

**Conclusion**

Fixing the Nginx port issue turned into an unexpected learning opportunity, not just in terms of technical troubleshooting but also in how to make these experiences engaging. And with that, I’ve learned to always keep my server configurations in check and my sense of humor close by.
