# -*- coding: utf-8 -*-
from fabric.api import local

"""
author: developed@goodcode.co.uk
date: Fri  7 Jun 22:36:10 BST 2013
licence: Gnu 2.0
description: implement server deployment prcedure

"""

def test():
    """run goodcode specyfic tests test"""
    local('./manage.py test goodcode_nv --settings=goodcode_nv.local_settings')


def deploy():
    """ deploy to goodcode.co.uk """

    test()
    local('git add -p && git commit')
    local('git push -u goodcode thinkpad')

def update_github():
    """push local changes to github"""
    local('git push -u github thinkpad')

def shell():
    """run shell"""
    local('./manage.py shell --settings=goodcode_nv.local_settings')

def syncdb():
    """run syncdb"""
    local('./manage.py syncdb --settings=goodcode_nv.local_settings')
