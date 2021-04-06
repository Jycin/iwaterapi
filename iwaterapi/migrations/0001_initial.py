# Generated by Django 3.1.7 on 2021-03-24 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IwaterAddresses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_id', models.IntegerField(blank=True, null=True)),
                ('contact', models.CharField(blank=True, max_length=255, null=True)),
                ('region', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('coords', models.CharField(blank=True, max_length=255, null=True)),
                ('full_address', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'iwater_addresses',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IwaterAddressesSwaped',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_id', models.IntegerField(blank=True, null=True)),
                ('contact', models.CharField(blank=True, max_length=255, null=True)),
                ('region', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('coords', models.CharField(blank=True, max_length=255, null=True)),
                ('full_address', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'iwater_addresses_swaped',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IwaterAppError',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=28)),
                ('text', models.TextField()),
            ],
            options={
                'db_table': 'iwater_app_error',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IwaterAuthApp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_id', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('password', models.CharField(blank=True, max_length=255, null=True)),
                ('salt', models.CharField(blank=True, max_length=255, null=True)),
                ('token', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'iwater_auth_app',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IwaterCategory',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=32)),
                ('company_id', models.CharField(max_length=4)),
                ('priority', models.IntegerField()),
            ],
            options={
                'db_table': 'iwater_category',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IwaterClients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField()),
                ('company_id', models.CharField(max_length=4)),
                ('name', models.CharField(max_length=255)),
                ('client_id', models.IntegerField()),
                ('region', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('address_full', models.CharField(max_length=255)),
                ('coords', models.CharField(max_length=255)),
                ('contact', models.CharField(max_length=16)),
                ('tanks', models.IntegerField()),
                ('for_delete', models.IntegerField()),
                ('time_change', models.IntegerField()),
                ('user_changing', models.IntegerField()),
                ('avg_difference', models.CharField(blank=True, max_length=20, null=True)),
                ('last_date', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'iwater_clients',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IwaterClientsApp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('session', models.CharField(max_length=32)),
                ('salt', models.CharField(max_length=255)),
                ('notification', models.CharField(max_length=255)),
                ('client_id', models.IntegerField()),
                ('company_id', models.CharField(max_length=4)),
                ('region', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=512)),
                ('phone', models.CharField(max_length=12)),
                ('email', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'iwater_clients_app',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IwaterClientsSwaped',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('salt', models.CharField(max_length=255)),
                ('client_id', models.IntegerField()),
                ('company_id', models.CharField(max_length=4)),
                ('region', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('address_full', models.CharField(max_length=255)),
                ('coords', models.CharField(max_length=255)),
                ('contact', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('for_delete', models.IntegerField()),
                ('time_change', models.IntegerField()),
                ('user_changing', models.IntegerField()),
            ],
            options={
                'db_table': 'iwater_clients_swaped',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IwaterCompany',
            fields=[
                ('id', models.CharField(max_length=4, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=32)),
                ('city', models.CharField(max_length=32)),
                ('region', models.CharField(max_length=32)),
                ('address', models.CharField(max_length=255)),
                ('coords', models.CharField(max_length=32)),
                ('contact', models.CharField(max_length=48)),
                ('period', models.CharField(max_length=255)),
                ('timing', models.CharField(max_length=255)),
                ('color', models.CharField(max_length=255)),
                ('gallery', models.TextField(blank=True, null=True)),
                ('schedule', models.CharField(max_length=64)),
                ('regions', models.TextField()),
                ('about', models.TextField()),
            ],
            options={
                'db_table': 'iwater_company',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IwaterCompanyRegions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('company_id', models.CharField(max_length=4)),
            ],
            options={
                'db_table': 'iwater_company_regions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IwaterDcontrol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField(unique=True)),
                ('time', models.IntegerField()),
                ('coord', models.CharField(max_length=64)),
                ('tank', models.IntegerField()),
                ('notice', models.TextField()),
            ],
            options={
                'db_table': 'iwater_dcontrol',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IwaterDimension',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('shname', models.CharField(max_length=255)),
                ('id_company', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'iwater_dimension',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IwaterDriver',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('login', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=255)),
                ('salt', models.CharField(max_length=255)),
                ('notification', models.CharField(max_length=178)),
                ('session', models.CharField(max_length=128)),
                ('company', models.CharField(max_length=4)),
                ('stat', models.CharField(max_length=8)),
            ],
            options={
                'db_table': 'iwater_driver',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IwaterHow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'iwater_how',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IwaterLinks',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('section', models.IntegerField()),
                ('desc', models.CharField(max_length=256)),
                ('level', models.SmallIntegerField()),
            ],
            options={
                'db_table': 'iwater_links',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IwaterLists',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=15)),
                ('file', models.CharField(max_length=255)),
                ('user_id', models.IntegerField()),
                ('create_date', models.CharField(max_length=15)),
                ('map_num', models.CharField(max_length=255)),
                ('driver_id', models.IntegerField(blank=True, null=True)),
                ('company_id', models.CharField(max_length=4)),
            ],
            options={
                'db_table': 'iwater_lists',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IwaterLogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('operation', models.CharField(max_length=255)),
                ('action', models.CharField(max_length=255)),
                ('data', models.CharField(max_length=255)),
                ('table', models.CharField(max_length=255)),
                ('time', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'iwater_logs',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IwaterMovedOrders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField(blank=True, null=True)),
                ('done', models.IntegerField(blank=True, null=True)),
                ('reason', models.CharField(blank=True, max_length=255, null=True)),
                ('comment', models.CharField(blank=True, max_length=255, null=True)),
                ('agreed', models.IntegerField(blank=True, null=True)),
                ('server_time', models.CharField(blank=True, max_length=50, null=True)),
                ('driver_coords', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'iwater_moved_orders',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IwaterNotice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dest_id', models.IntegerField()),
                ('dest_name', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('message', models.CharField(max_length=255)),
                ('noticed', models.CharField(max_length=255)),
                ('read', models.CharField(max_length=255)),
                ('date', models.IntegerField()),
            ],
            options={
                'db_table': 'iwater_notice',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IwaterOrders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_id', models.IntegerField()),
                ('mobile', models.IntegerField()),
                ('local_id', models.IntegerField(blank=True, null=True)),
                ('company_id', models.CharField(max_length=4)),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('contact', models.CharField(max_length=255)),
                ('date', models.CharField(blank=True, max_length=20, null=True)),
                ('no_date', models.IntegerField()),
                ('time', models.CharField(max_length=255)),
                ('period', models.CharField(max_length=50)),
                ('notice', models.TextField(blank=True, null=True)),
                ('water_total', models.IntegerField()),
                ('water_equip', models.CharField(max_length=255)),
                ('equip', models.TextField(blank=True, null=True)),
                ('checked', models.IntegerField()),
                ('dep', models.CharField(blank=True, max_length=255, null=True)),
                ('cash', models.CharField(max_length=15)),
                ('cash_formula', models.CharField(max_length=255)),
                ('cash_b_formula', models.CharField(max_length=255)),
                ('cash_b', models.CharField(blank=True, max_length=15, null=True)),
                ('on_floor', models.CharField(blank=True, max_length=15, null=True)),
                ('tank_b', models.IntegerField(blank=True, null=True)),
                ('tank_empty_now', models.IntegerField()),
                ('driver', models.IntegerField()),
                ('status', models.IntegerField()),
                ('reason', models.CharField(blank=True, max_length=255, null=True)),
                ('map_num', models.IntegerField(blank=True, null=True)),
                ('region', models.CharField(max_length=255)),
                ('list', models.IntegerField(blank=True, null=True)),
                ('coords', models.CharField(blank=True, max_length=255, null=True)),
                ('history', models.CharField(blank=True, max_length=255, null=True)),
                ('changed_driver', models.IntegerField()),
                ('number_visit', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'iwater_orders',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IwaterOrdersApp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_id', models.IntegerField()),
                ('name', models.CharField(max_length=128)),
                ('company_id', models.CharField(max_length=4)),
                ('address', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=128)),
                ('contact', models.CharField(max_length=128)),
                ('date', models.CharField(blank=True, max_length=20, null=True)),
                ('period', models.CharField(max_length=50)),
                ('notice', models.TextField(blank=True, null=True)),
                ('water_equip', models.CharField(max_length=255)),
                ('checked', models.SmallIntegerField()),
                ('status', models.IntegerField()),
                ('system', models.CharField(max_length=128)),
            ],
            options={
                'db_table': 'iwater_orders_app',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IwaterPerms',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'iwater_perms',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IwaterPermsOld',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('desc', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'iwater_perms_old',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IwaterProviders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_id', models.CharField(max_length=4)),
                ('name', models.CharField(max_length=128)),
                ('contact', models.CharField(max_length=128)),
            ],
            options={
                'db_table': 'iwater_providers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IwaterReportApp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driver_id', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('payment_type', models.CharField(max_length=255)),
                ('payment', models.FloatField()),
                ('number_containers', models.IntegerField()),
                ('orders_delivered', models.IntegerField()),
                ('total_money', models.FloatField()),
                ('date_created', models.CharField(max_length=15)),
                ('date', models.CharField(max_length=255)),
                ('company_id', models.CharField(max_length=4)),
            ],
            options={
                'db_table': 'iwater_report_app',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IwaterReportsApp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.IntegerField()),
                ('text', models.TextField()),
            ],
            options={
                'db_table': 'iwater_reports_app',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IwaterRoles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('perms', models.TextField()),
            ],
            options={
                'db_table': 'iwater_roles',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IwaterSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('data', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'iwater_settings',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IwaterStorage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'iwater_storage',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IwaterStorageAgr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('company_id', models.CharField(max_length=4)),
                ('name', models.CharField(max_length=255)),
                ('priority', models.IntegerField()),
                ('address', models.CharField(max_length=255)),
                ('coords', models.CharField(max_length=128)),
                ('storeman_name', models.CharField(max_length=128)),
                ('storeman_phone', models.CharField(max_length=64)),
                ('date_start', models.IntegerField()),
                ('date_finish', models.IntegerField()),
            ],
            options={
                'db_table': 'iwater_storage_agr',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IwaterStorageCount',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('unit_id', models.IntegerField()),
                ('storage', models.IntegerField()),
                ('shelf_life', models.IntegerField()),
                ('count', models.IntegerField()),
                ('last_update', models.IntegerField()),
            ],
            options={
                'db_table': 'iwater_storage_count',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IwaterStorageHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_id', models.IntegerField()),
                ('storage', models.IntegerField()),
                ('operation', models.CharField(max_length=16)),
                ('count', models.IntegerField()),
                ('comment', models.CharField(max_length=255)),
                ('date', models.IntegerField()),
            ],
            options={
                'db_table': 'iwater_storage_history',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IwaterUnits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=86)),
                ('shname', models.CharField(blank=True, max_length=16, null=True)),
                ('price', models.CharField(max_length=256)),
                ('discount', models.IntegerField()),
                ('category', models.IntegerField()),
                ('about', models.TextField(blank=True, null=True)),
                ('gallery', models.TextField(blank=True, null=True)),
                ('gl_id', models.IntegerField()),
            ],
            options={
                'db_table': 'iwater_units',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IwaterUnitsAgr',
            fields=[
                ('counter', models.AutoField(primary_key=True, serialize=False)),
                ('id', models.IntegerField()),
                ('name', models.CharField(max_length=86)),
                ('shname', models.CharField(blank=True, max_length=16, null=True)),
                ('price', models.CharField(max_length=256)),
                ('discount', models.IntegerField()),
                ('category', models.IntegerField()),
                ('about', models.TextField(blank=True, null=True)),
                ('gallery', models.TextField(blank=True, null=True)),
                ('gl_id', models.IntegerField()),
                ('date', models.IntegerField()),
                ('date_start', models.IntegerField()),
                ('date_finish', models.IntegerField()),
            ],
            options={
                'db_table': 'iwater_units_agr',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IwaterUnitsAgrOld',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=86)),
                ('shname', models.CharField(blank=True, max_length=16, null=True)),
                ('price', models.CharField(max_length=256)),
                ('discount', models.IntegerField()),
                ('category', models.IntegerField()),
                ('about', models.TextField(blank=True, null=True)),
                ('gallery', models.TextField(blank=True, null=True)),
                ('gl_id', models.IntegerField()),
                ('date_start', models.IntegerField()),
                ('date_finish', models.IntegerField()),
            ],
            options={
                'db_table': 'iwater_units_agr_old',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IwaterUnitsAgrSwap',
            fields=[
                ('counter', models.AutoField(primary_key=True, serialize=False)),
                ('id', models.IntegerField()),
                ('name', models.CharField(max_length=86)),
                ('shname', models.CharField(blank=True, max_length=16, null=True)),
                ('price', models.CharField(max_length=256)),
                ('discount', models.IntegerField()),
                ('category', models.IntegerField()),
                ('about', models.TextField(blank=True, null=True)),
                ('gallery', models.TextField(blank=True, null=True)),
                ('gl_id', models.IntegerField()),
                ('date_start', models.IntegerField()),
                ('date_finish', models.IntegerField()),
            ],
            options={
                'db_table': 'iwater_units_agr_swap',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IwaterUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('salt', models.CharField(max_length=255)),
                ('session', models.CharField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=15)),
                ('role', models.IntegerField()),
                ('company_id', models.CharField(max_length=4)),
                ('ban', models.IntegerField()),
                ('region', models.CharField(blank=True, max_length=255, null=True)),
                ('card', models.CharField(blank=True, max_length=32, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'iwater_users',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IwaterUsersApp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('lastname', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('session', models.CharField(max_length=255)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'iwater_users_app',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IwaterVipApp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('lastname', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('session', models.CharField(max_length=255)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('contract', models.CharField(blank=True, max_length=255, null=True)),
                ('inn', models.CharField(blank=True, db_column='INN', max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'iwater_vip_app',
                'managed': False,
            },
        ),
    ]