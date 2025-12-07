import sys
import os
from textnode import TextNode, TextType
from util import *
from markdown_blocks import *

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r", encoding="utf-8") as f:
        markdown_ = f.read()
    
    with open(template_path, "r", encoding="utf-8") as f:
        template_ = f.read()

    html_node = markdown_to_html_node(markdown_)
    html_content = html_node.to_html()

    title = extract_title(markdown_)

    final_html = template_.replace("{{ Title }}", title).replace("{{ Content }}", html_content)
    
    # Replace href="/ and src="/ with basepath
    final_html = final_html.replace('href="/', f'href="{basepath}')
    final_html = final_html.replace('src="/', f'src="{basepath}')

    # Ensure destination directory exists
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    # Write output
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(final_html)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    with os.scandir(dir_path_content) as entries:
        for entry in entries:
            #print(entry.name)
            if entry.is_file() and entry.name.endswith(".md"):
                #print(type(dir_path_content), dir_path_content)
                #print(type(dir_path_content), dest_dir_path)
                file_n = entry.name.replace(".md", ".html")
                generate_page(os.path.join(dir_path_content, entry.name), template_path, os.path.join(dest_dir_path, file_n), basepath)
            elif entry.is_dir():
                generate_pages_recursive(os.path.join(dir_path_content, entry.name), template_path, os.path.join(dest_dir_path, entry.name), basepath)



def main():
    # Get basepath from CLI argument, default to "/"
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Get the parent directory (project root)
    project_root = os.path.dirname(script_dir)
    
    # Build paths relative to project root
    static_dir = os.path.join(project_root, "static")
    content_dir = os.path.join(project_root, "content")
    template_path = os.path.join(project_root, "template.html")
    docs_dir = os.path.join(project_root, "docs")
    
    clear_directory(docs_dir)
    copy_recursive(static_dir, docs_dir)
    generate_pages_recursive(content_dir, template_path, docs_dir, basepath)
    """
    clear_directory("../public")
    copy_recursive("../static", "../public")
    generate_pages_recursive("../content", "template.html", "../public")

    clear_directory("public")
    copy_recursive("static", "public")

    generate_page("content/index.md", "template.html", "public/index.html")
    generate_page("content/blog/glorfindel/index.md", "template.html", "public/blog/glorfindel/index.html")
    generate_page("content/blog/tom/index.md", "template.html", "public/blog/tom/index.html")
    generate_page("content/blog/majesty/index.md", "template.html", "public/blog/majesty/index.html")
    generate_page("content/contact/index.md", "template.html", "public/contact/index.html")
    """


main()
