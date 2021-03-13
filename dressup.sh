#!/bin/sh

DIR_IDOLS="$1/modules"
if [ ! -d $DIR_IDOLS ]; then
     mkdir $DIR_IDOLS
     touch $DIR_IDOLS/__init__.py
fi

cp ./dir_Modules/Idols.py $1/.
cp ./dir_Girls/**/*.py $DIR_IDOLS/.

echo "Completed!"
