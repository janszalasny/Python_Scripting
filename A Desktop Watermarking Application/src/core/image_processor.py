# src/core/image_processor.py

from PIL import Image
from core.watermark_strategies import WatermarkStrategy

class ImageProcessor:
    """
    The main processor class that handles image loading and manipulation.
    This class utilizes the Strategy pattern to apply different watermarks.
    """
    def __init__(self, image_path: str):
        self._original_image = Image.open(image_path).convert("RGBA")
        self.processed_image = self._original_image.copy()

    @property
    def original_image(self):
        return self._original_image.copy()

    def apply_watermark(self, strategy: WatermarkStrategy):
        """
        Applies a watermark using the provided strategy object.
        It always applies the watermark to a fresh copy of the original image
        to prevent stacking multiple watermarks during preview updates.
        """
        self.processed_image = strategy.apply(self.original_image)
        print(f"Applied watermark using {strategy.__class__.__name__}")

    def save_image(self, path: str):
        """Saves the processed image to the specified path."""
        # Convert back to RGB for wider format compatibility (e.g., JPEG)
        if path.lower().endswith(('.jpg', '.jpeg')):
            self.processed_image.convert("RGB").save(path)
        else:
            self.processed_image.save(path)
        print(f"Image saved to {path}")