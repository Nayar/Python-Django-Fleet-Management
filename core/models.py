# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Agencies(models.Model):
    title = models.CharField(max_length=160, blank=True, null=True)

    class Meta:
        verbose_name = 'Agency'
        verbose_name_plural = 'Agencies'
        
        db_table = 'agencies'

    def __str__(self):
        return self.title


class City(models.Model):
    name = models.CharField(max_length=120, blank=True, null=True)
    state = models.ForeignKey('States', models.DO_NOTHING, db_column='state', blank=True, null=True)

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'
        
        db_table = 'city'

    def __str__(self):
        return self.name


class Drivers(models.Model):
    name = models.CharField(max_length=160, blank=True, null=True)
    sector = models.ForeignKey('Sectors', models.DO_NOTHING, db_column='sector', blank=True, null=True)

    class Meta:
        verbose_name = 'Driver'
        verbose_name_plural = 'Drivers'
        
        db_table = 'drivers'

    def __str__(self):
        return self.name


class FuelStations(models.Model):
    name = models.CharField(max_length=160, blank=True, null=True)
    city = models.ForeignKey(City, models.DO_NOTHING, db_column='city', blank=True, null=True)

    class Meta:
        verbose_name = 'Fuel Station'
        verbose_name_plural = 'Fuel Stations'
        
        db_table = 'fuel_stations'

    def __str__(self):
        return self.name


class Fuels(models.Model):
    name = models.CharField(max_length=160, blank=True, null=True)

    class Meta:
        verbose_name = 'Fuel'
        verbose_name_plural = 'Fuel'
        
        db_table = 'fuels'

    def __str__(self):
        return self.name


class Sectors(models.Model):
    title = models.CharField(max_length=160, blank=True, null=True)
    agency = models.ForeignKey(Agencies, on_delete=models.DO_NOTHING, db_column='agency', blank=True, null=True)

    class Meta:
        verbose_name = 'Sector'
        verbose_name_plural = 'Sectors'
        
        db_table = 'sectors'

    def __str__(self):
        return self.title


class States(models.Model):
    name = models.CharField(max_length=75, blank=True, null=True)
    uf = models.CharField(max_length=5, blank=True, null=True)
    country = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name = 'State'
        verbose_name_plural = 'States'
        
        db_table = 'states'

    def __str__(self):
        return self.name


class Supplies(models.Model):
    driver = models.ForeignKey(Drivers, models.DO_NOTHING, db_column='driver', blank=True, null=True)
    vehicle = models.ForeignKey('Vehicles', models.DO_NOTHING, db_column='vehicle', blank=True, null=True)
    fuel_station = models.ForeignKey(FuelStations, models.DO_NOTHING, db_column='fuel_station', blank=True, null=True)
    cost = models.FloatField(blank=True, null=True)
    liters = models.IntegerField(blank=True, null=True)
    auto_date = models.DateTimeField()

    class Meta:
        verbose_name = 'Supply'
        verbose_name_plural = 'Supplies'
        
        db_table = 'supplies'


class Travels(models.Model):
    origin = models.IntegerField(blank=True, null=True)
    destiny = models.IntegerField(blank=True, null=True)
    driver = models.ForeignKey(Drivers, models.DO_NOTHING, db_column='driver', blank=True, null=True)
    vehicle = models.ForeignKey('Vehicles', models.DO_NOTHING, db_column='vehicle', blank=True, null=True)

    class Meta:
        verbose_name = 'Travel'
        verbose_name_plural = 'Travels'
        
        db_table = 'travels'


class Users(models.Model):
    name = models.CharField(max_length=160)
    email = models.CharField(max_length=160)
    password = models.CharField(max_length=160)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        
        db_table = 'users'

    def __str__(self):
        return self.name


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
        verbose_name = 'Vehicle'
        verbose_name_plural = 'Vehicles'
        
        db_table = 'vehicles'

    def __str__(self):
        return self.plate


class VehiclesBrands(models.Model):
    name = models.CharField(max_length=160, blank=True, null=True)

    class Meta:
        verbose_name = 'Vehicle Brand'
        verbose_name_plural = 'Vehicle Brands'
        
        db_table = 'vehicles_brands'

    def __str__(self):
        return self.name


class VehiclesModels(models.Model):
    name = models.CharField(max_length=160, blank=True, null=True)
    brand = models.ForeignKey(VehiclesBrands, models.DO_NOTHING, db_column='brand', blank=True, null=True)

    class Meta:
        verbose_name = 'Vehicle Model'
        verbose_name_plural = 'Vehicle Models'
        
        db_table = 'vehicles_models'

    def __str__(self):
        return self.name


class VehiclesProvenances(models.Model):
    name = models.CharField(max_length=160, blank=True, null=True)

    class Meta:
        verbose_name = 'Vehicle Provenance'
        verbose_name_plural = 'Vehicle Provenances'
        
        db_table = 'vehicles_provenances'

    def __str__(self):
        return self.name


class VehiclesStatus(models.Model):
    name = models.CharField(max_length=160, blank=True, null=True)

    class Meta:
        verbose_name = 'Vehicle Status'
        verbose_name_plural = 'Vehicle Status'
        
        db_table = 'vehicles_status'

    def __str__(self):
        return self.name
