# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib import messages

from zif.sedna import protocol
import sys
import logging


def index(request):
    output = "Emaitza: \n"
    if request.method == "POST":
        try:
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

            conn.loadFile('bib.xml', 'bib')

            xqry = request.POST.get('xquery')

            begat_verses = conn.query(xqry)
            conn.traceOff()
            count = 0
            for k in begat_verses:
                count += 1
                # z = fromstring(k)
                # print count,z.text.strip()
                output += count + k.strip() + "\n"
            conn.commit()
            conn.close()
            messages.success(request, "Kontsulta zuzen egin da. Denbora:{d} Emaitza:".format(d=begat_verses.time))
        except:
            messages.error(request, "Errorea kontsulta egitean")

    return render(request, 'xquery.html', {"output": output})