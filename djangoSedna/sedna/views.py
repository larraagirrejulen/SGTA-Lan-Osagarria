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
            database = 'sdb'
            host = 'localhost'

            logging.basicConfig(stream=sys.stdout)
            log = logging.getLogger()
            log.setLevel(logging.DEBUG)

            conn = protocol.SednaProtocol(host, database, username, password, trace=True)

            docs = conn.documents

            i = 0
            while "bib"+str(i) in docs:
                i += 1
            conn.loadFile('bib.xml', "bib"+str(i))
            xqry = request.POST.get('xquery').replace("doc('bib')", "doc('bib" + str(i) + "')").replace('doc("bib")', 'doc("bib' + str(i) + '")')

            begat_verses = conn.query(xqry)
            conn.traceOff()
            for k in begat_verses:
                output += k.strip() + "\n"
            conn.commit()
            conn.close()
            messages.success(request, "Kontsulta zuzen egin da.")
        except:
            messages.error(request, "Errorea kontsulta egitean. Gogoratu kontsulta doc('bib') erabiltzea eta ez doc('bib.xml')")

    return render(request, 'xquery.html', {"output": output})