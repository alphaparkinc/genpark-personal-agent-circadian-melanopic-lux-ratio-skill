# -*- coding: utf-8 -*-
"""Circadian Melanopic Lux Ratio Sensor for GenPark Personal Agent."""
import json
from typing import Dict, Any

class CircadianMelanopicLuxRatioSensor:
    @staticmethod
    def calculate_equivalent_melanopic_lux(photopic_lux: float, light_source_type: str) -> Dict[str, Any]:
        # Melanopic-to-Photopic (M/P) ratio lookup
        mp_ratios = {
            "natural_daylight": 1.10,
            "cool_white_led_6500k": 0.92,
            "warm_incandescent_2700k": 0.45,
            "candlelight": 0.20
        }
        mp = mp_ratios.get(light_source_type, 0.70)
        eml = round(photopic_lux * mp * 1.218, 1)  # WELL EML conversion factor
        
        return {
            "light_source": light_source_type,
            "photopic_illuminance_lux": photopic_lux,
            "melanopic_photopic_ratio": mp,
            "equivalent_melanopic_lux_eml": eml,
            "iprgc_activation_tier": "HIGH_CIRCADIAN_STIMULATION" if eml >= 250 else ("LOW_CIRCADIAN_STIMULATION (Pre-sleep Safe)" if eml <= 50 else "MODERATE_AMBIENT")
        }

    @staticmethod
    def audit_well_building_circadian_lighting_compliance(eml_reading: float, time_of_day_24h: float) -> Dict[str, Any]:
        is_morning_work_hours = (9.0 <= time_of_day_24h <= 13.0)
        is_evening = (time_of_day_24h >= 20.0 or time_of_day_24h <= 6.0)
        
        if is_morning_work_hours:
            compliant = eml_reading >= 250.0
            status = "WELL_V2_FEATURE_L03_MET" if compliant else "CIRCADIAN_DEFICIT_INCREASE_LIGHTING"
        elif is_evening:
            compliant = eml_reading <= 50.0
            status = "PRE_SLEEP_COMPLIANT" if compliant else "MELATONIN_SUPPRESSION_RISK"
        else:
            compliant = True
            status = "TRANSITIONAL_AFTERNOON"
            
        return {
            "current_eml": eml_reading,
            "time_decimal": time_of_day_24h,
            "well_standard_compliant": compliant,
            "audit_verdict": status,
            "recommendation": "Step outdoors for 15 minutes of direct sunlight." if (is_morning_work_hours and not compliant) else "Dim screens and engage blue light filters."
        }
