import fitz

# Create a document object
doc = fitz.open('Scanned_pdf.pdf')  # or fitz.Document(filename)

# Open a text file to save the output with UTF-8 encoding
with open('output.txt', 'w', encoding='utf-8') as f:
    # Extract the number of pages (int)
    page_count = doc.page_count
    f.write(f"Number of pages: {page_count}\n")
    print(page_count)

    # The metadata (dict) e.g., the author, title, etc.
    metadata = doc.metadata
    f.write(f"Metadata: {metadata}\n")
    print(metadata)

    # Get the page by their index
    page = doc.load_page(0)
    # or page = doc[0]

    # Read a Page
    text = page.get_text()
    f.write(f"Text from page 0:\n{text}\n")
    print(text)

    # Render and save the page as an image
    pix = page.get_pixmap()
    pix.save(f"page-{page.number}.png")

    # Get all links on a page
    links = page.get_links()
    f.write(f"Links on page 0: {links}\n")
    print(links)

    # Render and save all the pages as images
    for i in range(doc.page_count):
        page = doc.load_page(i)
        pix = page.get_pixmap()
        pix.save("page-%i.png" % page.number)

    # Get the links on all pages
    for i in range(doc.page_count):
        page = doc.load_page(i)
        links = page.get_links()
        f.write(f"Links on page {i}: {links}\n")
        print(links)
