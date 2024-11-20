from dataclasses import dataclass


@dataclass
class LayersData:
    BLOCKS_LAYER_ID: str = ''
    NODES_LAYER_ID: str = ''
    SEGMENTS_LAYER_ID: str = ''
    LINEAR_OBSTACLES_LAYER_ID: str = ''
    POINT_OBSTACLES_LAYER_ID: str = ''
    ACCESSORIES_LAYER_ID: str = ''


@dataclass
class Language:
    LANGUAGE: str = ''


@dataclass
class LayerRaster:
    LAYER_RASTER: str = ''


@dataclass
class Costs:
    TRENCH_WIDTH: float = 0.0
    CRADLE_HEIGHT: float = 0.0
    WRAP_HEIGHT: float = 0.0
    SOIL_PERCENT: int = 0
    ROCK_PERCENT: int = 0
    MANUAL_PERCENT: int = 0
    MECHANICAL_PERCENT: int = 0
    OWN_PERCENT: int = 0
    CONTRIBUTION_PERCENT: int = 0
    DISPOSAL_DISTANCE: float = 0.0
