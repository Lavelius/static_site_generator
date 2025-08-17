import extract_title
import markdown_to_html_node

def generate_page(from_path, template_path, dest_path):
    import os
    print(f'Generating page from {from_path} using template {template_path} to {dest_path}')

    if not os.path.exists(from_path):
        raise FileNotFoundError(f'Input file {from_path} does not exist.')
    if not os.path.exists(template_path):
        raise FileNotFoundError(f'Template file {template_path} does not exist.')

    from_path = os.path.abspath(from_path)
    template_path = os.path.abspath(template_path)
    dest_path = os.path.abspath(dest_path)
    with open(from_path, 'r') as from_file:
        content = from_file.read()
        from_file.close()

    with open(template_path, 'r') as template_file:
        template = template_file.read()
        template_file.close()

    
    html_node = markdown_to_html_node.markdown_to_html_node(content)
    html_content = html_node.to_html()


    title = extract_title.extract_title(content)

    template = template.replace('{{ Content }}', html_content)
    template = template.replace('{{ Title }}', title if title else 'Untitled Page')

    if not os.path.exists(os.path.dirname(dest_path)):
        os.makedirs(os.path.dirname(dest_path))
    print(f'Writing to {dest_path}')
    with open(dest_path, 'w') as dest_file:
        dest_file.write(template)
        dest_file.close()
    print(f'Page generated at {dest_path}')

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    import os
    dir_path_content = os.path.abspath(dir_path_content)
    template_path = os.path.abspath(template_path)
    dest_dir_path = os.path.abspath(dest_dir_path)

    if not os.path.exists(dest_dir_path):
        os.makedirs(dest_dir_path, exist_ok=True)

    dir = os.listdir(dir_path_content)
    for item in dir:
        print(f'Processing item: {item}')
        if item.startswith('.'):
            print(f'Skipping hidden item: {item}')
            continue
        if os.path.isfile(os.path.join(dir_path_content,item)):
            if item.endswith('.md'):
                dest_file_path = os.path.join(dest_dir_path, item.replace('.md', '.html'))
                print(f'Generating page for {item} to {dest_file_path}')
                generate_page(os.path.join(dir_path_content, item), template_path, dest_file_path)
        elif os.path.isdir(os.path.join(dir_path_content,item)):
            print(f'Entering directory: {item}')
            if item.startswith('.'):
                print(f'Skipping hidden directory: {item}')
                continue
            generate_pages_recursive(
                os.path.join(dir_path_content, item),
                template_path,
                os.path.join(dest_dir_path, item)
            )
