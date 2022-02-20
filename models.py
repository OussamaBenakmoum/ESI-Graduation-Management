from odoo import models, fields, api
from datetime import datetime, timedelta



class Demande(models.Model):
    _name = 'graduation.demande'
    _description = "demandes de soutenance"

    firststudent = fields.Char(string="Premier étudiant", required=True)
    secondstudent = fields.Char(string="Deuxieme étudiant", required=False)
    projecttitle = fields.Char(string="Titre projet", required=True)
    linkpfe = fields.Char(string="Lien vers le PFE", required=True)
    supervisor = fields.Char(string="Nom promoteur", required=True)
    supervisormark = fields.Char(string="Note de sperviseur", required=True)
    date_prevue = fields.Date(string="Date prévue")


class Creneau(models.Model):
    _name = 'graduation.creneau'
    _inherit = 'graduation.demande'
    _description = "créneaux des soutenances"

    description = fields.Char(string="description creneau", required=True)
    descriptiondeux = fields.Char(string="description deux creneau", required=True)
