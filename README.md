# 🧾  PDF Parser

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

<img width="289" height="395" alt="image" src="https://github.com/user-attachments/assets/f93b2c9c-9cb3-4b43-afbc-45c48cddf238" />


---

## ⚙️ **Setup Instructions**

### 1️⃣ **Clone or Download the Repository**
```bash
git clone https://github.com/<your-username>/credit-card-pdf-parser.git
cd credit-card-pdf-parser
Create a Virtual Environment
python -m venv venv

3️⃣ Activate the Environment
🪟 Windows
venv\Scripts\activate

🐧 macOS/Linux
source venv/bin/activate

4️⃣ Install Dependencies
pip install -r requirements.txt


▶️ How to Run
Basic Usage:
python parser.py samples/chase_sample.pdf

Example Output:
{
  "issuer": "chase",
  "used_ocr": false,
  "cardholder_name": "John Doe",
  "card_last4": "3117",
  "card_variant": "REWARDS",
  "billing_cycle": "12/03/18 - 01/01/19",
  "payment_due_date": "01/25/2019",
  "new_balance": "1,245.00"
}

🧩 How It Works

Detects issuer – Identifies the bank name by scanning text for keywords (e.g., “Chase,” “HDFC,” “Amex”).

Extracts text – Reads PDFs using pdfplumber; if text is unreadable, switches to OCR via pytesseract.

Applies regex patterns – Extracts specific fields like dates, balances, and card numbers.

Outputs structured JSON – Displays extracted info neatly using the rich library.

<img width="699" height="237" alt="image" src="https://github.com/user-attachments/assets/5f34ce71-fa77-4527-92ac-8f2edec92cdb" />

