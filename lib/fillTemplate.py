#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Script to generate a scientific paper boiler plate."""

# compatibility for Python 2.x
from __future__ import print_function

__author__ = "Alexander Willner"
__copyright__ = "Copyright 2019, Alexander Willner"
__credits__ = ["Alexander Willner"]
__license__ = "Apache 2.0"
__version__ = "0.0.1"
__maintainer__ = "Alexander Willner"
__email__ = "alex@willner.ws"
__status__ = "Development"

import argparse
import re
import fileinput

CONST_TITLE="What is the core summary of the paper?"
CONST_CONTEXT="What is problem area, why is it interesting?"
CONST_PROBLEM="What is problem we specifically consider, why is it hard? (e.g., why do naive approaches fail?)"
CONST_WORK="Survey past relevant work. Why hasn’t it been solved before? Or, what’s wrong with previous proposed solutions?"
CONST_APPROACH="What are the key components of this approach and how does it differ to related work?"
CONST_EVAL="What are the expected/generated results and how will/have we validate(d) them?"
CONST_RESULT="The expected/generated scientific surplus value?"
CONST_OUTLOOK="How could this work be extended?"

def main(args):
    """ to be enhanced """
    print("Title: ",args.title)
    title = re.compile("(\\\\newcommand{\\\\metaTitle}{).*(})")
    for line in fileinput.input(['template.meta.tex'], inplace=True):
        print(title.sub("\\1" + str(args.title) + "\\2", line), end = '')

    print("First Name: ",args.firstname)
    print("Last Name: ",args.lastname)
    author = re.compile("(\\\\newcommand{\\\\metaAuthorFirst}{).*(})")
    for line in fileinput.input(['template.meta.tex'], inplace=True):
        print(author.sub("\\1" + str(args.firstname) + " " + str(args.lastname) + "\\2", line), end = '')

    print("Mail: ",args.mail)
    mail = re.compile("(\\\\newcommand{\\\\metaMailFirst}{).*(})")
    for line in fileinput.input(['template.meta.tex'], inplace=True):
        print(mail.sub("\\1" + str(args.mail) + "\\2", line), end = '')

    print("Institution: ",args.institution)
    print("Country: ",args.country)
    print("City: ",args.city)
    print("Zip: ",args.zip)
    instS = str(args.institution) + ", " + str(args.city) + ", " + str(args.country)
    inst = re.compile("(\\\\newcommand{\\\\metaInstFirst}{).*(})")
    for line in fileinput.input(['template.meta.tex'], inplace=True):
        print(inst.sub("\\1" + instS + "\\2", line), end = '')


    print("Context: ",args.context)
    context = re.compile(".*(%%context)")
    for line in fileinput.input(['src/00_abstract.tex'], inplace=True):
        print(context.sub(str(args.context) + " \\1", line), end = '')
    for line in fileinput.input(['src/01_introduction.tex'], inplace=True):
        print(context.sub("\\\\todotext{1 paragraph: " + str(args.context) + "} \\1", line), end = '')
    
    print("Problem: ",args.problem)
    problem = re.compile(".*(%%problem)")
    for line in fileinput.input(['src/00_abstract.tex'], inplace=True):
        print(problem.sub(str(args.problem) + " \\1", line), end = '')
    for line in fileinput.input(['src/01_introduction.tex'], inplace=True):
        print(problem.sub("\\\\todotext{1 paragraph: " + str(args.problem) + "} \\1", line), end = '')

    print("Work: ",args.work)
    work = re.compile(".*(%%work)")
    for line in fileinput.input(['src/00_abstract.tex'], inplace=True):
        print(work.sub(str(args.work) + " \\1", line), end = '')
    for line in fileinput.input(['src/01_introduction.tex'], inplace=True):
        print(work.sub("\\\\todotext{1 paragraph: " + str(args.work) + "} \\1", line), end = '')

    print("Approach: ",args.approach)
    approach = re.compile(".*(%%approach)")
    for line in fileinput.input(['src/00_abstract.tex'], inplace=True):
        print(approach.sub(str(args.approach) + " \\1", line), end = '')
    for line in fileinput.input(['src/01_introduction.tex'], inplace=True):
        print(approach.sub("\\\\todotext{1 paragraph: " + str(args.approach) + "} \\1", line), end = '')

    print("Evaluation: ",args.evaluation)
    evaluation = re.compile(".*(%%evaluation)")
    for line in fileinput.input(['src/00_abstract.tex'], inplace=True):
        print(evaluation.sub(str(args.evaluation) + " \\1", line), end = '')
    for line in fileinput.input(['src/01_introduction.tex'], inplace=True):
        print(evaluation.sub("\\\\todotext{1 paragraph: " + str(args.evaluation) + "} \\1", line), end = '')

    print("Result: ",args.result)
    result = re.compile(".*(%%result)")
    for line in fileinput.input(['src/00_abstract.tex'], inplace=True):
        print(result.sub(str(args.result) + " \\1", line), end = '')
    for line in fileinput.input(['src/01_introduction.tex'], inplace=True):
        print(result.sub("\\\\todotext{1 paragraph: " + str(args.result) + "} \\1", line), end = '')

    print("Outlook: ",args.outlook)
    outlook = re.compile(".*(%%outlook)")
    for line in fileinput.input(['src/00_abstract.tex'], inplace=True):
        print(outlook.sub(str(args.outlook) + " \\1", line), end = '')
    for line in fileinput.input(['src/01_introduction.tex'], inplace=True):
        print(outlook.sub("\\\\todotext{1 paragraph: " + str(args.outlook) + "} \\1", line), end = '')


if __name__ == "__main__":
    PARSER = argparse.ArgumentParser()

    PARSER.add_argument(
        "-v",
        "--version",
        action="version",
        version="%(prog)s (version {version})".format(version=__version__))

    PARSER.add_argument("-f", "--firstname", action="store", dest="firstname")
    PARSER.add_argument("-l", "--lastname", action="store", dest="lastname")
    PARSER.add_argument("-m", "--mail", action="store", dest="mail")
    PARSER.add_argument("-i", "--institution", action="store", dest="institution")
    PARSER.add_argument("--country", action="store", dest="country")
    PARSER.add_argument("--city", action="store", dest="city")
    PARSER.add_argument("--zip", action="store", dest="zip")
    PARSER.add_argument("-t", "--title", action="store", dest="title", help=CONST_TITLE)
    PARSER.add_argument("-c", "--context", action="store", dest="context", help=CONST_CONTEXT)
    PARSER.add_argument("-p", "--problem", action="store", dest="problem", help=CONST_PROBLEM)
    PARSER.add_argument("-w", "--work", action="store", dest="work", help=CONST_WORK)
    PARSER.add_argument("-a", "--approach", action="store", dest="approach", help=CONST_APPROACH)
    PARSER.add_argument("-r", "--result", action="store", dest="result", help=CONST_RESULT)
    PARSER.add_argument("-e", "--evaluation", action="store", dest="evaluation", help=CONST_EVAL)
    PARSER.add_argument("-o", "--outlook", action="store", dest="outlook", help=CONST_OUTLOOK)	

    MYARGS = PARSER.parse_args()
    main(MYARGS)
