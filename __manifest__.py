# Copyright 2020 Ilaria Franchini <i.franchini@apuliasoftware.it>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'Fix l10n_italy_ricevute_bancarie for enterprise',
    'version': '12.0.1.0.0',
    'author': 'Apulia software',
    'category': 'Localization/Italy',
    'summary': 'Fix l10n_italy_ricevute_bancarie for enterprise',
    'website': 'http://www.apuliasoftware.it',
    'depends' : [
                 'l10n_italy_ricevute_bancarie',
                ],
    'data': [
        'views/riba_view.xml'
            ],
    'installable': True,
}
