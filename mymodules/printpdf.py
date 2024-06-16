
# coding: utf-8
from __future__ import division, print_function, absolute_import, unicode_literals

import subprocess
import sys

# ref: https://geonet.esri.com/thread/59446
# ref: https://helpx.adobe.com/jp/acrobat/kb/510705.html


def main(pdffile, printer_name):
    # acroread = r'C:\Program Files (x86)\Adobe\Reader 11.0\Reader\AcroRd32.exe'
    acrobat = r'C:\Program Files (x86)\Adobe\Acrobat 11.0\Acrobat\Acrobat.exe'

    # '"%s"'is to wrap double quotes around paths
    # as subprocess will use list2cmdline internally if we pass it a list
    # which escapes double quotes and Adobe Reader doesn't like that

    cmd = '"{}" /N /T "{}" "{}"'.format(acrobat, pdffile, printer_name)

    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = proc.communicate()
    exit_code = proc.wait()


if __name__ == '__main__':
    pdffile = "../output.pdf"
    printer_name = sys.argv[0]
    main(pdffile, printer_name)