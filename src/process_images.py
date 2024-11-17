from pathlib import Path

from PIL import Image

IMAGE_FOLDER = Path(__file__).parents[1] / '_images'
INPUT_FOLDER = IMAGE_FOLDER / 'input'
PROCESSED_FOLDER = IMAGE_FOLDER / 'processed'


def process_image(input_filepath: Path, output_filepath: Path, quality: int = 80):
    print(f'Processing {input_filepath} -> {output_filepath}')
    image = Image.open(input_filepath)
    image = image.convert('RGB')

    # # downsize the image with an ANTIALIAS filter (gives the highest quality)
    # image = image.resize((160,300),Image.ANTIALIAS)
    image.save(output_filepath, optimize=True, quality=quality)


def main():
    section_folders = INPUT_FOLDER.glob('*')

    for section_folder in section_folders:
        processed_section_folder = PROCESSED_FOLDER / section_folder.name
        processed_section_folder.mkdir(exist_ok=True, parents=True)

        image_filepaths = list(section_folder.glob('*'))
        assert len(image_filepaths)

        section_name = section_folder.name[2:]
        print(section_name)
        hero_image_path = image_filepaths[-1]
        detail_image_paths = image_filepaths[:-1]
        assert hero_image_path.name[0] == 'x'

        processed_hero_imagepath = processed_section_folder
        process_image(hero_image_path, processed_hero_imagepath / f'{section_name}_hero.jpg')

        for i, image_filepath in enumerate(detail_image_paths):
            processed_image_filepath = processed_section_folder / f'{section_name}_{i:02d}.jpg'
            process_image(image_filepath, processed_image_filepath)


if __name__ == '__main__':
    main()
