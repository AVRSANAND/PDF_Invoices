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

    # for index,item in df.iterrows():
    #     print(item["product_id"])
    #     print(item["product_name"])
    #     print(item["price_per_unit"])
    #     print(item["total_price"])

    Doc_Name = Path(filepath).stem
    Invoice_No, Date = Doc_Name.split("-")

    pdf = FPDF(orientation="P",unit="mm",format="A4")
    pdf.add_page()
    pdf.set_font(family="Times",size=16,style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice no. {Invoice_No} ",ln=1 )
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Date {Date} ", ln=1)
    # for index, item in df.iterrows():
    #     pdf.set_font(family="Times", size=12)
    #     pdf.multi_cell(w=200, h=8, txt=f"{item['product_id']} | {item['product_name']} | {item['price_per_unit']} | {item['total_price']}")
    pdf.output(f"PDFs/{Doc_Name}.pdf")