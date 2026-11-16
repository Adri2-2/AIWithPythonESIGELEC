"""Lab 5: range les photos de lab05/captures/ dans des sous-dossiers A, B, C...
Les 5 premières images (ordre chronologique) vont dans A, les 5 suivantes dans B, etc.
Run: python lab05/scripts/sort_captures_by_letter.py [--source lab05/captures] [--per-letter 5] [--dry-run]
"""
import argparse
import shutil
import string
from pathlib import Path

IMAGE_EXTS = {'.jpg', '.jpeg', '.png', '.bmp', '.webp'}


def main():
    parser = argparse.ArgumentParser(description='Déplace les captures dans des dossiers A, B, C...')
    parser.add_argument('--source', default='lab05/captures', help='Dossier contenant les images')
    parser.add_argument('--dest', default=None, help='Dossier où créer A, B, C... (défaut: --source)')
    parser.add_argument('--per-letter', type=int, default=5, help='Nombre d\'images par lettre')
    parser.add_argument('--dry-run', action='store_true', help='Affiche les déplacements sans les faire')
    args = parser.parse_args()

    source = Path(args.source)
    dest = Path(args.dest) if args.dest else source
    if not source.is_dir():
        raise SystemExit(f'Dossier introuvable : {source}')

    # Les noms sont horodatés (frame_YYYYMMDD_HHMMSS_us.jpg) : tri alphabétique = ordre de capture.
    images = sorted(p for p in source.iterdir() if p.is_file() and p.suffix.lower() in IMAGE_EXTS)
    if not images:
        print(f'Aucune image dans {source}')
        return

    letters = string.ascii_uppercase
    max_images = len(letters) * args.per_letter
    if len(images) > max_images:
        print(f'Attention : {len(images)} images, seules les {max_images} premières seront rangées (A-Z).')
        images = images[:max_images]
    if len(images) % args.per_letter:
        print(f'Attention : {len(images)} images, la dernière lettre aura moins de {args.per_letter} photos.')

    for i, img in enumerate(images):
        letter = letters[i // args.per_letter]
        target_dir = dest / letter
        target = target_dir / img.name
        print(f'{img.name} -> {letter}/')
        if not args.dry_run:
            target_dir.mkdir(parents=True, exist_ok=True)
            shutil.move(str(img), str(target))

    used = (len(images) - 1) // args.per_letter + 1
    print(f'{len(images)} image(s) {"à ranger" if args.dry_run else "rangée(s)"} dans A-{letters[used - 1]}')


if __name__ == '__main__':
    main()
