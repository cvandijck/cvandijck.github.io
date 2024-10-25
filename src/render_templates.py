from dataclasses import dataclass
from pathlib import Path

import jinja2

ROOT_DIR = Path(__file__).parents[1]
TEMPLATES_DIR = ROOT_DIR / 'templates'
INDEX_TEMPLATE_FILENAME = 'index.html.jinja'
INDEX_FILEPATH = ROOT_DIR / 'index.html'


@dataclass
class SectionContent:
    id: str
    title: str
    content: list[str]
    hero_image: str
    detail_images: list[str]


@dataclass
class IndexContent:
    garden: SectionContent


def main():
    garden_section = SectionContent(
        id='tuin',
        title='Aangelegde stadstuin',
        content=[
            'Een zonovergoten stadstuin met ruim tuinhuis voor opslag van tuin- en klusmateriaal. Geniet ook elke zomer van appels en peren van eigen kweek!',
            'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Nobis reprehenderit inventore ut obcaecati minima amet sed, praesentium dolore odit, temporibus quaerat et illo natus! In ullam est a non aspernatur?',
        ],
        hero_image='https://i.ibb.co/jbGc0GN/image-23.png',
        detail_images=[
            'https://i.ibb.co/1ZnWNs7/image-20.png',
        ],
    )

    content = IndexContent(
        garden=garden_section,
    )

    template_loader = jinja2.FileSystemLoader(searchpath=TEMPLATES_DIR)
    template_env = jinja2.Environment(loader=template_loader)
    template = template_env.get_template(INDEX_TEMPLATE_FILENAME)
    index_output = template.render(content=content)  # this is where to put args to the template renderer

    INDEX_FILEPATH.write_text(index_output, encoding='utf-8')


if __name__ == '__main__':
    main()
