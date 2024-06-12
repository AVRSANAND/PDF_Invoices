import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path


filepaths = glob.glob("Invoices/*.xlsx")

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    print(df)

    # Predefined filepath

    # Doc_Name = filepath.strip(f"'Invoices\\'")
    # print(Doc_Name)
    # Invoice_No = Doc_Name[0:5]
    # print(Invoice_No)
    # Date = Doc_Name[6:15]
    # print(Date)

    Doc_Name = Path(filepath).stem
    Invoice_No = Doc_Name.split("-")[0]
    Date = Doc_Name.split("-")[1]

    pdf = FPDF(orientation="P",unit="mm",format="A4")
    pdf.add_page()
    pdf.set_font(family="Times",size=16,style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice nr. {Invoice_No} ",ln=1 )
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Date {Date} ", ln=1)

    pdf.output(f"PDFs/{Doc_Name}.pdf")