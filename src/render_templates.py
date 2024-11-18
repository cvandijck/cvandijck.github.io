from dataclasses import dataclass
from pathlib import Path

import jinja2

ROOT_DIR = Path(__file__).parents[1]
TEMPLATES_DIR = ROOT_DIR / 'templates'
INDEX_TEMPLATE_FILENAME = 'index.html.jinja'
INDEX_FILEPATH = ROOT_DIR / 'index.html'

LOREM_IPSUM = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Nobis reprehenderit inventore ut obcaecati minima amet sed, praesentium dolore odit, temporibus quaerat et illo natus! In ullam est a non aspernatur?'

IMAGE_PATH = Path(__file__).parents[1] / 'images'

BANNER = 'https://i.ibb.co/mHKCmw5/banner-hero.jpg'
LIGGING_HERO = 'https://i.ibb.co/gMLnfG3/ligging-hero.jpg'
GARDEN_DETAIL = [
    'https://i.ibb.co/bb93LSB/tuin-00.jpg',
    'https://i.ibb.co/nBPKnHy/tuin-01.jpg',
    'https://i.ibb.co/Qjxy2mK/tuin-02.jpg',
]

GARDEN_HERO = 'https://i.ibb.co/KmvGtF8/tuin-hero.jpg'

WASH_DETAIL = [
    'https://i.ibb.co/5jYydyx/badkamer-wasplaats-00.jpg',
    'https://i.ibb.co/sqDVv1s/badkamer-wasplaats-01.jpg',
    'https://i.ibb.co/2YVTy48/badkamer-wasplaats-02.jpg',
]

WASH_HERO = 'https://i.ibb.co/b19BKLZ/badkamer-wasplaats-hero.jpg'

ROOMS_DETAIL = [
    'https://i.ibb.co/q1Z4fcr/kamers-00.jpg',
    'https://i.ibb.co/BTY5rXx/kamers-01.jpg',
    'https://i.ibb.co/1rMwjQP/kamers-02.jpg',
    'https://i.ibb.co/vD4TZwm/kamers-03.jpg',
    'https://i.ibb.co/MMLY0XX/kamers-04.jpg',
    'https://i.ibb.co/qrxszP8/kamers-05.jpg',
]
ROOMS_HERO = 'https://i.ibb.co/Gnpd5bF/kamers-hero.jpg'

LIVING_DETAIL = [
    'https://i.ibb.co/YZBT1xG/leefruimte-00.jpg',
    'https://i.ibb.co/vxz4vpf/leefruimte-01.jpg',
    'https://i.ibb.co/dsNM2Ps/leefruimte-02.jpg',
    'https://i.ibb.co/938cL2n/leefruimte-03.jpg',
    'https://i.ibb.co/NW0STGL/leefruimte-04.jpg',
    'https://i.ibb.co/0q5NRj6/leefruimte-05.jpg',
    'https://i.ibb.co/HDhJsBS/leefruimte-06.jpg',
]
LIVING_HERO = 'https://i.ibb.co/6R6Ftg1/leefruimte-hero.jpg'

# ibb reuses the links to already existing images
INTRO_HERO = 'https://i.ibb.co/Qjxy2mK/tuin-02.jpg'
INTRO_DETAIL = [
    'https://i.ibb.co/YZBT1xG/leefruimte-00.jpg',
    'https://i.ibb.co/dMS6M7H/intro-00.jpg',
    'https://i.ibb.co/bb93LSB/tuin-00.jpg',
    'https://i.ibb.co/sqDVv1s/badkamer-wasplaats-01.jpg',
    'https://i.ibb.co/BTY5rXx/kamers-01.jpg',
]

MAILTO_RECEIVER = 'vlierstraat26@outlook.com'
MAILTO_SUBJECT = 'Afspraak bezichtiging Vlierstraat 26 op zaterdag 30 november'

MAILTO_BODY = """
Beste,

Ik heb interesse in uw woning en zou graag een bezichtiging inboeken op de kijkdag op 30 november.

Mijn voorkeur gaat uit naar:

U kan me contacteren op:
"""


def _format_mailto(s: str) -> str:
    s = s.strip('\n')
    s = s.replace(' ', '%20')
    s = s.replace('\n', '%0D%0A')
    return s


@dataclass
class MailTo:
    receiver: str
    subject: str
    body: str


@dataclass
class File:
    label: str
    path: str


@dataclass
class SectionContent:
    id: str
    title: str
    content: list[str]
    hero_image: str
    detail_images: list[str]


@dataclass
class PageContent:
    price: str
    mailto: MailTo
    banner: str
    sections: list[SectionContent]
    files: list[File]


def _generate_image_links(section: str) -> tuple[str, tuple[str, ...]]:
    image_folder = IMAGE_PATH / section
    images = [f.relative_to(ROOT_DIR) for f in image_folder.glob('*')]

    detail_images = [f.as_posix() for f in images[:-1]]
    hero_image = images[-1].as_posix()
    return hero_image, detail_images


def main():
    # intro_hero, intro_detail = _generate_image_links('0_intro')
    intro_section = SectionContent(
        id='intro',
        title='Maak kennis met deze prachtige gezinswoning',
        content=[LOREM_IPSUM, LOREM_IPSUM],
        hero_image=INTRO_HERO,
        detail_images=INTRO_DETAIL,
    )

    # living_hero, living_detail = _generate_image_links('1_leefruimte')
    living_section = SectionContent(
        id='leefruimte',
        title='Gezellige leefruimte',
        content=[LOREM_IPSUM, LOREM_IPSUM],
        hero_image=LIVING_HERO,
        detail_images=LIVING_DETAIL,
    )

    # room_hero, room_detail = _generate_image_links('2_kamers')
    room_section = SectionContent(
        id='kamers',
        title='Uiterst functionele ruimtes',
        content=[
            'drie volwaardige kamers, aparte ruime wasplaats. Overal kabel en ethernet aansluiting',
            LOREM_IPSUM,
        ],
        hero_image=ROOMS_HERO,
        detail_images=ROOMS_DETAIL,
    )

    # wash_hero, wash_detail = _generate_image_links('3_badkamer_wasplaats')
    wash_section = SectionContent(
        id='was',
        title='Uitgeruste badkamer en aparte wasplaats',
        content=[LOREM_IPSUM, LOREM_IPSUM],
        hero_image=WASH_HERO,
        detail_images=WASH_DETAIL,
    )

    # garden_hero, garden_detail = _generate_image_links('4_tuin')
    garden_section = SectionContent(
        id='tuin',
        title='Zonovergoten stadstuin',
        content=[
            'Een zonovergoten stadstuin met ruim tuinhuis voor opslag van tuin- en klusmateriaal. Geniet ook elke zomer van appels en peren van eigen kweek!',
            'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Nobis reprehenderit inventore ut obcaecati minima amet sed, praesentium dolore odit, temporibus quaerat et illo natus! In ullam est a non aspernatur?',
        ],
        hero_image=GARDEN_HERO,
        detail_images=GARDEN_DETAIL,
    )

    mailto = MailTo(
        receiver=MAILTO_RECEIVER,
        subject=_format_mailto(MAILTO_SUBJECT),
        body=_format_mailto(MAILTO_BODY),
    )
    # banner_image = IMAGE_PATH / 'x_banner' / 'banner_hero.jpg'
    # banner_image = banner_image.relative_to(ROOT_DIR).as_posix()
    banner = BANNER
    content = PageContent(
        price='€475.000',
        mailto=mailto,
        banner=banner,
        sections=[
            intro_section,
            living_section,
            room_section,
            wash_section,
            garden_section,
        ],
        files=[
            File('EPC Certificaat', 'files/epc_certificaat.pdf'),
            File('Asbest Attest', 'files/asbest_attest.pdf'),
        ],
    )

    template_loader = jinja2.FileSystemLoader(searchpath=TEMPLATES_DIR)
    template_env = jinja2.Environment(loader=template_loader, autoescape=True)
    template = template_env.get_template(INDEX_TEMPLATE_FILENAME)
    index_output = template.render(content=content)  # this is where to put args to the template renderer

    INDEX_FILEPATH.write_text(index_output, encoding='utf-8')


if __name__ == '__main__':
    main()
