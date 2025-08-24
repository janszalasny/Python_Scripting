# src/core/watermark_strategies.py

from abc import ABC, abstractmethod
from PIL import Image, ImageDraw, ImageFont, ImageEnhance


class WatermarkStrategy(ABC):
    """
    Abstract Base Class for the Strategy Pattern.
    Declares the interface common to all supported watermark algorithms.
    """
    
    @abstractmethod
    def apply(self, base_image: Image.Image) -> Image.Image:
        """Applies the watermark to the given base image."""
        pass


class TextWatermarkStrategy(WatermarkStrategy):
    """
    Concrete strategy for applying a text watermark.
    """
    
    def __init__(self, text, font_path, font_size, color, position, opacity):
        self.text = text
        self.font = ImageFont.truetype(font_path, font_size)
        self.color = self._hex_to_rgba(color, opacity)
        self.position_key = position
        self.opacity = opacity
    
    def _hex_to_rgba(self, hex_color, opacity):
        """Converts hex color string to an RGBA tuple."""
        hex_color = hex_color.lstrip('#')
        rgb = tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))
        return (*rgb, int(255 * opacity))
    
    def _get_position_coords(self, base_size, text_bbox):
        """Calculates the (x, y) coordinates based on the position key."""
        W, H = base_size
        w, h = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
        padding = int(min(W, H) * 0.02)  # 2% padding
        
        positions = {
            "top_left": (padding, padding),
            "top_center": ((W - w) // 2, padding),
            "top_right": (W - w - padding, padding),
            "center_left": (padding, (H - h) // 2),
            "center": ((W - w) // 2, (H - h) // 2),
            "center_right": (W - w - padding, (H - h) // 2),
            "bottom_left": (padding, H - h - padding),
            "bottom_center": ((W - w) // 2, H - h - padding),
            "bottom_right": (W - w - padding, H - h - padding),
        }
        return positions.get(self.position_key, positions["center"])
    
    def apply(self, base_image: Image.Image) -> Image.Image:
        # Create a transparent layer for the text watermark
        txt_layer = Image.new("RGBA", base_image.size, (255, 255, 255, 0))
        draw = ImageDraw.Draw(txt_layer)
        
        # Get text bounding box and calculate position
        text_bbox = draw.textbbox((0, 0), self.text, font=self.font)
        position = self._get_position_coords(base_image.size, text_bbox)
        
        draw.text(position, self.text, font=self.font, fill=self.color)
        
        # Composite the text layer onto the base image
        return Image.alpha_composite(base_image.convert("RGBA"), txt_layer)


class ImageWatermarkStrategy(WatermarkStrategy):
    """
    Concrete strategy for applying an image watermark.
    """
    
    def __init__(self, watermark_path, position, opacity, scale):
        self.watermark_image = Image.open(watermark_path).convert("RGBA")
        self.position_key = position
        self.opacity = opacity
        self.scale = scale
    
    def _get_position_coords(self, base_size, watermark_size):
        """Calculates the (x, y) coordinates for the watermark image."""
        W, H = base_size
        w, h = watermark_size
        padding = int(min(W, H) * 0.02)
        
        positions = {
            "top_left": (padding, padding),
            "top_center": ((W - w) // 2, padding),
            "top_right": (W - w - padding, padding),
            "center_left": (padding, (H - h) // 2),
            "center": ((W - w) // 2, (H - h) // 2),
            "center_right": (W - w - padding, (H - h) // 2),
            "bottom_left": (padding, H - h - padding),
            "bottom_center": ((W - w) // 2, H - h - padding),
            "bottom_right": (W - w - padding, H - h - padding),
        }
        return positions.get(self.position_key, positions["center"])
    
    def apply(self, base_image: Image.Image) -> Image.Image:
        # Scale watermark relative to the base image
        base_width, base_height = base_image.size
        max_size = (int(base_width * self.scale), int(base_height * self.scale))
        self.watermark_image.thumbnail(max_size, Image.Resampling.LANCZOS)
        
        # Apply opacity
        alpha = self.watermark_image.split()[3]
        alpha = ImageEnhance.Brightness(alpha).enhance(self.opacity)
        self.watermark_image.putalpha(alpha)
        
        # Create a transparent layer and paste the watermark
        watermark_layer = Image.new("RGBA", base_image.size, (255, 255, 255, 0))
        position = self._get_position_coords(base_image.size, self.watermark_image.size)
        watermark_layer.paste(self.watermark_image, position, self.watermark_image)
        
        # Composite the layers
        return Image.alpha_composite(base_image.convert("RGBA"), watermark_layer)