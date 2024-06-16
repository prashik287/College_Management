def setsec(cb1):
        sec = cb1.get()
        if sec == "Admission":
            return "AD"
        elif sec == "Fee":
            return "FE"
        elif sec == "Exam":
            return "EX"
        elif sec == "Library":
            return "LIB"
        elif sec == "Faculty":
            return "FAC"
        elif sec == "Admin":
            return "ADM"