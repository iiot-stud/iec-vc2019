#!/bin/bash

# inspired by https://hpi.de/en/naumann/people/felix-naumann/writing.html

returnval=0

msg() {
    echo "$@"
}

checkNoOccur() {
    grep --color -n -r "\b${1}\b" --include \*.tex
    if [ $? == 0 ]; then
        msg "####### -----> failed for '$1'"
        msg "Additional information: " $2
        msg ""
        msg ""
        if [ $returnval == 0 ]; then
            returnval=1
        fi
    fi
}

checkNoOccur "will" 'Can be removed without substitution in almost all instances, except when explicitly talking about the future.'

checkNoOccur "like" 'Probably you mean "such as". Remember commas before "such as"'

checkNoOccur "whole" 'Usually "entire" is better.'

checkNoOccur "very" 'Avoid it.'

checkNoOccur "bad" 'You probably mean "poor".'

checkNoOccur "seems to be" 'Avoid it.'

checkNoOccur "in order to" 'Usually can be replaced simply with "to".'

checkNoOccur "get" 'is quite colloquial. Try "obtain", "yield", "receive", etc.'

checkNoOccur "apply on" '"apply to", not "apply on" (this is a typical mistake for Germans)'

checkNoOccur "you" "replace by passive"

exit $returnval