from enum import Enum

class CategoryEnum(Enum):
    ACCESSORY = "accessory"
    TOP = "top"
    BOTTOM = "bottom"
    DRESS = "dress"
    FOOTWEAR = "footwear"
    OUTERWEAR = "Outerwear"
    SHOES = "Shoes"
    ACCESSORIES = "Accessories"
    BAGS = "Bags"
    JEWELRY = "Jewelry"
    HATS = "Hats"
    SCARVES = "Scarves"
    BELTS = "Belts"
    SOCKS = "Socks"
    UNDERWEAR = "Underwear"
    SWIMWEAR = "Swimwear"
    ACTIVEWEAR = "Activewear"
    SLEEPWEAR = "Sleepwear"
    OTHER = "Other"  # For items that don't fit into the above categories

class SeasonEnum(Enum):
    SUMMER = "summer"
    WINTER = "winter"
    SPRING = "spring"
    FALL = "fall"

class TypeEnum(Enum):
    FORMAL = "Formal"
    SEMI_FORMAL = "semi formal"
    CASUAL = "casual"
    SPORTS = "sports"
    BUSINESS = "business"
    PARTY = "party"
    BEACH = "beach"
    OTHER = "other"  # For items that don't fit into the above types