# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from zif.sedna import protocol
import sys
import logging


def index(request):
    username = 'SYSTEM'
    password = 'MANAGER'
    database = 'db'
    port = 5050
    host = 'localhost'

    logging.basicConfig(stream=sys.stdout)
    log = logging.getLogger()
    log.setLevel(logging.DEBUG)

    conn = protocol.SednaProtocol(host, database, username, password, trace=True)

    docs = conn.documents

    query = u'<bib> {for $h in doc("bib")//publisher return <item> {$h} {for $b in doc("bib")//publisher where $b=$h return $b/../title} </item>}</bib>'

    if 'bib' not in docs:
        conn.loadFile('bib.xml', 'bib')

    begat_verses = conn.query(query)
    print begat_verses.time
    conn.traceOff()
    count = 0
    for k in begat_verses:
        count += 1
        # z = fromstring(k)
        # print count,z.text.strip()
        print count, k.strip()
    conn.commit()
    conn.close()

    return HttpResponse("Hello, world. You're at the polls index.")