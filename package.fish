#!/usr/bin/env fish
set basedir $PWD
echo $basedir
rm cat_button.zip
zip -9 $basedir/cat_button.zip cat_button.py
cd cat_button_venv/lib/python3.6/site-packages 
zip -gr9 $basedir/cat_button.zip . 
