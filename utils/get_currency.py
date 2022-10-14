import locale
import ipdb

locale.setlocale( locale.LC_ALL, "pt_BR.UTF-8" )
# locale.setlocale(locale.LC_ALL, "Portuguese_Brazil.1252")

def get_currency(value):
    return locale.currency(value, grouping=True)