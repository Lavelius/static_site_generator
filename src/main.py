import sys

def remove_directory_contents(directory='public'):
    import os
    import shutil
    directory = os.path.abspath(directory)
    shutil.rmtree(directory, ignore_errors=True)
    


def move_contents_static_to_public(source_dir='static', target_dir='docs'):
    import os
    import shutil
    source_dir = os.path.abspath(source_dir)
    target_dir = os.path.abspath(target_dir)
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    for item in os.listdir(source_dir):
        source_item = os.path.join(source_dir, item)
        target_item = os.path.join(target_dir, item)
        if os.path.isdir(source_item):
            move_contents_static_to_public(source_item, target_item)
        else:
            shutil.copy(source_item, target_item)
    
    

def main():
    basepath = sys.argv[1]
    remove_directory_contents()
    move_contents_static_to_public()
    import generate_page
    generate_page.generate_pages_recursive(
        'content',
        'template.html',
        'docs',
        basepath
        
    )



main()

#fake comit
#another 
#bingoBongo