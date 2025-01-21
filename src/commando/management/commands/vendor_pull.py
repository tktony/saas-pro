import helpers
from pathlib import Path
from typing import Any
from django.conf import settings
from django.core.management.base import BaseCommand

# Directory where vendor static files are stored
STATICFILES_VENDOR_DIR = getattr(settings, 'STATICFILES_VENDOR_DIR')

# URLs to download vendor files
VENDOR_STATICFILES = {
    "flowbite.min.css": "https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.css",
    "flowbite.min.js": "https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.js",
}

def remove_source_mapping_urls(directory: Path):
    """
    Removes sourceMappingURL references from all `.js` files in the specified directory.
    """
    for js_file in directory.rglob("*.js"):  # Recursively find all .js files
        content = js_file.read_text(encoding="utf-8")  # Read the file
        cleaned_content = "\n".join(
            line for line in content.splitlines()
            if not line.strip().startswith("//# sourceMappingURL")
        )
        js_file.write_text(cleaned_content, encoding="utf-8")  # Overwrite the file

class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any):
        self.stdout.write("Downloading vendor static files")
        completed_urls = []
        for name, url in VENDOR_STATICFILES.items():
            out_path = STATICFILES_VENDOR_DIR / name
            dl_success = helpers.download_to_local(url, out_path)
            if dl_success:
                completed_urls.append(url)
            else:
                self.stdout.write(
                    self.style.ERROR(f'Failed to download {url}')
                )
        
        # Remove sourceMappingURL references after downloading files
        remove_source_mapping_urls(STATICFILES_VENDOR_DIR)
        
        # Check if all files were successfully downloaded
        if set(completed_urls) == set(VENDOR_STATICFILES.values()):
            self.stdout.write(
                self.style.SUCCESS('Successfully updated all vendor static files.')
            )
        else:
            self.stdout.write(
                self.style.WARNING('Some files were not updated')
            )