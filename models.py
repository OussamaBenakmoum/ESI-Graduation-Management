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
    teachermark = fields.Char(string="Note de enadrant", required=True)
    date_prevue = fields.Date(string="Date prévue")


class Creneau(models.Model):
    _name = 'graduation.creneau'
    _inherit = 'graduation.demande'
    _description = "créneaux des soutenances"

    description = fields.Char(string="description creneau", required=True)
    descriptiondeux = fields.Char(string="description deux creneau", required=True)
