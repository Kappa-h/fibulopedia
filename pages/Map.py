"""
Map page for Fibulopedia.

This page displays the Tibia 7.1 world map.
"""

import streamlit as st

from src.config import MAP_PATH
from src.ui.layout import (
    setup_page_config,
    load_custom_css,
    create_page_header,
    create_sidebar_navigation,
    create_footer
)
from src.logging_utils import setup_logger

logger = setup_logger(__name__)

# Configure page
setup_page_config("Map", "")
load_custom_css()
create_sidebar_navigation()


def main() -> None:
    """Main function to render the map page."""
    logger.info("Rendering map page")

    # Page header
    create_page_header(
        title="Tibia Map",
        subtitle="Classic Tibia 7.1 world map",
        icon=""
    )

    # Display map if available
    if MAP_PATH.exists():
        st.image(
            str(MAP_PATH),
            use_column_width=True
        )
    else:
        st.error(
            f"""
            **Map image not found.**
            
            Expected location: `{MAP_PATH}`
            
            Please ensure the map file exists at the correct location.
            """
        )

    # Footer
    create_footer()


if __name__ == "__main__":
    main()
