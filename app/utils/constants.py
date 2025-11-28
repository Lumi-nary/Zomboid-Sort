from enum import Enum
from typing import Any


class SortMethod(str, Enum):
    ALPHABETICAL = "Alphabetical"
    TOPOLOGICAL = "Topological"


DB_BUILDER_PRUNE_EXCEPTIONS = [
    "database",
    "rules",
]
DB_BUILDER_PURGE_KEYS = ["external_time_created", "external_time_updated"]
DB_BUILDER_RECURSE_EXCEPTIONS = [
    "dependencies",
    "incompatibleWith",
    "loadBefore",
    "loadAfter",
    "loadTop",
    "loadBottom",
]
MOD_RECURSE_EXCEPTIONS = [
    "incompatiblewith",
    "loadafter",
    "loadbefore",
    "moddependencies",
]
DEFAULT_USER_RULES: dict[str, int | dict[str, Any]] = {"timestamp": 0, "rules": {}}
GAME_DLC_METADATA = {
    "108600": {
        "packageid": "project.zomboid",
        "name": "Project Zomboid",
        "steam_url": "https://store.steampowered.com/app/108600/Project_Zomboid/",
        "description": "Base game",
    }
}
# Alias for backwards compatibility if needed, but better to update usages
RIMWORLD_DLC_METADATA = GAME_DLC_METADATA
RIMWORLD_PACKAGE_IDS = [v["packageid"] for v in GAME_DLC_METADATA.values()]
SEARCH_DATA_SOURCE_FILTER_INDEXES = [
    "all",
    "local",
    "git_repo",
    "steamcmd",
    "workshop",
]
KNOWN_MOD_REPLACEMENTS = {}
KNOWN_TIER_ZERO_MODS = {
    "project.zomboid",
}
KNOWN_TIER_ONE_MODS = {}
