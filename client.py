class CrossBorderDutyCustomsTariffEstimatorClient:
    def estimate_landed_customs_duty(self, hs_tariff_code='6109.10.00', declared_value_usd=85.00, origin_country='US', destination_country='DE'):
        duty_rate = 0.12
        vat_rate = 0.19
        duty = round(declared_value_usd * duty_rate, 2)
        vat = round((declared_value_usd + duty) * vat_rate, 2)
        total_tax = round(duty + vat, 2)
        return {
            'tariff_calculation_id': 'trf_cst_8812',
            'hs_tariff_code': hs_tariff_code,
            'import_duty_usd': duty,
            'import_vat_usd': vat,
            'total_customs_tax_usd': total_tax,
            'ddp_delivery_duty_paid_certified': True,
            'customs_breakdown_url': 'https://customs.border.genpark.ai/estimates/8812.json'
        }
