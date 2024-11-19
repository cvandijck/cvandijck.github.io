from dataclasses import dataclass
from pathlib import Path
from typing import Optional

import jinja2

ROOT_DIR = Path(__file__).parents[1]
TEMPLATES_DIR = ROOT_DIR / 'templates'
INDEX_TEMPLATE_FILENAME = 'index.html.jinja'
INDEX_FILEPATH = ROOT_DIR / 'index.html'

LOREM_IPSUM = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Nobis reprehenderit inventore ut obcaecati minima amet sed, praesentium dolore odit, temporibus quaerat et illo natus! In ullam est a non aspernatur?'

IMAGE_PATH = Path(__file__).parents[1] / 'images'

BANNER = 'https://i.ibb.co/mHKCmw5/banner-hero.jpg'

# INTRO
# ibb reuses the links to already existing images
INTRO_TITLE = 'Welkom in uw nieuwe thuis'
INTRO_CONTENT = [
    'Bent u op zoek naar een gezellige, praktische en instapklare woning? In deze mooi gerenoveerde, energiezuinige gezinswoning geniet u van modern comfort op een toplocatie in de gezelligste stad van Vlaanderen. Gelegen op een rustige eenrichtingsstraat in de zeer gegeerde Stropbuurt, geniet u van alle voordelen van de stad zonder het drukke verkeer. Winkels, scholen, voorzieningen voor sport en ontspanning liggen allemaal op wandel- of fietsafstand. De stad ontsnappen is ook geen probleem. In slechts enkele minuten bent u bij trein, tram of bus, of je rijdt de stad uit via elk van de belangrijke invalswegen. Ook de fiets biedt soelaas via de nabijgelegen fietssnelwegen. Voor natuur hoef je gelukkig niet ver te gaan met zowel het Citadelpark als de Plantentuin slechts een boogscheut verwijderd.',
    'De woning biedt niet alleen energiezuinigheid met een groen EPC-label B, maar ook verrassend veel ruimte. Hoge plafonds in alle slaapkamers, een handige wasruimte en een grote stadstuin met fruitbomen maken dit een zeldzame vondst. De zuidwest georiënteerde tuin biedt veel privacy en vormt een zonnige oase van rust midden in de stad. Kortom, een woning die alle praktische noden en comfort van het stadsleven vervult. Aarzel niet en plan vandaag nog een bezoek – uw toekomstige thuis wacht op u!',
]
INTRO_HERO = 'https://i.ibb.co/Qjxy2mK/tuin-02.jpg'
# INTRO_DETAIL = [
#     'https://i.ibb.co/dMS6M7H/intro-00.jpg',
#     'https://i.ibb.co/YZBT1xG/leefruimte-00.jpg',
#     'https://i.ibb.co/bb93LSB/tuin-00.jpg',
#     'https://i.ibb.co/sqDVv1s/badkamer-wasplaats-01.jpg',
#     'https://i.ibb.co/BTY5rXx/kamers-01.jpg',
# ]
INTRO_DETAIL = None

# LIVING
LIVING_TITLE = 'Leven in de stad – kom binnen in de gezellige leefruimte'
LIVING_CONTENT = [
    'We heten u welkom in de hal. Niet alleen een handige plaats voor jassen, maar vooral een ruimte die voorkomt dat u vanuit de straat rechtstreeks de gezellige leefruimte binnenstapt. Netjes betegeld zodat u zelfs met natte schoenen zonder zorgen kan binnen komen.',
    'Via de tussendeur komt u in de living die niet enkel plaats biedt aan een ruim salon, maar ook aan een extra ruimte die benut kan worden als speelhoek of bureau. Aansluitend vindt u de volledig geïnstalleerde leefkeuken met kwalitatieve toestellen. Met zicht op de tuin kook je hier naar hartenlust terwijl de kinderen spelen of de gasten al van een aperitief genieten.',
]
LIVING_HERO = 'https://i.ibb.co/6R6Ftg1/leefruimte-hero.jpg'
LIVING_DETAIL = [
    'https://i.ibb.co/YZBT1xG/leefruimte-00.jpg',
    'https://i.ibb.co/vxz4vpf/leefruimte-01.jpg',
    'https://i.ibb.co/dsNM2Ps/leefruimte-02.jpg',
    'https://i.ibb.co/938cL2n/leefruimte-03.jpg',
    'https://i.ibb.co/NW0STGL/leefruimte-04.jpg',
    'https://i.ibb.co/0q5NRj6/leefruimte-05.jpg',
    'https://i.ibb.co/HDhJsBS/leefruimte-06.jpg',
]

# ROOMS
ROOMS_TITLE = 'Ruimte en licht – een perfecte combinatie'
ROOMS_CONTENT = [
    'Deze woning verrast met haar ruime, lichte kamers. Als een van de enige huizen in de wijk met een volwaardige bovenverdieping biedt dit huis veel meer ruimte als vergelijkbare panden in de buurt. Mede dankzij deze configuratie en de aanwezige coax- en ethernetaansluitingen kunnen de slaapkamers optimaal benut worden als thuiskantoor of als kinder-, logeer- of hobbykamer en is de woning perfect afgestemd op de noden van een jong gezin.',
    'Alle kamers zijn voorzien van grote ramen die het natuurlijke licht maximaal binnenlaten, waardoor de ruimtes fris en uitnodigend aanvoelen. Een vliegenraam in elke kamer garanderen een ononderbroken slaap!',
]
ROOMS_HERO = 'https://i.ibb.co/Gnpd5bF/kamers-hero.jpg'
ROOMS_DETAIL = [
    'https://i.ibb.co/q1Z4fcr/kamers-00.jpg',
    'https://i.ibb.co/BTY5rXx/kamers-01.jpg',
    'https://i.ibb.co/1rMwjQP/kamers-02.jpg',
    'https://i.ibb.co/vD4TZwm/kamers-03.jpg',
    'https://i.ibb.co/MMLY0XX/kamers-04.jpg',
    'https://i.ibb.co/qrxszP8/kamers-05.jpg',
]

# WASH
WASH_TITLE = 'Kom tot rust in uw douche of ligbad, aan u de keuze'
WASH_CONTENT = [
    'De badkamer is fris en praktisch ingericht, ook in deze ruimte geniet u van veel licht door het grote raam. Naast een douche en ligbad vindt u een ladekast met dubbele lavabo en een spiegelkastje met extra opbergruimte. Naast de badkamer vindt u een apart toilet.',
    'Dankzij de extra wasruimte naast de inkomhal ligt uw leefruimte of badkamer nooit meer vol was – een praktisch voordeel dat u zeker zal waarderen. In deze ruimte plaatst u met gemak een wasmachine, droogkast en een extra koelkast of voorraadkast. De vaste rekken geven u een praktische opbergplaats voor uw huishoudelijke producten.',
]
WASH_HERO = 'https://i.ibb.co/b19BKLZ/badkamer-wasplaats-hero.jpg'
WASH_DETAIL = [
    'https://i.ibb.co/5jYydyx/badkamer-wasplaats-00.jpg',
    'https://i.ibb.co/sqDVv1s/badkamer-wasplaats-01.jpg',
    'https://i.ibb.co/2YVTy48/badkamer-wasplaats-02.jpg',
]


# GARDEN
GARDEN_TITLE = 'Uw eigen stadstuin – zon, privacy en fruit'
GARDEN_CONTENT = [
    'Een ruime, zonnige tuin in hartje Gent? Ja, u leest het goed! Deze zuidwest georiënteerde buitenruimte is een echte parel voor stadsliefhebbers die ook van groen willen genieten. De tuin biedt voldoende ruimte voor een gezellige barbecue, of om simpelweg te relaxen op het zonnige terras.',
    'Daarnaast is er een handig tuinhuisje die dienstdoet als opslagplaats én als werkplek voor de doe-het-zelver. Maar het meest bijzondere zijn de drie prachtige fruitbomen – twee perenbomen en een appelboom – die in de late zomer heerlijke vruchten opleveren. Omringd door groen en met weinig inkijk, geniet u hier in alle rust van een uniek stukje natuur in de stad. Dit is de perfecte plek om te ontsnappen aan de drukte, zonder de stad te verlaten.',
]
GARDEN_HERO = 'https://i.ibb.co/KmvGtF8/tuin-hero.jpg'
GARDEN_DETAIL = [
    'https://i.ibb.co/bb93LSB/tuin-00.jpg',
    'https://i.ibb.co/nBPKnHy/tuin-01.jpg',
    'https://i.ibb.co/Qjxy2mK/tuin-02.jpg',
]

# LOCATION
LOCATION_TITLE = 'Dicht bij alles, snel ver weg'
LOCATION_CONTENT = [
    'Deze woning is gelegen in de populaire Stropbuurt. Op een boogscheut van het Citadelpark, vindt u hier winkels en scholen op wandelafstand. Openbaar vervoer is steeds nabij met belangrijke buslijnen in de naburige straten en het Sint-Pietersstation op slechts 5 minuten fietsen. Ook met de wagen ben je via de grote invalswegen R4, E17 en E40 zo weer uit de stad. Voor ontspanning, cultuur en sport is er voor elk wat wils met verschillende musea, een cinema, zwembad "De Strop", en fitness centra op wandel- en fietsafstand.',
    'De Vlierstaat en omgeving worden binnenkort heraangelegd tot een autoluwe woonerf waarbij er ruimte wordt gemaakt voor de zwakke weggebruiker met o.a. groenzones en zitbanken. Meer informatie kan u terugvinden op de <a class="font-medium text-blue-100 dark:text-blue-500 hover:underline" href="https://stad.gent/nl/plannen-en-projecten/project-vlierstraat-en-omgeving" target="_blank">webpagina</a> van Stad Gent.',
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
    hero_image: Optional[str]
    detail_images: Optional[list[str]]


@dataclass
class PageContent:
    price: str
    mailto: MailTo
    banner: str
    sections: list[SectionContent]
    location: SectionContent
    files: list[File]
    important_files: list[File]


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
        title=INTRO_TITLE,
        content=INTRO_CONTENT,
        hero_image=INTRO_HERO,
        detail_images=INTRO_DETAIL,
    )

    # living_hero, living_detail = _generate_image_links('1_leefruimte')
    living_section = SectionContent(
        id='leefruimte',
        title=LIVING_TITLE,
        content=LIVING_CONTENT,
        hero_image=LIVING_HERO,
        detail_images=LIVING_DETAIL,
    )

    # room_hero, room_detail = _generate_image_links('2_kamers')
    room_section = SectionContent(
        id='kamers',
        title=ROOMS_TITLE,
        content=ROOMS_CONTENT,
        hero_image=ROOMS_HERO,
        detail_images=ROOMS_DETAIL,
    )

    # wash_hero, wash_detail = _generate_image_links('3_badkamer_wasplaats')
    wash_section = SectionContent(
        id='was',
        title=WASH_TITLE,
        content=WASH_CONTENT,
        hero_image=WASH_HERO,
        detail_images=WASH_DETAIL,
    )

    # garden_hero, garden_detail = _generate_image_links('4_tuin')
    garden_section = SectionContent(
        id='tuin',
        title=GARDEN_TITLE,
        content=GARDEN_CONTENT,
        hero_image=GARDEN_HERO,
        detail_images=GARDEN_DETAIL,
    )

    location_section = SectionContent(
        id='location',
        title=LOCATION_TITLE,
        content=LOCATION_CONTENT,
        hero_image=None,
        detail_images=None,
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
        location=location_section,
        files=[
            File('EPC Certificaat', 'files/epc_certificaat.pdf'),
            File('Asbest Attest', 'files/asbest_attest.pdf'),
            File('Bodem Attest', 'files/bodemattest.pdf'),
            File('Stedenbouwkundige Info', 'files/stedenbouw.pdf'),
            File('Kadaster Info', 'files/kadaster.pdf'),
            File('Perceel Plan', 'files/perceelplan.pdf'),
            File('Elektrische Keuring', 'files/elektrische_keuring.jpg'),
        ],
        important_files=[File('Bod Formulier', 'files/perceelplan.pdf')],
    )

    for file in content.files:
        assert (ROOT_DIR / file.path).is_file()

    for file in content.important_files:
        assert (ROOT_DIR / file.path).is_file()

    template_loader = jinja2.FileSystemLoader(searchpath=TEMPLATES_DIR)
    template_env = jinja2.Environment(loader=template_loader, autoescape=True)
    template = template_env.get_template(INDEX_TEMPLATE_FILENAME)
    index_output = template.render(content=content)  # this is where to put args to the template renderer

    INDEX_FILEPATH.write_text(index_output, encoding='utf-8')


if __name__ == '__main__':
    main()
