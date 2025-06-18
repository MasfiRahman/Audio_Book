import pyttsx3
from PyPDF2 import PdfReader

# PDF ফাইল ওপেন করো
book = open('oop.pdf', 'rb')
pdfReader = PdfReader(book)

# মোট পেজ সংখ্যা বের করো
pages = len(pdfReader.pages)
print(f"Total pages: {pages}")

# pyttsx3 voice engine initialize করো
friend = pyttsx3.init()

# ৭ নাম্বার পেজ থেকে শুরু করে শেষ পর্যন্ত পড়ে শোনাও
for num in range(7, pages):
    page = pdfReader.pages[num]
    text = page.extract_text()  # note: this might return None
    if text:  # যদি কিছু টেক্সট পাওয়া যায়
        friend.say(text)
        friend.runAndWait()
    else:
        print(f"No text found on page {num}")
