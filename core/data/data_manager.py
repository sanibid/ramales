from .data_access import LayersInfoDAO, CalculationInfoDAO, LanguageDAO, LayerRasterDAO, CostsDAO
from .models import LayersData, Language, LayerRaster, Costs


class ProjectDataManager:

    @staticmethod
    def get_language_project() -> Language:
        return Language(LANGUAGE=LanguageDAO.get_language_project()[0])

    @staticmethod
    def save_language_project(language: Language):
        sucess = (LanguageDAO.set_language_project(language.LANGUAGE))
        if sucess:
            LanguageDAO.set_done(True)
            return True
        return False

    @staticmethod
    def get_layer_raster() -> LayerRaster:
        return LayerRaster(LAYER_RASTER=LayerRasterDAO.get_layer_raster()[0])

    @staticmethod
    def save_layer_raster(layer_raster: LayerRaster):
        sucess = (LayerRasterDAO.set_layer_raster(layer_raster.LAYER_RASTER))
        if sucess:
            LayerRasterDAO.set_done(True)
            return True
        return False

    @staticmethod
    def get_layers_id() -> LayersData:
        return LayersData(
            BLOCKS_LAYER_ID='quadra_8b241a0c_9ae7_4de4_a4c3_5492c6a0ae95',  #LayersInfoDAO.get_blocks_layer_id()[0],
            NODES_LAYER_ID='caixas_3aa4568e_0320_4cd7_9d46_23301e83e344',  #LayersInfoDAO.get_nodes_layer_id()[0],
            SEGMENTS_LAYER_ID='trecho_02bfec5b_a476_4647_b15f_b87dd5800d80',  #LayersInfoDAO.get_segments_layer_id()[0],
            LINEAR_OBSTACLES_LAYER_ID='obst_lineares_4c64cb06_010a_4cbf_8037_01a856bbd75b',
            #LayersInfoDAO.get_linear_obstacles_layer_id()[0],
            POINT_OBSTACLES_LAYER_ID='obst_pontuais_6d45d1a6_4e74_4077_8b9d_c7deaead46de'
            #LayersInfoDAO.get_point_obstacles_layer_id()[0]
        )

    @staticmethod
    def save_layers_id(layers_data: LayersData):
        sucess = (LayersInfoDAO.set_blocks_layer_id(layers_data.BLOCKS_LAYER_ID) and
                  LayersInfoDAO.set_nodes_layer_id(layers_data.NODES_LAYER_ID) and
                  LayersInfoDAO.set_segments_layer_id(layers_data.SEGMENTS_LAYER_ID) and
                  LayersInfoDAO.set_linear_obstacles_layer_id(layers_data.LINEAR_OBSTACLES_LAYER_ID) and
                  LayersInfoDAO.set_point_obstacles_layer_id(layers_data.POINT_OBSTACLES_LAYER_ID))
        if sucess:
            LayersInfoDAO.set_done(True)
            return True
        return False

    @staticmethod
    def is_data_layers_id_loaded():
        return LayersInfoDAO.is_done()[0]

    @staticmethod
    def get_status_calculation() -> bool:
        return bool(
            CalculationInfoDAO.get_status_calculation()[0]
        )

    @staticmethod
    def save_status_calculation(status: bool):
        sucess = (CalculationInfoDAO.set_status_calculation(status))
        if sucess:
            CalculationInfoDAO.set_done(True)
            return True
        return False

    @staticmethod
    def is_status_calculation_loaded():
        return CalculationInfoDAO.is_done()[0]

    @staticmethod
    def get_costs():
        return Costs(
            TRENCH_WIDTH=CostsDAO.get_trench_width()[0],
            CRADLE_HEIGHT=CostsDAO.get_cradle_height()[0],
            WRAP_HEIGHT=CostsDAO.get_wrap_height()[0],
            SOIL_PERCENT=CostsDAO.get_soil_percent()[0],
            ROCK_PERCENT=CostsDAO.get_rock_percent()[0],
            MANUAL_PERCENT=CostsDAO.get_manual_percent()[0],
            MECHANICAL_PERCENT=CostsDAO.get_mechanical_percent()[0],
            OWN_PERCENT=CostsDAO.get_own_percent()[0],
            CONTRIBUTION_PERCENT=CostsDAO.get_contribution_percent()[0],
            DISPOSAL_DISTANCE=CostsDAO.get_disposal_distance()[0]
        )

    @staticmethod
    def save_costs(costs: Costs) -> bool:
        success = (CostsDAO.set_trench_width(costs.TRENCH_WIDTH) and
                   CostsDAO.set_cradle_height(costs.CRADLE_HEIGHT) and
                   CostsDAO.set_wrap_height(costs.WRAP_HEIGHT) and
                   CostsDAO.set_soil_percent(costs.SOIL_PERCENT) and
                   CostsDAO.set_rock_percent(costs.ROCK_PERCENT) and
                   CostsDAO.set_manual_percent(costs.MANUAL_PERCENT) and
                   CostsDAO.set_mechanical_percent(costs.MECHANICAL_PERCENT) and
                   CostsDAO.set_own_percent(costs.OWN_PERCENT) and
                   CostsDAO.set_contribution_percent(costs.CONTRIBUTION_PERCENT) and
                   CostsDAO.set_disposal_distance(costs.DISPOSAL_DISTANCE))
        if success:
            CostsDAO.set_done(True)
            return True
        return False

    @staticmethod
    def is_costs_loaded():
        return CostsDAO.is_done()[0]
