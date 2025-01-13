from ..data.models import Costs, Ramal, Segment
from typing import Dict
import math


class CostCalculationRamal:
    def __init__(self, costs: Costs, ramal: Ramal):
        self.costs = costs
        self.ramal = ramal

    def get_total_extention(self):
        return sum([segment.length + segment.h_tq for segment in self.ramal.segments])

    def get_total_extension_100(self):
        return sum([segment.length + segment.h_tq for segment in self.ramal.segments if segment.pvc_diameter in (100, 110)])

    def get_total_extension_150(self):
        return sum([segment.length + segment.h_tq for segment in self.ramal.segments if segment.pvc_diameter in (150, 160)])

    def get_total_volume(self):
        if self.ramal.is_aerial:
            return 0
        total_volume = 0
        for segment in self.ramal.segments:
            prof_media = (segment.up_qproject + segment.dwn_qproject) / 2
            width = self.costs.TRENCH_WIDTH
            area = width * segment.length
            cradle_height = self.costs.CRADLE_HEIGHT
            volume = area * (prof_media + cradle_height)
            total_volume += volume
        return total_volume

    def get_soil_volume(self):
        return self.get_total_volume() * self.costs.SOIL_PERCENT / 100

    def get_rock_volume(self):
        return self.get_total_volume() * self.costs.ROCK_PERCENT / 100

    def get_manual_volume(self):
        return self.get_soil_volume() * self.costs.MANUAL_PERCENT / 100

    def get_mechanical_volume(self):
        return self.get_soil_volume() * self.costs.MECHANICAL_PERCENT / 100

    def get_total_volume_tube_100(self):
        if self.ramal.is_aerial:
            return 0
        return math.pi * (0.1 / 2) ** 2 * self.get_total_extension_100()

    def get_total_volume_tube_150(self):
        if self.ramal.is_aerial:
            return 0
        return math.pi * (0.15 / 2) ** 2 * self.get_total_extension_150()

    def get_total_disposal_soil(self):
        return self.get_soil_volume()

    def get_total_disposal_soil_with_bulking(self):
        return self.get_total_disposal_soil() * self.costs.SOIL_BULKING

    def get_total_disposal_rock(self):
        return self.get_rock_volume()

    def get_total_disposal_rock_with_swelling(self):
        return self.get_total_disposal_rock() * self.costs.ROCK_SWELLING

    def get_total_backfill_soil(self):
        if self.ramal.is_aerial or self.costs.SOIL_PERCENT == 0:
            return 0

        return self.get_soil_volume() - self.get_total_volume_tube_100() - self.get_total_volume_tube_150()

    def get_total_backfill_rock(self):
        if self.ramal.is_aerial or self.costs.ROCK_PERCENT == 0:
            return 0

        return self.get_rock_volume() - self.get_total_volume_tube_100() - self.get_total_volume_tube_150()

    def get_total_backfill_enclosure_cradle(self):
        return ((self.get_total_extention() * self.costs.CRADLE_HEIGHT) *
                (self.costs.WRAP_HEIGHT + self.costs.CRADLE_HEIGHT))

    def get_total_backfill_own(self):
        if self.ramal.is_aerial or self.costs.SOIL_PERCENT == 0:
            return 0
        return self.get_total_backfill_soil() * self.costs.OWN_PERCENT / 100 - self.get_total_backfill_enclosure_cradle()

    def get_total_backfill_contribution(self):
        if self.ramal.is_aerial or self.costs.SOIL_PERCENT == 0:
            return 0
        return self.get_total_backfill_soil() * self.costs.CONTRIBUTION_PERCENT / 100 + \
            self.get_total_backfill_rock() - self.get_total_backfill_enclosure_cradle()

    def get_total_area(self):
        return self.get_total_extention() * self.costs.TRENCH_WIDTH

    def get_pavement_areas(self):
        result = {}
        for segment in self.ramal.segments:
            if segment.paviment_1 and segment.paviment_1 not in result:
                result[segment.paviment_1] = 0
            if segment.paviment_2 and segment.paviment_2 not in result:
                result[segment.paviment_2] = 0
            result[segment.paviment_1] += segment.percent_pav_1 * segment.length * self.costs.TRENCH_WIDTH
            result[segment.paviment_2] += segment.percent_pav_2 * segment.length * self.costs.TRENCH_WIDTH
        return result

    def get_node_counts(self):
        result = {}
        for i, segment in enumerate(self.ramal.segments):
            c1 = segment.UpBox.node_type
            c2 = segment.DownBox.node_type
            if c1 not in result:
                result[c1] = 0
            if c2 not in result and i == len(self.ramal.segments) - 1:
                result[c2] = 0
            result[c1] += 1
            if i == len(self.ramal.segments) - 1:
                result[c2] += 1
        return result


class CostCalculation:
    def __init__(self, costs: Costs, ramals: Dict[str, Ramal]):
        self.costs = costs
        self.ramals = ramals
        self.calculations = {}
        for key, ramal in ramals.items():
            self.calculations[key] = CostCalculationRamal(costs, ramal)

    def get_total_extention(self):
        return sum([calc.get_total_extention() for calc in self.calculations.values()])

    def get_total_extension_100(self):
        return sum([calc.get_total_extension_100() for calc in self.calculations.values()])

    def get_total_extension_150(self):
        return sum([calc.get_total_extension_150() for calc in self.calculations.values()])

    def get_total_volume(self):
        return sum([calc.get_total_volume() for calc in self.calculations.values()])

    def get_soil_volume(self):
        return sum([calc.get_soil_volume() for calc in self.calculations.values()])

    def get_rock_volume(self):
        return sum([calc.get_rock_volume() for calc in self.calculations.values()])

    def get_manual_volume(self):
        return sum([calc.get_manual_volume() for calc in self.calculations.values()])

    def get_mechanical_volume(self):
        return sum([calc.get_mechanical_volume() for calc in self.calculations.values()])

    def get_total_volume_tube_100(self):
        return sum([calc.get_total_volume_tube_100() for calc in self.calculations.values()])

    def get_total_volume_tube_150(self):
        return sum([calc.get_total_volume_tube_150() for calc in self.calculations.values()])

    def get_total_disposal_soil(self):
        return sum([calc.get_total_disposal_soil() for calc in self.calculations.values()])

    def get_total_disposal_soil_with_bulking(self):
        return sum([calc.get_total_disposal_soil_with_bulking() for calc in self.calculations.values()])

    def get_total_disposal_rock(self):
        return sum([calc.get_total_disposal_rock() for calc in self.calculations.values()])

    def get_total_disposal_rock_with_swelling(self):
        return sum([calc.get_total_disposal_rock_with_swelling() for calc in self.calculations.values()])

    def get_total_backfill_soil(self):
        return sum([calc.get_total_backfill_soil() for calc in self.calculations.values()])

    def get_total_backfill_rock(self):
        return sum([calc.get_total_backfill_rock() for calc in self.calculations.values()])

    def get_total_backfill_enclosure_cradle(self):
        return sum([calc.get_total_backfill_enclosure_cradle() for calc in self.calculations.values()])

    def get_total_backfill_own(self):
        return sum([calc.get_total_backfill_own() for calc in self.calculations.values()])

    def get_total_backfill_contribution(self):
        return sum([calc.get_total_backfill_contribution() for calc in self.calculations.values()])

    def get_total_area(self):
        return sum([calc.get_total_area() for calc in self.calculations.values()])

    def get_pavement_areas(self):
        total_pavement_areas = {}
        for calc in self.calculations.values():
            pavement_areas = calc.get_pavement_areas()
            for pavement, area in pavement_areas.items():
                if pavement not in total_pavement_areas:
                    total_pavement_areas[pavement] = 0
                total_pavement_areas[pavement] += area
        return total_pavement_areas

    def get_node_counts(self):
        total_node_counts = {}
        for calc in self.calculations.values():
            node_counts = calc.get_node_counts()
            for node_type, count in node_counts.items():
                if node_type not in total_node_counts:
                    total_node_counts[node_type] = 0
                total_node_counts[node_type] += count
        return total_node_counts

    def get_security_plate(self):
        return math.ceil(self.get_total_extention() / 100 * 10) / 10

    def get_security_fence(self):
        return self.get_total_extention() * 1.2

    def get_security_wood(self):
        return math.ceil(self.get_total_extention() / 50 * 10) / 10

    def get_security_metal(self):
        return math.ceil(self.get_total_extention() / 150 * 10) / 10



