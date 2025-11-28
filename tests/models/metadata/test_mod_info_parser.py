
import pytest
from pathlib import Path
from app.models.metadata.mod_info_parser import parse_mod_info

def test_parse_mod_info_basic(tmp_path: Path) -> None:
    mod_info_file = tmp_path / "mod.info"
    content = """name=My Mod
poster=poster.png
id=my_mod_id
description=Description of the mod.
url=http://example.com
require=Mod1,Mod2
"""
    mod_info_file.write_text(content, encoding='utf-8')

    data = parse_mod_info(mod_info_file)

    assert data['name'] == "My Mod"
    assert data['packageId'] == "my_mod_id"
    assert data['description'] == "Description of the mod."
    assert data['url'] == "http://example.com"
    assert "poster.png" in data['modIconPath']
    assert len(data['modDependencies']) == 2
    assert data['modDependencies'][0]['packageId'] == "Mod1"
    assert data['modDependencies'][1]['packageId'] == "Mod2"

def test_parse_mod_info_with_spaces_and_case(tmp_path: Path) -> None:
    mod_info_file = tmp_path / "mod.info"
    content = """Name=My Mod 2
    POSTER=icon.png
    ID=my_mod_id_2
    Description= Another Description
    """
    mod_info_file.write_text(content, encoding='utf-8')

    data = parse_mod_info(mod_info_file)

    assert data['name'] == "My Mod 2"
    assert data['packageId'] == "my_mod_id_2"
    assert data['description'] == "Another Description"
    assert "icon.png" in data['modIconPath']

def test_parse_mod_info_empty_or_invalid(tmp_path: Path) -> None:
    mod_info_file = tmp_path / "mod.info"
    mod_info_file.write_text("invalid content", encoding='utf-8')

    data = parse_mod_info(mod_info_file)
    # Should return empty or partial dict but not crash
    assert data == {'name': 'Unknown', 'packageId': 'unknown.mod', 'description': '', 'url': ''}

def test_parse_mod_info_file_not_found() -> None:
    path = Path("non_existent_file.info")
    data = parse_mod_info(path)
    assert data == {}
