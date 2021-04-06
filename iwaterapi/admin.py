from django.contrib import admin

from django.contrib import admin

# Register your models here.
from iwaterapi.models import (
IwaterAddresses,
IwaterAddressesSwaped,
IwaterAppError,
IwaterAuthApp,
IwaterCategory,
IwaterClients,
IwaterClientsApp,
IwaterClientsSwaped,
IwaterCompany,
IwaterCompanyRegions,
IwaterDcontrol,
IwaterDimension,
IwaterDriver,
IwaterHow,
IwaterLinks,
IwaterLists,
IwaterLogs,
IwaterMovedOrders,
IwaterNotice,
IwaterOrders,
IwaterOrdersApp,
IwaterPerms,
IwaterPermsOld,
IwaterProviders,
IwaterReportApp,
IwaterReportsApp,
IwaterRoles,
IwaterSettings,
IwaterStorage,
IwaterStorageAgr,
IwaterStorageCount,
IwaterStorageHistory,
IwaterUnits,
IwaterUnitsAgr,
IwaterUnitsAgrOld,
IwaterUnitsAgrSwap,
IwaterUsers,
IwaterUsersApp,
IwaterVipApp
)


@admin.register(IwaterAddresses)
class IwaterAddressesAdmin(admin.ModelAdmin):
    list_display = ('client_id', 'contact', 'region', 'address', 'coords', 'full_address')


@admin.register(IwaterAddressesSwaped)
class IwaterAddressesSwapedAdmin(admin.ModelAdmin):
    list_display = ('client_id', 'contact', 'region', 'address', 'coords', 'full_address')


@admin.register(IwaterAppError)
class IwaterAppErrorAdmin(admin.ModelAdmin):
    list_display = ('date', 'text')


@admin.register(IwaterAuthApp)
class IwaterAuthAppAdmin(admin.ModelAdmin):
    list_display = ('client_id', 'phone', 'password', 'salt', 'token')


@admin.register(IwaterCategory)
class IwaterCategoryAdmin(admin.ModelAdmin):
    list_display = ('category_id', 'category', 'company_id', 'priority')


@admin.register(IwaterClients)
class IwaterClientsAdmin(admin.ModelAdmin):
    list_display = (
'type', 'company_id', 'name', 'client_id', 'region', 'address', 'address_full', 'coords', 'contact', 'tanks',
'for_delete', 'time_change', 'user_changing', 'avg_difference', 'last_date')


@admin.register(IwaterClientsApp)
class IwaterClientsAppAdmin(admin.ModelAdmin):
    list_display = (
'name', 'password', 'session', 'salt', 'notification', 'client_id', 'company_id', 'region', 'address', 'phone',
'email')


@admin.register(IwaterClientsSwaped)
class IwaterClientsAppAdmin(admin.ModelAdmin):
    list_display = (
'type', 'name', 'password', 'salt', 'client_id', 'company_id', 'region', 'address', 'address_full', 'coords',
'contact', 'email', 'for_delete', 'time_change', 'user_changing')


@admin.register(IwaterCompany)
class IwaterCompanyAdmin(admin.ModelAdmin):
    list_display = (
'id', 'name', 'city', 'region', 'address', 'coords', 'contact', 'period', 'timing', 'color', 'gallery',
'schedule',
'regions', 'about')


@admin.register(IwaterCompanyRegions)
class IwaterCompanyRegionsAdmin(admin.ModelAdmin):
    list_display = ('name', 'company_id')


@admin.register(IwaterDcontrol)
class IwaterDcontrolAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'time', 'coord', 'tank', 'notice')


@admin.register(IwaterDimension)
class IwaterDimensionAdmin(admin.ModelAdmin):
    list_display = ('name', 'shname', 'id_company')


@admin.register(IwaterDriver)
class IwaterDriverAdmin(admin.ModelAdmin):
    list_display = ('id', 'login', 'password', 'salt', 'notification', 'session', 'company', 'stat')


@admin.register(IwaterHow)
class IwaterHowdmin(admin.ModelAdmin):
    list_display = ('email',)


@admin.register(IwaterLinks)
class IwaterLinksAdmin(admin.ModelAdmin):
    list_display = ('id', 'section', 'desc', 'level')


@admin.register(IwaterLists)
class IwaterListsAdmin(admin.ModelAdmin):
    list_display = ('date', 'file', 'user_id', 'create_date', 'map_num', 'driver_id', 'company_id')


@admin.register(IwaterLogs)
class IwaterLogsAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'operation', 'action', 'data', 'table', 'time')


@admin.register(IwaterMovedOrders)
class IwaterMovedOrdersAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'done', 'reason', 'comment', 'agreed', 'server_time', 'driver_coords')


@admin.register(IwaterNotice)
class IwaterNoticeAdmin(admin.ModelAdmin):
    list_display = ('dest_id', 'dest_name', 'title', 'message', 'noticed', 'read', 'date')


@admin.register(IwaterOrders)
class IwaterOrdersAdmin(admin.ModelAdmin):
    list_display = (
'client_id', 'mobile', 'local_id', 'company_id', 'name', 'address', 'contact', 'date', 'no_date', 'time',
'period',
'notice', 'water_total', 'water_equip', 'equip', 'checked', 'dep', 'cash', 'cash_formula', 'cash_b_formula',
'cash_b', 'on_floor', 'tank_b', 'tank_empty_now', 'driver', 'status', 'reason', 'map_num', 'region', 'list',
'coords', 'history', 'changed_driver', 'number_visit')


@admin.register(IwaterOrdersApp)
class IwaterOrdersAppAdmin(admin.ModelAdmin):
    list_display = (
'client_id', 'name', 'company_id', 'address', 'email', 'contact', 'date', 'period', 'notice', 'water_equip',
'checked', 'status', 'system')


@admin.register(IwaterPerms)
class IwaterPermsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'title')


@admin.register(IwaterProviders)
class IwaterProvidersAdmin(admin.ModelAdmin):
    list_display = ('company_id', 'name', 'contact')


@admin.register(IwaterPermsOld)
class IwaterPermsOldAdmin(admin.ModelAdmin):
    list_display = ('name', 'desc')


@admin.register(IwaterReportApp)
class IwaterReportAppAdmin(admin.ModelAdmin):
    list_display = (
'driver_id', 'name', 'payment_type', 'payment', 'number_containers', 'orders_delivered', 'total_money',
'date_created', 'date', 'company_id')


@admin.register(IwaterReportsApp)
class IwaterReportsAppAdmin(admin.ModelAdmin):
    list_display = ('date', 'text')


@admin.register(IwaterRoles)
class IwaterRolesAdmin(admin.ModelAdmin):
    list_display = ('name', 'perms')


@admin.register(IwaterSettings)
class IwaterSettingsAdmin(admin.ModelAdmin):
    list_display = ('name', 'data')


admin.site.register(IwaterStorage)


@admin.register(IwaterStorageAgr)
class IwaterStorageAgrAdmin(admin.ModelAdmin):
    list_display = (
'number', 'company_id', 'name', 'priority', 'address', 'coords', 'storeman_name', 'storeman_phone',
'date_start',
'date_finish')


@admin.register(IwaterStorageCount)
class IwaterStorageCountAdmin(admin.ModelAdmin):
    list_display = ('id', 'unit_id', 'storage', 'shelf_life', 'count', 'last_update')


admin.site.register(IwaterStorageHistory)


@admin.register(IwaterUnits)
class IwaterUnitsAdmin(admin.ModelAdmin):
    list_display = ('name', 'shname', 'price', 'discount', 'category', 'about', 'gallery', 'gl_id')


@admin.register(IwaterUnitsAgr)
class IwaterUnitsAgrAdmin(admin.ModelAdmin):
    list_display = (
'counter', 'id', 'name', 'shname', 'price', 'discount', 'category', 'about', 'gallery', 'gl_id', 'date',
'date_start', 'date_finish')


admin.site.register(IwaterUnitsAgrOld)
admin.site.register(IwaterUnitsAgrSwap)


@admin.register(IwaterUsers)
class IwaterUsersAdmin(admin.ModelAdmin):
    list_display = (
'login', 'password', 'salt', 'session', 'name', 'phone', 'role', 'company_id', 'ban', 'region', 'card',
'address', 'email')


@admin.register(IwaterUsersApp)
class IwaterUsersAppAdmin(admin.ModelAdmin):
    list_display = ('name', 'lastname', 'email', 'session', 'phone', 'city', 'address')


@admin.register(IwaterVipApp)
class IwaterVipAppAdmin(admin.ModelAdmin):
    list_display = ('name', 'lastname', 'email', 'session', 'phone', 'contract', 'inn', 'city', 'address')