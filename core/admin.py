from django.contrib import admin
from models import Vehicles, Travels, Agencies, Sectors, FuelStations, Drivers, VehiclesModels, VehiclesBrands, VehiclesProvenances, VehiclesStatus, Fuels

admin.site.site_header = "Python Fleet Management"

# Register your models here.

@admin.register(Vehicles)
class VehiclesAdmin(admin.ModelAdmin):
	list_display = ('plate', 'model')
	fields = ('plate', 'chassis', 'sector', 'model', 'price', 'km', 'ano', 'km_per_liter', 'purchase_date', 'renavan', 'kind', 'color', 'ano_fab', 'fuel', 'conservation', 'provenance')


@admin.register(Travels)
class TravelsAdmin(admin.ModelAdmin):
	list_display = ('origin', 'destiny')


@admin.register(VehiclesBrands)
class VehiclesBrandsAdmin(admin.ModelAdmin):
	list_display = ('name',)


@admin.register(VehiclesModels)
class VehiclesModelsAdmin(admin.ModelAdmin):
	list_display = ('name',)


@admin.register(Agencies)
class AgenciesAdmin(admin.ModelAdmin):
	list_display = ('title',)


@admin.register(Sectors)
class SectorAdmin(admin.ModelAdmin):
	list_display = ('title',)


@admin.register(FuelStations)
class FuelStationsAdmin(admin.ModelAdmin):
	list_display = ('name',)


@admin.register(Drivers)
class DriversAdmin(admin.ModelAdmin):
	list_display = ('name',)


@admin.register(Fuels)
class FuelsAdmin(admin.ModelAdmin):
	list_display = ('name',)


@admin.register(VehiclesProvenances)
class VehiclesProvenancesAdmin(admin.ModelAdmin):
	list_display = ('name',)


@admin.register(VehiclesStatus)
class VehiclesStatusAdmin(admin.ModelAdmin):
	list_display = ('name',)