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
    sections: list[SectionContent]


def main():
    room_section = SectionContent(
        id='kamers',
        title='Uiterst functionele ruimtes',
        content=[
            'drie volwaardige kamers, aparte ruime wasplaats. Overal kabel en ethernet aansluiting',
            'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Nobis reprehenderit inventore ut obcaecati minima amet sed, praesentium dolore odit, temporibus quaerat et illo natus! In ullam est a non aspernatur?',
        ],
        hero_image='https://i.ibb.co/W2Sbf84/PXL-20241102-153658351.jpg',
        detail_images=[
            'https://i.ibb.co/W2Sbf84/PXL-20241102-153658351.jpg',
            'https://i.ibb.co/9Y3X0BF/PXL-20241102-153755720.jpg',
            'https://i.ibb.co/hgBWFNR/PXL-20241102-152808454-MP.jpg',
            'https://i.ibb.co/KXw6fck/PXL-20241102-144944796-MP.jpg',
        ],
    )
    garden_section = SectionContent(
        id='tuin',
        title='Zonovergoten stadstuin',
        content=[
            'Een zonovergoten stadstuin met ruim tuinhuis voor opslag van tuin- en klusmateriaal. Geniet ook elke zomer van appels en peren van eigen kweek!',
            'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Nobis reprehenderit inventore ut obcaecati minima amet sed, praesentium dolore odit, temporibus quaerat et illo natus! In ullam est a non aspernatur?',
        ],
        hero_image='https://i.ibb.co/jbGc0GN/image-23.png',
        detail_images=[
            'https://i.ibb.co/1ZnWNs7/image-20.png',
            'https://i.ibb.co/Mc0LBR2/image-21.png',
        ],
    )

    content = IndexContent(
        sections=[room_section, garden_section],
    )

    template_loader = jinja2.FileSystemLoader(searchpath=TEMPLATES_DIR)
    template_env = jinja2.Environment(loader=template_loader, autoescape=True)
    template = template_env.get_template(INDEX_TEMPLATE_FILENAME)
    index_output = template.render(content=content)  # this is where to put args to the template renderer

    INDEX_FILEPATH.write_text(index_output, encoding='utf-8')


if __name__ == '__main__':
    main()
