# Productivity Scripts

## murmur2page

Quick script for applying custom punctuation and capitalisation to audio transcription files, where this isn't handled natively. Heavily customisable and adaptable -- just add your own natural voice commands where applicable. For example, if you use "next line" as a verbal flag, you would add this under `LINEBREAK MARKERS`. 

Be careful not to add any commands that are likely to use in your own writing, such as "on my return, I will make coffee," if `return` is listed as one of your markers. 

This script automatically corrects capital letters and spacing around new sentences, but can be easily customised or removed in the case of unexpected behaviour. As this is a quick script, this has not been fully tested. 

`murmur2page.py` takes a raw unedited input.txt and produces output.txt. 

## pay_check

Simple sanity-checking linear regression for confirming stated vs actual hourly rates for freelancers, to easily highlight hidden penalties and weird behaviour, and provide evidence for further action if necessary.
