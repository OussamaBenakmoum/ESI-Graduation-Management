from email.policy import default
from odoo import models, fields, api
from datetime import datetime, timedelta



class Demande(models.Model):
    _name = 'graduation.demande'
    _description = "demandes de soutenance"

    firststudent = fields.Char(string="Premier étudiant", required=True)
    checkbinome = fields.Boolean('Projet Binome ?', default=False)
    if checkbinome :
        secondstudent = fields.Char(string="Deuxieme étudiant", required=False)
    else :
        secondstudent = None
    projecttitle = fields.Char(string="Titre projet", required=True)
    linkpfe = fields.Char(string="Lien vers le PFE", required=True)
    teacher = fields.Many2one('res.users','Encadrant', default=lambda self: self.env.user, readonly=True)
    teachermark = fields.Float(string="Note de enadrant", required=True)
    date_prevue = fields.Date(string="Date prévue")


class Creneau(models.Model):
    _name = 'graduation.creneau'
    _inherit = 'graduation.demande'
    _description = "créneaux des soutenances"


    premierjury = fields.Char(string="Premier jury", required=True)
    premierenote = fields.Float(string="Première note", required=True)

    deuxiemejury = fields.Char(string="Deuxième jury", required=True)
    deuxiemenote = fields.Float(string="Deuxième note", required=True)

    troisiemejury = fields.Char(string="Troisième jury", required=True)
    troisiemenote = fields.Float(string="Troisièmeième note", required=True)

    date_soutenance = fields.Date(string="Date Soutenance")
