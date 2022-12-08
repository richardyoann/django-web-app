# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Adresse(models.Model):
    adresseid = models.AutoField(db_column='AdresseId', primary_key=True)  # Field name made lowercase.
    villeid = models.ForeignKey('Ville', models.DO_NOTHING, db_column='VilleId', blank=True, null=True)  # Field name made lowercase.
    adresse1 = models.CharField(db_column='Adresse1', max_length=50)  # Field name made lowercase.
    adresse2 = models.CharField(db_column='Adresse2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    valide = models.IntegerField(db_column='Valide')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adresse'


class Adressesurinscription(models.Model):
    inscriptionid = models.OneToOneField('Inscription', models.DO_NOTHING, db_column='InscriptionId', primary_key=True)  # Field name made lowercase.
    adresseid = models.ForeignKey(Adresse, models.DO_NOTHING, db_column='AdresseId')  # Field name made lowercase.
    facturation = models.IntegerField(db_column='Facturation')  # Field name made lowercase.
    convention = models.IntegerField(db_column='Convention')  # Field name made lowercase.
    lettreconvention = models.IntegerField(db_column='LettreConvention')  # Field name made lowercase.
    attestation = models.IntegerField(db_column='Attestation')  # Field name made lowercase.
    copie = models.IntegerField(db_column='Copie')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adressesurinscription'
        unique_together = (('inscriptionid', 'adresseid'),)


class AuditContact(models.Model):
    nom = models.CharField(db_column='Nom', max_length=50, blank=True, null=True)  # Field name made lowercase.
    prenom = models.CharField(db_column='Prenom', max_length=50, blank=True, null=True)  # Field name made lowercase.
    qui = models.CharField(db_column='Qui', max_length=50, blank=True, null=True)  # Field name made lowercase.
    quand = models.DateTimeField(db_column='Quand', blank=True, null=True)  # Field name made lowercase.
    operation = models.CharField(db_column='Operation', max_length=6, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'audit_contact'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Contact(models.Model):
    contactid = models.AutoField(db_column='ContactId', primary_key=True)  # Field name made lowercase.
    titre = models.CharField(db_column='Titre', max_length=3, blank=True, null=True)  # Field name made lowercase.
    nom = models.CharField(db_column='Nom', max_length=50)  # Field name made lowercase.
    prenom = models.CharField(db_column='Prenom', max_length=50, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=150, blank=True, null=True)  # Field name made lowercase.
    telephone = models.CharField(db_column='Telephone', max_length=15, blank=True, null=True)  # Field name made lowercase.
    telecopie = models.CharField(db_column='Telecopie', max_length=15, blank=True, null=True)  # Field name made lowercase.
    sexe = models.CharField(db_column='Sexe', max_length=1, blank=True, null=True)  # Field name made lowercase.
    portable = models.CharField(db_column='Portable', max_length=15, blank=True, null=True)  # Field name made lowercase.
    adressepostaleid = models.IntegerField(db_column='AdressePostaleId', blank=True, null=True)  # Field name made lowercase.
    societeid = models.ForeignKey('Societe', models.DO_NOTHING, db_column='SocieteId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'contact'


class Dates(models.Model):
    jour = models.DateField(unique=True, blank=True, null=True)
    joursemaine = models.IntegerField(db_column='JourSemaine', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dates'


class Decideur(models.Model):
    decideurid = models.AutoField(db_column='DecideurId', primary_key=True)  # Field name made lowercase.
    contactid = models.ForeignKey(Contact, models.DO_NOTHING, db_column='ContactId', blank=True, null=True)  # Field name made lowercase.
    dateannulation = models.DateField(db_column='DateAnnulation', blank=True, null=True)  # Field name made lowercase.
    envoisparemail = models.IntegerField(db_column='EnvoisParEmail')  # Field name made lowercase.
    envoisparcourrier = models.IntegerField(db_column='EnvoisParCourrier')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'decideur'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Elections(models.Model):
    parti = models.CharField(max_length=5, blank=True, null=True)
    candidat = models.CharField(unique=True, max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'elections'


class Employe(models.Model):
    employeid = models.IntegerField(db_column='EmployeId', primary_key=True)  # Field name made lowercase.
    nom = models.CharField(db_column='Nom', unique=True, max_length=50)  # Field name made lowercase.
    chefid = models.IntegerField(db_column='ChefId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'employe'


class Evaluation(models.Model):
    evaluationid = models.AutoField(db_column='EvaluationId', primary_key=True)  # Field name made lowercase.
    contactid = models.ForeignKey(Contact, models.DO_NOTHING, db_column='ContactId', blank=True, null=True)  # Field name made lowercase.
    tauxsatisfaction = models.IntegerField(db_column='TauxSatisfaction')  # Field name made lowercase.
    interet = models.IntegerField(db_column='Interet', blank=True, null=True)  # Field name made lowercase.
    tempsaccorde = models.IntegerField(db_column='TempsAccorde', blank=True, null=True)  # Field name made lowercase.
    exercices = models.IntegerField(db_column='Exercices', blank=True, null=True)  # Field name made lowercase.
    support = models.IntegerField(db_column='Support', blank=True, null=True)  # Field name made lowercase.
    animation = models.IntegerField(db_column='Animation', blank=True, null=True)  # Field name made lowercase.
    equilibre = models.IntegerField(db_column='Equilibre', blank=True, null=True)  # Field name made lowercase.
    observations = models.CharField(db_column='Observations', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    ajouter = models.CharField(db_column='Ajouter', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    supprimer = models.CharField(db_column='Supprimer', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    attentes = models.IntegerField(db_column='Attentes', blank=True, null=True)  # Field name made lowercase.
    organisation = models.IntegerField(db_column='Organisation', blank=True, null=True)  # Field name made lowercase.
    accueil = models.IntegerField(db_column='Accueil', blank=True, null=True)  # Field name made lowercase.
    confort = models.IntegerField(db_column='Confort', blank=True, null=True)  # Field name made lowercase.
    connaissancepacha = models.IntegerField(db_column='ConnaissancePacha', blank=True, null=True)  # Field name made lowercase.
    nouveautes = models.IntegerField(db_column='Nouveautes', blank=True, null=True)  # Field name made lowercase.
    recommandation = models.IntegerField(db_column='Recommandation', blank=True, null=True)  # Field name made lowercase.
    jour1interet = models.IntegerField(db_column='Jour1Interet', blank=True, null=True)  # Field name made lowercase.
    jour2interet = models.IntegerField(db_column='Jour2Interet', blank=True, null=True)  # Field name made lowercase.
    jour3interet = models.IntegerField(db_column='Jour3Interet', blank=True, null=True)  # Field name made lowercase.
    jour4interet = models.IntegerField(db_column='Jour4Interet', blank=True, null=True)  # Field name made lowercase.
    jour5interet = models.IntegerField(db_column='Jour5Interet', blank=True, null=True)  # Field name made lowercase.
    jour1pedagogie = models.IntegerField(db_column='Jour1Pedagogie', blank=True, null=True)  # Field name made lowercase.
    jour2pedagogie = models.IntegerField(db_column='Jour2Pedagogie', blank=True, null=True)  # Field name made lowercase.
    jour3pedagogie = models.IntegerField(db_column='Jour3Pedagogie', blank=True, null=True)  # Field name made lowercase.
    jour4pedagogie = models.IntegerField(db_column='Jour4Pedagogie', blank=True, null=True)  # Field name made lowercase.
    jour5pedagogie = models.IntegerField(db_column='Jour5Pedagogie', blank=True, null=True)  # Field name made lowercase.
    formation = models.CharField(db_column='Formation', max_length=512, blank=True, null=True)  # Field name made lowercase.
    dateevaluation = models.DateTimeField(db_column='DateEvaluation')  # Field name made lowercase.
    typesaisie = models.IntegerField(db_column='TypeSaisie', blank=True, null=True)  # Field name made lowercase.
    annulee = models.IntegerField(db_column='Annulee', blank=True, null=True)  # Field name made lowercase.
    moyenne = models.DecimalField(db_column='Moyenne', max_digits=4, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    miseajour = models.IntegerField(db_column='MiseAJour')  # Field name made lowercase.
    datemiseajour = models.DateTimeField(db_column='DateMiseAJour', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'evaluation'


class Facture(models.Model):
    facturecd = models.CharField(db_column='FactureCd', primary_key=True, max_length=50)  # Field name made lowercase.
    coderemise = models.CharField(db_column='CodeRemise', max_length=2, blank=True, null=True)  # Field name made lowercase.
    remise = models.DecimalField(db_column='Remise', max_digits=10, decimal_places=7, blank=True, null=True)  # Field name made lowercase.
    datecreation = models.DateTimeField(db_column='DateCreation')  # Field name made lowercase.
    datefacture = models.DateField(db_column='DateFacture', blank=True, null=True)  # Field name made lowercase.
    relance = models.PositiveIntegerField(db_column='Relance')  # Field name made lowercase.
    daterelance = models.DateField(db_column='DateRelance', blank=True, null=True)  # Field name made lowercase.
    part = models.DecimalField(db_column='PART', max_digits=7, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    referencecommande = models.CharField(db_column='ReferenceCommande', max_length=100, blank=True, null=True)  # Field name made lowercase.
    montantht = models.DecimalField(db_column='MontantHT', max_digits=7, decimal_places=2)  # Field name made lowercase.
    montantttc = models.DecimalField(db_column='MontantTTC', max_digits=7, decimal_places=2)  # Field name made lowercase.
    tauxtva = models.DecimalField(db_column='TauxTVA', max_digits=5, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'facture'


class Formateur(models.Model):
    formateurid = models.AutoField(db_column='FormateurId', primary_key=True)  # Field name made lowercase.
    nosecuritesociale = models.CharField(db_column='NoSecuriteSociale', max_length=18, blank=True, null=True)  # Field name made lowercase.
    statut = models.CharField(db_column='Statut', max_length=1, blank=True, null=True)  # Field name made lowercase.
    commentaires = models.CharField(db_column='Commentaires', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    nepascontacter = models.IntegerField(db_column='NePasContacter')  # Field name made lowercase.
    cv = models.IntegerField(db_column='CV', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateField(db_column='CreationDate')  # Field name made lowercase.
    creationuser = models.CharField(db_column='CreationUser', max_length=128)  # Field name made lowercase.
    contactid = models.OneToOneField(Contact, models.DO_NOTHING, db_column='ContactId')  # Field name made lowercase.
    societeformateurid = models.ForeignKey('Societeformateur', models.DO_NOTHING, db_column='SocieteFormateurId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'formateur'


class Inscription(models.Model):
    inscriptionid = models.AutoField(db_column='InscriptionId', primary_key=True)  # Field name made lowercase.
    sessionid = models.IntegerField(db_column='SessionId')  # Field name made lowercase.
    decideurinscriptionid = models.ForeignKey(Decideur, models.DO_NOTHING, db_column='DecideurInscriptionId', blank=True, null=True)  # Field name made lowercase.
    contactid = models.ForeignKey(Contact, models.DO_NOTHING, db_column='ContactId', blank=True, null=True)  # Field name made lowercase.
    dateannulation = models.DateField(db_column='DateAnnulation', blank=True, null=True)  # Field name made lowercase.
    remise = models.PositiveIntegerField(db_column='Remise')  # Field name made lowercase.
    present = models.IntegerField(db_column='Present')  # Field name made lowercase.
    datecreation = models.DateTimeField(db_column='DateCreation')  # Field name made lowercase.
    referencecommande = models.CharField(db_column='ReferenceCommande', max_length=100, blank=True, null=True)  # Field name made lowercase.
    conventionenvoyee = models.IntegerField(db_column='ConventionEnvoyee')  # Field name made lowercase.
    convocationenvoyee = models.IntegerField(db_column='ConvocationEnvoyee')  # Field name made lowercase.
    listeattente = models.IntegerField(db_column='ListeAttente')  # Field name made lowercase.
    feuilleemargement = models.CharField(db_column='FeuilleEmargement', max_length=1000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'inscription'


class Inscriptionfacture(models.Model):
    inscriptionid = models.OneToOneField(Inscription, models.DO_NOTHING, db_column='InscriptionId', primary_key=True)  # Field name made lowercase.
    facturecd = models.ForeignKey(Facture, models.DO_NOTHING, db_column='FactureCd')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'inscriptionfacture'
        unique_together = (('inscriptionid', 'facturecd'),)


class Langue(models.Model):
    languecd = models.CharField(db_column='LangueCd', primary_key=True, max_length=2)  # Field name made lowercase.
    nomlocal = models.CharField(db_column='NomLocal', unique=True, max_length=50)  # Field name made lowercase.
    nomfrancais = models.CharField(db_column='NomFrancais', unique=True, max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'langue'


class Lieuformation(models.Model):
    lieuformationid = models.AutoField(db_column='LieuFormationId', primary_key=True)  # Field name made lowercase.
    nom = models.CharField(db_column='Nom', max_length=30, blank=True, null=True)  # Field name made lowercase.
    adresse1 = models.CharField(db_column='Adresse1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    adresse2 = models.CharField(db_column='Adresse2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    codepostal = models.CharField(db_column='CodePostal', max_length=7, blank=True, null=True)  # Field name made lowercase.
    ville = models.CharField(db_column='Ville', max_length=20, blank=True, null=True)  # Field name made lowercase.
    metro = models.CharField(db_column='Metro', max_length=30, blank=True, null=True)  # Field name made lowercase.
    telephone = models.CharField(db_column='Telephone', max_length=25, blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='Fax', max_length=25, blank=True, null=True)  # Field name made lowercase.
    planacces = models.CharField(db_column='PlanAcces', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nomcontact = models.CharField(db_column='NomContact', max_length=50, blank=True, null=True)  # Field name made lowercase.
    emailcontact = models.CharField(db_column='EmailContact', max_length=200, blank=True, null=True)  # Field name made lowercase.
    estcentrepacha = models.IntegerField(db_column='EstCentrePacha')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lieuformation'


class Modepaiement(models.Model):
    modepaiementcd = models.CharField(db_column='ModePaiementCd', primary_key=True, max_length=8)  # Field name made lowercase.
    libelle = models.CharField(db_column='Libelle', unique=True, max_length=64)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'modepaiement'


class Nombre(models.Model):
    nombre = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'nombre'


class Pays(models.Model):
    payscd = models.CharField(db_column='PaysCD', primary_key=True, max_length=3)  # Field name made lowercase.
    nomfrancais = models.CharField(db_column='NomFrancais', unique=True, max_length=50)  # Field name made lowercase.
    nomanglais = models.CharField(db_column='NomAnglais', max_length=50)  # Field name made lowercase.
    code2 = models.CharField(db_column='Code2', max_length=2)  # Field name made lowercase.
    capitale = models.CharField(db_column='Capitale', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pays'


class Region(models.Model):
    regionid = models.AutoField(db_column='RegionId', primary_key=True)  # Field name made lowercase.
    payscd = models.ForeignKey(Pays, models.DO_NOTHING, db_column='PaysCD')  # Field name made lowercase.
    typeregion = models.CharField(db_column='TypeRegion', max_length=20, blank=True, null=True)  # Field name made lowercase.
    coderegion = models.CharField(db_column='CodeRegion', max_length=10, blank=True, null=True)  # Field name made lowercase.
    nom = models.CharField(db_column='Nom', max_length=50)  # Field name made lowercase.
    codecheflieu = models.CharField(db_column='CodeChefLieu', max_length=3, blank=True, null=True)  # Field name made lowercase.
    nomcheflieu = models.CharField(db_column='NomChefLieu', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xcheflieu = models.SmallIntegerField(db_column='XChefLieu', blank=True, null=True)  # Field name made lowercase.
    ycheflieu = models.SmallIntegerField(db_column='YChefLieu', blank=True, null=True)  # Field name made lowercase.
    xcentroide = models.SmallIntegerField(db_column='XCentroide', blank=True, null=True)  # Field name made lowercase.
    ycentroide = models.SmallIntegerField(db_column='YCentroide', blank=True, null=True)  # Field name made lowercase.
    codedepartement = models.CharField(db_column='CodeDepartement', max_length=2, blank=True, null=True)  # Field name made lowercase.
    nomdepartement = models.CharField(db_column='NomDepartement', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'region'


class Salleformation(models.Model):
    salleformationid = models.AutoField(db_column='SalleFormationId', primary_key=True)  # Field name made lowercase.
    lieuformationid = models.ForeignKey(Lieuformation, models.DO_NOTHING, db_column='LieuFormationId')  # Field name made lowercase.
    places = models.PositiveIntegerField(db_column='Places')  # Field name made lowercase.
    nom = models.CharField(db_column='Nom', max_length=20, blank=True, null=True)  # Field name made lowercase.
    numero = models.CharField(db_column='Numero', max_length=3, blank=True, null=True)  # Field name made lowercase.
    couloir = models.CharField(db_column='Couloir', max_length=1, blank=True, null=True)  # Field name made lowercase.
    direction = models.CharField(db_column='Direction', max_length=1, blank=True, null=True)  # Field name made lowercase.
    etage = models.PositiveIntegerField(db_column='Etage', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'salleformation'


class Session(models.Model):
    sessionid = models.AutoField(db_column='SessionId', primary_key=True)  # Field name made lowercase.
    stageid = models.ForeignKey('Stagelangue', models.DO_NOTHING, db_column='StageId', related_name='StageId_session')  # Field name made lowercase.
    languecd = models.ForeignKey('Stagelangue', models.DO_NOTHING, db_column='LangueCd', related_name='LangueCd_session')  # Field name made lowercase.
    salleformationid = models.ForeignKey(Salleformation, models.DO_NOTHING, db_column='SalleFormationId', blank=True, null=True)  # Field name made lowercase.
    datedebut = models.DateField(db_column='DateDebut')  # Field name made lowercase.
    prix = models.DecimalField(db_column='Prix', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    note = models.PositiveIntegerField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    statut = models.CharField(db_column='Statut', max_length=10, blank=True, null=True)  # Field name made lowercase.
    datecreation = models.DateField(db_column='DateCreation')  # Field name made lowercase.
    duree = models.PositiveIntegerField(db_column='Duree', blank=True, null=True)  # Field name made lowercase.
    intraentrerprise = models.IntegerField(db_column='IntraEntrerprise')  # Field name made lowercase.
    remarques = models.CharField(db_column='Remarques', max_length=1500, blank=True, null=True)  # Field name made lowercase.
    formateurid = models.ForeignKey(Formateur, models.DO_NOTHING, db_column='FormateurId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'session'
        unique_together = (('datedebut', 'salleformationid'),)


class Societe(models.Model):
    societeid = models.AutoField(db_column='SocieteId', primary_key=True)  # Field name made lowercase.
    nom = models.CharField(db_column='Nom', unique=True, max_length=60)  # Field name made lowercase.
    numerotva = models.CharField(db_column='NumeroTVA', max_length=30, blank=True, null=True)  # Field name made lowercase.
    typerelance = models.SmallIntegerField(db_column='TypeRelance')  # Field name made lowercase.
    facturationavantinscription = models.IntegerField(db_column='FacturationAvantInscription')  # Field name made lowercase.
    telephone2 = models.CharField(db_column='Telephone2', max_length=30, blank=True, null=True)  # Field name made lowercase.
    telephone1 = models.CharField(db_column='Telephone1', max_length=30, blank=True, null=True)  # Field name made lowercase.
    remise = models.PositiveIntegerField(db_column='Remise')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'societe'


class Societeadresse(models.Model):
    societeid = models.OneToOneField(Societe, models.DO_NOTHING, db_column='SocieteId', primary_key=True)  # Field name made lowercase.
    adresseid = models.ForeignKey(Adresse, models.DO_NOTHING, db_column='AdresseId')  # Field name made lowercase.
    typeadresse = models.CharField(db_column='TypeAdresse', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'societeadresse'
        unique_together = (('societeid', 'adresseid'),)


class Societeformateur(models.Model):
    societeformateurid = models.AutoField(db_column='SocieteFormateurId', primary_key=True)  # Field name made lowercase.
    nom = models.CharField(db_column='Nom', unique=True, max_length=50)  # Field name made lowercase.
    adresseformateurid = models.ForeignKey(Adresse, models.DO_NOTHING, db_column='AdresseFormateurId')  # Field name made lowercase.
    telephonesociete = models.CharField(db_column='TelephoneSociete', max_length=30, blank=True, null=True)  # Field name made lowercase.
    telephoneadministratif = models.CharField(db_column='TelephoneAdministratif', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='Fax', max_length=30, blank=True, null=True)  # Field name made lowercase.
    contact = models.CharField(db_column='Contact', max_length=150, blank=True, null=True)  # Field name made lowercase.
    commentaires = models.CharField(db_column='Commentaires', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    statut = models.CharField(db_column='Statut', max_length=1, blank=True, null=True)  # Field name made lowercase.
    emailcontact = models.CharField(db_column='EmailContact', max_length=150, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'societeformateur'


class Stage(models.Model):
    stageid = models.AutoField(db_column='StageId', primary_key=True)  # Field name made lowercase.
    categorie = models.CharField(db_column='Categorie', max_length=2)  # Field name made lowercase.
    domaine = models.CharField(db_column='Domaine', max_length=2)  # Field name made lowercase.
    datecreation = models.DateTimeField(db_column='DateCreation')  # Field name made lowercase.
    dateannulation = models.DateField(db_column='DateAnnulation', blank=True, null=True)  # Field name made lowercase.
    commentairesplanification = models.CharField(db_column='CommentairesPlanification', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    commentairesproduction = models.CharField(db_column='CommentairesProduction', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    duree = models.PositiveIntegerField(db_column='Duree')  # Field name made lowercase.
    nombrestagiairesmaximum = models.PositiveIntegerField(db_column='NombreStagiairesMaximum')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'stage'


class Stagelangue(models.Model):
    stageid = models.OneToOneField(Stage, models.DO_NOTHING, db_column='StageId', primary_key=True)  # Field name made lowercase.
    languecd = models.ForeignKey(Langue, models.DO_NOTHING, db_column='LangueCd')  # Field name made lowercase.
    titre = models.CharField(db_column='Titre', max_length=200)  # Field name made lowercase.
    soustitre = models.CharField(db_column='SousTitre', max_length=200, blank=True, null=True)  # Field name made lowercase.
    phrasesynthese = models.CharField(db_column='PhraseSynthese', max_length=500, blank=True, null=True)  # Field name made lowercase.
    prerequis = models.CharField(db_column='PreRequis', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    profilparticipants = models.CharField(db_column='ProfilParticipants', max_length=500, blank=True, null=True)  # Field name made lowercase.
    objectifs = models.CharField(db_column='Objectifs', max_length=1000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'stagelangue'
        unique_together = (('stageid', 'languecd'),)


class Suivifacture(models.Model):
    suivifactureid = models.AutoField(db_column='SuiviFactureId', primary_key=True)  # Field name made lowercase.
    facturecd = models.ForeignKey(Facture, models.DO_NOTHING, db_column='FactureCd', blank=True, null=True)  # Field name made lowercase.
    datepaiement = models.DateField(db_column='DatePaiement')  # Field name made lowercase.
    typepaiement = models.CharField(db_column='TypePaiement', max_length=1)  # Field name made lowercase.
    nochequebanque = models.CharField(db_column='NoChequeBanque', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nobordereau = models.CharField(db_column='NoBordereau', max_length=10, blank=True, null=True)  # Field name made lowercase.
    montant = models.DecimalField(db_column='Montant', max_digits=8, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'suivifacture'


class Tarifformateur(models.Model):
    tarifformateurid = models.AutoField(db_column='TarifFormateurId', primary_key=True)  # Field name made lowercase.
    formateurid = models.ForeignKey(Formateur, models.DO_NOTHING, db_column='FormateurId')  # Field name made lowercase.
    datedebut = models.DateField(db_column='DateDebut')  # Field name made lowercase.
    datefin = models.DateField(db_column='DateFin', blank=True, null=True)  # Field name made lowercase.
    tarifjournalier = models.DecimalField(db_column='TarifJournalier', max_digits=6, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tarifformateur'


class Tarifspecial(models.Model):
    tarifspecialid = models.AutoField(db_column='TarifSpecialId', primary_key=True)  # Field name made lowercase.
    tarifformateurid = models.ForeignKey(Tarifformateur, models.DO_NOTHING, db_column='TarifFormateurId')  # Field name made lowercase.
    regionid = models.PositiveIntegerField(db_column='RegionId', blank=True, null=True)  # Field name made lowercase.
    stageid = models.IntegerField(db_column='StageId', blank=True, null=True)  # Field name made lowercase.
    languecd = models.CharField(db_column='LangueCd', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tarifjournalier = models.DecimalField(db_column='TarifJournalier', max_digits=6, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tarifspecial'


class Tauxtva(models.Model):
    datedebut = models.DateField(db_column='DateDebut', primary_key=True)  # Field name made lowercase.
    datefin = models.DateField(db_column='DateFin', blank=True, null=True)  # Field name made lowercase.
    taux1 = models.DecimalField(db_column='TAUX1', max_digits=5, decimal_places=2)  # Field name made lowercase.
    taux2 = models.DecimalField(db_column='TAUX2', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tauxtva'


class Titre(models.Model):
    titrecd = models.CharField(db_column='TitreCd', primary_key=True, max_length=8)  # Field name made lowercase.
    libelle = models.CharField(db_column='Libelle', unique=True, max_length=32)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'titre'


class Typeadresse(models.Model):
    typeadresseid = models.PositiveIntegerField(db_column='TypeAdresseId', primary_key=True)  # Field name made lowercase.
    libelle = models.CharField(db_column='Libelle', unique=True, max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'typeadresse'


class Ville(models.Model):
    villeid = models.AutoField(db_column='VilleId', primary_key=True)  # Field name made lowercase.
    regionid = models.IntegerField(db_column='RegionId', blank=True, null=True)  # Field name made lowercase.
    nomville = models.CharField(db_column='NomVille', max_length=255, blank=True, null=True)  # Field name made lowercase.
    codepostal = models.CharField(db_column='CodePostal', max_length=10, blank=True, null=True)  # Field name made lowercase.
    codeinsee = models.FloatField(db_column='CodeINSEE', blank=True, null=True)  # Field name made lowercase.
    coderegion = models.FloatField(db_column='CodeRegion', blank=True, null=True)  # Field name made lowercase.
    latitude = models.DecimalField(db_column='Latitude', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    longitude = models.CharField(db_column='Longitude', max_length=255, blank=True, null=True)  # Field name made lowercase.
    eloignement = models.CharField(db_column='Eloignement', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ville'
