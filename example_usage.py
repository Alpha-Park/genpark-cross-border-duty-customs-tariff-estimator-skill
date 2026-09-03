from client import CrossBorderDutyCustomsTariffEstimatorClient

def main():
    client = CrossBorderDutyCustomsTariffEstimatorClient()
    res = client.estimate_landed_customs_duty('6203.42.00', 120.00, 'US', 'GB')
    print('Cross-Border Tariff Estimator: ' + res['tariff_calculation_id'])
    print('Duty: $' + str(res['import_duty_usd']) + ' | VAT: $' + str(res['import_vat_usd']) + ' | Total: $' + str(res['total_customs_tax_usd']))
    print('Breakdown URL: ' + res['customs_breakdown_url'])

if __name__ == '__main__':
    main()
