#!/bin/bash

# Replace these three settings.
PROJDIR="/home/goodcode/goodcode_nv/"
PIDFILE="$PROJDIR/goodcode.pid"
SOCKET="$PROJDIR/goodcode.sock"

cd $PROJDIR
if [ -f $PIDFILE ]; then
        kill `cat -- $PIDFILE`
            rm -f -- $PIDFILE
        fi

        source /home/goodcode/goodcode_nv/vcode/bin/activate
        exec ./manage.py runfcgi socket=$SOCKET pidfile=$PIDFILE
