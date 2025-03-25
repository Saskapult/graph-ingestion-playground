from pypdf import PdfReader
from kg_gen import KGGen, Graph


def get_pdf_pages_text(path):
	reader = PdfReader(path)
	return [page.extract_text() for page in reader.pages]


# Makes windows for chunk ingestion
def make_pdf_chunks(pages_text, expand_chars=50):
	chunks = []
	for i, page_text in enumerate(pages_text):
		chunk = page_text
		if (i-1) >= 0:
			chunk = pages_text[i-1][max(len(pages_text[i-1])-expand_chars, 0):] + chunk
		if (i+1) < len(pages_text):
			chunk = chunk + pages_text[i+1][:expand_chars]
		chunks.append(chunk)
	return chunks


# # Ingest text until a character target is passed 
# # Returns chunks along with the page numbers they draw from
# def make_smarter_chunks(pages_text, chunk_min=5000, overlap=100):
# 	# full_text = "".join(pages_text)

# 	chunks = []
# 	page_i = 0
# 	page_j = 0
# 	chunk = ""
# 	refs = []
# 	while page_i < len(pages_text):
# 		page = pages_text[page_i]
# 		# If remaining text fits in the chunk
# 		if (len(page) - page_j) < 
	


# 	pass
