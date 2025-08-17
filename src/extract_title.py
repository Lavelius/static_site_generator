def extract_title(markdown):
    split_markdown = markdown.split('\n')
    for line in split_markdown:
        if line.startswith('#') and line[1] != '#':
            return line.lstrip('#').strip()
    