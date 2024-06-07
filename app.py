import regex as re
from bs4 import BeautifulSoup
from fastapi import FastAPI, UploadFile

app = FastAPI()

elements_to_remove = [
    ({"name": "footer"}, True),
    ({"class_": re.compile(".*footer*")}, True),
    ({"name": "nav"}, False),
    ({"name": "div", "class_": re.compile(".*menu.*")}, False),
    ({"name": "header"}, False),
    ({"name": "div", "class_": re.compile(".*header.*")}, False),
    ({"name": "div", "class_": re.compile(".*alert.*")}, False),
    ({"name": "div", "class_": re.compile(".*meta.*")}, False),
    ({"name": "div", "class_": re.compile(".*side.*bar.*")}, False),
    ({"name": "form"}, False),
    ({"name": "table"}, False),
    ({"name": "div", "class_": re.compile(".*modal.*")}, False),
]


@app.post("/parse")
async def parse_html_file(file: UploadFile) -> str:
    """Parse HTML in a text file and return it's content in a human-readable way"""
    page = await file.read()

    soup = BeautifulSoup(page, "html.parser")
    remove_elements(soup, elements_to_remove)

    content = []
    for element in soup.select("p, code"):
        if element.find("img") is None and element.parent.name not in ["figcaption"]:
            text = element.text.strip()
            if text:
                content.append(text)

    content = re.sub("[\s\u3164]+", " ", " ".join(content)).strip()
    content = " ".join(content.split()[:200])

    return content


def remove_elements(page: BeautifulSoup, elements: list[tuple]):
    for kwargs, remove_siblings in elements:
        for element in page.find_all(**kwargs):
            if remove_siblings:
                for sibling in element.find_all_next():
                    sibling.decompose()
            element.decompose()
