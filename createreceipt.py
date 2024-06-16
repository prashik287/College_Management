import jinja2
import pdfkit
from datetime import datetime
# import aspose.pdf as ap

# Initialize document object

# receipt_no = 74747473
# adm_no = 85843833
# std_name = 'Prashik Jadhav'
# depart = 'Information technology'
# clas = 'DSE'
# method = "cash"
# drawn = "Santosh Jadhav"
# amount_in_words = "Thirty Thousand"
# paid = 30000
# balance = 6256

def printreceipt(std_name,receipt_no,amount_in_words,paid,balance,clas,depart,method,drawn):
    today_date = datetime.today().strftime("%d %b, %Y")
    context = {
        'my_name': std_name,
        'receipt_no': receipt_no,
        'amount_words': amount_in_words,
        'paid': paid,
        'balance': balance,
        'date': today_date,
        'class': clas,
        'department': depart,
        # 'admission_no': adm_no,
        'method': method,
        'drawn': drawn
    }

    template_loader = jinja2.FileSystemLoader('./')
    template_env = jinja2.Environment(loader=template_loader)

    template = template_env.get_template('index.html')
    output_text = template.render(context)

    pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
    pdfkit.from_string(output_text, f'C:/Users/HP/Desktop/Output/Receipt/{receipt_no}.pdf')
#
# printreceipt(std_name, receipt_no, amount_in_words, paid, balance, clas, depart, adm_no, method, drawn)
def printmarksheet(stdid,std_name,mothername,emv,python,COA,OS,CNND,GT,BAtch,CGPA,Result,depart):
    today_date = datetime.today().strftime("%d %b, %Y")
    context = {
        'my_name': std_name,
        'mname':mothername,
        'emv': emv,
        'python':python,
        'COA': COA,
        'date': today_date,
        'OS':OS,
        'BAtch':BAtch,
        'CNND':CNND,
        'GT':GT,
        'CGPA':CGPA,
        "Result":Result,
        'department': depart,
        # 'admission_no': adm_no,


    }

    template_loader = jinja2.FileSystemLoader('./')
    template_env = jinja2.Environment(loader=template_loader)

    template = template_env.get_template('result.html')
    output_text = template.render(context)

    pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
    pdfkit.from_string(output_text, f'C:/Users/HP/Desktop/Output/Result/{stdid}.pdf')
printreceipt("Kali","Dev","l1",'3','1','2','4','4','2')