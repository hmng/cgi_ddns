#!/bin/sh

DOMAIN=example.com

echo "Content-type: text/htm"
echo
echo "Hello! Deleting $REMOTE_USER from $REMOTE_ADDR"

nsupdate << EOF
server 127.0.0.1
zone ${DOMAIN}
update delete ${REMOTE_USER}.${DOMAIN} 
show
send
show

EOF

echo "Done!"

