from django.db import models

# Create your models here.


class IwaterAddresses(models.Model):
    client_id = models.IntegerField(blank=True, null=True)
    contact = models.CharField(max_length=255, blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    coords = models.CharField(max_length=255, blank=True, null=True)
    full_address = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'iwater_addresses'

    def __str__(self):
        return self.client_id


class IwaterAddressesSwaped(models.Model):
    client_id = models.IntegerField(blank=True, null=True)
    contact = models.CharField(max_length=255, blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    coords = models.CharField(max_length=255, blank=True, null=True)
    full_address = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'iwater_addresses_swaped'

    def __str__(self):
        return self.client_id


class IwaterAppError(models.Model):
    date = models.CharField(max_length=28)
    text = models.TextField()

    class Meta:
        managed = False
        db_table = 'iwater_app_error'

    def __str__(self):
        return self.date


class IwaterAuthApp(models.Model):
    client_id = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    salt = models.CharField(max_length=255, blank=True, null=True)
    token = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'iwater_auth_app'

    def __str__(self):
        return self.client_id


class IwaterCategory(models.Model):
    category_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=32)
    company_id = models.CharField(max_length=4)
    priority = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'iwater_category'

    def __str__(self):
        return self.category_id


class IwaterClients(models.Model):
    type = models.IntegerField()
    company_id = models.CharField(max_length=4)
    name = models.CharField(max_length=255)
    client_id = models.IntegerField()
    region = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    address_full = models.CharField(max_length=255)
    coords = models.CharField(max_length=255)
    contact = models.CharField(max_length=16)
    tanks = models.IntegerField()
    for_delete = models.IntegerField()
    time_change = models.IntegerField()
    user_changing = models.IntegerField()
    avg_difference = models.CharField(max_length=20, blank=True, null=True)
    last_date = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'iwater_clients'

    def __str__(self):
        return self.name


class IwaterClientsApp(models.Model):
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    session = models.CharField(max_length=32)
    salt = models.CharField(max_length=255)
    notification = models.CharField(max_length=255)
    client_id = models.IntegerField()
    company_id = models.CharField(max_length=4)
    region = models.CharField(max_length=255)
    address = models.CharField(max_length=512)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'iwater_clients_app'

    def __str__(self):
        return self.name


class IwaterClientsSwaped(models.Model):
    type = models.IntegerField()
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    salt = models.CharField(max_length=255)
    client_id = models.IntegerField()
    company_id = models.CharField(max_length=4)
    region = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    address_full = models.CharField(max_length=255)
    coords = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    for_delete = models.IntegerField()
    time_change = models.IntegerField()
    user_changing = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'iwater_clients_swaped'

    def __str__(self):
        return self.name


class IwaterCompany(models.Model):
    id = models.CharField(primary_key=True, unique=True, max_length=4)
    name = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    region = models.CharField(max_length=32)
    address = models.CharField(max_length=255)
    coords = models.CharField(max_length=32)
    contact = models.CharField(max_length=48)
    period = models.CharField(max_length=255)
    timing = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    gallery = models.TextField(blank=True, null=True)
    schedule = models.CharField(max_length=64)
    regions = models.TextField()
    about = models.TextField()

    class Meta:
        managed = False
        db_table = 'iwater_company'

    def __str__(self):
        return self.name


class IwaterCompanyRegions(models.Model):
    name = models.CharField(max_length=255)
    company_id = models.CharField(max_length=4)

    class Meta:
        managed = False
        db_table = 'iwater_company_regions'

    def __str__(self):
        return self.name


class IwaterDcontrol(models.Model):
    order_id = models.IntegerField(unique=True)
    time = models.IntegerField()
    coord = models.CharField(max_length=64)
    tank = models.IntegerField()
    notice = models.TextField()

    class Meta:
        managed = False
        db_table = 'iwater_dcontrol'

    def __str__(self):
        return self.order_id


class IwaterDimension(models.Model):
    name = models.CharField(max_length=255)
    shname = models.CharField(max_length=255)
    id_company = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'iwater_dimension'

    def __str__(self):
        return self.name


class IwaterDriver(models.Model):
    id = models.IntegerField(primary_key=True)
    login = models.CharField(max_length=32)
    password = models.CharField(max_length=255)
    salt = models.CharField(max_length=255)
    notification = models.CharField(max_length=178)
    session = models.CharField(max_length=128)
    company = models.CharField(max_length=4)
    stat = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'iwater_driver'

    def __str__(self):
        return self.login


class IwaterHow(models.Model):
    email = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'iwater_how'

    def __str__(self):
        return self.email


class IwaterLinks(models.Model):
    id = models.IntegerField(primary_key=True)
    section = models.IntegerField()
    desc = models.CharField(max_length=256)
    level = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'iwater_links'

    def __str__(self):
        return self.id


class IwaterLists(models.Model):
    date = models.CharField(max_length=15)
    file = models.CharField(max_length=255)
    user_id = models.IntegerField()
    create_date = models.CharField(max_length=15)
    map_num = models.CharField(max_length=255)
    driver_id = models.IntegerField(blank=True, null=True)
    company_id = models.CharField(max_length=4)

    class Meta:
        managed = False
        db_table = 'iwater_lists'

    def __str__(self):
        return self.date


class IwaterLogs(models.Model):
    user_id = models.IntegerField()
    operation = models.CharField(max_length=255)
    action = models.CharField(max_length=255)
    data = models.CharField(max_length=255)
    table = models.CharField(max_length=255)
    time = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'iwater_logs'

    def __str__(self):
        return self.user_id


class IwaterMovedOrders(models.Model):
    order_id = models.IntegerField(blank=True, null=True)
    done = models.IntegerField(blank=True, null=True)
    reason = models.CharField(max_length=255, blank=True, null=True)
    comment = models.CharField(max_length=255, blank=True, null=True)
    agreed = models.IntegerField(blank=True, null=True)
    server_time = models.CharField(max_length=50, blank=True, null=True)
    driver_coords = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'iwater_moved_orders'

    def __str__(self):
        return self.order_id


class IwaterNotice(models.Model):
    dest_id = models.IntegerField()
    dest_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    message = models.CharField(max_length=255)
    noticed = models.CharField(max_length=255)
    read = models.CharField(max_length=255)
    date = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'iwater_notice'

    def __str__(self):
        return self.dest_name


class IwaterOrders(models.Model):
    client_id = models.IntegerField()
    mobile = models.IntegerField()
    local_id = models.IntegerField(blank=True, null=True)
    company_id = models.CharField(max_length=4)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    date = models.CharField(max_length=20, blank=True, null=True)
    no_date = models.IntegerField()
    time = models.CharField(max_length=255)
    period = models.CharField(max_length=50)
    notice = models.TextField(blank=True, null=True)
    water_total = models.IntegerField()
    water_equip = models.CharField(max_length=255)
    equip = models.TextField(blank=True, null=True)
    checked = models.IntegerField()
    dep = models.CharField(max_length=255, blank=True, null=True)
    cash = models.CharField(max_length=15)
    cash_formula = models.CharField(max_length=255)
    cash_b_formula = models.CharField(max_length=255)
    cash_b = models.CharField(max_length=15, blank=True, null=True)
    on_floor = models.CharField(max_length=15, blank=True, null=True)
    tank_b = models.IntegerField(blank=True, null=True)
    tank_empty_now = models.IntegerField()
    driver = models.IntegerField()
    status = models.IntegerField()
    reason = models.CharField(max_length=255, blank=True, null=True)
    map_num = models.IntegerField(blank=True, null=True)
    region = models.CharField(max_length=255)
    list = models.IntegerField(blank=True, null=True)
    coords = models.CharField(max_length=255, blank=True, null=True)
    history = models.CharField(max_length=255, blank=True, null=True)
    changed_driver = models.IntegerField()
    number_visit = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'iwater_orders'

    def __str__(self):
        return self.client_id


class IwaterOrdersApp(models.Model):
    client_id = models.IntegerField()
    name = models.CharField(max_length=128)
    company_id = models.CharField(max_length=4)
    address = models.CharField(max_length=255)
    email = models.CharField(max_length=128)
    contact = models.CharField(max_length=128)
    date = models.CharField(max_length=20, blank=True, null=True)
    period = models.CharField(max_length=50)
    notice = models.TextField(blank=True, null=True)
    water_equip = models.CharField(max_length=255)
    checked = models.SmallIntegerField()
    status = models.IntegerField()
    system = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'iwater_orders_app'

    def __str__(self):
        return self.name


class IwaterPerms(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'iwater_perms'

    def __str__(self):
        return self.name


class IwaterPermsOld(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'iwater_perms_old'

    def __str__(self):
        return self.name


class IwaterProviders(models.Model):
    company_id = models.CharField(max_length=4)
    name = models.CharField(max_length=128)
    contact = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'iwater_providers'

    def __str__(self):
        return self.name


class IwaterReportApp(models.Model):
    driver_id = models.IntegerField()
    name = models.CharField(max_length=255)
    payment_type = models.CharField(max_length=255)
    payment = models.FloatField()
    number_containers = models.IntegerField()
    orders_delivered = models.IntegerField()
    total_money = models.FloatField()
    date_created = models.CharField(max_length=15)
    date = models.CharField(max_length=255)
    company_id = models.CharField(max_length=4)

    class Meta:
        managed = False
        db_table = 'iwater_report_app'

    def __str__(self):
        return self.name


class IwaterReportsApp(models.Model):
    date = models.IntegerField()
    text = models.TextField()

    class Meta:
        managed = False
        db_table = 'iwater_reports_app'

    def __str__(self):
        return self.date


class IwaterRoles(models.Model):
    name = models.CharField(max_length=255)
    perms = models.TextField()

    class Meta:
        managed = False
        db_table = 'iwater_roles'

    def __str__(self):
        return self.name


class IwaterSettings(models.Model):
    name = models.CharField(max_length=255)
    data = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'iwater_settings'

    def __str__(self):
        return self.name


class IwaterStorage(models.Model):

    class Meta:
        managed = False
        db_table = 'iwater_storage'


class IwaterStorageAgr(models.Model):
    number = models.IntegerField()
    company_id = models.CharField(max_length=4)
    name = models.CharField(max_length=255)
    priority = models.IntegerField()
    address = models.CharField(max_length=255)
    coords = models.CharField(max_length=128)
    storeman_name = models.CharField(max_length=128)
    storeman_phone = models.CharField(max_length=64)
    date_start = models.IntegerField()
    date_finish = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'iwater_storage_agr'

    def __str__(self):
        return self.name


class IwaterStorageCount(models.Model):
    id = models.IntegerField(primary_key=True,)
    unit_id = models.IntegerField()
    storage = models.IntegerField()
    shelf_life = models.IntegerField()
    count = models.IntegerField()
    last_update = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'iwater_storage_count'

    def __str__(self):
        return self.id


class IwaterStorageHistory(models.Model):
    unit_id = models.IntegerField()
    storage = models.IntegerField()
    operation = models.CharField(max_length=16)
    count = models.IntegerField()
    comment = models.CharField(max_length=255)
    date = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'iwater_storage_history'

    def __str__(self):
        return self.storage


class IwaterUnits(models.Model):
    name = models.CharField(max_length=86)
    shname = models.CharField(max_length=16, blank=True, null=True)
    price = models.CharField(max_length=256)
    discount = models.IntegerField()
    category = models.IntegerField()
    about = models.TextField(blank=True, null=True)
    gallery = models.TextField(blank=True, null=True)
    gl_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'iwater_units'

    def __str__(self):
        return self.name


class IwaterUnitsAgr(models.Model):
    counter = models.AutoField(primary_key=True)
    id = models.IntegerField()
    name = models.CharField(max_length=86)
    shname = models.CharField(max_length=16, blank=True, null=True)
    price = models.CharField(max_length=256)
    discount = models.IntegerField()
    category = models.IntegerField()
    about = models.TextField(blank=True, null=True)
    gallery = models.TextField(blank=True, null=True)
    gl_id = models.IntegerField()
    date = models.IntegerField()
    date_start = models.IntegerField()
    date_finish = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'iwater_units_agr'

    def __str__(self):
        return self.name


class IwaterUnitsAgrOld(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=86)
    shname = models.CharField(max_length=16, blank=True, null=True)
    price = models.CharField(max_length=256)
    discount = models.IntegerField()
    category = models.IntegerField()
    about = models.TextField(blank=True, null=True)
    gallery = models.TextField(blank=True, null=True)
    gl_id = models.IntegerField()
    date_start = models.IntegerField()
    date_finish = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'iwater_units_agr_old'

    def __str__(self):
        return self.name


class IwaterUnitsAgrSwap(models.Model):
    counter = models.AutoField(primary_key=True)
    id = models.IntegerField()
    name = models.CharField(max_length=86)
    shname = models.CharField(max_length=16, blank=True, null=True)
    price = models.CharField(max_length=256)
    discount = models.IntegerField()
    category = models.IntegerField()
    about = models.TextField(blank=True, null=True)
    gallery = models.TextField(blank=True, null=True)
    gl_id = models.IntegerField()
    date_start = models.IntegerField()
    date_finish = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'iwater_units_agr_swap'

    def __str__(self):
        return self.name


class IwaterUsers(models.Model):
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    salt = models.CharField(max_length=255)
    session = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    role = models.IntegerField()
    company_id = models.CharField(max_length=4)
    ban = models.IntegerField()
    region = models.CharField(max_length=255, blank=True, null=True)
    card = models.CharField(max_length=32, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'iwater_users'

    def __str__(self):
        return self.name


class IwaterUsersApp(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    lastname = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    session = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'iwater_users_app'

    def __str__(self):
        return self.name


class IwaterVipApp(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    lastname = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    session = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, blank=True, null=True)
    contract = models.CharField(max_length=255, blank=True, null=True)
    inn = models.CharField(db_column='INN', max_length=255, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'iwater_vip_app'

    def __str__(self):
        return self.name