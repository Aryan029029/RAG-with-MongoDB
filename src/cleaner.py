def clean_pages(pages, min_words=20):
    """
    Remove pages that contain fewer than `min_words` words.

    Args:
        pages: List of LangChain Document objects.
        min_words: Minimum number of words required to keep a page.

    Returns:
        List of cleaned pages.
    """

    cleaned_pages = []

    for page in pages:

        word_count = len(page.page_content.split())

        if word_count > min_words:
            cleaned_pages.append(page)

    return cleaned_pages