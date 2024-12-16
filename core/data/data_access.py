from abc import ABC, abstractmethod

from qgis.core import QgsProject

from typing import Tuple


class DAO(ABC):
    KEY_DONE = 'done'

    proj: QgsProject = QgsProject.instance()

    @property
    @classmethod
    @abstractmethod
    def SCOPE(cls):
        return NotImplementedError

    @classmethod
    def is_done(cls):
        return cls.proj.readBoolEntry(cls.SCOPE, cls.KEY_DONE, False)

    @classmethod
    def set_done(cls, done=True):
        return cls.proj.writeEntryBool(cls.SCOPE, cls.KEY_DONE, done)


class LayerRasterDAO(DAO):
    SCOPE = 'RamalesLayerRasterScope'
    KEY_LAYER_RASTER = 'LAYER_RASTER'

    @classmethod
    def get_layer_raster(cls):
        return cls.proj.readEntry(cls.SCOPE, cls.KEY_LAYER_RASTER, None)

    @classmethod
    def set_layer_raster(cls, layer_raster: str):
        return cls.proj.writeEntry(cls.SCOPE, cls.KEY_LAYER_RASTER, layer_raster)


class LanguageDAO(DAO):
    SCOPE = 'RamalesLanguageScope'
    KEY_LANGUAGE = 'LANGUAGE'

    @classmethod
    def get_language_project(cls):
        return cls.proj.readEntry(cls.SCOPE, cls.KEY_LANGUAGE, None)

    @classmethod
    def set_language_project(cls, language: str):
        return cls.proj.writeEntry(cls.SCOPE, cls.KEY_LANGUAGE, language)


class LayersInfoDAO(DAO):
    SCOPE = 'RamalesLayersInfoScope'
    KEY_BLOCKS_LAYER = 'BLOCKS_LAYER'
    KEY_RESUME_FRAME_LAYER = 'RESUME_FRAME_LAYER'
    KEY_NODES_LAYER = 'NODES_LAYER'
    KEY_SEGMENTS_LAYER = 'SEGMENTS_LAYER'
    KEY_LINEAR_OBSTACLES_LAYER = 'LINEAR_OBSTACLES_LAYER'
    KEY_POINT_OBSTACLES_LAYER = 'POINT_OBSTACLES_LAYER'
    KEY_ACCESSORIES_LAYER = 'ACCESSORIES_LAYER'

    @classmethod
    def get_blocks_layer_id(cls):
        return cls.proj.readEntry(cls.SCOPE, cls.KEY_BLOCKS_LAYER, None)

    @classmethod
    def get_resume_frame_layer_id(cls):
        return cls.proj.readEntry(cls.SCOPE, cls.KEY_RESUME_FRAME_LAYER, None)

    @classmethod
    def get_nodes_layer_id(cls):
        return cls.proj.readEntry(cls.SCOPE, cls.KEY_NODES_LAYER, None)

    @classmethod
    def get_segments_layer_id(cls):
        return cls.proj.readEntry(cls.SCOPE, cls.KEY_SEGMENTS_LAYER, None)

    @classmethod
    def get_linear_obstacles_layer_id(cls):
        return cls.proj.readEntry(cls.SCOPE, cls.KEY_LINEAR_OBSTACLES_LAYER, None)

    @classmethod
    def get_point_obstacles_layer_id(cls):
        return cls.proj.readEntry(cls.SCOPE, cls.KEY_POINT_OBSTACLES_LAYER, None)

    @classmethod
    def get_accessories_layer_id(cls):
        return cls.proj.readEntry(cls.SCOPE, cls.KEY_ACCESSORIES_LAYER, None)

    @classmethod
    def set_blocks_layer_id(cls, blocks_layer):
        return cls.proj.writeEntry(cls.SCOPE, cls.KEY_BLOCKS_LAYER, blocks_layer)

    @classmethod
    def set_resume_frame_layer_id(cls, resume_frame_layer):
        return cls.proj.writeEntry(cls.SCOPE, cls.KEY_RESUME_FRAME_LAYER, resume_frame_layer)

    @classmethod
    def set_nodes_layer_id(cls, nodes_layer):
        return cls.proj.writeEntry(cls.SCOPE, cls.KEY_NODES_LAYER, nodes_layer)

    @classmethod
    def set_segments_layer_id(cls, segments_layer):
        return cls.proj.writeEntry(cls.SCOPE, cls.KEY_SEGMENTS_LAYER, segments_layer)

    @classmethod
    def set_linear_obstacles_layer_id(cls, linear_obstacles_layer):
        return cls.proj.writeEntry(cls.SCOPE, cls.KEY_LINEAR_OBSTACLES_LAYER, linear_obstacles_layer)

    @classmethod
    def set_point_obstacles_layer_id(cls, points_obstacles_layer):
        return cls.proj.writeEntry(cls.SCOPE, cls.KEY_POINT_OBSTACLES_LAYER, points_obstacles_layer)

    @classmethod
    def set_accessories_layer_id(cls, accessories_layer):
        return cls.proj.writeEntry(cls.SCOPE, cls.KEY_ACCESSORIES_LAYER, accessories_layer)


class CalculationInfoDAO(DAO):
    SCOPE = 'RamalesCalculationInfoScope'
    KEY_CALCULATION_STATUS = None

    @classmethod
    def get_status_calculation(cls):
        return cls.proj.readBoolEntry(cls.SCOPE, cls.KEY_CALCULATION_STATUS)

    @classmethod
    def set_status_calculation(cls, status: bool):
        return cls.proj.writeEntryBool(cls.SCOPE, cls.KEY_CALCULATION_STATUS, status)


class CostsDAO(DAO):
    SCOPE = 'RamalesCostsScope'
    KEY_TRENCH_WIDTH = 'TRENCH_WIDTH'
    KEY_CRADLE_HEIGHT = 'CRADLE_HEIGHT'
    KEY_WRAP_HEIGHT = 'WRAP_HEIGHT'
    KEY_SOIL_PERCENT = 'SOIL_PERCENT'
    KEY_ROCK_PERCENT = 'ROCK_PERCENT'
    KEY_MANUAL_PERCENT = 'MANUAL_PERCENT'
    KEY_MECHANICAL_PERCENT = 'MECHANICAL_PERCENT'
    KEY_OWN_PERCENT = 'OWN_PERCENT'
    KEY_CONTRIBUTION_PERCENT = 'CONTRIBUTION_PERCENT'
    KEY_DISPOSAL_DISTANCE = 'DISPOSAL_DISTANCE'
    KEY_SOIL_BULKING = 'SOIL_BULKING'
    KEY_ROCK_SWELLING = 'ROCK_SWELLING'

    @classmethod
    def get_trench_width(cls) -> Tuple[float, bool]:
        return cls.proj.readDoubleEntry(cls.SCOPE, cls.KEY_TRENCH_WIDTH)

    @classmethod
    def set_trench_width(cls, trench_width: float) -> bool:
        return cls.proj.writeEntryDouble(cls.SCOPE, cls.KEY_TRENCH_WIDTH, trench_width)

    @classmethod
    def get_cradle_height(cls) -> Tuple[float, bool]:
        return cls.proj.readDoubleEntry(cls.SCOPE, cls.KEY_CRADLE_HEIGHT)

    @classmethod
    def set_cradle_height(cls, cradle_height: float) -> bool:
        return cls.proj.writeEntryDouble(cls.SCOPE, cls.KEY_CRADLE_HEIGHT, cradle_height)

    @classmethod
    def get_wrap_height(cls) -> Tuple[float, bool]:
        return cls.proj.readDoubleEntry(cls.SCOPE, cls.KEY_WRAP_HEIGHT)

    @classmethod
    def set_wrap_height(cls, wrap_height: float) -> bool:
        return cls.proj.writeEntryDouble(cls.SCOPE, cls.KEY_WRAP_HEIGHT, wrap_height)

    @classmethod
    def get_soil_percent(cls) -> Tuple[int, bool]:
        return cls.proj.readNumEntry(cls.SCOPE, cls.KEY_SOIL_PERCENT)

    @classmethod
    def set_soil_percent(cls, soil_percent: int) -> bool:
        return cls.proj.writeEntry(cls.SCOPE, cls.KEY_SOIL_PERCENT, soil_percent)

    @classmethod
    def get_rock_percent(cls) -> Tuple[int, bool]:
        return cls.proj.readNumEntry(cls.SCOPE, cls.KEY_ROCK_PERCENT)

    @classmethod
    def set_rock_percent(cls, rock_percent: int) -> bool:
        return cls.proj.writeEntry(cls.SCOPE, cls.KEY_ROCK_PERCENT, rock_percent)

    @classmethod
    def get_manual_percent(cls) -> Tuple[int, bool]:
        return cls.proj.readNumEntry(cls.SCOPE, cls.KEY_MANUAL_PERCENT)

    @classmethod
    def set_manual_percent(cls, manual_percent: int) -> bool:
        return cls.proj.writeEntry(cls.SCOPE, cls.KEY_MANUAL_PERCENT, manual_percent)

    @classmethod
    def get_mechanical_percent(cls) -> Tuple[int, bool]:
        return cls.proj.readNumEntry(cls.SCOPE, cls.KEY_MECHANICAL_PERCENT)

    @classmethod
    def set_mechanical_percent(cls, mechanical_percent: int) -> bool:
        return cls.proj.writeEntry(cls.SCOPE, cls.KEY_MECHANICAL_PERCENT, mechanical_percent)

    @classmethod
    def get_own_percent(cls) -> Tuple[int, bool]:
        return cls.proj.readNumEntry(cls.SCOPE, cls.KEY_OWN_PERCENT)

    @classmethod
    def set_own_percent(cls, own_percent: int) -> bool:
        return cls.proj.writeEntry(cls.SCOPE, cls.KEY_OWN_PERCENT, own_percent)

    @classmethod
    def get_contribution_percent(cls) -> Tuple[int, bool]:
        return cls.proj.readNumEntry(cls.SCOPE, cls.KEY_CONTRIBUTION_PERCENT)

    @classmethod
    def set_contribution_percent(cls, contribution_percent: int) -> bool:
        return cls.proj.writeEntry(cls.SCOPE, cls.KEY_CONTRIBUTION_PERCENT, contribution_percent)

    @classmethod
    def get_disposal_distance(cls) -> Tuple[float, bool]:
        return cls.proj.readDoubleEntry(cls.SCOPE, cls.KEY_DISPOSAL_DISTANCE)

    @classmethod
    def set_disposal_distance(cls, disposal_distance: float) -> bool:
        return cls.proj.writeEntryDouble(cls.SCOPE, cls.KEY_DISPOSAL_DISTANCE, disposal_distance)

    @classmethod
    def get_soil_bulking(cls) -> Tuple[float, bool]:
        return cls.proj.readDoubleEntry(cls.SCOPE, cls.KEY_SOIL_BULKING)

    @classmethod
    def set_soil_bulking(cls, soil_bulking: float) -> bool:
        return cls.proj.writeEntryDouble(cls.SCOPE, cls.KEY_SOIL_BULKING, soil_bulking)

    @classmethod
    def get_rock_swelling(cls) -> Tuple[float, bool]:
        return cls.proj.readDoubleEntry(cls.SCOPE, cls.KEY_ROCK_SWELLING)

    @classmethod
    def set_rock_swelling(cls, rock_swelling: float) -> bool:
        return cls.proj.writeEntryDouble(cls.SCOPE, cls.KEY_ROCK_SWELLING, rock_swelling)

