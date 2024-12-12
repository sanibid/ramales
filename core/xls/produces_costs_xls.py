import json

from PyQt5.QtCore import Qt, QLocale, QCoreApplication
from qgis._core import QgsProject, QgsVectorLayer
from xlwt import Workbook, easyxf
import os

from ...helpers.globals import get_language_file
from ...core.data.data_manager import ProjectDataManager


class ProducesReportCostsXls:

    def tr(self, message):
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('SanihubRamales', message)

    def __init__(self):
        self.data_json = None
        self.segments = None
        self.loc = QLocale()
        self.MAX_COLUMN = 15

    def generate_report_costs(self, local_file):
        local_file = os.path.normpath(local_file)
        block = QgsProject.instance().mapLayer(ProjectDataManager.get_layers_id().BLOCKS_LAYER_ID)
        block_fields = [field.name() for field in block.fields()]
        block_values = [f.attributes() for f in block.getFeatures()]
        block_dict = dict(zip(block_fields, block_values[0]))
        list_block_values = list(block_dict.values())
        nodes = []
        nodes_lyr = QgsProject.instance().mapLayer(ProjectDataManager.get_layers_id().NODES_LAYER_ID)
        all_nodes = nodes_lyr.getFeatures()
        for n in all_nodes:
            nodes.append(n)
        self.segments = QgsProject.instance().mapLayer(ProjectDataManager.get_layers_id().SEGMENTS_LAYER_ID)
        all_segs = self.segments.getFeatures()
        segments = []
        for s in all_segs:
            segments.append(s)
        segments = sorted(segments, key=lambda item:
        (item[self.__get_idx_attr(self.segments, 'segments', 'branch_id')],
         item[self.__get_idx_attr(self.segments, 'segments', 'segment_id')]))
        branchs = []
        for feat in segments:
            branchs.append(feat[self.__get_idx_attr_segments('branch_id')])

        branchs = set(branchs)
        workbook = Workbook()
        for branch in branchs:
            q_row = 0
            for feat in segments:
                if feat[self.__get_idx_attr_segments('branch_id')] == branch:
                    q_row += 1
            worksheet = workbook.add_sheet('R-' + str(branch), cell_overwrite_ok=True)
            worksheet.set_fit_num_pages(1)
            worksheet.show_grid = False

            is_aerial = False
            h_branch = 0.00
            for feat in segments:
                if feat[self.__get_idx_attr_segments('branch_id')] == branch:
                    branch_position = int(feat[self.__get_idx_attr_segments("branch_position")])
                    if branch_position == 2:
                        is_aerial = True
                        h_branch = self.get_element_layer_nodes(
                            node=feat[self.__get_idx_attr_segments('up_box')], name_attr='h_branch')
                    break

            # CAIXA
            worksheet.col(0).width = 2000
            worksheet.col(1).width = 2100

            # DISTÂNCIA
            worksheet.col(2).width = 1550

            # COTA TERRENO
            worksheet.col(3).width = 1550
            worksheet.col(4).width = 1550

            # COTA RAMAL
            worksheet.col(5).width = 1550
            worksheet.col(6).width = 1550

            # PROFUNDIDADE
            worksheet.col(7).width = 1700
            worksheet.col(8).width = 1700

            # GABARITO
            worksheet.col(9).width = 1550

            # COTA RÉGUA
            worksheet.col(10).width = 1550
            worksheet.col(11).width = 1550

            # PROF. CRÍTICA
            worksheet.col(12).width = 1550

            # CAIM. TRECHO
            worksheet.col(13).width = 1550

            # TUBO DE QUEDA
            worksheet.col(14).width = 2600

            # OBS
            worksheet.col(15).width = 2600

            worksheet.row(7).height_mismatch = True
            worksheet.row(7).height = 130
            worksheet.row(11).height_mismatch = True
            worksheet.row(11).height = 130
            worksheet.row(16).height_mismatch = True
            worksheet.row(16).height = 130
            worksheet.write_merge(2, 0, 0, 1, self.tr('BACIA:'), TEXT_BOLD_LEFT_12_QUADRA)
            worksheet.write_merge(2, 1, 2, 2, '', TEXT_NORMAL_LEFT_12_QUADRA)
            worksheet.write_merge(3, 0, 0, 1, self.tr('LOCAL:'), TEXT_BOLD_LEFT_12_RAMAL)
            worksheet.write_merge(3, 1, 2, 2, '', TEXT_NORMAL_CENTER_12_RAMAL)
            worksheet.write_merge(4, 0, 0, 1, self.tr('QUADRA:'), TEXT_BOLD_LEFT_12_BACIA)
            worksheet.write_merge(4, 1, 2, 1, '', TEXT_NORMAL_CENTER_12_BACIA)
            worksheet.write_merge(5, 0, 0, 1, self.tr('DATA:'), TEXT_NORMAL_CENTER_12_BACIA)
            worksheet.write_merge(5, 1, 2, 1, '', TEXT_BOLD_LEFT_12_DATA)
            worksheet.write_merge(7, 0, 0, self.MAX_COLUMN, self.tr('ORÇAMENTO RAMAIS'),
                                  TEXT_BOLD_CENTER_12_BORDER)
            worksheet.write_row(8, 0, [self.tr('ITEM'), self.tr('DESCRIÇÃO DOS SERVIÇOS'), self.tr('UN'),
                                       self.tr('QUANTIDADE'), self.tr('P. UNIT USD'), self.tr('VALOR')],
                                TEXT_NORMAL_CENTER_CAIXA)
            worksheet.write_row(9, 0, [self.tr('01'), self.tr('SERVIÇOS')], TEXT_NORMAL_CENTER_CAIXA)
            worksheet.write_row(10, 0, [self.tr('01.01'), self.tr('SINALIZAÇÃO E SEGURANÇA')], TEXT_NORMAL_CENTER_CAIXA)
            worksheet.write_row(11, 0, [self.tr('01.01.01'), self.tr('PLACA DE SINALIZAÇAO E ADVERTENCIA,INCL.FORNEC.,'
                                                                     'TRANSP.,INSTAL.E REMOÇAO P/OUTRO LOCAL DA OBRA '),
                                        self.tr('m²'), '', '', ''], TEXT_NORMAL_CENTER_CAIXA)
            worksheet.write_row(12, 0, [self.tr('01.01.02'), self.tr('CERCA DE PROTECAO S/ SINALIZACAO LUMINOSA C/ '
                                                                     'MONTANTES E TELA PVC'),
                                        self.tr('m²'), '', '', ''], TEXT_NORMAL_CENTER_CAIXA)
            worksheet.write_row(13, 0, [self.tr('01.01.03'), self.tr('PASSADICO EM MADEIRA, P/PEDESTRES'),
                                        self.tr('m²'), '', '', ''], TEXT_NORMAL_CENTER_CAIXA)
            worksheet.write_row(14, 0, [self.tr('01.01.04'), self.tr('PASSADICO METALICO P/ VEICULOS'),
                                        self.tr('m²'), '', '', ''], TEXT_NORMAL_CENTER_CAIXA)
            worksheet.write_row(15, 0, [self.tr('01.02'), self.tr('SERVICOS TOPOGRAFICOS')], TEXT_NORMAL_CENTER_CAIXA)
            worksheet.write_row(16, 0, [self.tr('01.02.01'), self.tr('SERVICOS TOPOGRAFICOS, GEOTECNICOS, INSPECAO DE '
                                                                     'MATERIAIS, DETALHAMENTO DE PROJETOS E CADASTRO '),
                                        self.tr('m'), '', '', ''], TEXT_NORMAL_CENTER_CAIXA)
            worksheet.write_row(17, 0, [self.tr('01.03'), self.tr('ESCAVACOES')], TEXT_NORMAL_CENTER_CAIXA)
            worksheet.write_row(18, 0, [self.tr('01.03.01'), self.tr('ESCAV. MANUAL DE VALAS'),
                                        self.tr('m³'), '', '', ''], TEXT_NORMAL_CENTER_CAIXA)
            worksheet.write_row(19, 0, [self.tr('01.03.02'), self.tr('ESCAV. MECANIZ. DE VALAS   EM SOLO'),
                                        self.tr('m³'), '', '', ''], TEXT_NORMAL_CENTER_CAIXA)
            worksheet.write_row(20, 0, [self.tr('01.03.03'), self.tr('ESCAV. DE VALAS - EM ROCHA'),
                                        self.tr('m³'), '', '', ''], TEXT_NORMAL_CENTER_CAIXA)
            worksheet.write_row(21, 0, [self.tr('01.04'), self.tr('ATERROS E ENVOLTORIAS')], TEXT_NORMAL_CENTER_CAIXA)
            worksheet.write_row(22, 0, [self.tr('01.04.01'), self.tr('EXEC. DE ATERRO EM VALAS/POÇOS/CAVAS DE FUNDAÇAO '
                                                                     'C/ SOLO PROVENIENTE DAS ESCAVAÇOES'),
                                        self.tr('m³'), '', '', ''], TEXT_NORMAL_CENTER_CAIXA)
            worksheet.write_row(23, 0, [self.tr('01.04.02'), self.tr('EXEC. DE ATERRO EM VALAS/POÇOS/CAVAS DE '
                                                                     'FUNDAÇAO, C/ FORNEC. DE SOLO'),
                                        self.tr('m³'), '', '', ''], TEXT_NORMAL_CENTER_CAIXA)
            worksheet.write_row(24, 0, [self.tr('01.04.03'), self.tr('EXEC. DE ENVOLTORIA OU BERCO DE AREIA EM VALAS'),
                                        self.tr('m³'), '', '', ''], TEXT_NORMAL_CENTER_CAIXA)
            worksheet.write_row(25, 0, [self.tr('01.05'), self.tr('TRANSPORTE DE MATERIAIS')], TEXT_NORMAL_CENTER_CAIXA)
            worksheet.write_row(26, 0, [self.tr('01.05.01'), self.tr('CARGA E DESCARGA DE SOLO'),
                                        self.tr('m³'), '', '', ''], TEXT_NORMAL_CENTER_CAIXA)
            worksheet.write_row(27, 0,
                                [self.tr('01.05.02'), self.tr('MOMENTO DE TRANSPORTE DE SOLO, EM CAMINHAO BASCULANTE'),
                                 self.tr('m³xkm'), '', '', ''], TEXT_NORMAL_CENTER_CAIXA)
            worksheet.write_row(28, 0, [self.tr('01.05.03'), self.tr('CARGA E DESCARGA DE ROCHA'),
                                        self.tr('m³'), '', '', ''], TEXT_NORMAL_CENTER_CAIXA)
            worksheet.write_row(29, 0,
                                [self.tr('01.05.04'), self.tr('MOMENTO DE TRANSPORTE DE ROCHA, EM CAMINHAO BASCULANTE'),
                                 self.tr('m³xkm'), '', '', ''], TEXT_NORMAL_CENTER_CAIXA)
            worksheet.write_row(30, 0, [self.tr('01.06'), self.tr('CAIXAS E POCOS DE VISITA')],
                                TEXT_NORMAL_CENTER_CAIXA)
            worksheet.write_row(31, 0, [self.tr('01.06.01'), self.tr('CAIXA P/LIGACAO PREDIAL DE ESGOTO SANITARIO, EM '
                                                                     'ANEL DE CONCRETO PRE MOLDADODN=0,40m, e=7cm INCL.'
                                                                     ' TAMPA DE CONCR. ARMADO C/ e=0,07m '),
                                        self.tr('un'), '', '', ''], TEXT_NORMAL_CENTER_CAIXA)
            worksheet.write_row(32, 0, [self.tr('01.06.02'), self.tr('CAIXA P/ LIGAÇAO PREDIAL DE ESGOTO SANITARIO, EM '
                                                                     'ANEL DE CONCRETO DN=0,60m, e=7cm,INCL. TAMPA DE '
                                                                     'CONCR. ARMADO  C/ e=0,07m '),
                                        self.tr('un'), '', '', ''], TEXT_NORMAL_CENTER_CAIXA)
            worksheet.write_row(33, 0, [self.tr('01.06.03'), self.tr('CAIXA P/LIGACAO PREDIAL DE ESGOTO SANITARIO,EM '
                                                                     'ALVENARIA DE TIJOLO MACICO, C/ FORNEC. E ASSENT. '
                                                                     'DE TAMPA DE CONCRETO'),
                                        self.tr('un'), '', '', ''], TEXT_NORMAL_CENTER_CAIXA)
            worksheet.write_row(34, 0, [self.tr('01.06.04'), self.tr('CAIXA P/LIGACAO PREDIAL DE ESGOTO SANITARIO,DE '
                                                                     'CONCRETO ARMADO, e=0,07 m,C/ FORNEC.E ASSENT.DE '
                                                                     'TAMPA'),
                                        self.tr('un'), '', '', ''], TEXT_NORMAL_CENTER_CAIXA)
            worksheet.write_row(35, 0, [self.tr('01.06.05'), self.tr('DISPOSITIVO DE PASSAGEM P/ ESGOT. SANITARIO, '
                                                                     'SIMILAR TIL DE PASSAGEM , C/ FORNEC. DO MAT. E '
                                                                     'ANEL'),
                                        self.tr('un'), '', '', ''], TEXT_NORMAL_CENTER_CAIXA)
            worksheet.write_row(36, 0, [self.tr('01.07'), self.tr('DEMOLICOES')], TEXT_NORMAL_CENTER_CAIXA)
            worksheet.write_row(37, 0, [self.tr('01.07.01'), self.tr('DEMOLICAO E RECOMPOSIÇÃO DE PASSEIO EM PISO '
                                                                     'CERÂMICO,ARDOSIA E MARMORE'),
                                        self.tr('m²'), '', '', ''], TEXT_NORMAL_CENTER_CAIXA)
            worksheet.write_row(38, 0, [self.tr('01.07.02'), self.tr('DEMOLIÇÃO E RECOMPOSIÇÃO  DE PLACAS PRE-MOLDADAS '
                                                                     'DE CONCRETO EM PASSEIO'),
                                        self.tr('m²'), '', '', ''], TEXT_NORMAL_CENTER_CAIXA)
            worksheet.write_row(39, 0, [self.tr('01.07.03'), self.tr('DEMOLIÇÃO E RECOMPOSIÇÃO DE PARALELEPIPEDO OU '
                                                                     'PEDRA IRREGULAR'),
                                        self.tr('m²'), '', '', ''], TEXT_NORMAL_CENTER_CAIXA)
            worksheet.write_row(40, 0, [self.tr('01.07.04'), self.tr('RETIRADA E PLANTIO DE GRAMA'),
                                        self.tr('m²'), '', '', ''], TEXT_NORMAL_CENTER_CAIXA)
            worksheet.write_row(41, 0,
                                [self.tr('01.07.05'), self.tr('DEMOLIÇÃO E RECOMPOSIÇÃO DE PAVIMENTO EM ASFALTO'),
                                 self.tr('m²'), '', '', ''], TEXT_NORMAL_CENTER_CAIXA)
            worksheet.write_row(42, 0, [self.tr('01.07.06'), self.tr('DEMOLIÇÃO E RECOMPOSIÇÃO  DE BLOCO ARTICULADO DE '
                                                                     'CONCRETO (INTERTRAVADO)'),
                                        self.tr('m²'), '', '', ''], TEXT_NORMAL_CENTER_CAIXA)
            worksheet.write_row(43, 0, [self.tr('01.07.07'), self.tr('DEMOLIÇAO E RECOMPOSIÇÃO  DE PISO CIMENTADO SOBRE'
                                                                     ' LASTRO DE CONCRETO SIMPLES'),
                                        self.tr('m²'), '', '', ''], TEXT_NORMAL_CENTER_CAIXA)
            worksheet.write_row(44, 0, [self.tr('01.07.08'), self.tr('DEMOLICAO E RECOMPOSIÇÃO DE PAVIMENTO EM CONCRETO'
                                                                     ' SIMPLES'),
                                        self.tr('m²'), '', '', ''], TEXT_NORMAL_CENTER_CAIXA)
            worksheet.write_row(45, 0, [self.tr('01.07.09'), self.tr('DEMOLICAO E RECOMPOSIÇÃO DE PAVIMENTO EM CONCRETO'
                                                                     ' REFORÇADO'),
                                        self.tr('m²'), '', '', ''], TEXT_NORMAL_CENTER_CAIXA)
            worksheet.write_row(46, 0, [self.tr('01.07.10'), self.tr('LEVANTAMENTOE RECOMPOSIÇÃO  DE PEDRA PORTUGUESA'),
                                        self.tr('m²'), '', '', ''], TEXT_NORMAL_CENTER_CAIXA)
            worksheet.write_row(47, 0, [self.tr('01.08'), self.tr('SERVICOS DIVERSOS')], TEXT_NORMAL_CENTER_CAIXA)
            worksheet.write_row(48, 0, [self.tr('01.08.01'), self.tr('EXEC. DE  ENVELOPAMENTO C/ CONCRETO SIMPLES, '
                                                                     'INCL. FORNEC. DE MAT., PRODUCAO, TRANSP.MANUAL., '
                                                                     'LANC. VERT., ADENS., CURA E FORMA'),
                                        self.tr('m³'), '', '', ''], TEXT_NORMAL_CENTER_CAIXA)
            worksheet.write_row(49, 0, [self.tr('01.09'), self.tr('ASSENTAMENTO DE TUBULACOES')],
                                TEXT_NORMAL_CENTER_CAIXA)
            worksheet.write_row(50, 0, [self.tr('01.09.01'), self.tr('ASSENT. DE TUBOS EM PVC RIG OU PEAD. PB JE- '
                                                                     'ESGOTO - DN   100 mm'),
                                        self.tr('m'), '', '', ''], TEXT_NORMAL_CENTER_CAIXA)
            worksheet.write_row(51, 0, [self.tr('01.09.02'), self.tr('ASSENT. DE TUBOS EM PVC RIG OU PEAD. PB JE- '
                                                                     'ESGOTO - DN   150 mm'),
                                        self.tr('m'), '', '', ''], TEXT_NORMAL_CENTER_CAIXA)
            worksheet.write_row(52, 0, [self.tr('TOTAL DO ITEM  01'), ''], TEXT_NORMAL_CENTER_CAIXA)
            worksheet.write_row(53, 0, [self.tr('02'), self.tr('MATERIAIS')], TEXT_NORMAL_CENTER_CAIXA)
            worksheet.write_row(54, 0, [self.tr('02.01'), self.tr('TUBULAÇÕES')], TEXT_NORMAL_CENTER_CAIXA)
            worksheet.write_row(55, 0, [self.tr('02.01.01'), self.tr('TUBO ES PVC OU PEAD PB JE P/ ESG. DN 100'),
                                        self.tr('m'), '', ''], TEXT_NORMAL_CENTER_CAIXA)
            worksheet.write_row(56, 0, [self.tr('02.01.02'), self.tr('TUBO ES PVC OU PEAD PB JE P/ ESG. DN 150'),
                                        self.tr('m'), '', ''], TEXT_NORMAL_CENTER_CAIXA)
            worksheet.write_row(57, 0, [self.tr('02.02'), self.tr('PECAS E CONEXOES')], TEXT_NORMAL_CENTER_CAIXA)
            worksheet.write_row(58, 0, [self.tr('02.02.01'), self.tr('SELIM ES PVC JE'), self.tr('pc'), '', '', ''],
                                TEXT_NORMAL_CENTER_CAIXA)
            worksheet.write_row(59, 0, [self.tr('02.02.02'), self.tr('C90 ES PVC PB JE DN 100'), self.tr('pc'), '', '',
                                        ''], TEXT_NORMAL_CENTER_CAIXA)
            worksheet.write_row(60, 0, [self.tr('02.02.03'), self.tr('C90 ES PVC PB JE DN 150'), self.tr('pc'), '', '',
                                        ''], TEXT_NORMAL_CENTER_CAIXA)
            worksheet.write_row(61, 0, [self.tr('02.02.04'), self.tr('TE ES PVC BBB JE DN 100'), self.tr('pc'), '', '',
                                        ''], TEXT_NORMAL_CENTER_CAIXA)
            worksheet.write_row(62, 0, [self.tr('02.02.05'), self.tr('TE ES PVC BBB JE DN 150'), self.tr('pc'), '', '',
                                        ''], TEXT_NORMAL_CENTER_CAIXA)
            worksheet.write_row(63, 0, [self.tr('TOTAL DO ITEM 02'), ''], TEXT_NORMAL_CENTER_CAIXA)
            worksheet.write_row(64, 0, [self.tr('TOTAL GERAL'), ''], TEXT_NORMAL_CENTER_CAIXA)
            worksheet.write_row(66, 0, [self.tr('VALOR POR METRO'), ''], TEXT_NORMAL_CENTER_CAIXA)
        workbook.save(local_file)

    def get_element_layer_nodes(self, node: str, name_attr: str):
        nodes_lyr = QgsProject.instance().mapLayer(ProjectDataManager.get_layers_id().NODES_LAYER_ID)
        all_nodes = nodes_lyr.getFeatures()
        for n in all_nodes:
            if n.attributes()[self.__get_idx_attr(nodes_lyr, 'nodes', 'name')] == node:
                return n.attributes()[self.__get_idx_attr(nodes_lyr, 'nodes', name_attr)]
        return

    def __get_idx_attr(self, layer: QgsVectorLayer, name_lyr: str, name_attr: str):
        attrs = layer.fields().names()
        return attrs.index(self.__get_json_attr(name_lyr, name_attr))

    def __get_idx_attr_segments(self, name_attr: str):
        attrs = self.segments.fields().names()
        return attrs.index(self.__get_json_attr('segments', name_attr))

    def __get_json_attr(self, name_lyr: str, attribute: str):
        if self.data_json is None:
            self.__set_data_json()
        lyr = self.data_json[name_lyr][1]

        def get_key(val):
            for k, v in lyr.items():
                if v == val:
                    return k
            return

        try:
            return lyr[attribute]
        except KeyError:
            att = get_key(attribute)
            if att is not None:
                return lyr[att]
            return

    def __set_data_json(self):
        plg_dir = os.path.dirname(__file__)
        plg_dir = plg_dir.replace('core' + os.sep + 'xls', 'resources' + os.sep + 'localizations' + os.sep)
        # TODO: Tirar 2 linhas abaixo após receber geopackage
        from ..data.models import Language
        ProjectDataManager.save_language_project(Language(LANGUAGE='pt_BR'))

        lang = ProjectDataManager.get_language_project().LANGUAGE
        lang = lang if lang != '' else get_language_file()
        file_json = open(os.path.join(plg_dir, lang + '.json'), 'r')
        self.data_json = json.load(file_json)
        file_json.close()

    def __str_to_float_locale(self, value: str) -> float:
        # if QgsApplication.instance().locale() == 'pt_BR':
        if type(value) is str and len(value) > 0:
            if value[-1].isnumeric():
                return self.loc.toFloat(value)[0]
            return 0.00
        elif type(value) is float:
            return value
        else:
            return 0.00


TEXT_BOLD_CENTER_12_BORDER = easyxf('font: name Arial, height 240, bold True; '
                                    'align: vert center, horiz center;'
                                    'borders: left 2, right 2, top 2, bottom 0;')
TEXT_BOLD_LEFT_12 = easyxf('font: name Arial, height 240, bold True; '
                           'align: vert center, horiz left; borders: left 2, right 0, top 2, bottom 1;')
TEXT_BOLD_LEFT_12_QUADRA = easyxf('font: name Arial, height 240, bold True; '
                                  'align: vert center, horiz left; '
                                  'borders: left 2, right 0, top 2, bottom 1;')
TEXT_NORMAL_CENTER_12_QUADRA = easyxf('font: name Arial, height 240; '
                                      'align: vert center, horiz center; '
                                      'borders: left 0, right 1, top 2, bottom 1;')
TEXT_NORMAL_LEFT_12_QUADRA = easyxf('font: name Arial, height 240; '
                                    'align: vert center, horiz left; '
                                    'borders: left 1, right 0, top 2, bottom 1;')
TEXT_BOLD_LEFT_12_RAMAL = easyxf('font: name Arial, height 240, bold True; '
                                 'align: vert center, horiz left; '
                                 'borders: left 0, right 0, top 2, bottom 1;')
TEXT_NORMAL_CENTER_12_RAMAL = easyxf('font: name Arial, height 240; '
                                     'align: vert center, horiz center; '
                                     'borders: left 0, right 2, top 2, bottom 1;')
TEXT_BOLD_CENTER_10_RAMAL = easyxf('font: name Arial, height 200, bold True; '
                                   'align: vert center, horiz center; '
                                   'borders: left 2, right 2, top 0, bottom 0;')
TEXT_BOLD_CENTER_10_OS = easyxf('font: name Arial, height 200, bold True; '
                                'align: vert center, horiz center;'
                                'borders: left 2, right 2, top 0, bottom 2;')
TEXT_BOLD_LEFT_12_BACIA = easyxf('font: name Arial, height 240, bold True; '
                                 'align: vert center, horiz left; '
                                 'borders: left 2, right 0, top 1, bottom 1;')
TEXT_NORMAL_CENTER_12_BACIA = easyxf('font: name Arial, height 240; '
                                     'align: vert center, horiz center; '
                                     'borders: left 0, right 0, top 1, bottom 1;')
TEXT_BOLD_LEFT_12_DATA = easyxf('font: name Arial, height 240, bold True; '
                                'align: vert center, horiz left; '
                                'borders: left 0, right 0, top 1, bottom 1;')
TEXT_NORMAL_CENTER_12_DATA = easyxf('font: name Arial, height 240; '
                                    'align: vert center, horiz center; '
                                    'borders: left 0, right 2, top 1, bottom 1;',
                                    num_format_str='DD/MM/YYYY')
TEXT_NORMAL_RIGHT_PROF = easyxf('font: name Arial, height 160; align: vert center, horiz right; '
                                'borders: left 2, right 0, top 1, bottom 2;')
TEXT_NORMAL_CENTER_PROF = easyxf('font: name Arial, height 160; align: vert center, horiz center; '
                                 'borders: left 0, right 0, top 1, bottom 2;')
TEXT_NORMAL_RIGHT_DECLIV = easyxf('font: name Arial, height 160; align: vert center, horiz right; '
                                  'borders: left 1, right 0, top 1, bottom 2;')
TEXT_NORMAL_CENTER_DECLIV = easyxf('font: name Arial, height 160; align: vert center, horiz center; '
                                   'borders: left 0, right 2, top 1, bottom 2;')
TEXT_BOLD_CENTER_12_QUANT = easyxf('font: name Arial, height 240, bold True; '
                                   'align: vert center, horiz center; '
                                   'borders: left 0, right 0, top 0, bottom 2;')
TEXT_NORMAL_LEFT_REV = easyxf('font: name Arial, height 160; align: vert center, horiz left; '
                              'borders: left 2, right 0, top 2, bottom 1;')
TEXT_NORMAL_CENTER_REV = easyxf('font: name Arial, height 160; align: vert center, horiz center; '
                                'borders: left 0, right 1, top 2, bottom 1;')
TEXT_NORMAL_LEFT_DATA_REV = easyxf('font: name Arial, height 160; align: vert center, horiz left; '
                                   'borders: left 1, right 1, top 2, bottom 1;')
TEXT_NORMAL_LEFT_DATA_BRANCH = easyxf('font: name Arial, height 160; align: vert center, horiz left; '
                                      'borders: left 1, right 1, top 1, bottom 1;')
TEXT_NORMAL_CENTER_EXTEN = easyxf('font: name Arial, height 160; align: vert center, horiz center; '
                                  'borders: left 1, right 2, top 2, bottom 1;')
TEXT_NORMAL_CENTER_BRANCH = easyxf('font: name Arial, height 160; align: vert center, horiz center; '
                                   'borders: left 1, right 2, top 1, bottom 1;', num_format_str='#,##0.00')
TEXT_NORMAL_LEFT_NULL = easyxf('font: name Arial, height 160; align: vert center, horiz center; '
                               'borders: left 2, right 1, top 1, bottom 1;')
TEXT_NORMAL_RIGHT_NULL = easyxf('font: name Arial, height 160; align: vert center, horiz center; '
                                'borders: left 1, right 2, top 1, bottom 1;')
TEXT_NORMAL_CENTER_NULL = easyxf('font: name Arial, height 160; align: vert center, horiz center; '
                                 'borders: left 1, right 1, top 1, bottom 1;')
TEXT_NORMAL_LEFT_TUBO = easyxf('font: name Arial, height 160; align: vert center, horiz left; '
                               'borders: left 2, right 0, top 1, bottom 2;')
TEXT_NORMAL_CENTER_TUBO = easyxf('font: name Arial, height 160; align: vert center, horiz center; '
                                 'borders: left 0, right 0, top 1, bottom 2;')
TEXT_NORMAL_MERGE_TUBO_L = easyxf('font: name Arial, height 160; align: vert center, horiz left; '
                                  'borders: left 0, right 1, top 1, bottom 2;')
TEXT_NORMAL_MERGE_TUBO_R = easyxf('font: name Arial, height 160; align: vert center, horiz left; '
                                  'borders: left 1, right 2, top 1, bottom 2;')
TEXT_NORMAL_CENTER_CAIXA = easyxf('font: name Arial, height 160; '
                                  'align: wrap on, vert center, horiz center; '
                                  'borders: left 2, right 1, top 2, bottom 1;')
TEXT_NORMAL_CENTER_HEADER_V = easyxf('font: name Arial, height 160; '
                                     'align: wrap on, vert center, horiz center; '
                                     'borders: left 1, right 1, top 2, bottom 2;')
TEXT_NORMAL_CENTER_HEADER_H = easyxf('font: name Arial, height 160; '
                                     'align: wrap on, vert center, horiz center; '
                                     'borders: left 1, right 1, top 2, bottom 1;')
TEXT_NORMAL_CENTER_HEADER_OBS = easyxf('font: name Arial, height 160; align: vert center, horiz center; '
                                       'borders: left 1, right 2, top 2, bottom 2;')
TEXT_NORMAL_CENTER_HEADER_BOTTON_L = easyxf('font: name Arial, height 160; '
                                            'align: vert center, horiz center; '
                                            'borders: left 2, right 1, top 1, bottom 2;')
TEXT_NORMAL_CENTER_HEADER_BOTTON_R = easyxf('font: name Arial, height 160; '
                                            'align: vert center, horiz center; '
                                            'borders: left 1, right 1, top 1, bottom 2;')
TEXT_NORMAL_CENTER_BODY_L = easyxf('font: name Arial, height 160; align: vert center, horiz center; '
                                   'borders: left 2, right 1, bottom 1;')
NUMBER_NORMAL_CENTER_BODY_C = easyxf('font: name Arial, height 160; align: vert center, horiz center; '
                                     'borders: left 1, right 1, bottom 1;', num_format_str='#,##0.00')
NUMBER_NORMAL_CENTER_BODY_C_000 = easyxf('font: name Arial, height 160; align: vert center, horiz center; '
                                         'borders: left 1, right 1, bottom 1;', num_format_str='#,##0.000')
NUMBER_NORMAL_CENTER_BODY_C_0 = easyxf('font: name Arial, height 160; align: vert center, horiz center; '
                                       'borders: left 1, right 1, bottom 1;', num_format_str='#,##0.0')
TEXT_NORMAL_CENTER_BODY_R = easyxf('font: name Arial, height 160; align: vert center, horiz center; '
                                   'borders: left 1, right 2, bottom 1;', num_format_str='#,##0.00')
TEXT_NOTES_SPACE = easyxf('font: name Arial, height 240, bold True; '
                          'align: vert center, horiz center; '
                          'borders: left 2, right 2, top 2, bottom 2;')
TEXT_BOLD_CENTER_OBS_0 = easyxf('font: name Arial, height 240, bold True; '
                                'align: vert center, horiz center; '
                                'borders: left 2, right 2, top 2, bottom 0;')
TEXT_NORMAL_CENTER_OBS_1 = easyxf('font: name Arial, height 200; align: vert center, horiz left; '
                                  'borders: left 2, right 0, top 0, bottom 0;')
TEXT_NORMAL_CENTER_OBS_2 = easyxf('font: name Arial, height 200; align: vert center, horiz center; '
                                  'borders: left 0, right 2, top 0, bottom 0;')
TEXT_NORMAL_CENTER_OBS_3 = easyxf('font: name Arial, height 200; align: vert center, horiz center; '
                                  'borders: left 2, right 2, top 0, bottom 0;')
TEXT_NORMAL_LEFT_EMIS = easyxf('font: name Arial, height 160; align: vert center, horiz left; '
                               'borders: left 2, right 1, top 2, bottom 0;')
TEXT_NORMAL_CENTER_EMIS_POR = easyxf('font: name Arial, height 160; align: vert center, horiz center; '
                                     'borders: left 2, right 0, top 0, bottom 0;')
TEXT_NORMAL_CENTER_EMIS_ROW = easyxf('font: name Arial, height 160; align: vert center, horiz center; '
                                     'borders: left 0, right 1, top 0, bottom 0;')
TEXT_NORMAL_CENTER_EMIS_PROJ = easyxf('font: name Arial, height 160; align: vert center, horiz center; '
                                      'borders: left 2, right 1, top 0, bottom 2;')
TEXT_NORMAL_CENTER_LIB = easyxf('font: name Arial, height 160; align: vert center, horiz center; '
                                'borders: left 1, right 1, top 2, bottom 0;')
TEXT_NORMAL_CENTER_LIB_POR = easyxf('font: name Arial, height 160; align: vert center, horiz center; '
                                    'borders: left 1, right 0, top 0, bottom 0;')
TEXT_NORMAL_CENTER_LIB_ROW = easyxf('font: name Arial, height 160; align: vert center, horiz center; '
                                    'borders: left 0, right 1, top 0, bottom 0;')
TEXT_NORMAL_CENTER_LIB_FIS = easyxf('font: name Arial, height 160; align: vert center, horiz center; '
                                    'borders: left 1, right 1, top 0, bottom 2;')
TEXT_NORMAL_CENTER_REC = easyxf('font: name Arial, height 160; align: vert center, horiz center; '
                                'borders: left 1, right 2, top 2, bottom 0;')
TEXT_NORMAL_CENTER_REC_POR = easyxf('font: name Arial, height 160; align: vert center, horiz center; '
                                    'borders: left 1, right 0, top 0, bottom 0;')
TEXT_NORMAL_CENTER_REC_ROW = easyxf('font: name Arial, height 160; align: vert center, horiz center; '
                                    'borders: left 0, right 2, top 0, bottom 0;')
TEXT_NORMAL_CENTER_REC_CONS = easyxf('font: name Arial, height 160; align: vert center, horiz center; '
                                     'borders: left 1, right 2, top 0, bottom 2;')
TEXT_BOLD_LEFT = easyxf('font: name Arial, height 160, bold True; align: vert center, horiz left;')
TEXT_NORMAL_CENTER = easyxf('font: name Arial, height 160; align: wrap on, vert center, horiz center;')
TEXT_NORMAL_LEFT = easyxf('font: name Arial, height 160; align: vert center, horiz left;')
TEXT_NORMAL_RIGHT = easyxf('font: name Arial, height 160; align: vert center, horiz right;')
NUMBER_STYLE = easyxf(num_format_str='#,##0.00')
DATE_STYLE = easyxf(num_format_str='D-MMM-YY')
BORDER_1 = easyxf('borders: left 2, right 2, top 2, bottom 2;')
BORDER_2 = easyxf('borders: left 2, right 2, top 2, bottom 0;')
BORDER_LEFT = easyxf('borders: left 2, right 0, top 0, bottom 0;')
BORDER_RIGHT = easyxf('borders: left 0, right 2, top 0, bottom 0;')
