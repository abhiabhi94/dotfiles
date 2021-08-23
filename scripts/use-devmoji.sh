#!/bin/bash
set -euo pipefail

FILE="$PWD/.git/hooks/commit-msg"
touch $FILE 
chmod 775 $FILE
printf "#\!/bin/sh\n\nCOMMIT_MSG_FILE=\$1\nCOMMIT_MSG=\$(cat \$COMMIT_MSG_FILE)\n\necho \"\${COMMIT_MSG}\" | devmoji --no-commit --lint > \$1" > $FILE
