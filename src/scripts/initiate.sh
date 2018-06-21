#!/bin/bash
set -e

### Configuration ###

SERVER=root@donaldmcdougal.com
APP_DIR=/root/britecore-test
KEYFILE=id_rsa
REMOTE_SCRIPT_PATH=/tmp/deploy-myapp.sh


### Library ###

function run()
{
  echo "Running: $@"
  "$@"
}


### Automation steps ###

if [[ "$KEYFILE" != "" ]]; then
  KEYARG="-i $KEYFILE"
else
  KEYARG=
fi

run scp $KEYARG deploy/work.sh $SERVER:$REMOTE_SCRIPT_PATH
echo
echo "---- Running deployment script on remote server ----"
run ssh $KEYARG $SERVER bash $REMOTE_SCRIPT_PATH
