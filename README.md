# Invoice to PDF Converter

This project reads invoice data from Excel files and generates corresponding PDFs with a summary of total cost/expenditure. The input Excel files are stored in the `Invoices` folder, and the generated PDFs are saved in the `PDFs` folder.

## Features

- Reads invoice data from Excel files.
- Generates PDF invoices with detailed information and total cost.
- Organizes PDFs into a specified folder.

## Requirements

- pandas
- fpdf
- glob
- pathlib

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/AVRSANAND/PDF_Invoices.git
    cd PDF_Invoices
    ```

2. Install the required Python packages:
    ```sh
    pip install pandas fpdf
    ```

## Usage

1. Place your invoice Excel files in the `Invoices` folder. The filenames should follow the format `10001-2024.06.13.xlsx` where Inovice No. and Date are seperated by '-'.

2. Run the script:
    ```sh
    python main.py
    ```

3. The PDFs will be generated and saved in the `PDFs` folder with the same name as the corresponding Excel file.

## Folder Structure

```
invoice-to-pdf-converter/
├── Invoices/
│   ├── 10001-2024.06.13.xlsx
│   ├── ...
├── PDFs/
│   ├── 10001-2024.06.13.pdf
│   ├── ...
├── main.py
└── README.md
```

## Script Explanation

The script reads each Excel file from the `Invoices` folder and creates a PDF for each invoice. Each PDF includes:

- Invoice number and date.
- A table with product details (product ID, name, amount purchased, price per unit, and total price).
- A summary of the total cost.
