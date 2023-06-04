import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")

print(filepaths)

for file in filepaths:
    df = pd.read_excel(file, sheet_name="Sheet 1")

    filename = Path(file).stem
    invoice_nr = filename.split("-")[0]
    filedate = filename.split("-")[1]

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice nr.{invoice_nr}", ln=1)

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Date{filedate}")

    pdf.output(f"PDFs/{filename}.pdf")
