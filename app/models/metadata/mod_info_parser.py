from typing import Any
from pathlib import Path
from loguru import logger
import re

def parse_mod_info(path: Path) -> dict[str, Any]:
    """
    Parse a mod.info file into a dictionary compatible with AboutXmlMod fields.
    """
    data = {}
    try:
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                line = line.strip()
                if not line or '=' not in line:
                    continue
                key, value = line.split('=', 1)
                key = key.strip().lower()
                value = value.strip()
                data[key] = value
    except Exception as e:
        logger.error(f"Failed to read mod.info at {path}: {e}")
        return {}

    # Map mod.info fields to AboutXmlMod fields
    mapped_data = {}
    mapped_data['name'] = data.get('name', 'Unknown')
    mapped_data['packageId'] = data.get('id', 'unknown.mod')
    mapped_data['description'] = data.get('description', '')
    mapped_data['url'] = data.get('url', '')

    # Handle poster/icon
    if 'poster' in data:
        # Poster is relative to mod root
        mapped_data['modIconPath'] = str(path.parent / data['poster'])
    elif 'icon' in data: # Some mods might use icon?
         mapped_data['modIconPath'] = str(path.parent / data['icon'])

    # Handle dependencies
    # require=ModID1,ModID2
    if 'require' in data:
        deps = [d.strip() for d in data['require'].split(',') if d.strip()]
        mod_deps = []
        for dep in deps:
            mod_deps.append({'packageId': dep, 'displayName': dep})
        mapped_data['modDependencies'] = mod_deps

    # Project Zomboid doesn't really have standardized author/version in mod.info usually,
    # but sometimes they might add it.

    return mapped_data
