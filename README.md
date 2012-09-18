cgi_ddns
========

Solution for dynamic DNS using nsupdate and cgi-bin script.

Instructions:

Create directory /var/www/cgi-bin/nsupdate
Copy scripts into it.

Change domain in nsupdate.cgi and nsdelete.cgi

Drop nsupdate.conf in /etc/httpd/conf

Create passwords for names that are allowed to change it's dns A record:

    $ cd /et/httpd
    $ htdigest -c user.passwd.nsupdate DNS <hostname>


On the machine that has a public dynamic IP or is on a private subnet
behind a NAT router with dynamic IP:

crontab  -e
 
    0,15,30,45 * * * * curl --digest --user <hostname>:<password> -s http://<YOURWEBSERVER>/nsupdate/nsupdate.cgi > /dev/null

