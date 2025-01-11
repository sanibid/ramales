import os

from PyQt5.QtCore import QLocale, QCoreApplication
from qgis._core import QgsProject
from xlwt import Workbook, easyxf

from ...core.data.data_manager import ProjectDataManager
from ...helpers.utils import Utils


class ProducesReportCostsXls:

    def tr(self, message):
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('SanihubRamales', message)

    def __init__(self):
        self.data_json = None
        self.segments = None
        self.loc = QLocale()
        self.MAX_COLUMN = 6
        self.utils = Utils()

    def generate_report_costs(self, local_file):
        local_file = os.path.normpath(local_file)
        blocks = QgsProject.instance().mapLayer(ProjectDataManager.get_layers_id().BLOCKS_LAYER_ID)
        blocks_fields = [field.name() for field in blocks.fields()]
        blocks_values = [f.attributes() for f in blocks.getFeatures()]
        blocks_dict = dict(zip(blocks_fields, blocks_values[0]))
        # list_block_values = list(blocks_dict.values())
        node = []
        node_lyr = QgsProject.instance().mapLayer(ProjectDataManager.get_layers_id().NODES_LAYER_ID)
        all_node = node_lyr.getFeatures()
        for n in all_node:
            node.append(n)
        self.segments = QgsProject.instance().mapLayer(ProjectDataManager.get_layers_id().SEGMENTS_LAYER_ID)
        all_seg = self.segments.getFeatures()
        segment = []
        for s in all_seg:
            segment.append(s)
        segment = sorted(segment, key=lambda item:
        (item[self.utils.get_idx_attr(self.segments, 'segments', 'branch_id')],
         item[self.utils.get_idx_attr(self.segments, 'segments', 'segment_id')]))
        branch = []
        for feat in segment:
            branch.append(feat[self.utils.get_idx_attr_segments('branch_id')])

        branch = set(branch)
        workbook = Workbook()
        worksheet = workbook.add_sheet('CUSTOS', cell_overwrite_ok=True)
        worksheet.set_fit_num_pages(1)
        worksheet.show_grid = False

        worksheet.col(0).width = 1000
        worksheet.col(1).width = 2000
        worksheet.col(2).width = 12000
        worksheet.col(4).width = 4000
        worksheet.col(5).width = 3000
        worksheet.col(6).width = 5000

        worksheet.row(8).height_mismatch = True
        worksheet.row(8).height = 800
        worksheet.write(2, 1, self.tr('BACIA:'))
        worksheet.write(3, 1, self.tr('LOCAL:'))
        worksheet.write(4, 1, self.tr('QUADRA:'))
        worksheet.write(5, 1, self.tr('DATA:'))

        worksheet.write_merge(7, 7, 1, self.MAX_COLUMN, self.tr('ORÇAMENTO RAMAIS'), TEXT_BOLD_CENTER_12_BORDER)

        worksheet.write(8, 1, self.tr('ITEM'), TEXT_BOLD_CENTER_10_BORDER)
        worksheet.write(8, 2, self.tr('DESCRIÇÃO DOS SERVIÇOS'), TEXT_BOLD_CENTER_10_BORDER)
        worksheet.write(8, 3, self.tr('UN'), TEXT_BOLD_CENTER_10_BORDER)
        worksheet.write(8, 4, self.tr('QUANTIDADE'), TEXT_BOLD_CENTER_10_BORDER)
        worksheet.write(8, 5, self.tr('P. UNIT USD'), TEXT_BOLD_CENTER_10_BORDER)
        worksheet.write(8, 6, self.tr('VALOR'), TEXT_BOLD_CENTER_10_BORDER)

        worksheet.write(9, 1, self.tr('01'), TEXT_BOLD_LEFT_10_BORDER)
        worksheet.write(9, 2, self.tr('SERVIÇOS'), TEXT_BOLD_LEFT_10_BORDER)
        worksheet.write(9, 3, '', TEXT_NORMAL_CENTER)
        worksheet.write(9, 4, '', TEXT_NORMAL_CENTER)
        worksheet.write(9, 5, '', TEXT_NORMAL_CENTER)
        worksheet.write(9, 6, '', TEXT_NORMAL_CENTER)

        worksheet.write(10, 1, self.tr('01.01'), TEXT_BOLD_LEFT_10_BORDER)
        worksheet.write(10, 2, self.tr('SINALIZAÇÃO E SEGURANÇA'), TEXT_BOLD_LEFT_10_BORDER)
        worksheet.write(10, 3, '', TEXT_NORMAL_CENTER)
        worksheet.write(10, 4, '', TEXT_NORMAL_CENTER)
        worksheet.write(10, 5, '', TEXT_NORMAL_CENTER)
        worksheet.write(10, 6, '', TEXT_NORMAL_CENTER)

        worksheet.write(11, 1, self.tr('01.01.01'), TEXT_NORMAL_LEFT)
        worksheet.write(11, 2, self.tr('PLACA DE SINALIZAÇAO E ADVERTENCIA,INCL.FORNEC., TRANSP., INSTAL.E REMOÇAO '
                                       'P/OUTRO LOCAL DA OBRA '), TEXT_NORMAL_LEFT)
        worksheet.write(11, 3, self.tr('m²'), TEXT_NORMAL_CENTER)
        worksheet.write(11, 4, '', TEXT_NORMAL_RIGHT)
        worksheet.write(11, 5, '', TEXT_NORMAL_RIGHT)
        worksheet.write(11, 6, '', TEXT_NORMAL_RIGHT)

        worksheet.write(12, 1, self.tr('01.01.02'), TEXT_NORMAL_LEFT)
        worksheet.write(12, 2, self.tr('CERCA DE PROTECAO S/ SINALIZACAO LUMINOSA C/ MONTANTES E TELA PVC'),
                        TEXT_NORMAL_LEFT)
        worksheet.write(12, 3, self.tr('m²'), TEXT_NORMAL_CENTER)
        worksheet.write(12, 4, '', TEXT_NORMAL_RIGHT)
        worksheet.write(12, 5, '', TEXT_NORMAL_RIGHT)
        worksheet.write(12, 6, '', TEXT_NORMAL_RIGHT)

        worksheet.write(13, 1, self.tr('01.01.03'), TEXT_NORMAL_LEFT)
        worksheet.write(13, 2, self.tr('PASSADICO EM MADEIRA, P/PEDESTRES'), TEXT_NORMAL_LEFT)
        worksheet.write(13, 3, self.tr('m²'), TEXT_NORMAL_CENTER)
        worksheet.write(13, 4, '', TEXT_NORMAL_RIGHT)
        worksheet.write(13, 5, '', TEXT_NORMAL_RIGHT)
        worksheet.write(13, 6, '', TEXT_NORMAL_RIGHT)

        worksheet.write(14, 1, self.tr('01.01.04'), TEXT_NORMAL_LEFT)
        worksheet.write(14, 2, self.tr('PASSADICO METALICO P/ VEICULOS'), TEXT_NORMAL_LEFT)
        worksheet.write(14, 3, self.tr('m²'), TEXT_NORMAL_CENTER)
        worksheet.write(14, 4, '', TEXT_NORMAL_RIGHT)
        worksheet.write(14, 5, '', TEXT_NORMAL_RIGHT)
        worksheet.write(14, 6, '', TEXT_NORMAL_RIGHT)

        worksheet.write(15, 1, self.tr('01.02'), TEXT_BOLD_LEFT_10_BORDER)
        worksheet.write(15, 2, self.tr('SERVICOS TOPOGRAFICOS'), TEXT_BOLD_LEFT_10_BORDER)
        worksheet.write(15, 3, '', TEXT_NORMAL_RIGHT)
        worksheet.write(15, 4, '', TEXT_NORMAL_RIGHT)
        worksheet.write(15, 5, '', TEXT_NORMAL_RIGHT)
        worksheet.write(15, 6, '', TEXT_NORMAL_RIGHT)

        worksheet.write(16, 1, self.tr('01.02.01'), TEXT_NORMAL_LEFT)
        worksheet.write(16, 2, self.tr('SERVICOS TOPOGRAFICOS, GEOTECNICOS, INSPECAO DE MATERIAIS, '
                                       'DETALHAMENTO DE PROJETOS E CADASTRO '), TEXT_NORMAL_LEFT)
        worksheet.write(16, 3, self.tr('m'), TEXT_NORMAL_CENTER)
        worksheet.write(16, 4, '', TEXT_NORMAL_RIGHT)
        worksheet.write(16, 5, '', TEXT_NORMAL_RIGHT)
        worksheet.write(16, 6, '', TEXT_NORMAL_RIGHT)

        worksheet.write(17, 1, self.tr('01.03'), TEXT_BOLD_LEFT_10_BORDER)
        worksheet.write(17, 2, self.tr('ESCAVACOES'), TEXT_BOLD_LEFT_10_BORDER)
        worksheet.write(17, 3, '', TEXT_NORMAL_RIGHT)
        worksheet.write(17, 4, '', TEXT_NORMAL_RIGHT)
        worksheet.write(17, 5, '', TEXT_NORMAL_RIGHT)
        worksheet.write(17, 6, '', TEXT_NORMAL_RIGHT)

        worksheet.write(18, 1, self.tr('01.03.01'), TEXT_NORMAL_LEFT)
        worksheet.write(18, 2, self.tr('ESCAV. MANUAL DE VALAS'), TEXT_NORMAL_LEFT)
        worksheet.write(18, 3, self.tr('m³'), TEXT_NORMAL_CENTER)
        worksheet.write(18, 4, '', TEXT_NORMAL_RIGHT)
        worksheet.write(18, 5, '', TEXT_NORMAL_RIGHT)
        worksheet.write(18, 6, '', TEXT_NORMAL_RIGHT)

        worksheet.write(19, 1, self.tr('01.03.02'), TEXT_NORMAL_LEFT)
        worksheet.write(19, 2, self.tr('ESCAV. MECANIZ. DE VALAS   EM SOLO'), TEXT_NORMAL_LEFT)
        worksheet.write(19, 3, self.tr('m³'), TEXT_NORMAL_CENTER)
        worksheet.write(19, 4, '', TEXT_NORMAL_RIGHT)
        worksheet.write(19, 5, '', TEXT_NORMAL_RIGHT)
        worksheet.write(19, 6, '', TEXT_NORMAL_RIGHT)

        worksheet.write(20, 1, self.tr('01.03.03'), TEXT_NORMAL_LEFT)
        worksheet.write(20, 2, self.tr('ESCAV. DE VALAS - EM ROCHA'), TEXT_NORMAL_LEFT)
        worksheet.write(20, 3, self.tr('m³'), TEXT_NORMAL_CENTER)
        worksheet.write(20, 4, '', TEXT_NORMAL_RIGHT)
        worksheet.write(20, 5, '', TEXT_NORMAL_RIGHT)
        worksheet.write(20, 6, '', TEXT_NORMAL_RIGHT)

        worksheet.write(21, 1, self.tr('01.04'), TEXT_BOLD_LEFT_10_BORDER)
        worksheet.write(21, 2, self.tr('ATERROS E ENVOLTORIAS'), TEXT_BOLD_LEFT_10_BORDER)
        worksheet.write(21, 3, '', TEXT_NORMAL_RIGHT)
        worksheet.write(21, 4, '', TEXT_NORMAL_RIGHT)
        worksheet.write(21, 5, '', TEXT_NORMAL_RIGHT)
        worksheet.write(21, 6, '', TEXT_NORMAL_RIGHT)

        worksheet.write(22, 1, self.tr('01.04.01'), TEXT_NORMAL_LEFT)
        worksheet.write(22, 2, self.tr('EXEC. DE ATERRO EM VALAS/POÇOS/CAVAS DE FUNDAÇAO C/ SOLO '
                                       'PROVENIENTE DAS ESCAVAÇOES'), TEXT_NORMAL_LEFT)
        worksheet.write(22, 3, self.tr('m³'), TEXT_NORMAL_CENTER)
        worksheet.write(22, 4, '', TEXT_NORMAL_RIGHT)
        worksheet.write(22, 5, '', TEXT_NORMAL_RIGHT)
        worksheet.write(22, 6, '', TEXT_NORMAL_RIGHT)

        worksheet.write(23, 1, self.tr('01.04.02'), TEXT_NORMAL_LEFT)
        worksheet.write(23, 2, self.tr('EXEC. DE ATERRO EM VALAS/POÇOS/CAVAS DE FUNDAÇAO, C/ FORNEC. DE SOLO'),
                        TEXT_NORMAL_LEFT)
        worksheet.write(23, 3, self.tr('m³'), TEXT_NORMAL_CENTER)
        worksheet.write(23, 4, '', TEXT_NORMAL_RIGHT)
        worksheet.write(23, 5, '', TEXT_NORMAL_RIGHT)
        worksheet.write(23, 6, '', TEXT_NORMAL_RIGHT)

        worksheet.write(24, 1, self.tr('01.04.03'), TEXT_NORMAL_LEFT)
        worksheet.write(24, 2, self.tr('EXEC. DE ENVOLTORIA OU BERCO DE AREIA EM VALAS'), TEXT_NORMAL_LEFT)
        worksheet.write(24, 3, self.tr('m³'), TEXT_NORMAL_CENTER)
        worksheet.write(24, 4, '', TEXT_NORMAL_RIGHT)
        worksheet.write(24, 5, '', TEXT_NORMAL_RIGHT)
        worksheet.write(24, 6, '', TEXT_NORMAL_RIGHT)

        worksheet.write(25, 1, self.tr('01.05'), TEXT_BOLD_LEFT_10_BORDER)
        worksheet.write(25, 2, self.tr('TRANSPORTE DE MATERIAIS'), TEXT_BOLD_LEFT_10_BORDER)
        worksheet.write(25, 3, '', TEXT_NORMAL_LEFT)
        worksheet.write(25, 4, '', TEXT_NORMAL_LEFT)
        worksheet.write(25, 5, '', TEXT_NORMAL_LEFT)
        worksheet.write(25, 6, '', TEXT_NORMAL_LEFT)

        worksheet.write(26, 1, self.tr('01.05.01'), TEXT_NORMAL_LEFT)
        worksheet.write(26, 2, self.tr('CARGA E DESCARGA DE SOLO'), TEXT_NORMAL_LEFT)
        worksheet.write(26, 3, self.tr('m³'), TEXT_NORMAL_CENTER)
        worksheet.write(26, 4, '', TEXT_NORMAL_RIGHT)
        worksheet.write(26, 5, '', TEXT_NORMAL_RIGHT)
        worksheet.write(26, 6, '', TEXT_NORMAL_RIGHT)

        worksheet.write(27, 1, self.tr('01.05.02'), TEXT_NORMAL_LEFT)
        worksheet.write(27, 2, self.tr('MOMENTO DE TRANSPORTE DE SOLO, EM CAMINHAO BASCULANTE'), TEXT_NORMAL_LEFT)
        worksheet.write(27, 3, self.tr('m³xkm'), TEXT_NORMAL_CENTER)
        worksheet.write(27, 4, '', TEXT_NORMAL_RIGHT)
        worksheet.write(27, 5, '', TEXT_NORMAL_RIGHT)
        worksheet.write(27, 6, '', TEXT_NORMAL_RIGHT)

        worksheet.write(28, 1, self.tr('01.05.03'), TEXT_NORMAL_LEFT)
        worksheet.write(28, 2, self.tr('CARGA E DESCARGA DE ROCHA'), TEXT_NORMAL_LEFT)
        worksheet.write(28, 3, self.tr('m³'), TEXT_NORMAL_CENTER)
        worksheet.write(28, 4, '', TEXT_NORMAL_RIGHT)
        worksheet.write(28, 5, '', TEXT_NORMAL_RIGHT)
        worksheet.write(28, 6, '', TEXT_NORMAL_RIGHT)

        worksheet.write(29, 1, self.tr('01.05.04'), TEXT_NORMAL_LEFT)
        worksheet.write(29, 2, self.tr('MOMENTO DE TRANSPORTE DE ROCHA, EM CAMINHAO BASCULANTE'), TEXT_NORMAL_LEFT)
        worksheet.write(29, 3, self.tr('m³xkm'), TEXT_NORMAL_CENTER)
        worksheet.write(29, 4, '', TEXT_NORMAL_RIGHT)
        worksheet.write(29, 5, '', TEXT_NORMAL_RIGHT)
        worksheet.write(29, 6, '', TEXT_NORMAL_RIGHT)

        worksheet.write(30, 1, self.tr('01.06'), TEXT_BOLD_LEFT_10_BORDER)
        worksheet.write(30, 2, self.tr('CAIXAS E POCOS DE VISITA'), TEXT_BOLD_LEFT_10_BORDER)
        worksheet.write(30, 3, '', TEXT_NORMAL_CENTER)
        worksheet.write(30, 4, '', TEXT_NORMAL_RIGHT)
        worksheet.write(30, 5, '', TEXT_NORMAL_RIGHT)
        worksheet.write(30, 6, '', TEXT_NORMAL_RIGHT)

        worksheet.write(31, 1, self.tr('01.06.01'), TEXT_NORMAL_LEFT)
        worksheet.write(31, 2, self.tr('CAIXA P/LIGACAO PREDIAL DE ESGOTO SANITARIO, EM ANEL DE CONCRETO PRE '
                                       'MOLDADODN=0,40m, e=7cm INCL. TAMPA DE CONCR. ARMADO C/ e=0,07m '),
                        TEXT_NORMAL_LEFT)
        worksheet.write(31, 3, self.tr('un'), TEXT_NORMAL_CENTER)
        worksheet.write(31, 4, '', TEXT_NORMAL_RIGHT)
        worksheet.write(31, 5, '', TEXT_NORMAL_RIGHT)
        worksheet.write(31, 6, '', TEXT_NORMAL_RIGHT)

        worksheet.write(32, 1, self.tr('01.06.02'), TEXT_NORMAL_LEFT)
        worksheet.write(32, 2, self.tr('CAIXA P/ LIGAÇAO PREDIAL DE ESGOTO SANITARIO, EM ANEL DE CONCRETO DN=0,60m, '
                                       'e=7cm,INCL. TAMPA DE CONCR. ARMADO  C/ e=0,07m '), TEXT_NORMAL_LEFT)
        worksheet.write(32, 3, self.tr('un'), TEXT_NORMAL_CENTER)
        worksheet.write(32, 4, '', TEXT_NORMAL_RIGHT)
        worksheet.write(32, 5, '', TEXT_NORMAL_RIGHT)
        worksheet.write(32, 6, '', TEXT_NORMAL_RIGHT)

        worksheet.write(33, 1, self.tr('01.06.03'), TEXT_NORMAL_LEFT)
        worksheet.write(33, 2, self.tr('CAIXA P/LIGACAO PREDIAL DE ESGOTO SANITARIO,EM ALVENARIA DE TIJOLO MACICO, '
                                       'C/ FORNEC. E ASSENT. DE TAMPA DE CONCRETO'), TEXT_NORMAL_LEFT)
        worksheet.write(33, 3, self.tr('un'), TEXT_NORMAL_CENTER)
        worksheet.write(33, 4, '', TEXT_NORMAL_RIGHT)
        worksheet.write(33, 5, '', TEXT_NORMAL_RIGHT)
        worksheet.write(33, 6, '', TEXT_NORMAL_RIGHT)

        worksheet.write(34, 1, self.tr('01.06.04'), TEXT_NORMAL_LEFT)
        worksheet.write(34, 2, self.tr('CAIXA P/LIGACAO PREDIAL DE ESGOTO SANITARIO,DE CONCRETO ARMADO, e=0,07 m,C/ '
                                       'FORNEC.E ASSENT.DE TAMPA'), TEXT_NORMAL_LEFT)
        worksheet.write(34, 3, self.tr('un'), TEXT_NORMAL_CENTER)
        worksheet.write(34, 4, '', TEXT_NORMAL_RIGHT)
        worksheet.write(34, 5, '', TEXT_NORMAL_RIGHT)
        worksheet.write(34, 6, '', TEXT_NORMAL_RIGHT)

        worksheet.write(35, 1, self.tr('01.06.05'), TEXT_NORMAL_LEFT)
        worksheet.write(35, 2, self.tr('DISPOSITIVO DE PASSAGEM P/ ESGOT. SANITARIO, SIMILAR TIL DE PASSAGEM , '
                                       'C/ FORNEC. DO MAT. E ANEL'), TEXT_NORMAL_LEFT)
        worksheet.write(35, 3, self.tr('un'), TEXT_NORMAL_CENTER)
        worksheet.write(35, 4, '', TEXT_NORMAL_RIGHT)
        worksheet.write(35, 5, '', TEXT_NORMAL_RIGHT)
        worksheet.write(35, 6, '', TEXT_NORMAL_RIGHT)

        worksheet.write(36, 1, self.tr('01.07'), TEXT_BOLD_LEFT_10_BORDER)
        worksheet.write(36, 2, self.tr('DEMOLICOES'), TEXT_BOLD_LEFT_10_BORDER)
        worksheet.write(36, 3, '', TEXT_NORMAL_CENTER)
        worksheet.write(36, 4, '', TEXT_NORMAL_RIGHT)
        worksheet.write(36, 5, '', TEXT_NORMAL_RIGHT)
        worksheet.write(36, 6, '', TEXT_NORMAL_RIGHT)

        worksheet.write(37, 1, self.tr('01.07.01'), TEXT_NORMAL_LEFT)
        worksheet.write(37, 2, self.tr('DEMOLICAO E RECOMPOSIÇÃO DE PASSEIO EM PISO CERÂMICO,ARDOSIA E MARMORE'),
                        TEXT_NORMAL_LEFT)
        worksheet.write(37, 3, self.tr('m²'), TEXT_NORMAL_CENTER)
        worksheet.write(37, 4, '', TEXT_NORMAL_RIGHT)
        worksheet.write(37, 5, '', TEXT_NORMAL_RIGHT)
        worksheet.write(37, 6, '', TEXT_NORMAL_RIGHT)

        worksheet.write(38, 1, self.tr('01.07.02'), TEXT_NORMAL_LEFT)
        worksheet.write(38, 2, self.tr('DEMOLIÇÃO E RECOMPOSIÇÃO  DE PLACAS PRE-MOLDADAS DE CONCRETO EM PASSEIO'),
                        TEXT_NORMAL_LEFT)
        worksheet.write(38, 3, self.tr('m²'), TEXT_NORMAL_CENTER)
        worksheet.write(38, 4, '', TEXT_NORMAL_RIGHT)
        worksheet.write(38, 5, '', TEXT_NORMAL_RIGHT)
        worksheet.write(38, 6, '', TEXT_NORMAL_RIGHT)

        worksheet.write(39, 1, self.tr('01.07.03'), TEXT_NORMAL_LEFT)
        worksheet.write(39, 2, self.tr('DEMOLIÇÃO E RECOMPOSIÇÃO DE PARALELEPIPEDO OU PEDRA IRREGULAR'),
                        TEXT_NORMAL_LEFT)
        worksheet.write(39, 3, self.tr('m²'), TEXT_NORMAL_CENTER)
        worksheet.write(39, 4, '', TEXT_NORMAL_RIGHT)
        worksheet.write(39, 5, '', TEXT_NORMAL_RIGHT)
        worksheet.write(39, 6, '', TEXT_NORMAL_RIGHT)

        worksheet.write(40, 1, self.tr('01.07.04'), TEXT_NORMAL_LEFT)
        worksheet.write(40, 2, self.tr('RETIRADA E PLANTIO DE GRAMA'), TEXT_NORMAL_LEFT)
        worksheet.write(40, 3, self.tr('m²'), TEXT_NORMAL_CENTER)
        worksheet.write(40, 4, '', TEXT_NORMAL_RIGHT)
        worksheet.write(40, 5, '', TEXT_NORMAL_RIGHT)
        worksheet.write(40, 6, '', TEXT_NORMAL_RIGHT)

        worksheet.write(41, 1, self.tr('01.07.05'), TEXT_NORMAL_LEFT)
        worksheet.write(41, 2, self.tr('DEMOLIÇÃO E RECOMPOSIÇÃO DE PAVIMENTO EM ASFALTO'), TEXT_NORMAL_LEFT)
        worksheet.write(41, 3, self.tr('m²'), TEXT_NORMAL_CENTER)
        worksheet.write(41, 4, '', TEXT_NORMAL_RIGHT)
        worksheet.write(41, 5, '', TEXT_NORMAL_RIGHT)
        worksheet.write(41, 6, '', TEXT_NORMAL_RIGHT)

        worksheet.write(42, 1, self.tr('01.07.06'), TEXT_NORMAL_LEFT)
        worksheet.write(42, 2, self.tr('DEMOLIÇÃO E RECOMPOSIÇÃO  DE BLOCO ARTICULADO DE CONCRETO (INTERTRAVADO)'),
                        TEXT_NORMAL_LEFT)
        worksheet.write(42, 3, self.tr('m²'), TEXT_NORMAL_CENTER)
        worksheet.write(42, 4, '', TEXT_NORMAL_RIGHT)
        worksheet.write(42, 5, '', TEXT_NORMAL_RIGHT)
        worksheet.write(42, 6, '', TEXT_NORMAL_RIGHT)

        worksheet.write(43, 1, self.tr('01.07.07'), TEXT_NORMAL_LEFT)
        worksheet.write(43, 2, self.tr('DEMOLIÇAO E RECOMPOSIÇÃO  DE PISO CIMENTADO SOBRE LASTRO DE CONCRETO SIMPLES'),
                        TEXT_NORMAL_LEFT)
        worksheet.write(43, 3, self.tr('m²'), TEXT_NORMAL_CENTER)
        worksheet.write(43, 4, '', TEXT_NORMAL_RIGHT)
        worksheet.write(43, 5, '', TEXT_NORMAL_RIGHT)
        worksheet.write(43, 6, '', TEXT_NORMAL_RIGHT)

        worksheet.write(44, 1, self.tr('01.07.08'), TEXT_NORMAL_LEFT)
        worksheet.write(44, 2, self.tr('DEMOLICAO E RECOMPOSIÇÃO DE PAVIMENTO EM CONCRETO SIMPLES'), TEXT_NORMAL_LEFT)
        worksheet.write(44, 3, self.tr('m²'), TEXT_NORMAL_CENTER)
        worksheet.write(44, 4, '', TEXT_NORMAL_RIGHT)
        worksheet.write(44, 5, '', TEXT_NORMAL_RIGHT)
        worksheet.write(44, 6, '', TEXT_NORMAL_RIGHT)

        worksheet.write(45, 1, self.tr('01.07.09'), TEXT_NORMAL_LEFT)
        worksheet.write(45, 2, self.tr('DEMOLICAO E RECOMPOSIÇÃO DE PAVIMENTO EM CONCRETO REFORÇADO'), TEXT_NORMAL_LEFT)
        worksheet.write(45, 3, self.tr('m²'), TEXT_NORMAL_CENTER)
        worksheet.write(45, 4, '', TEXT_NORMAL_RIGHT)
        worksheet.write(45, 5, '', TEXT_NORMAL_RIGHT)
        worksheet.write(45, 6, '', TEXT_NORMAL_RIGHT)

        worksheet.write(46, 1, self.tr('01.07.10'), TEXT_NORMAL_LEFT)
        worksheet.write(46, 2, self.tr('LEVANTAMENTOE RECOMPOSIÇÃO  DE PEDRA PORTUGUESA'), TEXT_NORMAL_LEFT)
        worksheet.write(46, 3, self.tr('m²'), TEXT_NORMAL_CENTER)
        worksheet.write(46, 4, '', TEXT_NORMAL_RIGHT)
        worksheet.write(46, 5, '', TEXT_NORMAL_RIGHT)
        worksheet.write(46, 6, '', TEXT_NORMAL_RIGHT)

        worksheet.write(47, 1, self.tr('01.08'), TEXT_BOLD_LEFT_10_BORDER)
        worksheet.write(47, 2, self.tr('SERVICOS DIVERSOS'), TEXT_BOLD_LEFT_10_BORDER)
        worksheet.write(47, 3, '', TEXT_NORMAL_CENTER)
        worksheet.write(47, 4, '', TEXT_NORMAL_RIGHT)
        worksheet.write(47, 5, '', TEXT_NORMAL_RIGHT)
        worksheet.write(47, 6, '', TEXT_NORMAL_RIGHT)

        worksheet.write(48, 1, self.tr('01.08.01'), TEXT_NORMAL_LEFT)
        worksheet.write(48, 2, self.tr('EXEC. DE  ENVELOPAMENTO C/ CONCRETO SIMPLES, INCL. FORNEC. DE MAT., PRODUCAO, '
                                       'TRANSP.MANUAL., LANC. VERT., ADENS., CURA E FORMA'), TEXT_NORMAL_LEFT)
        worksheet.write(48, 3, self.tr('m³'), TEXT_NORMAL_CENTER)
        worksheet.write(48, 4, '', TEXT_NORMAL_RIGHT)
        worksheet.write(48, 5, '', TEXT_NORMAL_RIGHT)
        worksheet.write(48, 6, '', TEXT_NORMAL_RIGHT)

        worksheet.write(49, 1, self.tr('01.09'), TEXT_BOLD_LEFT_10_BORDER)
        worksheet.write(49, 2, self.tr('ASSENTAMENTO DE TUBULACOES'), TEXT_BOLD_LEFT_10_BORDER)
        worksheet.write(49, 3, '', TEXT_NORMAL_CENTER)
        worksheet.write(49, 4, '', TEXT_NORMAL_RIGHT)
        worksheet.write(49, 5, '', TEXT_NORMAL_RIGHT)
        worksheet.write(49, 6, '', TEXT_NORMAL_RIGHT)

        worksheet.write(50, 1, self.tr('01.09.01'), TEXT_NORMAL_LEFT)
        worksheet.write(50, 2, self.tr('ASSENT. DE TUBOS EM PVC RIG OU PEAD. PB JE- ESGOTO - DN   100 mm'),
                        TEXT_NORMAL_LEFT)
        worksheet.write(50, 3, self.tr('m'), TEXT_NORMAL_CENTER)
        worksheet.write(50, 4, '', TEXT_NORMAL_RIGHT)
        worksheet.write(50, 5, '', TEXT_NORMAL_RIGHT)
        worksheet.write(50, 6, '', TEXT_NORMAL_RIGHT)

        worksheet.write(51, 1, self.tr('01.09.02'), TEXT_NORMAL_LEFT)
        worksheet.write(51, 2, self.tr('ASSENT. DE TUBOS EM PVC RIG OU PEAD. PB JE- ESGOTO - DN   150 mm'),
                        TEXT_NORMAL_LEFT)
        worksheet.write(51, 3, self.tr('m'), TEXT_NORMAL_CENTER)
        worksheet.write(51, 4, '', TEXT_NORMAL_RIGHT)
        worksheet.write(51, 5, '', TEXT_NORMAL_RIGHT)
        worksheet.write(51, 6, '', TEXT_NORMAL_RIGHT)

        worksheet.write_merge(52, 52, 1, 5, self.tr('TOTAL DO ITEM  01'), TEXT_BOLD_LEFT_10_BORDER)
        worksheet.write(52, 6, '', TEXT_BOLD_RIGHT_10_BORDER)

        worksheet.write(53, 1, self.tr('02'), TEXT_BOLD_LEFT_10_BORDER)
        worksheet.write(53, 2, self.tr('MATERIAIS'), TEXT_BOLD_LEFT_10_BORDER)
        worksheet.write(53, 3, '', TEXT_NORMAL_CENTER)
        worksheet.write(53, 4, '', TEXT_NORMAL_RIGHT)
        worksheet.write(53, 5, '', TEXT_NORMAL_RIGHT)
        worksheet.write(53, 6, '', TEXT_NORMAL_RIGHT)

        worksheet.write(54, 1, self.tr('02.01'), TEXT_BOLD_LEFT_10_BORDER)
        worksheet.write(54, 2, self.tr('TUBULAÇÕES'), TEXT_BOLD_LEFT_10_BORDER)
        worksheet.write(54, 3, '', TEXT_NORMAL_CENTER)
        worksheet.write(54, 4, '', TEXT_NORMAL_RIGHT)
        worksheet.write(54, 5, '', TEXT_NORMAL_RIGHT)
        worksheet.write(54, 6, '', TEXT_NORMAL_RIGHT)

        worksheet.write(55, 1, self.tr('02.01.01'), TEXT_NORMAL_LEFT)
        worksheet.write(55, 2, self.tr('TUBO ES PVC OU PEAD PB JE P/ ESG. DN 100'), TEXT_NORMAL_LEFT)
        worksheet.write(55, 3, self.tr('m'), TEXT_NORMAL_CENTER)
        worksheet.write(55, 4, '', TEXT_NORMAL_RIGHT)
        worksheet.write(55, 5, '', TEXT_NORMAL_RIGHT)
        worksheet.write(55, 6, '', TEXT_NORMAL_RIGHT)

        worksheet.write(56, 1, self.tr('02.01.02'), TEXT_NORMAL_LEFT)
        worksheet.write(56, 2, self.tr('TUBO ES PVC OU PEAD PB JE P/ ESG. DN 150'), TEXT_NORMAL_LEFT)
        worksheet.write(56, 3, self.tr('m'), TEXT_NORMAL_CENTER)
        worksheet.write(56, 4, '', TEXT_NORMAL_RIGHT)
        worksheet.write(56, 5, '', TEXT_NORMAL_RIGHT)
        worksheet.write(56, 6, '', TEXT_NORMAL_RIGHT)

        worksheet.write(57, 1, self.tr('02.02'), TEXT_BOLD_LEFT_10_BORDER)
        worksheet.write(57, 2, self.tr('PECAS E CONEXOES'), TEXT_BOLD_LEFT_10_BORDER)
        worksheet.write(57, 3, '', TEXT_NORMAL_CENTER)
        worksheet.write(57, 4, '', TEXT_NORMAL_RIGHT)
        worksheet.write(57, 5, '', TEXT_NORMAL_RIGHT)
        worksheet.write(57, 6, '', TEXT_NORMAL_RIGHT)

        worksheet.write(58, 1, self.tr('02.02.01'), TEXT_NORMAL_LEFT)
        worksheet.write(58, 2, self.tr('SELIM ES PVC JE'), TEXT_NORMAL_LEFT)
        worksheet.write(58, 3, self.tr('pc'), TEXT_NORMAL_CENTER)
        worksheet.write(58, 4, '', TEXT_NORMAL_RIGHT)
        worksheet.write(58, 5, '', TEXT_NORMAL_RIGHT)
        worksheet.write(58, 6, '', TEXT_NORMAL_RIGHT)

        worksheet.write(59, 1, self.tr('02.02.02'), TEXT_NORMAL_LEFT)
        worksheet.write(59, 2, self.tr('C90 ES PVC PB JE DN 100'), TEXT_NORMAL_LEFT)
        worksheet.write(59, 3, self.tr('pc'), TEXT_NORMAL_CENTER)
        worksheet.write(59, 4, '', TEXT_NORMAL_RIGHT)
        worksheet.write(59, 5, '', TEXT_NORMAL_RIGHT)
        worksheet.write(59, 6, '', TEXT_NORMAL_RIGHT)

        worksheet.write(60, 1, self.tr('02.02.03'), TEXT_NORMAL_LEFT)
        worksheet.write(60, 2, self.tr('C90 ES PVC PB JE DN 150'), TEXT_NORMAL_LEFT)
        worksheet.write(60, 3, self.tr('pc'), TEXT_NORMAL_CENTER)
        worksheet.write(60, 4, '', TEXT_NORMAL_RIGHT)
        worksheet.write(60, 5, '', TEXT_NORMAL_RIGHT)
        worksheet.write(60, 6, '', TEXT_NORMAL_RIGHT)

        worksheet.write(61, 1, self.tr('02.02.04'), TEXT_NORMAL_LEFT)
        worksheet.write(61, 2, self.tr('TE ES PVC BBB JE DN 100'), TEXT_NORMAL_LEFT)
        worksheet.write(61, 3, self.tr('pc'), TEXT_NORMAL_CENTER)
        worksheet.write(61, 4, '', TEXT_NORMAL_RIGHT)
        worksheet.write(61, 5, '', TEXT_NORMAL_RIGHT)
        worksheet.write(61, 6, '', TEXT_NORMAL_RIGHT)

        worksheet.write(62, 1, self.tr('02.02.05'), TEXT_NORMAL_LEFT)
        worksheet.write(62, 2, self.tr('TE ES PVC BBB JE DN 150'), TEXT_NORMAL_LEFT)
        worksheet.write(62, 3, self.tr('pc'), TEXT_NORMAL_CENTER)
        worksheet.write(62, 4, '', TEXT_NORMAL_RIGHT)
        worksheet.write(62, 5, '', TEXT_NORMAL_RIGHT)
        worksheet.write(62, 6, '', TEXT_NORMAL_RIGHT)

        worksheet.write_merge(63, 63, 1, 5, self.tr('TOTAL DO ITEM 02'), TEXT_BOLD_LEFT_10_BORDER)
        worksheet.write(63, 6, '', TEXT_BOLD_RIGHT_10_BORDER)

        worksheet.write_merge(64, 64, 1, 5, self.tr('TOTAL GERAL'), TEXT_BOLD_LEFT_10_BORDER)
        worksheet.write(64, 6, '', TEXT_BOLD_RIGHT_10_BORDER)

        worksheet.write_merge(66, 66, 1, 5, self.tr('VALOR POR METRO'), TEXT_BOLD_LEFT_10_BORDER)
        worksheet.write(66, 6, '', TEXT_BOLD_RIGHT_10_BORDER)

        workbook.save(local_file)



TEXT_BOLD_CENTER_12_BORDER = easyxf('font: name Arial, height 240, bold True; '
                                    'align: vert center, horiz center;'
                                    'borders: left 0, right 0, top 0, bottom 0;')
TEXT_BOLD_CENTER_10_BORDER = easyxf('font: name Arial, height 160, bold True; '
                                    'align: vert center, horiz center;'
                                    'borders: left 2, right 2, top 2, bottom 2;')
TEXT_BOLD_LEFT_10_BORDER = easyxf('font: name Arial, height 160, bold True; '
                                  'align: vert center, horiz left;'
                                  'borders: left 1, right 1, top 1, bottom 1;')
TEXT_BOLD_RIGHT_10_BORDER = easyxf('font: name Arial, height 160, bold True; '
                                   'align: vert center, horiz right;'
                                   'borders: left 1, right 1, top 1, bottom 1;')
TEXT_NORMAL_RIGHT = easyxf('font: name Arial, height 160; align: vert center, horiz right; '
                           'borders: left 1, right 1, bottom 1;')
TEXT_NORMAL_LEFT = easyxf('font: name Arial, height 160; align: wrap on, vert center, horiz left; '
                          'borders: left 1, right 1, bottom 1;')
TEXT_NORMAL_CENTER = easyxf('font: name Arial, height 160; align: vert center, horiz center; '
                            'borders: left 1, right 1, bottom 1;')
