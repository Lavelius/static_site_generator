def generate_page(from_path, template_path, dest_path):
    import os
    print(f'Generating page from {from_path} using template {template_path} to {dest_path}')
    content = os.read(from_path)
    template = os.read(template_path)
