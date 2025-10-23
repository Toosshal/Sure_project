# 🧾 Credit Card PDF Parser

A lightweight Python tool to **extract key information** from credit card statements across **multiple issuers** — automatically detecting the bank, reading real-world PDFs, and extracting structured data like due dates, balances, and billing cycles.

---

## 🎯 **Objective**

To build a unified PDF parser that extracts **5 key data points** from credit card statements of **five major issuers**:

- ✅ Chase  
- ✅ HDFC Bank  
- ✅ SBI (State Bank of India)  
- ✅ Citibank  
- ✅ American Express  

---

## 🧠 **Features**

- 🔍 **Automatic issuer detection** (via text analysis)
- 📄 **PDF text extraction** using `pdfplumber`
- 🧾 **OCR fallback** for scanned statements using `pytesseract`
- 💡 **Regex-based data extraction**
- 💻 **Clean JSON output** (pretty printed with `rich`)
- ⚙️ **Modular structure** — easy to add new banks

pdf_pro/
│
├── parser.py
├── extractors/
│ ├── init.py
│ ├── chase_extractor.py
│ ├── amex_extractor.py
│ ├── citi_extractor.py
│ ├── hdfc_extractor.py
│ └── sbi_extractor.py
│
├── utils/
│ ├── init.py
│ └── pdf_utils.py
│
├── samples/
│ └── chase_sample.pdf
│
├── requirements.txt
└── README.md

