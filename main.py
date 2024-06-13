import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path


filepaths = glob.glob("Invoices/*.xlsx")

for filepath in filepaths:

    # Filepaths without pathlib

    # Doc_Name = filepath.strip(f"'Invoices\\'")
    # print(Doc_Name)
    # Invoice_No = Doc_Name[0:5]
    # print(Invoice_No)
    # Date = Doc_Name[6:15]
    # print(Date)

    Doc_Name = Path(filepath).stem
    Invoice_No, Date = Doc_Name.split("-")

    pdf = FPDF(orientation="P",unit="mm",format="A4")
    pdf.add_page()

    pdf.set_font(family="Times",size=16,style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice no. {Invoice_No} ",ln=1 )

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Date {Date} ", ln=1)

    df = pd.read_excel(filepath, sheet_name="Sheet 1")

    # Header
    headers = list(df.columns)
    headers = [item.replace("_", " ").title() for item in headers]
    pdf.set_font(family="Times", size=10, style="B")
    pdf.set_text_color(80,80,80)

    pdf.cell(w=30, h=8, txt=headers[0], border=1)
    pdf.cell(w=70, h=8, txt=headers[1], border=1)
    pdf.cell(w=35, h=8, txt=headers[2], border=1)
    pdf.cell(w=30, h=8, txt=headers[3], border=1)
    pdf.cell(w=30, h=8, txt=headers[4], border=1, ln=1)

    # Values
    for index, item in df.iterrows():
        pdf.set_font(family="Times", size=10)
        pdf.set_text_color(80,80,80)
        pdf.cell(w=30, h=8, txt=f"{item['product_id']}",border=1)
        pdf.cell(w=70, h=8, txt=f"{item['product_name']}",border=1)
        pdf.cell(w=35, h=8, txt=f"{item['amount_purchased']}",border=1)
        pdf.cell(w=30, h=8, txt=f"{item['price_per_unit']}",border=1)
        pdf.cell(w=30, h=8, txt=f"{item['total_price']}",border=1, ln=1)

    pdf.output(f"PDFs/{Doc_Name}.pdf")