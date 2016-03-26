#!/bin/bash
/usr/bin/supervisord -c /etc/supervisor/supervisord.conf 
tail -F /var/log/* /var/log/*/* 2> /dev/null
