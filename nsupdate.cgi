#!/bin/sh

DOMAIN=example.com

echo "Content-type: text/htm"
echo
echo "Hello! $REMOTE_USER from $REMOTE_ADDR"

#First delete old records

nsupdate << EOF
server 127.0.0.1
zone ${DOMAIN}
update delete ${REMOTE_USER}.${DOMAIN}.
show
send
show

EOF

#Now create new

nsupdate << EOF
server 127.0.0.1
zone ${DOMAIN}
update add ${REMOTE_USER}.${DOMAIN}. 3600 A $REMOTE_ADDR
show
send

EOF

echo "Done!"



