#!/usr/bin/python
import sys
import json


def int_checker(value):
    try:
        return int(value)
    except:
        return ""


def float_checker(value):
    try:
        return float(value)
    except:
        return ""


reader = sys.stdin
next(reader)

for line in reader:
    line = line.replace("\\,", ".")
    row_parts = line.strip().split(",")

    if len(row_parts) == 5:
        temp_dict = {"orgno": int_checker(row_parts[0]), "company_name": row_parts[1], "phone_number": row_parts[2],
                     "sni_code": int_checker(row_parts[3]), "sni_text": row_parts[4]}
        print(row_parts[0] + "||" + json.dumps(temp_dict))
    else:
        temp_dict = {"date_from": row_parts[2], "date_to": row_parts[3], "profit_margin_percent": float_checker(row_parts[4]),
                     "net_operating_income": int_checker(row_parts[5])}
        print(row_parts[1] + "||" + json.dumps(temp_dict))

