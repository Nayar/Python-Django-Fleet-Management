# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Agencies(models.Model):
    title = models.CharField(max_length=160, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agencies'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
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
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class City(models.Model):
    name = models.CharField(max_length=120, blank=True, null=True)
    state = models.ForeignKey('States', models.DO_NOTHING, db_column='state', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'city'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
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


class Drivers(models.Model):
    name = models.CharField(max_length=160, blank=True, null=True)
    sector = models.ForeignKey('Sectors', models.DO_NOTHING, db_column='sector', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'drivers'


class FuelStations(models.Model):
    name = models.CharField(max_length=160, blank=True, null=True)
    city = models.ForeignKey(City, models.DO_NOTHING, db_column='city', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fuel_stations'


class Fuels(models.Model):
    name = models.CharField(max_length=160, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fuels'

    def __unicode__(self):
        return self.name


class Sectors(models.Model):
    title = models.CharField(max_length=160, blank=True, null=True)
    agency = models.ForeignKey(Agencies, models.DO_NOTHING, db_column='agency', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sectors'

    def __unicode__(self):
        return self.title


class States(models.Model):
    name = models.CharField(max_length=75, blank=True, null=True)
    uf = models.CharField(max_length=5, blank=True, null=True)
    country = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'states'


class Supplies(models.Model):
    driver = models.ForeignKey(Drivers, models.DO_NOTHING, db_column='driver', blank=True, null=True)
    vehicle = models.ForeignKey('Vehicles', models.DO_NOTHING, db_column='vehicle', blank=True, null=True)
    fuel_station = models.ForeignKey(FuelStations, models.DO_NOTHING, db_column='fuel_station', blank=True, null=True)
    cost = models.FloatField(blank=True, null=True)
    liters = models.IntegerField(blank=True, null=True)
    auto_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'supplies'


class Travels(models.Model):
    origin = models.IntegerField(blank=True, null=True)
    destiny = models.IntegerField(blank=True, null=True)
    driver = models.ForeignKey(Drivers, models.DO_NOTHING, db_column='driver', blank=True, null=True)
    vehicle = models.ForeignKey('Vehicles', models.DO_NOTHING, db_column='vehicle', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'travels'


class Users(models.Model):
    name = models.CharField(max_length=160)
    email = models.CharField(max_length=160)
    password = models.CharField(max_length=160)

    class Meta:
        managed = False
        db_table = 'users'


class Vehicles(models.Model):
    plate = models.CharField(max_length=160, blank=True, null=True)
    chassis = models.CharField(max_length=160)
    sector = models.ForeignKey(Sectors, models.DO_NOTHING, db_column='sector')
    auto_date = models.DateTimeField()
    model = models.ForeignKey('VehiclesModels', models.DO_NOTHING, db_column='model', blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    km = models.CharField(max_length=160, blank=True, null=True)
    ano = models.TextField(blank=True, null=True)  # This field type is a guess.
    km_per_liter = models.IntegerField(blank=True, null=True)
    purchase_date = models.DateField(blank=True, null=True)
    renavan = models.CharField(max_length=160, blank=True, null=True)
    kind = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=80, blank=True, null=True)
    ano_fab = models.TextField(blank=True, null=True)  # This field type is a guess.
    fuel = models.ForeignKey(Fuels, models.DO_NOTHING, db_column='fuel', blank=True, null=True)
    conservation = models.ForeignKey('VehiclesStatus', models.DO_NOTHING, db_column='conservation', blank=True, null=True)
    provenance = models.ForeignKey('VehiclesProvenances', models.DO_NOTHING, db_column='provenance', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vehicles'


class VehiclesBrands(models.Model):
    name = models.CharField(max_length=160, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vehicles_brands'

    def __unicode__(self):
        return self.name


class VehiclesModels(models.Model):
    name = models.CharField(max_length=160, blank=True, null=True)
    brand = models.ForeignKey(VehiclesBrands, models.DO_NOTHING, db_column='brand', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vehicles_models'

    def __unicode__(self):
        return self.name


class VehiclesProvenances(models.Model):
    name = models.CharField(max_length=160, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vehicles_provenances'

    def __unicode__(self):
        return self.name


class VehiclesStatus(models.Model):
    name = models.CharField(max_length=160, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vehicles_status'

    def __unicode__(self):
        return self.name
