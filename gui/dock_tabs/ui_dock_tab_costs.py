from typing import Optional

from ..generate_costs_ui import GenerateCostsUI
from ...core.calculate.CostsCalculation import CostCalculation
from .base.ui_dock_tab_costs_base import DockTabCostsBase
from ...core.data.data_manager import ProjectDataManager
from ...core.data.models import Costs


class DockTabCosts(DockTabCostsBase):
    def __init__(self, dock):
        super().__init__(dock)
        self.costs_calculator: Optional[CostCalculation] = None
        self.loaded_from_db = False
        self.costs: Optional[Costs] = None
        self.costs_calculation = ''
        self.generate_costs = GenerateCostsUI()

    def set_logic(self):
        self.sb_soil.valueChanged.connect(self.on_data_changed)
        self.sb_rock.valueChanged.connect(self.on_data_changed)
        self.sb_manual.valueChanged.connect(self.on_data_changed)
        self.sb_mechanical.valueChanged.connect(self.on_data_changed)
        self.sb_own.valueChanged.connect(self.on_data_changed)
        self.sb_contribution.valueChanged.connect(self.on_data_changed)
        self.dsb_wrap_height.valueChanged.connect(self.on_data_changed)
        self.dsb_cradle_height.valueChanged.connect(self.on_data_changed)
        self.dsb_trench_width.valueChanged.connect(self.on_data_changed)
        self.dsb_disposal_distance.valueChanged.connect(self.on_data_changed)
        self.dsb_soil_bulking.valueChanged.connect(self.on_data_changed)
        self.dsb_rock_swelling.valueChanged.connect(self.on_data_changed)

        self.cb_show_data_costs.toggled.connect(self.on_cb_costs_toggle)
        self.pb_report_costs.clicked.connect(self.__show_report_costs)
        self.pb_generate_xls_costs.clicked.connect(self.__generete_xls_costs)
        # self.repOutCosts.pb_saveEditCosts.clicked.connect(self.on_services_cost_update)

    def load_data(self):
        if ProjectDataManager.is_costs_loaded():
            self.costs = ProjectDataManager.get_costs()
        self.load_costs_calculations()
        self.load_user_input()
        self.load_costs_values()
        self.loaded_from_db = True

    def load_user_input(self):
        if self.costs is not None:
            self.sb_soil.setValue(self.costs.SOIL_PERCENT)
            self.sb_rock.setValue(self.costs.ROCK_PERCENT)
            self.sb_manual.setValue(self.costs.MANUAL_PERCENT)
            self.sb_mechanical.setValue(self.costs.MECHANICAL_PERCENT)
            self.sb_own.setValue(self.costs.OWN_PERCENT)
            self.sb_contribution.setValue(self.costs.CONTRIBUTION_PERCENT)
            self.dsb_wrap_height.setValue(self.costs.WRAP_HEIGHT)
            self.dsb_cradle_height.setValue(self.costs.CRADLE_HEIGHT)
            self.dsb_trench_width.setValue(self.costs.TRENCH_WIDTH)
            self.dsb_disposal_distance.setValue(self.costs.DISPOSAL_DISTANCE)
            self.dsb_rock_swelling.setValue(self.costs.ROCK_SWELLING)
            self.dsb_soil_bulking.setValue(self.costs.SOIL_BULKING)
        else:
            self.sb_soil.setValue(100)
            self.sb_rock.setValue(0)
            self.sb_manual.setValue(100)
            self.sb_mechanical.setValue(0)
            self.sb_own.setValue(100)
            self.sb_contribution.setValue(0)
            self.dsb_wrap_height.setValue(0)
            self.dsb_cradle_height.setValue(0)
            self.dsb_trench_width.setValue(0)
            self.dsb_disposal_distance.setValue(0)
            self.dsb_rock_swelling.setValue(1)
            self.dsb_soil_bulking.setValue(1)

    def load_costs_values(self):
        pass

    def load_costs_calculations(self):
        pass

    def reload(self):
        self.loaded_from_db = False
        self.load_data()

    def on_cb_costs_toggle(self, checked: bool):
        if self.cb_show_data_costs.isChecked():
            self.gb_DataCosts.show()
        else:
            self.gb_DataCosts.hide()

    def on_data_changed(self):
        if not self.loaded_from_db:
            return
        tmp_costs = Costs(
            SOIL_PERCENT=self.sb_soil.value(),
            ROCK_PERCENT=self.sb_rock.value(),
            MANUAL_PERCENT=self.sb_manual.value(),
            MECHANICAL_PERCENT=self.sb_mechanical.value(),
            OWN_PERCENT=self.sb_own.value(),
            CONTRIBUTION_PERCENT=self.sb_contribution.value(),
            WRAP_HEIGHT=self.dsb_wrap_height.value(),
            CRADLE_HEIGHT=self.dsb_cradle_height.value(),
            TRENCH_WIDTH=self.dsb_trench_width.value(),
            DISPOSAL_DISTANCE=self.dsb_disposal_distance.value(),
            SOIL_BULKING=self.dsb_soil_bulking.value(),
            ROCK_SWELLING=self.dsb_rock_swelling.value()
        )
        # if self.costs is None:
        #     tmp_costs.services = Costs().services

        if tmp_costs != self.costs:
            self.costs = tmp_costs
            ProjectDataManager.save_costs(self.costs)
            self.dock.reload()

        # if self.check_data_costs():
        #     self.rb_show_data_costs.setChecked(False)

    # def on_services_cost_update(self):
    #     self.repOutCosts.saveChanges()
    #     services = [self.repOutCosts.costs.getVlItem01(),
    #                 self.repOutCosts.costs.getVlItem02(),
    #                 self.repOutCosts.costs.getVlItem03(),
    #                 self.repOutCosts.costs.getVlItem04(),
    #                 self.repOutCosts.costs.getVlItem05(),
    #                 self.repOutCosts.costs.getVlItem06(),
    #                 self.repOutCosts.costs.getVlItem07(),
    #                 self.repOutCosts.costs.getVlItem08(),
    #                 self.repOutCosts.costs.getVlItem09(),
    #                 self.repOutCosts.costs.getVlItem10(),
    #                 self.repOutCosts.costs.getVlItem11(),
    #                 self.repOutCosts.costs.getVlItem12(),
    #                 self.repOutCosts.costs.getVlItem13(),
    #                 self.repOutCosts.costs.getVlItem14(),
    #                 self.repOutCosts.costs.getVlItem15(),
    #                 self.repOutCosts.costs.getVlItem16(),
    #                 self.repOutCosts.costs.getVlItem17()]
    #     if self.costs is not None:
    #         self.costs.services = services
    #     ProjectDataManager.save_project_costs(self.costs)
    #     self.dock_reload()
    #     self.load_costs_values()

    def setCosts(self):
        pass
        # if self.costs_calculator is not None:
        #     self.costs_calculator.loadData(costs=self.costs, calculation=self.calculation,
        #                                    entranceData=self.project_data)
        # else:
        #     self.load_costs_calculator()

    def __show_report_costs(self):
        self.rep_out_costs.loadReportCosts(self.costs_calculation)
        self.rep_out_costs.showReportCosts()

    def __generete_xls_costs(self):
        self.generate_costs.show_generate_costs()


    def showReportCosts(self):
        pass
        # if self.check_data_costs():
        #     self.setCosts()
        #     # TODO verificar se project config é não nula
        #     self.repOutCosts.loadReportCosts(self.costs_calculator, self.project_config.has_sedimentation_tank,
        #                                      self.title)
        #     self.repOutCosts.showReportCosts()
        # elif self.loaded_from_db:
        #     icon = QMessageBox.Critical
        #     self.utils.showDialog(self.title,
        #                           self.tr('Diâmetro e profundidade da tubulação devem ser informados!'), icon)
