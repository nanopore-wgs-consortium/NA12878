#!/usr/bin/env bash
# $1 is the input name

zgrep -F -f "$1"/ends_filenames.txt Notts_all.txt > "$1"/ends/urls.txt
zgrep -F -f "$1"/starts_filenames.txt Notts_all.txt > "$1"/starts/urls.txt

mkdir -p "$1"/ends/original/fast5
cd $_
xargs -n 1 curl -O# < ../../urls.txt
cd ../../../
mkdir -p starts/original/fast5
cd $_
xargs -n 1 curl -O# < ../../urls.txt
cd ../../../
