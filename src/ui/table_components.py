"""
Table components for Fibulopedia.

This module provides reusable table components with custom styling,
sortable columns, and zebra striping for better readability.
"""

from typing import Any
import streamlit as st
from src.logging_utils import setup_logger

logger = setup_logger(__name__)


def create_sortable_table(
    data: list[dict[str, Any]],
    columns: list[str],
    column_widths: dict[str, str] | None = None,
    column_alignments: dict[str, str] | None = None,
    allow_html: bool = True
) -> None:
    """
    Create a sortable HTML table with zebra striping and custom styling.
    
    Args:
        data: List of dictionaries representing table rows.
        columns: List of column names to display (keys from data dicts).
        column_widths: Optional dict mapping column names to CSS width values.
        column_alignments: Optional dict mapping column names to alignment ('left', 'center', 'right').
        allow_html: If True, allows HTML content in cells (for images, etc).
    
    Example:
        >>> data = [
        ...     {"Name": "Sword", "Attack": 10, "Defense": 5},
        ...     {"Name": "Axe", "Attack": 12, "Defense": 3}
        ... ]
        >>> create_sortable_table(data, ["Name", "Attack", "Defense"])
    """
    if not data:
        st.info("No data to display.")
        return
    
    # Default column settings
    if column_widths is None:
        column_widths = {}
    if column_alignments is None:
        column_alignments = {}
    
    # Generate unique table ID
    import hashlib
    table_id = "table_" + hashlib.md5(str(columns).encode()).hexdigest()[:8]
    
    # CSS for table styling
    table_css = f"""
    <style>
    #{table_id} {{
        width: 100%;
        background-color: #1a1a1a;
        color: #e0e0e0;
        border-collapse: collapse;
        font-size: 14px;
    }}
    
    #{table_id} thead tr {{
        background-color: #2d2d2d;
        border-bottom: 2px solid #444;
    }}
    
    #{table_id} thead th {{
        padding: 12px 8px;
        text-align: left;
        font-weight: bold;
        cursor: pointer;
        user-select: none;
    }}
    
    #{table_id} thead th:hover {{
        background-color: #3d3d3d;
    }}
    
    #{table_id} tbody tr {{
        border-bottom: 1px solid #333;
    }}
    
    #{table_id} tbody tr:nth-child(odd) {{
        background-color: #1a1a1a;
    }}
    
    #{table_id} tbody tr:nth-child(even) {{
        background-color: #2a2a2a;
    }}
    
    #{table_id} tbody tr:hover {{
        background-color: #353535;
    }}
    
    #{table_id} tbody td {{
        padding: 10px 8px;
    }}
    </style>
    """
    
    # JavaScript for sorting
    sort_js = f"""
    <script>
    (function() {{
        const table = document.getElementById('{table_id}');
        const headers = table.querySelectorAll('thead th');
        const tbody = table.querySelector('tbody');
        
        let sortDirection = {{}};
        
        headers.forEach((header, index) => {{
            header.addEventListener('click', () => {{
                const rows = Array.from(tbody.querySelectorAll('tr'));
                const currentDirection = sortDirection[index] || 'asc';
                const newDirection = currentDirection === 'asc' ? 'desc' : 'asc';
                sortDirection[index] = newDirection;
                
                rows.sort((a, b) => {{
                    const aValue = a.children[index].textContent.trim();
                    const bValue = b.children[index].textContent.trim();
                    
                    // Try to parse as numbers
                    const aNum = parseFloat(aValue);
                    const bNum = parseFloat(bValue);
                    
                    if (!isNaN(aNum) && !isNaN(bNum)) {{
                        return newDirection === 'asc' ? aNum - bNum : bNum - aNum;
                    }} else {{
                        return newDirection === 'asc' 
                            ? aValue.localeCompare(bValue)
                            : bValue.localeCompare(aValue);
                    }}
                }});
                
                // Re-append sorted rows
                rows.forEach(row => tbody.appendChild(row));
            }});
        }});
    }})();
    </script>
    """
    
    # Build HTML table
    html = table_css + f'<table id="{table_id}"><thead><tr>'
    
    # Headers
    for col in columns:
        width_style = f' style="width: {column_widths.get(col, "auto")};"' if col in column_widths else ""
        html += f'<th{width_style}>{col}</th>'
    
    html += '</tr></thead><tbody>'
    
    # Rows
    for row in data:
        html += '<tr>'
        for col in columns:
            alignment = column_alignments.get(col, "left")
            align_style = f' style="text-align: {alignment};"'
            cell_content = row.get(col, "")
            html += f'<td{align_style}>{cell_content}</td>'
        html += '</tr>'
    
    html += '</tbody></table>' + sort_js
    
    # Render
    st.markdown(html, unsafe_allow_html=True)
    
    logger.info(f"Rendered sortable table with {len(data)} rows and {len(columns)} columns")
