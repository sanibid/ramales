from PyQt5.QtCore import Qt, QCoreApplication, QLocale
from PyQt5.QtWidgets import (QMessageBox, QStyledItemDelegate, QTableWidgetItem, QDoubleSpinBox, QAbstractItemView,
                             QApplication, QDialog, QGridLayout, QTableWidget, QPushButton, QLabel)

from ..helpers.utils import Utils
# from ..core.calculation.CostsCalculation import CostsCalculation


class RepOutDataCostsUI():
    screen = QDialog()
    layout = QGridLayout()
    table = QTableWidget()
    title = 'Ramales'
    loc = QLocale()
    utils = Utils()
    # costs: CostsCalculation
    pb_saveEditCosts = QPushButton()
    lb_costs = QLabel()

    max = 9999999

    dsb_item01_unity_dollar = QDoubleSpinBox()
    dsb_item02_unity_dollar = QDoubleSpinBox()
    dsb_item03_unity_dollar = QDoubleSpinBox()
    dsb_item04_unity_dollar = QDoubleSpinBox()
    dsb_item05_unity_dollar = QDoubleSpinBox()
    dsb_item06_unity_dollar = QDoubleSpinBox()
    dsb_item07_unity_dollar = QDoubleSpinBox()
    dsb_item08_unity_dollar = QDoubleSpinBox()
    dsb_item09_unity_dollar = QDoubleSpinBox()
    dsb_item10_unity_dollar = QDoubleSpinBox()
    dsb_item11_unity_dollar = QDoubleSpinBox()
    dsb_item12_unity_dollar = QDoubleSpinBox()
    dsb_item13_unity_dollar = QDoubleSpinBox()
    dsb_item14_unity_dollar = QDoubleSpinBox()
    dsb_item15_unity_dollar = QDoubleSpinBox()
    dsb_item16_unity_dollar = QDoubleSpinBox()
    dsb_item17_unity_dollar = QDoubleSpinBox()
    dsb_item18_unity_dollar = QDoubleSpinBox()
    dsb_item19_unity_dollar = QDoubleSpinBox()
    dsb_item20_unity_dollar = QDoubleSpinBox()
    dsb_item21_unity_dollar = QDoubleSpinBox()
    dsb_item22_unity_dollar = QDoubleSpinBox()
    dsb_item23_unity_dollar = QDoubleSpinBox()
    dsb_item24_unity_dollar = QDoubleSpinBox()
    dsb_item25_unity_dollar = QDoubleSpinBox()
    dsb_item26_unity_dollar = QDoubleSpinBox()
    dsb_item27_unity_dollar = QDoubleSpinBox()
    dsb_item28_unity_dollar = QDoubleSpinBox()
    dsb_item29_unity_dollar = QDoubleSpinBox()
    dsb_item30_unity_dollar = QDoubleSpinBox()
    dsb_item31_unity_dollar = QDoubleSpinBox()
    dsb_item32_unity_dollar = QDoubleSpinBox()
    dsb_item33_unity_dollar = QDoubleSpinBox()
    dsb_item34_unity_dollar = QDoubleSpinBox()
    dsb_item35_unity_dollar = QDoubleSpinBox()
    dsb_item36_unity_dollar = QDoubleSpinBox()
    dsb_item37_unity_dollar = QDoubleSpinBox()
    dsb_item38_unity_dollar = QDoubleSpinBox()
    dsb_item39_unity_dollar = QDoubleSpinBox()
    dsb_item40_unity_dollar = QDoubleSpinBox()

    dsb_list_entrance = [dsb_item01_unity_dollar, dsb_item02_unity_dollar, dsb_item03_unity_dollar,
                         dsb_item04_unity_dollar, dsb_item05_unity_dollar, dsb_item06_unity_dollar,
                         dsb_item07_unity_dollar, dsb_item08_unity_dollar, dsb_item09_unity_dollar,
                         dsb_item10_unity_dollar, dsb_item11_unity_dollar, dsb_item12_unity_dollar,
                         dsb_item13_unity_dollar, dsb_item14_unity_dollar, dsb_item15_unity_dollar,
                         dsb_item16_unity_dollar, dsb_item17_unity_dollar, dsb_item18_unity_dollar,
                         dsb_item19_unity_dollar, dsb_item20_unity_dollar, dsb_item21_unity_dollar,
                         dsb_item22_unity_dollar, dsb_item23_unity_dollar, dsb_item24_unity_dollar,
                         dsb_item25_unity_dollar, dsb_item26_unity_dollar, dsb_item27_unity_dollar,
                         dsb_item28_unity_dollar, dsb_item29_unity_dollar, dsb_item30_unity_dollar,
                         dsb_item31_unity_dollar, dsb_item32_unity_dollar, dsb_item33_unity_dollar,
                         dsb_item34_unity_dollar, dsb_item35_unity_dollar, dsb_item36_unity_dollar,
                         dsb_item37_unity_dollar, dsb_item38_unity_dollar, dsb_item39_unity_dollar,
                         dsb_item40_unity_dollar]



    for i in dsb_list_entrance:
        i.setMaximum(max)
        i.setAlignment(Qt.AlignHCenter)
        i.setGroupSeparatorShown(True)

    # noinspection PyMethodMayBeStatic
    def translate(self, msg, disambiguation=None, n=-1):
        return QCoreApplication.translate(RepOutDataCostsUI.__name__, msg, disambiguation, n)

    def showReportCosts(self):
        self.table.verticalHeader().setVisible(False)
        app = QApplication.instance()
        allScreen = app.primaryScreen()
        geometry = allScreen.availableGeometry()
        self.screen.setGeometry(
            int((geometry.width() - self.table.horizontalHeader().length() * 1.1) / 2.0),
            int((geometry.height() - self.table.verticalHeader().length() * 0.48) / 2.0),
            int(self.table.horizontalHeader().length() * 1.055),
            int(self.table.verticalHeader().length() * 0.5)
        )
        self.screen.exec_()

    def loadReportCosts(self, quantities_calculator):
        self.quantities_calculator = quantities_calculator
        self.screen.setWindowTitle(self.title + self.translate(' - Custos'))
        self.pb_saveEditCosts.setText(self.translate('Salvar'))
        self.pb_saveEditCosts.setFixedSize(100, 25)
        self.layout.addWidget(self.pb_saveEditCosts, 0, 0, Qt.AlignRight)
        self.loadTable()
        self.layout.addWidget(self.table, 1, 0)
        self.screen.setLayout(self.layout)

    def loadTable(self):
        colLabels = [self.translate('Item'), self.translate('Descrição dos serviços'), self.translate('Unidade'),
                     self.translate('Qtd.'), self.translate('Preço unitário USD'), self.translate('Valor USD')]
        self.table.setRowCount(53)
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(colLabels)
        self.table.setColumnWidth(0, 50)
        self.table.setColumnWidth(1, 330)
        self.table.setColumnWidth(2, 80)
        self.table.setColumnWidth(3, 80)
        self.table.setColumnWidth(4, 130)
        self.table.setColumnWidth(5, 110)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)  # does not allow table editing
        self.table.setSelectionBehavior(
            QAbstractItemView.SelectRows)  # Used to select entire rows instead of just the cell
        delegate = AlignDelegate(self.table)  # whole column alignment
        self.table.setItemDelegateForColumn(0, delegate)
        self.table.setItemDelegateForColumn(2, delegate)
        self.table.setItemDelegateForColumn(3, delegate)
        self.table.setItemDelegateForColumn(5, delegate)

        for index in range(40):
            self.dsb_list_entrance[index].setValue(self.quantities_calculator.costs.SERVICES[index])

        i = 0
        self.table.setItem(i, 0, QTableWidgetItem(self.translate('SERVIÇOS')))
        self.table.setSpan(i, 0, 1, 6)
        self.table.item(i, 0).setFont(self.utils.formatBoldText())
        i += 1
        self.table.setItem(i, 0, QTableWidgetItem(self.translate('SINALIZAÇÃO E SEGURANÇA')))
        self.table.setSpan(i, 0, 1, 6)
        self.table.item(i, 0).setFont(self.utils.formatBoldText())
        i += 1
        self.table.setItem(i, 0, QTableWidgetItem(str(i - 1)))
        self.table.setItem(i, 1, QTableWidgetItem(self.translate(
            'PLACA DE SINALIZAÇAO E ADVERTENCIA,INCL.FORNEC.,TRANSP.,INSTAL.E REMOÇAO P/OUTRO LOCAL DA OBRA')))
        self.table.setItem(i, 2, QTableWidgetItem(self.translate('m²')))
        self.table.setItem(i, 3, QTableWidgetItem(self.utils.formatNum2Dec(self.quantities_calculator.get_01_01_01()))) #self.costs.get_5_2_55_qtd())))
        self.table.setCellWidget(i, 4, self.dsb_item01_unity_dollar)
        self.table.setItem(i, 5, QTableWidgetItem(
            self.utils.formatNum2Dec(self.quantities_calculator.get_01_01_01() * self.dsb_item01_unity_dollar.value())))
        i += 1
        self.table.setItem(i, 0, QTableWidgetItem(str(i - 1)))
        self.table.setItem(i, 1, QTableWidgetItem(self.translate(
            'CERCA DE PROTECAO S/ SINALIZACAO LUMINOSA C/ MONTANTES E TELA PVC')))
        self.table.setItem(i, 2, QTableWidgetItem(self.translate('m²')))
        self.table.setItem(i, 3, QTableWidgetItem(self.utils.formatNum2Dec(self.quantities_calculator.get_01_01_02()))) #self.costs.get_5_2_67_qtd())))
        self.table.setCellWidget(i, 4, self.dsb_item02_unity_dollar)
        self.table.setItem(i, 5, QTableWidgetItem(
            self.utils.formatNum2Dec(self.quantities_calculator.get_01_01_02() * self.dsb_item02_unity_dollar.value())))
        i += 1
        self.table.setItem(i, 0, QTableWidgetItem(str(i - 1)))
        self.table.setItem(i, 1, QTableWidgetItem(self.translate('PASSADICO EM MADEIRA ,P/PEDESTRES')))
        self.table.setItem(i, 2, QTableWidgetItem(self.translate('m²')))
        self.table.setItem(i, 3, QTableWidgetItem(self.utils.formatNum2Dec(self.quantities_calculator.get_01_01_03()))) #self.costs.get_6_1_4_qtd())))
        self.table.setCellWidget(i, 4, self.dsb_item03_unity_dollar)
        self.table.setItem(i, 5, QTableWidgetItem(
            self.utils.formatNum2Dec(self.quantities_calculator.get_01_01_03() * self.dsb_item03_unity_dollar.value())))
        i += 1
        self.table.setItem(i, 0, QTableWidgetItem(str(i - 1)))
        self.table.setItem(i, 1, QTableWidgetItem(
            self.translate('PASSADICO METALICO P/ VEICULOS ')))
        self.table.setItem(i, 2, QTableWidgetItem(self.translate('m²')))
        self.table.setItem(i, 3, QTableWidgetItem(self.utils.formatNum2Dec(self.quantities_calculator.get_01_01_04()))) #self.costs.get_6_2_4_qtd())))
        self.table.setCellWidget(i, 4, self.dsb_item04_unity_dollar)
        self.table.setItem(i, 5, QTableWidgetItem(
            self.utils.formatNum2Dec(self.quantities_calculator.get_01_01_04() * self.dsb_item04_unity_dollar.value())))
        i += 1
        self.table.setItem(i, 0, QTableWidgetItem(self.translate('SERVICOS TOPOGRAFICOS')))
        self.table.setSpan(i, 0, 1, 6)
        self.table.item(i, 0).setFont(self.utils.formatBoldText())
        i += 1
        self.table.setItem(i, 0, QTableWidgetItem(str(i - 2)))
        self.table.setItem(i, 1, QTableWidgetItem(self.translate(
            'SERVICOS TOPOGRAFICOS, GEOTECNICOS, INSPECAO DE MATERIAIS, DETALHAMENTO DE PROJETOS E CADASTRO ')))
        self.table.setItem(i, 2, QTableWidgetItem(self.translate('m')))
        self.table.setItem(i, 3, QTableWidgetItem(self.utils.formatNum2Dec(self.quantities_calculator.get_01_02_01()))) #self.costs.get_6_2_1_qtd())))
        self.table.setCellWidget(i, 4, self.dsb_item05_unity_dollar)
        self.table.setItem(i, 5, QTableWidgetItem(
            self.utils.formatNum2Dec(self.quantities_calculator.get_01_02_01() * self.dsb_item05_unity_dollar.value())))
        i += 1
        self.table.setItem(i, 0, QTableWidgetItem(self.translate('ESCAVACOES')))
        self.table.setSpan(i, 0, 1, 6)
        self.table.item(i, 0).setFont(self.utils.formatBoldText())
        i += 1
        self.table.setItem(i, 0, QTableWidgetItem(str(i - 3)))
        self.table.setItem(i, 1, QTableWidgetItem(self.translate('ESCAV. MANUAL DE VALAS')))
        self.table.setItem(i, 2, QTableWidgetItem(self.translate('m³')))
        self.table.setItem(i, 3, QTableWidgetItem(self.utils.formatNum2Dec(self.quantities_calculator.get_01_03_01()))) #self.costs.get_7_9_2_qtd())))
        self.table.setCellWidget(i, 4, self.dsb_item06_unity_dollar)
        self.table.setItem(i, 5, QTableWidgetItem(
            self.utils.formatNum2Dec(self.quantities_calculator.get_01_03_01() * self.dsb_item06_unity_dollar.value())))
        i += 1
        self.table.setItem(i, 0, QTableWidgetItem(str(i - 3)))
        self.table.setItem(i, 1, QTableWidgetItem(self.translate('ESCAV. MECANIZ. DE VALAS   EM SOLO')))
        self.table.setItem(i, 2, QTableWidgetItem(self.translate('m³')))
        self.table.setItem(i, 3, QTableWidgetItem(self.utils.formatNum2Dec(self.quantities_calculator.get_01_03_02()))) #self.costs.get_7_9_2_qtd())))
        self.table.setCellWidget(i, 4, self.dsb_item07_unity_dollar)
        self.table.setItem(i, 5, QTableWidgetItem(
            self.utils.formatNum2Dec(self.quantities_calculator.get_01_03_02() * self.dsb_item07_unity_dollar.value())))
        i += 1
        self.table.setItem(i, 0, QTableWidgetItem(str(i - 3)))
        self.table.setItem(i, 1, QTableWidgetItem(self.translate('ESCAV. DE VALAS - EM ROCHA')))
        self.table.setItem(i, 2, QTableWidgetItem(self.translate('m³')))
        self.table.setItem(i, 3, QTableWidgetItem(self.utils.formatNum2Dec(self.quantities_calculator.get_01_03_03()))) #self.costs.get_7_9_2_qtd())))
        self.table.setCellWidget(i, 4, self.dsb_item08_unity_dollar)
        self.table.setItem(i, 5, QTableWidgetItem(
            self.utils.formatNum2Dec(self.quantities_calculator.get_01_03_03() * self.dsb_item08_unity_dollar.value())))
        i += 1
        self.table.setItem(i, 0, QTableWidgetItem(self.translate('ATERROS E ENVOLTORIAS')))
        self.table.setSpan(i, 0, 1, 6)
        self.table.item(i, 0).setFont(self.utils.formatBoldText())
        i += 1
        self.table.setItem(i, 0, QTableWidgetItem(str(i - 4)))
        self.table.setItem(i, 1, QTableWidgetItem(self.translate(
            'EXEC. DE ATERRO EM VALAS/POÇOS/CAVAS DE FUNDAÇAO C/ SOLO PROVENIENTE DAS ESCAVAÇOES')))
        self.table.setItem(i, 2, QTableWidgetItem(self.translate('m³')))
        self.table.setItem(i, 3, QTableWidgetItem(self.utils.formatNum2Dec(self.quantities_calculator.get_01_04_01())))
        self.table.setCellWidget(i, 4, self.dsb_item09_unity_dollar)
        self.table.setItem(i, 5, QTableWidgetItem(
            self.utils.formatNum2Dec(self.quantities_calculator.get_01_04_01() * self.dsb_item09_unity_dollar.value())))
        i += 1
        self.table.setItem(i, 0, QTableWidgetItem(str(i - 4)))
        self.table.setItem(i, 1, QTableWidgetItem(
            self.translate('EXEC. DE ATERRO EM VALAS/POÇOS/CAVAS DE FUNDAÇAO, C/ FORNEC. DE SOLO')))
        self.table.setItem(i, 2, QTableWidgetItem(self.translate('m³')))
        self.table.setItem(i, 3, QTableWidgetItem(self.utils.formatNum2Dec(self.quantities_calculator.get_01_04_02())))
        self.table.setCellWidget(i, 4, self.dsb_item10_unity_dollar)
        self.table.setItem(i, 5, QTableWidgetItem(
            self.utils.formatNum2Dec(self.quantities_calculator.get_01_04_02() * self.dsb_item10_unity_dollar.value())))
        i += 1
        self.table.setItem(i, 0, QTableWidgetItem(str(i - 4)))
        self.table.setItem(i, 1, QTableWidgetItem(
            self.translate('EXEC. DE ENVOLTORIA OU BERCO DE AREIA EM VALAS')))
        self.table.setItem(i, 2, QTableWidgetItem(self.translate('m³')))
        self.table.setItem(i, 3, QTableWidgetItem(self.utils.formatNum2Dec(self.quantities_calculator.get_01_04_03())))
        self.table.setCellWidget(i, 4, self.dsb_item11_unity_dollar)
        self.table.setItem(i, 5, QTableWidgetItem(
            self.utils.formatNum2Dec(self.quantities_calculator.get_01_04_03() * self.dsb_item11_unity_dollar.value())))
        i += 1
        self.table.setItem(i, 0, QTableWidgetItem(self.translate('TRANSPORTE DE MATERIAIS')))
        self.table.setSpan(i, 0, 1, 6)
        self.table.item(i, 0).setFont(self.utils.formatBoldText())
        i += 1
        self.table.setItem(i, 0, QTableWidgetItem(str(i - 5)))
        self.table.setItem(i, 1, QTableWidgetItem(self.translate('CARGA E DESCARGA DE SOLO')))
        self.table.setItem(i, 2, QTableWidgetItem(self.translate('m³')))
        self.table.setItem(i, 3, QTableWidgetItem(self.utils.formatNum2Dec(self.quantities_calculator.get_01_05_01())))
        self.table.setCellWidget(i, 4, self.dsb_item12_unity_dollar)
        self.table.setItem(i, 5, QTableWidgetItem(
            self.utils.formatNum2Dec(self.quantities_calculator.get_01_05_01() * self.dsb_item12_unity_dollar.value())))
        i += 1
        self.table.setItem(i, 0, QTableWidgetItem(str(i - 5)))
        self.table.setItem(i, 1, QTableWidgetItem(self.translate(
            'MOMENTO DE TRANSPORTE DE SOLO, EM CAMINHAO BASCULANTE')))
        self.table.setItem(i, 2, QTableWidgetItem(self.translate('m³xkm')))
        self.table.setItem(i, 3, QTableWidgetItem(self.utils.formatNum2Dec(self.quantities_calculator.get_01_05_02())))
        self.table.setCellWidget(i, 4, self.dsb_item13_unity_dollar)
        self.table.setItem(i, 5, QTableWidgetItem(
            self.utils.formatNum2Dec(self.quantities_calculator.get_01_05_02() * self.dsb_item13_unity_dollar.value())))
        i += 1
        self.table.setItem(i, 0, QTableWidgetItem(str(i - 5)))
        self.table.setItem(i, 1, QTableWidgetItem(self.translate('CARGA E DESCARGA DE ROCHA')))
        self.table.setItem(i, 2, QTableWidgetItem(self.translate('m³')))
        self.table.setItem(i, 3, QTableWidgetItem(self.utils.formatNum2Dec(self.quantities_calculator.get_01_05_03())))
        self.table.setCellWidget(i, 4, self.dsb_item14_unity_dollar)
        self.table.setItem(i, 5, QTableWidgetItem(
            self.utils.formatNum2Dec(self.quantities_calculator.get_01_05_03() * self.dsb_item14_unity_dollar.value())))
        i += 1
        self.table.setItem(i, 0, QTableWidgetItem(str(i - 5)))
        self.table.setItem(i, 1, QTableWidgetItem(self.translate('MOMENTO DE TRANSPORTE DE ROCHA, EM CAMINHAO BASCULANTE')))
        self.table.setItem(i, 2, QTableWidgetItem(self.translate('m³xkm')))
        self.table.setItem(i, 3, QTableWidgetItem(self.utils.formatNum2Dec(self.quantities_calculator.get_01_05_04())))
        self.table.setCellWidget(i, 4, self.dsb_item15_unity_dollar)
        self.table.setItem(i, 5, QTableWidgetItem(
            self.utils.formatNum2Dec(self.quantities_calculator.get_01_05_04() * self.dsb_item15_unity_dollar.value())))
        i += 1
        self.table.setItem(i, 0, QTableWidgetItem(self.translate('CAIXAS E POCOS DE VISITA')))
        self.table.setSpan(i, 0, 1, 6)
        self.table.item(i, 0).setFont(self.utils.formatBoldText())
        i += 1
        self.table.setItem(i, 0, QTableWidgetItem(str(i - 6)))
        self.table.setItem(i, 1, QTableWidgetItem(self.translate(
            'CAIXA P/LIGACAO PREDIAL DE ESGOTO SANITARIO, EM ANEL DE CONCRETO PRE MOLDADODN=0,40m, e=7cm INCL. TAMPA DE CONCR. ARMADO C/ e=0,07m')))
        self.table.setItem(i, 2, QTableWidgetItem(self.translate('un')))
        self.table.setItem(i, 3, QTableWidgetItem(self.utils.formatNum2Dec(self.quantities_calculator.get_01_06_01())))
        self.table.setCellWidget(i, 4, self.dsb_item16_unity_dollar)
        self.table.setItem(i, 5, QTableWidgetItem(
            self.utils.formatNum2Dec(self.quantities_calculator.get_01_06_01() * self.dsb_item16_unity_dollar.value())))
        i += 1
        self.table.setItem(i, 0, QTableWidgetItem(str(i - 6)))
        self.table.setItem(i, 1, QTableWidgetItem(self.translate(
            'CAIXA P/ LIGAÇAO PREDIAL DE ESGOTO SANITARIO, EM ANEL DE CONCRETO DN=0,60m, e=7cm,INCL. TAMPA DE CONCR. ARMADO  C/ e=0,07m')))
        self.table.setItem(i, 2, QTableWidgetItem(self.translate('un')))
        self.table.setItem(i, 3, QTableWidgetItem(self.utils.formatNum2Dec(self.quantities_calculator.get_01_06_02())))
        self.table.setCellWidget(i, 4, self.dsb_item17_unity_dollar)
        self.table.setItem(i, 5, QTableWidgetItem(
            self.utils.formatNum2Dec(self.quantities_calculator.get_01_06_02() * self.dsb_item17_unity_dollar.value())))
        i += 1
        self.table.setItem(i, 0, QTableWidgetItem(str(i - 6)))
        self.table.setItem(i, 1, QTableWidgetItem(self.translate(
            'CAIXA P/LIGACAO PREDIAL DE ESGOTO SANITARIO,EM ALVENARIA DE TIJOLO MACICO, C/ FORNEC. E ASSENT. DE TAMPA DE CONCRETO')))
        self.table.setItem(i, 2, QTableWidgetItem(self.translate('un')))
        self.table.setItem(i, 3, QTableWidgetItem(self.utils.formatNum2Dec(self.quantities_calculator.get_01_06_03())))
        self.table.setCellWidget(i, 4, self.dsb_item18_unity_dollar)
        self.table.setItem(i, 5, QTableWidgetItem(
            self.utils.formatNum2Dec(self.quantities_calculator.get_01_06_03() * self.dsb_item18_unity_dollar.value())))
        i += 1
        self.table.setItem(i, 0, QTableWidgetItem(str(i - 6)))
        self.table.setItem(i, 1, QTableWidgetItem(self.translate(
            'CAIXA P/LIGACAO PREDIAL DE ESGOTO SANITARIO,DE CONCRETO ARMADO, e=0,07 m,C/ FORNEC.E ASSENT.DE TAMPA')))
        self.table.setItem(i, 2, QTableWidgetItem(self.translate('un')))
        self.table.setItem(i, 3, QTableWidgetItem(self.utils.formatNum2Dec(self.quantities_calculator.get_01_06_04())))
        self.table.setCellWidget(i, 4, self.dsb_item19_unity_dollar)
        self.table.setItem(i, 5, QTableWidgetItem(
            self.utils.formatNum2Dec(self.quantities_calculator.get_01_06_04() * self.dsb_item19_unity_dollar.value())))
        i += 1
        self.table.setItem(i, 0, QTableWidgetItem(str(i - 6)))
        self.table.setItem(i, 1, QTableWidgetItem(self.translate(
            'DISPOSITIVO DE PASSAGEM P/ ESGOT. SANITARIO, SIMILAR TIL DE PASSAGEM , C/ FORNEC. DO MAT. E ANEL')))
        self.table.setItem(i, 2, QTableWidgetItem(self.translate('un')))
        self.table.setItem(i, 3, QTableWidgetItem(self.utils.formatNum2Dec(self.quantities_calculator.get_01_06_05())))
        self.table.setCellWidget(i, 4, self.dsb_item20_unity_dollar)
        self.table.setItem(i, 5, QTableWidgetItem(
            self.utils.formatNum2Dec(self.quantities_calculator.get_01_06_05() * self.dsb_item20_unity_dollar.value())))
        i += 1
        self.table.setItem(i, 0, QTableWidgetItem(self.translate('DEMOLICOES')))
        self.table.setSpan(i, 0, 1, 6)
        self.table.item(i, 0).setFont(self.utils.formatBoldText())
        i += 1
        self.table.setItem(i, 0, QTableWidgetItem(str(i - 7)))
        self.table.setItem(i, 1, QTableWidgetItem(self.translate(
            'DEMOLICAO E RECOMPOSIÇÃO DE PASSEIO EM PISO CERÂMICO,ARDOSIA E MARMORE')))
        self.table.setItem(i, 2, QTableWidgetItem(self.translate('m²')))
        self.table.setItem(i, 3, QTableWidgetItem(self.utils.formatNum2Dec(self.quantities_calculator.get_01_07_01())))
        self.table.setCellWidget(i, 4, self.dsb_item21_unity_dollar)
        self.table.setItem(i, 5, QTableWidgetItem(
            self.utils.formatNum2Dec(self.quantities_calculator.get_01_07_01() * self.dsb_item21_unity_dollar.value())))
        i += 1
        self.table.setItem(i, 0, QTableWidgetItem(str(i - 7)))
        self.table.setItem(i, 1, QTableWidgetItem(self.translate(
            'DEMOLIÇÃO E RECOMPOSIÇÃO  DE PLACAS PRE-MOLDADAS DE CONCRETO EM PASSEIO')))
        self.table.setItem(i, 2, QTableWidgetItem(self.translate('m²')))
        self.table.setItem(i, 3, QTableWidgetItem(self.utils.formatNum2Dec(self.quantities_calculator.get_01_07_02())))
        self.table.setCellWidget(i, 4, self.dsb_item22_unity_dollar)
        self.table.setItem(i, 5, QTableWidgetItem(
            self.utils.formatNum2Dec(self.quantities_calculator.get_01_07_02() * self.dsb_item22_unity_dollar.value())))
        i += 1
        self.table.setItem(i, 0, QTableWidgetItem(str(i - 7)))
        self.table.setItem(i, 1, QTableWidgetItem(self.translate(
            'DEMOLIÇÃO E RECOMPOSIÇÃO DE PARALELEPIPEDO OU PEDRA IRREGULAR')))
        self.table.setItem(i, 2, QTableWidgetItem(self.translate('m²')))
        self.table.setItem(i, 3, QTableWidgetItem(self.utils.formatNum2Dec(self.quantities_calculator.get_01_07_03())))
        self.table.setCellWidget(i, 4, self.dsb_item23_unity_dollar)
        self.table.setItem(i, 5, QTableWidgetItem(
            self.utils.formatNum2Dec(self.quantities_calculator.get_01_07_03() * self.dsb_item23_unity_dollar.value())))
        i += 1
        self.table.setItem(i, 0, QTableWidgetItem(str(i - 7)))
        self.table.setItem(i, 1, QTableWidgetItem(self.translate('RETIRADA E PLANTIO DE GRAMA')))
        self.table.setItem(i, 2, QTableWidgetItem(self.translate('m²')))
        self.table.setItem(i, 3, QTableWidgetItem(self.utils.formatNum2Dec(self.quantities_calculator.get_01_07_04())))
        self.table.setCellWidget(i, 4, self.dsb_item24_unity_dollar)
        self.table.setItem(i, 5, QTableWidgetItem(
            self.utils.formatNum2Dec(self.quantities_calculator.get_01_07_04() * self.dsb_item24_unity_dollar.value())))
        i += 1
        self.table.setItem(i, 0, QTableWidgetItem(str(i - 7)))
        self.table.setItem(i, 1, QTableWidgetItem(self.translate(
            'DEMOLIÇÃO E RECOMPOSIÇÃO DE PAVIMENTO EM ASFALTO')))
        self.table.setItem(i, 2, QTableWidgetItem(self.translate('m²')))
        self.table.setItem(i, 3, QTableWidgetItem(self.utils.formatNum2Dec(self.quantities_calculator.get_01_07_05())))
        self.table.setCellWidget(i, 4, self.dsb_item25_unity_dollar)
        self.table.setItem(i, 5, QTableWidgetItem(
            self.utils.formatNum2Dec(self.quantities_calculator.get_01_07_05() * self.dsb_item25_unity_dollar.value())))
        i += 1
        self.table.setItem(i, 0, QTableWidgetItem(str(i - 7)))
        self.table.setItem(i, 1, QTableWidgetItem(self.translate(
            'DEMOLIÇÃO E RECOMPOSIÇÃO  DE BLOCO ARTICULADO DE CONCRETO (INTERTRAVADO)')))
        self.table.setItem(i, 2, QTableWidgetItem(self.translate('m²')))
        self.table.setItem(i, 3, QTableWidgetItem(self.utils.formatNum2Dec(self.quantities_calculator.get_01_07_06())))
        self.table.setCellWidget(i, 4, self.dsb_item26_unity_dollar)
        self.table.setItem(i, 5, QTableWidgetItem(
            self.utils.formatNum2Dec(self.quantities_calculator.get_01_07_06() * self.dsb_item26_unity_dollar.value())))
        i += 1
        self.table.setItem(i, 0, QTableWidgetItem(str(i - 7)))
        self.table.setItem(i, 1, QTableWidgetItem(self.translate(
            'DEMOLIÇAO E RECOMPOSIÇÃO  DE PISO CIMENTADO SOBRE LASTRO DE CONCRETO SIMPLES')))
        self.table.setItem(i, 2, QTableWidgetItem(self.translate('m²')))
        self.table.setItem(i, 3, QTableWidgetItem(self.utils.formatNum2Dec(self.quantities_calculator.get_01_07_07())))
        self.table.setCellWidget(i, 4, self.dsb_item27_unity_dollar)
        self.table.setItem(i, 5, QTableWidgetItem(
            self.utils.formatNum2Dec(self.quantities_calculator.get_01_07_07() * self.dsb_item27_unity_dollar.value())))
        i += 1
        self.table.setItem(i, 0, QTableWidgetItem(str(i - 7)))
        self.table.setItem(i, 1, QTableWidgetItem(self.translate(
            'DEMOLICAO E RECOMPOSIÇÃO DE PAVIMENTO EM CONCRETO SIMPLES')))
        self.table.setItem(i, 2, QTableWidgetItem(self.translate('m²')))
        self.table.setItem(i, 3, QTableWidgetItem(self.utils.formatNum2Dec(self.quantities_calculator.get_01_07_08())))
        self.table.setCellWidget(i, 4, self.dsb_item28_unity_dollar)
        self.table.setItem(i, 5, QTableWidgetItem(
            self.utils.formatNum2Dec(self.quantities_calculator.get_01_07_08() * self.dsb_item28_unity_dollar.value())))
        i += 1
        self.table.setItem(i, 0, QTableWidgetItem(str(i - 7)))
        self.table.setItem(i, 1, QTableWidgetItem(self.translate(
            'DEMOLICAO E RECOMPOSIÇÃO DE PAVIMENTO EM CONCRETO REFORÇADO')))
        self.table.setItem(i, 2, QTableWidgetItem(self.translate('m²')))
        self.table.setItem(i, 3, QTableWidgetItem(self.utils.formatNum2Dec(self.quantities_calculator.get_01_07_09())))
        self.table.setCellWidget(i, 4, self.dsb_item29_unity_dollar)
        self.table.setItem(i, 5, QTableWidgetItem(
            self.utils.formatNum2Dec(self.quantities_calculator.get_01_07_09() * self.dsb_item29_unity_dollar.value())))
        i += 1
        self.table.setItem(i, 0, QTableWidgetItem(str(i - 7)))
        self.table.setItem(i, 1, QTableWidgetItem(self.translate(
            'LEVANTAMENTOE RECOMPOSIÇÃO  DE PEDRA PORTUGUESA')))
        self.table.setItem(i, 2, QTableWidgetItem(self.translate('m²')))
        self.table.setItem(i, 3, QTableWidgetItem(self.utils.formatNum2Dec(self.quantities_calculator.get_01_07_10())))
        self.table.setCellWidget(i, 4, self.dsb_item30_unity_dollar)
        self.table.setItem(i, 5, QTableWidgetItem(
            self.utils.formatNum2Dec(self.quantities_calculator.get_01_07_10() * self.dsb_item30_unity_dollar.value())))
        i += 1
        self.table.setItem(i, 0, QTableWidgetItem(self.translate('SERVICOS DIVERSOS')))
        self.table.setSpan(i, 0, 1, 6)
        self.table.item(i, 0).setFont(self.utils.formatBoldText())
        i += 1
        self.table.setItem(i, 0, QTableWidgetItem(str(i - 8)))
        self.table.setItem(i, 1, QTableWidgetItem(self.translate(
            'EXEC. DE  ENVELOPAMENTO C/ CONCRETO SIMPLES, INCL. FORNEC. DE MAT., PRODUCAO, TRANSP.MANUAL., LANC. VERT., ADENS., CURA E FORMA')))
        self.table.setItem(i, 2, QTableWidgetItem(self.translate('m³')))
        self.table.setItem(i, 3, QTableWidgetItem(self.utils.formatNum2Dec(self.quantities_calculator.get_01_08_01())))
        self.table.setCellWidget(i, 4, self.dsb_item31_unity_dollar)
        self.table.setItem(i, 5, QTableWidgetItem(
            self.utils.formatNum2Dec(self.quantities_calculator.get_01_08_01() * self.dsb_item31_unity_dollar.value())))
        i += 1
        self.table.setItem(i, 0, QTableWidgetItem(self.translate('ASSENTAMENTO DE TUBULACOES')))
        self.table.setSpan(i, 0, 1, 6)
        self.table.item(i, 0).setFont(self.utils.formatBoldText())
        i += 1
        self.table.setItem(i, 0, QTableWidgetItem(str(i - 9)))
        self.table.setItem(i, 1, QTableWidgetItem(self.translate(
            'ASSENT. DE TUBOS EM PVC RIG OU PEAD. PB JE- ESGOTO - DN   100 mm')))
        self.table.setItem(i, 2, QTableWidgetItem(self.translate('m')))
        self.table.setItem(i, 3, QTableWidgetItem(self.utils.formatNum2Dec(self.quantities_calculator.get_01_09_01())))
        self.table.setCellWidget(i, 4, self.dsb_item32_unity_dollar)
        self.table.setItem(i, 5, QTableWidgetItem(
            self.utils.formatNum2Dec(self.quantities_calculator.get_01_09_01() * self.dsb_item32_unity_dollar.value())))
        i += 1
        self.table.setItem(i, 0, QTableWidgetItem(str(i - 9)))
        self.table.setItem(i, 1, QTableWidgetItem(self.translate(
            'ASSENT. DE TUBOS EM PVC RIG OU PEAD. PB JE- ESGOTO - DN   150 mm')))
        self.table.setItem(i, 2, QTableWidgetItem(self.translate('m')))
        self.table.setItem(i, 3, QTableWidgetItem(self.utils.formatNum2Dec(self.quantities_calculator.get_01_09_02())))
        self.table.setCellWidget(i, 4, self.dsb_item33_unity_dollar)
        self.table.setItem(i, 5, QTableWidgetItem(
            self.utils.formatNum2Dec(self.quantities_calculator.get_01_09_02() * self.dsb_item33_unity_dollar.value())))
        i += 1
        self.table.setItem(i, 0, QTableWidgetItem(self.translate('MATERIAIS')))
        self.table.setSpan(i, 0, 1, 6)
        self.table.item(i, 0).setFont(self.utils.formatBoldText())
        i += 1
        self.table.setItem(i, 0, QTableWidgetItem(self.translate('TUBULAÇÕES')))
        self.table.setSpan(i, 0, 1, 6)
        self.table.item(i, 0).setFont(self.utils.formatBoldText())
        i += 1
        self.table.setItem(i, 0, QTableWidgetItem(str(i - 11)))
        self.table.setItem(i, 1, QTableWidgetItem(self.translate('TUBO ES PVC OU PEAD PB JE P/ ESG. DN 100')))
        self.table.setItem(i, 2, QTableWidgetItem(self.translate('m')))
        self.table.setItem(i, 3, QTableWidgetItem(self.utils.formatNum2Dec(self.quantities_calculator.get_02_01_01())))
        self.table.setCellWidget(i, 4, self.dsb_item34_unity_dollar)
        self.table.setItem(i, 5, QTableWidgetItem(
            self.utils.formatNum2Dec(self.quantities_calculator.get_02_01_01() * self.dsb_item34_unity_dollar.value())))
        i += 1
        self.table.setItem(i, 0, QTableWidgetItem(str(i - 11)))
        self.table.setItem(i, 1, QTableWidgetItem(self.translate('TUBO ES PVC OU PEAD PB JE P/ ESG. DN 150')))
        self.table.setItem(i, 2, QTableWidgetItem(self.translate('m')))
        self.table.setItem(i, 3, QTableWidgetItem(self.utils.formatNum2Dec(self.quantities_calculator.get_02_01_02())))
        self.table.setCellWidget(i, 4, self.dsb_item35_unity_dollar)
        self.table.setItem(i, 5, QTableWidgetItem(
            self.utils.formatNum2Dec(self.quantities_calculator.get_02_01_02() * self.dsb_item35_unity_dollar.value())))
        i += 1
        self.table.setItem(i, 0, QTableWidgetItem(self.translate('PECAS E CONEXOES')))
        self.table.setSpan(i, 0, 1, 6)
        self.table.item(i, 0).setFont(self.utils.formatBoldText())
        i += 1
        self.table.setItem(i, 0, QTableWidgetItem(str(i - 12)))
        self.table.setItem(i, 1, QTableWidgetItem(self.translate('SELIM ES PVC JE')))
        self.table.setItem(i, 2, QTableWidgetItem(self.translate('pc')))
        self.table.setItem(i, 3, QTableWidgetItem(self.utils.formatNum2Dec(self.quantities_calculator.get_02_02_01())))
        self.table.setCellWidget(i, 4, self.dsb_item36_unity_dollar)
        self.table.setItem(i, 5, QTableWidgetItem(
            self.utils.formatNum2Dec(self.quantities_calculator.get_02_02_01() * self.dsb_item36_unity_dollar.value())))
        i += 1
        self.table.setItem(i, 0, QTableWidgetItem(str(i - 12)))
        self.table.setItem(i, 1, QTableWidgetItem(self.translate('C90 ES PVC PB JE DN 100')))
        self.table.setItem(i, 2, QTableWidgetItem(self.translate('pc')))
        self.table.setItem(i, 3, QTableWidgetItem(self.utils.formatNum2Dec(self.quantities_calculator.get_02_02_02())))
        self.table.setCellWidget(i, 4, self.dsb_item37_unity_dollar)
        self.table.setItem(i, 5, QTableWidgetItem(
            self.utils.formatNum2Dec(self.quantities_calculator.get_02_02_02() * self.dsb_item37_unity_dollar.value())))
        i += 1
        self.table.setItem(i, 0, QTableWidgetItem(str(i - 12)))
        self.table.setItem(i, 1, QTableWidgetItem(self.translate('C90 ES PVC PB JE DN 150')))
        self.table.setItem(i, 2, QTableWidgetItem(self.translate('pc')))
        self.table.setItem(i, 3, QTableWidgetItem(self.utils.formatNum2Dec(self.quantities_calculator.get_02_02_03())))
        self.table.setCellWidget(i, 4, self.dsb_item38_unity_dollar)
        self.table.setItem(i, 5, QTableWidgetItem(
            self.utils.formatNum2Dec(self.quantities_calculator.get_02_02_03() * self.dsb_item38_unity_dollar.value())))
        i += 1
        self.table.setItem(i, 0, QTableWidgetItem(str(i - 12)))
        self.table.setItem(i, 1, QTableWidgetItem(self.translate('TE ES PVC BBB JE DN 100')))
        self.table.setItem(i, 2, QTableWidgetItem(self.translate('pc')))
        self.table.setItem(i, 3, QTableWidgetItem(self.utils.formatNum2Dec(self.quantities_calculator.get_02_02_04())))
        self.table.setCellWidget(i, 4, self.dsb_item39_unity_dollar)
        self.table.setItem(i, 5, QTableWidgetItem(
            self.utils.formatNum2Dec(self.quantities_calculator.get_02_02_04() * self.dsb_item39_unity_dollar.value())))
        i += 1
        self.table.setItem(i, 0, QTableWidgetItem(str(i - 12)))
        self.table.setItem(i, 1, QTableWidgetItem(self.translate('TE ES PVC BBB JE DN 150')))
        self.table.setItem(i, 2, QTableWidgetItem(self.translate('pc')))
        self.table.setItem(i, 3, QTableWidgetItem(self.utils.formatNum2Dec(self.quantities_calculator.get_02_02_05())))
        self.table.setCellWidget(i, 4, self.dsb_item40_unity_dollar)
        self.table.setItem(i, 5, QTableWidgetItem(
            self.utils.formatNum2Dec(self.quantities_calculator.get_02_02_05() * self.dsb_item40_unity_dollar.value())))
        i += 1
        # Conectando os sinais usando uma única função com lambdas
        # as adições sao para contar as linhas de cabeçalho
        for index in range(0, 4):  # SINALIZAÇÃO E SEGURANÇA
            self.dsb_list_entrance[index].valueChanged.connect(
                lambda _, item_index=index: self.set_item(item_index, item_index + 2))
        for index in range(4, 5):  # SERVIÇOS TOPOGRÁFICOS
            self.dsb_list_entrance[index].valueChanged.connect(
                lambda _, item_index=index: self.set_item(item_index, item_index + 3))
        for index in range(5, 8):  # ESCAVAÇÕES
            self.dsb_list_entrance[index].valueChanged.connect(
                lambda _, item_index=index: self.set_item(item_index, item_index + 4))
        for index in range(8, 11):  # ATERROS E ENVOLTÓRIAS
            self.dsb_list_entrance[index].valueChanged.connect(
                lambda _, item_index=index: self.set_item(item_index, item_index + 5))
        for index in range(11, 15):  # TRANSPORTE DE MATERIAIS
            self.dsb_list_entrance[index].valueChanged.connect(
                lambda _, item_index=index: self.set_item(item_index, item_index + 6))
        for index in range(15, 20):  # CAIXAS E POÇOS DE VISITA
            self.dsb_list_entrance[index].valueChanged.connect(
                lambda _, item_index=index: self.set_item(item_index, item_index + 7))
        for index in range(20, 30):  # DEMOLIÇÕES
            self.dsb_list_entrance[index].valueChanged.connect(
                lambda _, item_index=index: self.set_item(item_index, item_index + 8))
        for index in range(30, 31):  # SERVIÇOS DIVERSOS
            self.dsb_list_entrance[index].valueChanged.connect(
                lambda _, item_index=index: self.set_item(item_index, item_index + 9))
        for index in range(31, 33):  # ASSENTAMENTO DE TUBULAÇÕES
            self.dsb_list_entrance[index].valueChanged.connect(
                lambda _, item_index=index: self.set_item(item_index, item_index + 10))
        for index in range(33, 35):  # TUBULAÇÕES
            self.dsb_list_entrance[index].valueChanged.connect(
                lambda _, item_index=index: self.set_item(item_index, item_index + 12))
        for index in range(35, 40):  # PEÇAS E CONEXÕES
            self.dsb_list_entrance[index].valueChanged.connect(
                lambda _, item_index=index: self.set_item(item_index, item_index + 13))





    def set_item(self, dsb_index, table_index):
        price_methods = [method for method in dir(self.quantities_calculator) if method.startswith('get_')]
        price_methods.sort()
        value = self.dsb_list_entrance[dsb_index].value()

        # Atualizando a lista de custos
        self.quantities_calculator.costs.SERVICES[dsb_index] = value
        value *= getattr(self.quantities_calculator, price_methods[dsb_index])()

        # Atualizando a tabela
        self.table.setItem(
            table_index, 5, QTableWidgetItem(self.utils.formatNum2Dec(value))
        )


        # Atualizando o spin box com o novo valor
        #self.dsb_list_entrance[item_index].setValue(value)

    def checkData(self):
        # Verifica se todos os itens têm valores diferentes de 0
        for i in range(40):  # De 1 a 40
            spin_box = self.dsb_list_entrance[i]
            if spin_box is None or spin_box.value() == 0:
                return False
        return True

    def saveChanges(self):
        print("saveChanges called")
        if self.checkData():
            for i in range(40):
                value = self.dsb_list_entrance[i].value()
                self.quantities_calculator.costs.SERVICES[i - 1] = value

            icon = QMessageBox.Information
            self.utils.show_dialog(self.title, self.translate('Dados alterados com sucesso!'), icon)
            self.screen.close()
        else:
            icon = QMessageBox.Critical
            self.utils.show_dialog(self.title, self.translate('Existe serviços com valores zerados.'), icon)


class AlignDelegate(QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = Qt.AlignCenter