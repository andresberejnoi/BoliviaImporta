
import argparse

GA_taxes_dict = {
    'electronics': 0.10,
    'leather_shoes': 0.40,
    'sport_shoes':0.10,
    'clothes':0.10,
}

def round_number_up(number):
    '''In this case, we want to round the number up to the next integer if it is above .5
    However, if it is below .5 we don't round down. We keep it as it is, for tax purposes.'''

    rounded = round(number)
    if rounded < number:
        return number
    return rounded

def get_FOB(price):
    '''FOB is "Free on Board" (basically the cost of the item without shipping)'''

def get_CIF(price,shipping,insurance,currency='USD',exchange_rate=6.96):
    """Returns tuple with CIF and original price after currency conversion.
    CIF is Cost, Insurance and Freight

    price: price of the product without shipping (FOB number)(Usually in USD)
    shipping: cost of shipping  (usually in USD but it should match the currency for price)
    insurance: cost of insurance paid for the product
    currency: the original currency for price and shipping
    exchange_rate: the going rate for converting the currency selected to bolivianos (bs)
    """

    if currency.lower() != 'bs':        #if the currency used was not bolivianos to begin with, use the exchange_rate
        bs_price = price * exchange_rate
    else:
        bs_price = price

    #--Now calculate CIF
    cif = bs_price
    if shipping > 0:
        cif += 5
    else:
        cif += round_number_up(bs_price*0.05)    #five percent of the price when shipping is free
    if insurance > 0:
        pass
    else:
        cif += round_number_up(bs_price*0.02)

    return cif, bs_price

def get_GA(cif,product_type='electronics'):
    '''Add customs tax based on product type. The tax rates should be updated regularly to make sure they are up to date.
    Returns GA tax based on product type (not added to CIF)
    '''

    tax_rate = GA_taxes_dict[product_type]

    GA = round_number_up(cif * tax_rate)
    return GA

def get_IVA(value, iva_rate=0.1494):
    '''Return IVA tax to pay based on current rate'''
    iva = round_number_up(value * iva_rate)
    return iva

def calculate_tax_percentage(price,tax):
    '''Just a simple calculation to see how much the tax compares to the actual product.
    Make sure price and tax numbers are in the same currency.
    Returns percentage of tax to price (from 0 to 100)'''
    tax_percent = (tax*100) / price
    return tax_percent

def convert_to_bolivianos(price,currency='USD',exchange_rate=6.96):
    '''convert any currency to bolivanos using the exchange rate.
    If price is already in bolivanos then set currency to "BS" or "bs"
    '''
    if currency.lower() != 'bs':        #if the currency used was not bolivianos to begin with, use the exchange_rate
        bs_price = price * exchange_rate
    else:
        bs_price = price
    return bs_price

def convert_bolivianos_to_other(price,currency='USD',exchange_rate=6.96):
    '''Converts bolivanos to original currency. Assumes that function convert_to_bolivianos has already been used
    so basically, use this function to revert back the conversion'''
    if currency.lower() == 'bs':
        return price

    converted_price = price / exchange_rate
    return converted_price

def print_report(price,total_tax,tax_percent,currency,exchange_rate):
    final_price = price + total_tax
    original_currency_final_price = convert_bolivianos_to_other(final_price)
    print("")
    print("{:<23} : bs {:.2f}".format("Impuesto final",total_tax))
    print("{:<23} : bs {:.2f}".format("Producto + impuesto",final_price))
    print("{:<23} : {:.2f}%".format("Porcentaje de impuesto",tax_percent))

    print("")
    print("{:<23} : {:.2f} {}".format("Costo final en Moneda original",original_currency_final_price,currency))

def main(args):
    price         = args.price
    shipping      = args.shipping
    insurance     = args.insurance
    currency      = args.currency
    exchange_rate = args.exchange_rate
    product_type  = args.product_type
    iva_rate      = args.iva

    inital_cost       = price + shipping + insurance
    inital_cost_in_bs = convert_to_bolivianos(inital_cost,currency,exchange_rate)
    # First we calculate CIF
    cif, bs_price = get_CIF(price,shipping,insurance)
    ga = get_GA(cif,product_type)

    _value = cif + ga
    iva    = get_IVA(_value, iva_rate)

    total_tax   = iva + ga
    tax_percent = calculate_tax_percentage(bs_price,total_tax)

    #Create report for user
    print_report(inital_cost_in_bs, total_tax, tax_percent, currency,exchange_rate)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Caluladora de Impuestos de Aduana Bolivana (Importaciones)')
    parser.add_argument('-p','--price', type=float, help="Precio del articulo a importar (no incluir envio ni seguro)")
    parser.add_argument('-s','--shipping',type=float, help="Costo del envio")
    parser.add_argument('-i','--insurance',default=0, type=float, help="Costo del seguro. Falta implementar. Por el momento solo funciona cuando es 0")
    parser.add_argument('-c','--currency',default='USD', type=str, help="Moneda usada para la compra (default: USD)")
    parser.add_argument('-ex','--exchange_rate',default=6.96, type=float,
                        help="Precio de la moneda de compra en bolivianos. Por defeccto es 6.96 para dolar a bolivanos")
    parser.add_argument('-pt','--product_type',default='electronics',choices=['electronics','leather_shoes','sport_shoes','clothes'],
                        type=str,help="Tipo de producto importado para determinar impuesto de arancel.")
    parser.add_argument('-iva', default=0.1494, type=float, help="Porcentaje del impuesto IVA. Por defecto esta en 14.94%% (como 0.1494)")

    args = parser.parse_args()
    main(args)
