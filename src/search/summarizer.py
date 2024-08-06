from abc import  ABC, abstractmethod
import os
import textract
from pptx import Presentation
import PyPDF2
import docx
import pandas as pd
from transformers import pipeline
import xlrd
import win32com.client

class BaseSummarizer(ABC):
    def __init__(self, type="txt"):
        self.type = type

    @abstractmethod
    def summarize(self):
        raise NotImplemented("Must implement this")




# Initialize the summarizer pipeline
summarizer = pipeline("summarization")


def describe_file(file_path):
    _, ext = os.path.splitext(file_path)

    if ext.lower() == '.txt':
        return describe_txt(file_path)
    elif ext.lower() == '.docx':
        return describe_docx(file_path)
    elif ext.lower() == '.doc':
        return describe_doc(file_path)
    elif ext.lower() == '.xlsx':
        return describe_xlsx(file_path)
    elif ext.lower() == '.xls':
        return describe_xls(file_path)
    elif ext.lower() == '.pptx':
        return describe_pptx(file_path)
    elif ext.lower() == '.ppt':
        return describe_ppt(file_path)
    elif ext.lower() == '.pdf':
        return describe_pdf(file_path)
    else:
        return "Unsupported file type"


def summarize_text(text):
    # Split text into chunks if too long
    max_chunk_size = 1024
    text_chunks = [text[i:i + max_chunk_size] for i in range(0, len(text), max_chunk_size)]
    summaries = []
    for chunk in text_chunks:
        summary = summarizer(chunk, max_length=150, min_length=30, do_sample=False)[0]['summary_text']
        summaries.append(summary)
    return " ".join(summaries)


def describe_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    summary = summarize_text(content)
    return f"TXT File Summary:\n{summary}"


def describe_docx(file_path):
    doc = docx.Document(file_path)
    content = '\n'.join([para.text for para in doc.paragraphs])
    summary = summarize_text(content)
    return f"DOCX File Summary:\n{summary}"


def describe_doc(file_path):
    word = win32com.client.Dispatch("Word.Application")
    word.Visible = False
    doc = word.Documents.Open(file_path)
    content = doc.Content.Text
    doc.Close()
    word.Quit()
    summary = summarize_text(content)
    return f"DOC File Summary:\n{summary}"


def describe_xlsx(file_path):
    xls = pd.ExcelFile(file_path)
    sheet_descriptions = []
    for sheet_name in xls.sheet_names:
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        sheet_descriptions.append(f"Sheet: {sheet_name}\n{df.head().to_string(index=False)}\n")
    combined_sheets = "\n".join(sheet_descriptions)
    summary = summarize_text(combined_sheets)
    return f"XLSX File Summary:\n{summary}"


def describe_xls(file_path):
    xls = xlrd.open_workbook(file_path)
    sheet_descriptions = []
    for sheet_name in xls.sheet_names():
        sheet = xls.sheet_by_name(sheet_name)
        rows = [sheet.row_values(rownum) for rownum in range(min(sheet.nrows, 5))]  # Limit to first 5 rows
        df = pd.DataFrame(rows)
        sheet_descriptions.append(f"Sheet: {sheet_name}\n{df.to_string(index=False)}\n")
    combined_sheets = "\n".join(sheet_descriptions)
    summary = summarize_text(combined_sheets)
    return f"XLS File Summary:\n{summary}"


def describe_pptx(file_path):
    prs = Presentation(file_path)
    slides_content = []
    for slide in prs.slides:
        slide_text = []
        for shape in slide.shapes:
            if hasattr(shape, "text"):
                slide_text.append(shape.text)
        slides_content.append("\n".join(slide_text))
    combined_slides = "\n".join(slides_content)
    summary = summarize_text(combined_slides)
    return f"PPTX File Summary:\n{summary}"


def describe_ppt(file_path):
    powerpoint = win32com.client.Dispatch("PowerPoint.Application")
    powerpoint.Visible = False
    presentation = powerpoint.Presentations.Open(file_path, WithWindow=False)
    slides_content = []
    for slide in presentation.Slides:
        slide_text = []
        for shape in slide.Shapes:
            if hasattr(shape, "TextFrame") and shape.TextFrame.HasText:
                slide_text.append(shape.TextFrame.TextRange.Text)
        slides_content.append("\n".join(slide_text))
    presentation.Close()
    powerpoint.Quit()
    combined_slides = "\n".join(slides_content)
    summary = summarize_text(combined_slides)
    return f"PPT File Summary:\n{summary}"


def describe_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        content = []
        for page in reader.pages:
            content.append(page.extract_text())
    combined_content = "\n".join(content)
    summary = summarize_text(combined_content)
    return f"PDF File Summary:\n{summary}"


# Example usage
file_path = 'example.doc'  # Change this to the path of your file
description = describe_file(file_path)
print(description)
