from typing import Optional, Any
from BaseClasses import MultiWorld


# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the category, False to disable it, or None to use the default behavior
def before_is_category_enabled(multiworld: MultiWorld, player: int, category_name: str) -> Optional[bool]:
    from ..Helpers import get_option_value 
    dlc = get_option_value(multiworld, player, "enabled_DLCs")

    if category_name == "DLC_S1":
        return "Alternate Dimension" in dlc or "GAKU−RAN" in dlc or "Anti-ParadoX" in dlc

    if category_name == "DLC_PO":
        return "Pre-Order Bonus" in dlc

    if category_name == "DLC_AD":
        return "Alternate Dimension" in dlc

    if category_name == "DLC_G-R":
        return "GAKU−RAN" in dlc

    if category_name == "DLC_APX":
        return "Anti-ParadoX" in dlc

    if category_name == "DLC_HOS":
        return "Halls of Stuff" in dlc

    if category_name == "DLC_C_Public":
        return "Costume Public Safety Suit Set" in dlc

    if category_name == "DLC_C_Digimon":
        return "Costume Digimon Set" in dlc

    if category_name == "DLC_C_Chosen":
        return "Costume Chosen Children Set" in dlc

    if category_name == "DLC_C_Swimwear":
        return "Costume Swimwear Set" in dlc

    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the item, False to disable it, or None to use the default behavior
def before_is_item_enabled(multiworld: MultiWorld, player: int, item:  dict[str, Any]) -> Optional[bool]:
    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the location, False to disable it, or None to use the default behavior
def before_is_location_enabled(multiworld: MultiWorld, player: int, location:  dict[str, Any]) -> Optional[bool]:
    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the event, False to disable it, or None to use the default behavior
def before_is_event_enabled(multiworld: MultiWorld, player: int, event:  dict[str, Any]) -> Optional[bool]:
    return None
