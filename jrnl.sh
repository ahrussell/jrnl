#!/usr/local/bin/zsh
m=`ps -ax | grep -o mongod | wc -l`
if [ $m -le 2 ] ; then
    (>&2 echo "Error: Mongo not started!")
    exit 1
fi

source `which virtualenvwrapper.sh`
workon jrnl
MYDIR=`dirname $0`
python ${MYDIR}/__main__.py
deactivate

exit 0 # success!