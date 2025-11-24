"""
Image utilities for Fibulopedia.

This module provides utilities for handling images in the application,
including conversion to base64 for embedding in HTML.
"""

import base64
from pathlib import Path
from typing import Optional

from src.logging_utils import setup_logger

logger = setup_logger(__name__)


def image_to_base64(image_path: str | Path) -> Optional[str]:
    """
    Convert an image file to base64 encoded string.
    
    Args:
        image_path: Path to the image file (relative or absolute).
    
    Returns:
        Base64 encoded string with data URI prefix, or None if file not found.
    
    Example:
        >>> img_data = image_to_base64("assets/spike_sword.gif")
        >>> if img_data:
        ...     print(f'<img src="{img_data}" alt="Spike Sword">')
    """
    try:
        img_file = Path(image_path)
        
        # Convert relative paths to absolute
        if not img_file.is_absolute():
            img_file = Path.cwd() / str(image_path).lstrip("./")
        
        if not img_file.exists():
            logger.warning(f"Image file not found: {img_file}")
            return None
        
        # Read image bytes
        with open(img_file, "rb") as f:
            img_bytes = f.read()
        
        # Encode to base64
        img_base64 = base64.b64encode(img_bytes).decode("utf-8")
        
        # Determine MIME type from extension
        ext = img_file.suffix.lower().lstrip(".")
        mime_types = {
            "gif": "image/gif",
            "png": "image/png",
            "jpg": "image/jpeg",
            "jpeg": "image/jpeg",
            "webp": "image/webp",
            "svg": "image/svg+xml"
        }
        mime_type = mime_types.get(ext, "image/png")
        
        # Return data URI
        data_uri = f"data:{mime_type};base64,{img_base64}"
        logger.debug(f"Successfully converted image to base64: {img_file.name}")
        return data_uri
        
    except Exception as e:
        logger.error(f"Error converting image to base64: {e}")
        return None


def create_image_html(
    image_path: Optional[str], 
    alt_text: str = "", 
    width: int = 32, 
    height: int = 32,
    css_class: str = ""
) -> str:
    """
    Create HTML img tag with base64 encoded image.
    
    Args:
        image_path: Path to the image file, or None for no image.
        alt_text: Alternative text for the image.
        width: Image width in pixels.
        height: Image height in pixels.
        css_class: CSS class to apply to the img tag.
    
    Returns:
        HTML img tag string, or empty string if image_path is None.
    
    Example:
        >>> html = create_image_html("assets/sword.gif", "Sword", 32, 32, "weapon-icon")
        >>> print(html)
        <img src="data:image/gif;base64,..." alt="Sword" width="32" height="32" class="weapon-icon">
    """
    if not image_path:
        return ""
    
    img_data = image_to_base64(image_path)
    if not img_data:
        return ""
    
    class_attr = f' class="{css_class}"' if css_class else ""
    
    html = (
        f'<img src="{img_data}" '
        f'alt="{alt_text}" '
        f'width="{width}" '
        f'height="{height}"'
        f'{class_attr}>'
    )
    
    return html
