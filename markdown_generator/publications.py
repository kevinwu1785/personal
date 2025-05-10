import pandas as pd
import os

# 讀入資料
publications = pd.read_csv("publications.tsv", sep="\t", header=0)

# HTML escape function
html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;"
}
def html_escape(text):
    return "".join(html_escape_table.get(c, c) for c in text)

# 產出 markdown 檔案
for row, item in publications.iterrows():
    
    md_filename = str(item.pub_date) + "-" + item.url_slug + ".md"
    html_filename = str(item.pub_date) + "-" + item.url_slug
    year = item.pub_date[:4]
    
    # YAML metadata
    md = "---\ntitle: \"" + item.title + '"\n'
    md += "collection: publications"
    md += "\npermalink: /publication/" + html_filename

    if len(str(item.excerpt)) > 5:
        md += "\nexcerpt: '" + html_escape(item.excerpt) + "'"

    md += "\ndate: " + str(item.pub_date)

    # **移除這行以隱藏 Published in**
    # md += "\nvenue: '" + html_escape(item.venue) + "'"

    if len(str(item.paper_url)) > 5:
        md += "\npaperurl: '" + item.paper_url + "'"

    md += "\ncitation: '" + html_escape(item.citation) + "'"
    md += "\n---"

    # Markdown description
    if len(str(item.paper_url)) > 5:
        md += "\n\n<a href='" + item.paper_url + "'>Download paper here</a>\n"
    
    if len(str(item.excerpt)) > 5:
        md += "\n" + html_escape(item.excerpt) + "\n"
        
    md += "\nRecommended citation: " + item.citation

    md_filename = os.path.basename(md_filename)
    with open("../_publications/" + md_filename, 'w') as f:
        f.write(md)



